(function(){
  var b=document.querySelector('.burger'),m=document.getElementById('menu');
  if(!b||!m)return;
  function set(o){m.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu');}
  b.addEventListener('click',function(){set(!m.classList.contains('open'));});
  m.addEventListener('click',function(e){if(e.target.closest('a'))set(false);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open')){set(false);b.focus();}});
  window.addEventListener('resize',function(){if(window.innerWidth>980)set(false);});
})();
