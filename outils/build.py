#!/usr/bin/env python3
"""Génère les pages intérieures à partir de l'en-tête/pied de page de index.html.
Usage : python3 outils/build.py"""
import re, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx = open(R + '/index.html', encoding='utf-8').read()
FOOT_OLD = '<a href="contact.html">Contact</a></nav>'
FOOT_NEW = '<a href="contact.html">Contact</a><a href="mentions-legales.html">Mentions légales</a></nav>'
if FOOT_OLD in idx:
    idx = idx.replace(FOOT_OLD, FOOT_NEW); open(R + '/index.html', 'w', encoding='utf-8').write(idx)
HEAD_FONTS = re.search(r'(<link rel="preconnect".*?<link rel="stylesheet" href="css/style.css">)', idx, re.S).group(1)
HEADER = re.search(r'<a class="skip".*?</header>', idx, re.S).group(0)
FOOTER = re.search(r'<footer.*?</footer>', idx, re.S).group(0)
PH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'

def page(fn, cur, title, desc, body, extra=''):
    h = HEADER
    h = h.replace(' aria-current="page"', '')
    h = h.replace('href="%s"' % cur, 'href="%s" aria-current="page"' % cur, 1)
    out = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/png" href="images/logo.png">
{HEAD_FONTS}
</head>
<body>
{h}

<main id="contenu">
{body}
</main>

{FOOTER}
<script src="js/main.js"></script>{extra}
</body>
</html>
'''
    open(R + '/' + fn, 'w', encoding='utf-8').write(out)

# ---------------- PRESTATIONS ----------------
prest = f'''<section class="ph" aria-labelledby="h1">
  <div class="wrap ph-grid">
    <div>
      <span class="eyebrow">Nos prestations</span>
      <h1 id="h1">Piscine, bassin, jardin : tout l'entretien au même endroit</h1>
      <p>Hivernage, rénovation, changement de liner, traitement de l'eau, entretien de jardins et lieux de détente : AquaPro intervient autour de l'eau comme autour des plantes.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="tel:+33650183691">{PH}Appeler le 06 50 18 36 91</a>
        <a class="btn btn-ghost" href="contact.html">Demander un échange</a>
      </div>
    </div>
    <div class="mosaic">
      <img src="images/piscine-eau-cristalline.jpg" width="800" height="533" alt="Piscine à l'eau turquoise bordée de margelles en pierre">
      <img src="images/traitement-eau-piscine.jpg" width="800" height="533" alt="Technicien analysant l'eau d'une piscine">
      <img src="images/renovation-liner-piscine.jpg" width="800" height="534" alt="Pose d'un liner dans un bassin de piscine">
    </div>
  </div>
</section>

<section class="sec-auto tint-mist" id="piscine" aria-labelledby="h-pisc">
  <div class="wrap row">
    <div>
      <span class="eyebrow">Piscines, SPA &amp; bassins</span>
      <h2 id="h-pisc">Une eau limpide, toute l'année</h2>
      <p>AquaPro assure l'entretien des installations extérieures : piscines, SPA et bassins. Une eau équilibrée est translucide ; notre équipe s'en charge pour que la baignade reste un plaisir.</p>
      <ul class="dl">
        <li><strong>Entretien de piscines</strong><span>Suivi régulier du bassin et de ses abords.</span></li>
        <li><strong>Traitement de l'eau</strong><span>Traitement professionnel pour une qualité d'eau durable.</span></li>
        <li><strong>Hivernage</strong><span>Mise en sommeil du bassin pour la saison froide.</span></li>
        <li><strong>Rénovation et changement de liner</strong><span>Remise en état des piscines et des bassins.</span></li>
      </ul>
    </div>
    <img class="big" src="images/piscine-terrasse-pierre.jpg" width="800" height="533" loading="lazy" alt="Piscine devant une maison en pierre, terrasse et mobilier de jardin">
  </div>
</section>

