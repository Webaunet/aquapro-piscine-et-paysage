#!/usr/bin/env python3
"""Test réutilisable : python3 outils/test.py [largeurs...]  (défaut 390 1440)
Contrôle : débordement horizontal, liens internes, texte < 16 px, cibles < 44 px,
poids des images, hauteurs de sections. Capture : outils/shot_<page>_<w>.png avec --shot"""
import sys, os, glob, re
from playwright.sync_api import sync_playwright
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
W = [int(a) for a in args] or [390, 1440]
shot = '--shot' in sys.argv
pages = sorted(glob.glob(R + '/*.html'))
bad = 0
def say(m):
    global bad; bad += 1; print('  ✗', m)
for p in pages:
    name = os.path.basename(p); html = open(p, encoding='utf-8').read()
    print(name)
    for l in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', html):
        if not os.path.exists(os.path.join(R, l)): say('lien/fichier manquant ' + l)
    tot = sum(os.path.getsize(os.path.join(R, i)) for i in set(re.findall(r'src="(images/[^"]+)"', html)) if os.path.exists(os.path.join(R, i)))
    for i in set(re.findall(r'src="(images/[^"]+)"', html)):
        if os.path.exists(os.path.join(R, i)) and os.path.getsize(os.path.join(R, i)) > 250000: say('image > 250 Ko ' + i)
    if tot > 1500000: say('images page > 1,5 Mo (%d Ko)' % (tot // 1024))
    if len(re.findall(r'<h1[ >]', html)) != 1: say('h1 != 1')
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if os.path.exists('/opt/pw-browsers/chromium-1194/chrome-linux/chrome') else pw.chromium.launch()
        for w in W:
            pg = b.new_page(viewport={'width': w, 'height': 800})
            pg.route('**/*', lambda r: r.abort() if r.request.url.startswith('http') else r.continue_())
            pg.goto('file://' + p); pg.wait_for_timeout(300)
            r = pg.evaluate('''()=>{const o={};const de=document.documentElement;o.ov=de.scrollWidth-de.clientWidth;
              o.small=[...document.querySelectorAll('body *')].filter(e=>e.childNodes.length&&[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim())&&getComputedStyle(e).display!='none'&&e.offsetParent!==null&&parseFloat(getComputedStyle(e).fontSize)<16).map(e=>e.tagName+'.'+e.className+' '+getComputedStyle(e).fontSize+' "'+e.textContent.trim().slice(0,20)+'"');
              o.tap=[...document.querySelectorAll('a,button')].filter(e=>e.offsetParent!==null&&!e.closest('.menu:not(.open)')).map(e=>[e,e.getBoundingClientRect()]).filter(([e,r])=>r.width>0&&(r.height<44||r.width<44)&&getComputedStyle(e).display!='inline').map(([e,r])=>e.textContent.trim().slice(0,20)+' '+Math.round(r.width)+'x'+Math.round(r.height));
              o.sec=[...document.querySelectorAll('main>section')].map(s=>Math.round(s.getBoundingClientRect().height/innerHeight*100));o.vh=innerHeight;
              o.foot=Math.round(document.querySelector('.site-footer').getBoundingClientRect().height/innerHeight*100);
              o.total=Math.round(de.scrollHeight/innerHeight*100)/100;
              o.imgs=[...document.images].filter(i=>i.complete&&i.naturalWidth&&(i.clientWidth>i.naturalWidth+1)).map(i=>i.getAttribute('src')+' agrandie '+i.clientWidth+'>'+i.naturalWidth);return o}''')
            if r['ov'] > 0: say('%d px débordement horizontal à %d' % (r['ov'], w))
            for s in r['small']: say('texte <16px à %d : %s' % (w, s))
            for s in r['tap']: say('cible <44px à %d : %s' % (w, s))
            for s in r['imgs']: say('image %s à %d' % (s, w))
            if r['foot'] > 30: say('pied de page %d%% à %d' % (r['foot'], w))
            print('  %4d px  sections(%% écran)=%s pied=%d%% pages-écran=%s' % (w, r['sec'], r['foot'], r['total']))
            if shot:
                pg.evaluate('async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}scrollTo(0,0)}');pg.wait_for_timeout(400)
            if shot: pg.screenshot(path='%s/outils/shot_%s_%d.png' % (R, name[:-5], w), full_page=True)
            pg.close()
        b.close()
print('OK' if not bad else '%d anomalie(s)' % bad)
sys.exit(1 if bad else 0)
