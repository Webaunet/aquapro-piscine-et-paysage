(function(){
  var f=document.getElementById('form');if(!f)return;
  var recap=document.getElementById('recap'),txt=document.getElementById('recap-txt'),st=document.getElementById('status');
  var TEL='+33650183691',MAIL='aquapro246@hotmail.com';
  function g(id){return document.getElementById(id);}
  function setErr(id,msg){var i=g(id),e=g('e-'+id);e.textContent=msg||'';if(msg)i.setAttribute('aria-invalid','true');else i.removeAttribute('aria-invalid');return !msg;}
  function validate(){
    var ok=[],v=function(id){return g(id).value.trim();};
    ok.push(setErr('prenom',v('prenom').length<2?'Indiquez votre prénom.':''));
    ok.push(setErr('nom',v('nom').length<2?'Indiquez votre nom.':''));
    ok.push(setErr('tel',/^(?:\+33|0033|0)\s?[1-9](?:[\s.-]?\d{2}){4}$/.test(v('tel'))?'':'Saisissez un numéro français valide, par exemple 06 12 34 56 78.'));
    ok.push(setErr('email',v('email')&&!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v('email'))?'Saisissez une adresse e-mail valide.':''));
    ok.push(setErr('sujet',v('sujet')?'':'Choisissez votre besoin.'));
    ok.push(setErr('msg',v('msg').length<10?'Décrivez votre demande en quelques mots (10 caractères minimum).':''));
    return ok.indexOf(false)<0;
  }
  ['prenom','nom','tel','email','sujet','msg'].forEach(function(id){g(id).addEventListener('input',function(){if(g(id).getAttribute('aria-invalid'))validate();});});
  f.addEventListener('submit',function(e){
    e.preventDefault();st.textContent='';
    if(!validate()){var bad=f.querySelector('[aria-invalid="true"]');if(bad)bad.focus();return;}
    var v=function(id){return g(id).value.trim();};
    var m='Bonjour, je suis '+v('prenom')+' '+v('nom')+'.\nBesoin : '+v('sujet')+'.\n'+v('msg')+'\nTéléphone : '+v('tel')+(v('email')?'\nE-mail : '+v('email'):'');
    txt.textContent=m;
    g('sms').href='sms:'+TEL+'?&body='+encodeURIComponent(m);
    g('mail').href='mailto:'+MAIL+'?subject='+encodeURIComponent('Demande : '+v('sujet'))+'&body='+encodeURIComponent(m);
    recap.hidden=false;recap.focus();recap.scrollIntoView({behavior:'smooth',block:'center'});
  });
  g('copy').addEventListener('click',function(){
    var t=txt.textContent;
    function done(ok){st.textContent=ok?'Message copié.':'Copie impossible : sélectionnez le texte ci-dessus.';}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(function(){done(true);},function(){fallback();});}else fallback();
    function fallback(){try{var r=document.createRange();r.selectNodeContents(txt);var s=getSelection();s.removeAllRanges();s.addRange(r);done(document.execCommand('copy'));}catch(x){done(false);}}
  });
})();