<section class="sec-auto tint-sand" id="jardin" aria-labelledby="h-jar">
  <div class="wrap row rev">
    <div>
      <span class="eyebrow">Jardins &amp; lieux de détente</span>
      <h2 id="h-jar">Le bruit de l'eau, la douceur de l'herbe</h2>
      <p>Nous réalisons des lieux de détente adaptés à vos besoins : une terrasse, des massifs, un SPA (jacuzzi, sauna, hammam, douche…). Un large choix d'objets, de matériaux et de plantes permet de créer l'atmosphère sur mesure dont vous rêvez.</p>
      <ul class="dl">
        <li><strong>Entretien de jardins</strong><span>Pelouses, massifs et haies.</span></li>
        <li><strong>Terrasses et massifs</strong><span>Des espaces pensés selon l'usage.</span></li>
        <li><strong>SPA</strong><span>Jacuzzi, sauna, hammam, douche.</span></li>
      </ul>
    </div>
    <img class="big" src="images/jardin-piscine-pergola.jpg" width="419" height="493" loading="lazy" alt="Terrasse avec pergola et graminées devant une piscine" style="max-width:420px;justify-self:center;aspect-ratio:5/6">
  </div>
</section>

<section class="sec-auto" aria-labelledby="h-cta">
  <div class="wrap">
    <div class="strip">
      <h2 id="h-cta">Un devis ou une question sur l'entretien ?</h2>
      <div class="cta-row" style="margin:0">
        <a class="btn btn-primary" href="tel:+33650183691">Appeler</a>
        <a class="btn btn-ghost" href="contact.html">Écrire</a>
      </div>
    </div>
  </div>
</section>'''
page('prestations.html', 'prestations.html', 'Prestations | AquaPro Piscine et Paysage, Goussonville',
     "Entretien, hivernage, rénovation, changement de liner et traitement de l'eau de piscine ; entretien de jardins et lieux de détente à Goussonville (78).", prest)

# ---------------- À PROPOS ----------------
apropos = f'''<section class="ap-hero" aria-labelledby="h1">
  <div class="wrap">
    <div>
      <span class="eyebrow">À propos</span>
      <h1 id="h1">Pisciniste et paysagiste, installés à Goussonville</h1>
      <p>AquaPro Piscine et Paysage est une entreprise de services d'aménagement paysager basée à Goussonville, dans les Yvelines. Spécialistes de l'entretien, nous prenons soin des piscines, des SPA, des bassins et des jardins.</p>
      <p>Un pisciniste doit être capable de répondre à toutes vos envies et tous vos besoins : une piscine chauffée pour se détendre, un couloir de nage froid pour le sport. Nous adaptons nos prestations à tous types de réalisations.</p>
    </div>
    <ul class="facts">
      <li><b>Où</b><span>12b Route des Laris, 78930 Goussonville</span></li>
      <li><b>Métier</b><span>Pisciniste &amp; paysagiste</span></li>
      <li><b>Zone</b><span>Yvelines (78)</span></li>
      <li><b>Contact</b><span>06 50 18 36 91</span></li>
    </ul>
  </div>
</section>

<section class="sec-auto" aria-labelledby="h-vals">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Notre façon de travailler</span><h2 id="h-vals">Trois idées simples</h2></div>
    <div class="vals">
      <div class="val a"><h3>L'eau avant tout</h3><p>Une eau équilibrée est translucide. Notre travail : qu'elle le reste, pour que la piscine soit un plaisir et non une corvée.</p></div>
      <div class="val b"><h3>Le jardin autour</h3><p>Le bruit de l'eau, la douceur de l'herbe : nous réalisons des lieux de détente où bassin et plantes forment un tout.</p></div>
      <div class="val c"><h3>Du sur-mesure</h3><p>Objets, matériaux, plantes : un large choix pour créer l'atmosphère que vous imaginez.</p></div>
    </div>
  </div>
</section>

<section class="sec-auto tint-sand" aria-labelledby="h-ph">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">En images</span><h2 id="h-ph">Quelques lieux photographiés par l'entreprise</h2></div>
    <div class="trio">
      <figure><img src="images/piscine-double-bassin.jpg" width="1200" height="900" loading="lazy" alt="Piscine à double bassin dans un jardin arboré"><figcaption>Piscine double bassin</figcaption></figure>
      <figure><img src="images/terrasse-palmiers.jpg" width="1000" height="750" loading="lazy" alt="Terrasse en bois avec palmiers et massifs"><figcaption>Esprit méditerranéen</figcaption></figure>
      <figure><img src="images/callistemon-piscine.jpg" width="1000" height="749" loading="lazy" alt="Callistemon rouge devant une piscine"><figcaption>Ciel bleu et touche de rose</figcaption></figure>
    </div>
  </div>
</section>

<section class="sec-auto" aria-labelledby="h-cta">
  <div class="wrap">
    <div class="strip center">
      <span class="eyebrow" style="color:#ffd88a">Premier contact</span>
      <h2 id="h-cta">Faisons connaissance au téléphone</h2>
      <a class="btn btn-primary" href="tel:+33650183691">{PH}06 50 18 36 91</a>
    </div>
  </div>
</section>'''
page('a-propos.html', 'a-propos.html', 'À propos | AquaPro Piscine et Paysage, Goussonville',
     "AquaPro Piscine et Paysage, pisciniste et paysagiste à Goussonville (78) : qui nous sommes et comment nous travaillons.", apropos)

# ---------------- CONTACT ----------------
contact = f'''<section class="ct-hero" aria-labelledby="h1">
  <div class="wrap">
    <h1 id="h1">Parlons de votre projet</h1>
    <p>Remplissez le formulaire : il prépare un message prêt à envoyer par SMS, par e-mail ou à copier. Vous préférez parler ? Appelez le 06 50 18 36 91.</p>
  </div>
</section>

<section class="sec-auto" aria-labelledby="h-form">
  <div class="wrap ct-grid">
    <div>
      <form class="form" id="form" novalidate aria-labelledby="h-form">
        <h2 id="h-form" style="font-size:1.6rem">Votre demande</h2>
        <div class="fields">
          <div class="f"><label for="prenom">Prénom <span class="req" aria-hidden="true">*</span></label><input id="prenom" name="prenom" autocomplete="given-name" required aria-describedby="e-prenom"><span class="err" id="e-prenom" role="alert"></span></div>
          <div class="f"><label for="nom">Nom <span class="req" aria-hidden="true">*</span></label><input id="nom" name="nom" autocomplete="family-name" required aria-describedby="e-nom"><span class="err" id="e-nom" role="alert"></span></div>
          <div class="f"><label for="tel">Téléphone <span class="req" aria-hidden="true">*</span></label><input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="06 12 34 56 78" required aria-describedby="e-tel"><span class="err" id="e-tel" role="alert"></span></div>
          <div class="f"><label for="email">E-mail (facultatif)</label><input id="email" name="email" type="email" autocomplete="email" aria-describedby="e-email"><span class="err" id="e-email" role="alert"></span></div>
          <div class="f full"><label for="sujet">Votre besoin <span class="req" aria-hidden="true">*</span></label>
            <select id="sujet" name="sujet" required aria-describedby="e-sujet">
              <option value="">Choisir…</option>
              <option>Entretien de piscine</option>
              <option>Traitement de l'eau</option>
              <option>Hivernage</option>
              <option>Rénovation de piscine ou de bassin, liner</option>
              <option>Entretien de jardin</option>
              <option>Terrasse, massifs, SPA</option>
              <option>Autre demande</option>
            </select><span class="err" id="e-sujet" role="alert"></span></div>
          <div class="f full"><label for="msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="msg" name="msg" required minlength="10" aria-describedby="e-msg"></textarea><span class="err" id="e-msg" role="alert"></span></div>
        </div>
        <div class="cta-row"><button class="btn btn-teal" type="submit">Préparer mon message</button></div>
        <p class="note" style="margin:1rem 0 0">Les champs marqués d'un astérisque sont obligatoires. Rien n'est envoyé depuis cette page.</p>
      </form>
      <div class="recap" id="recap" hidden tabindex="-1" aria-labelledby="h-recap">
        <h2 id="h-recap" style="font-size:1.4rem">Votre message est prêt</h2>
        <pre id="recap-txt"></pre>
        <div class="cta-row">
          <a class="btn btn-primary" id="sms" href="sms:+33650183691">Envoyer par SMS</a>
          <button class="btn btn-ghost" type="button" id="copy">Copier</button>
          <a class="btn btn-ghost" href="tel:+33650183691">Appeler</a>
          <a class="btn btn-ghost" id="mail" href="mailto:aquapro246@hotmail.com">Envoyer par e-mail</a>
        </div>
        <p class="status" id="status" role="status"></p>
      </div>
    </div>
    <aside class="aside-card" aria-labelledby="h-coord">
      <h2 id="h-coord">Nos coordonnées</h2>
      <ul class="contact-list">
        <li>{PH}<a href="tel:+33650183691">06 50 18 36 91</a></li>
        <li>{MAIL}<a href="mailto:aquapro246@hotmail.com">aquapro246@hotmail.com</a></li>
        <li>{PIN}<span>12b Route des Laris<br>78930 Goussonville</span></li>
      </ul>
      <p style="margin:1.4rem 0 0;color:#cfe3e6">Pisciniste et paysagiste, interventions dans les Yvelines (78).</p>
    </aside>
  </div>
</section>'''
page('contact.html', 'contact.html', 'Contact | AquaPro Piscine et Paysage, Goussonville',
     "Contactez AquaPro Piscine et Paysage à Goussonville (78) : téléphone 06 50 18 36 91, e-mail, formulaire de demande.", contact,
     '\n<script src="js/contact.js"></script>')

# ---------------- MENTIONS LÉGALES ----------------
legal = '''<section class="ct-hero" aria-labelledby="h1">
  <div class="wrap"><h1 id="h1">Mentions légales</h1><p>Informations sur l'éditeur de ce site.</p></div>
</section>
<section class="sec-auto" aria-label="Mentions légales">
  <div class="wrap legal">
    <h2>Éditeur</h2>
    <dl>
      <dt>Nom</dt><dd>AquaPro Piscine et Paysage</dd>
      <dt>SIREN</dt><dd>984064246</dd>
      <dt>Commune</dt><dd>Goussonville (78930)</dd>
      <dt>Adresse</dt><dd>12b Route des Laris, 78930 Goussonville</dd>
      <dt>Téléphone</dt><dd><a href="tel:+33650183691">06 50 18 36 91</a></dd>
      <dt>E-mail</dt><dd><a href="mailto:aquapro246@hotmail.com">aquapro246@hotmail.com</a></dd>
      <dt>Forme juridique</dt><dd class="todo">À compléter par l'entreprise</dd>
      <dt>Responsable de la publication</dt><dd class="todo">À compléter par l'entreprise</dd>
    </dl>
    <h2>Hébergement</h2>
    <p>Cette maquette est hébergée sur GitHub Pages (GitHub, Inc.). L'hébergeur définitif sera indiqué à la mise en ligne du site.</p>
    <h2>Statut du site</h2>
    <p>Ce site est une maquette de présentation : il n'est pas référencé et aucune donnée saisie n'est enregistrée ni envoyée.</p>
  </div>
</section>'''
page('mentions-legales.html', 'mentions-legales.html', 'Mentions légales | AquaPro Piscine et Paysage',
     "Mentions légales du site d'AquaPro Piscine et Paysage, Goussonville (78) : éditeur, hébergement.", legal)
print('pages générées')
