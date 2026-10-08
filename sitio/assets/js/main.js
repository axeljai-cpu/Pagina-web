/* Estudio J, C & S — interacciones. Patrón IIFE, sin módulos ni dependencias. */
(function () {
  'use strict';

  var BRAND = window.__BRAND__ = window.__BRAND__ || {
    email: 'info@estudiojcs.com.ar',
    whatsapp: '5491151785782'
  };
  var doc = document;

  function safe(fn, name) {
    try { fn(); } catch (err) { if (window.console) console.warn('[JCS] ' + name + ':', err); }
  }
  function $all(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }
  function track(event, data) {
    window.dataLayer = window.dataLayer || [];
    var payload = { event: event };
    for (var k in data) if (Object.prototype.hasOwnProperty.call(data, k)) payload[k] = data[k];
    window.dataLayer.push(payload);
  }

  /* ---------- Cabecera ---------- */
  function initHeader() {
    var header = doc.querySelector('[data-header]');
    if (!header) return;
    var ticking = false;
    var update = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); ticking = false; };
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  /* ---------- Menú móvil ---------- */
  function initMenu() {
    var btn = doc.querySelector('[data-menu-btn]');
    var nav = doc.querySelector('[data-mobile-nav]');
    if (!btn || !nav) return;
    var set = function (open) {
      nav.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      doc.documentElement.style.overflow = open ? 'hidden' : '';
    };
    btn.addEventListener('click', function () { set(!nav.classList.contains('is-open')); });
    $all('a', nav).forEach(function (a) { a.addEventListener('click', function () { set(false); }); });
    doc.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
    window.addEventListener('resize', function () { if (window.innerWidth >= 1240) set(false); });
  }

  /* ---------- Revelado al hacer scroll ---------- */
  function initReveal() {
    var items = $all('.reveal');
    if (!items.length) return;
    if (!('IntersectionObserver' in window)) { items.forEach(function (el) { el.classList.add('is-in'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-in'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.05, rootMargin: '0px 0px -5% 0px' });
    items.forEach(function (el) { io.observe(el); });
    // Red de seguridad: nada queda oculto más de 6 s
    setTimeout(function () { items.forEach(function (el) { el.classList.add('is-in'); }); }, 6000);
  }

  /* ---------- Preguntas frecuentes: una abierta por bloque ---------- */
  function initFaq() {
    $all('.faq').forEach(function (group) {
      var items = $all('details', group);
      items.forEach(function (d) {
        d.addEventListener('toggle', function () {
          if (!d.open) return;
          items.forEach(function (o) { if (o !== d) o.open = false; });
        });
      });
    });
  }

  /* ---------- Origen de campañas (UTM) ---------- */
  function initUtm() {
    var keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid'];
    var params = new URLSearchParams(window.location.search);
    var found = [];
    keys.forEach(function (k) { if (params.get(k)) found.push(k + '=' + params.get(k)); });
    try {
      if (found.length) sessionStorage.setItem('jcs_utm', found.join('&'));
      var stored = sessionStorage.getItem('jcs_utm') || '';
      $all('input[name="utm"]').forEach(function (i) { i.value = stored; });
    } catch (e) { /* almacenamiento no disponible */ }
  }

  /* ---------- Motivo de consulta preseleccionado ---------- */
  function setMotivo(value) {
    if (!value) return;
    $all('select[name="motivo"]').forEach(function (s) {
      for (var i = 0; i < s.options.length; i++) {
        if (s.options[i].value === value) { s.value = value; break; }
      }
    });
  }

  function initMotivo() {
    doc.addEventListener('click', function (e) {
      var link = e.target.closest ? e.target.closest('[data-motivo]') : null;
      if (link) setMotivo(link.getAttribute('data-motivo'));
    });
    var params = new URLSearchParams(window.location.search);
    setMotivo(params.get('motivo'));
  }

  /* ---------- Medición de clics de contacto ---------- */
  function initTracking() {
    doc.addEventListener('click', function (e) {
      var el = e.target.closest ? e.target.closest('[data-track]') : null;
      if (el) track('contacto_' + el.getAttribute('data-track'), { pagina: window.location.pathname });
    });
  }

  /* ---------- Formulario ---------- */
  function validate(form) {
    var ok = true;
    $all('[required]', form).forEach(function (input) {
      var wrap = input.closest('.field, .consent');
      var v = input.value.trim();
      var valid;
      if (input.type === 'checkbox') valid = input.checked;
      else if (input.type === 'email') valid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
      else if (input.type === 'tel') valid = v.replace(/\D/g, '').length >= 8;
      else valid = v.length > 0;
      if (wrap) wrap.classList.toggle('is-invalid', !valid);
      if (!valid) ok = false;
    });
    return ok;
  }

  function summary(form) {
    var get = function (n) { var el = form.querySelector('[name="' + n + '"]'); return el ? el.value.trim() : ''; };
    return 'Nombre: ' + get('nombre') + '\nTeléfono: ' + get('telefono') + '\nEmail: ' + get('email') +
      '\nMotivo: ' + get('motivo') + '\n\n' + get('mensaje');
  }

  function showFallback(form) {
    var box = form.querySelector('[data-fallback]');
    if (!box) return;
    var text = 'Hola, quisiera realizar una consulta jurídica.\n\n' + summary(form);
    var wa = box.querySelector('[data-fallback-wa]');
    var mail = box.querySelector('[data-fallback-mail]');
    if (wa) wa.href = 'https://wa.me/' + BRAND.whatsapp + '?text=' + encodeURIComponent(text);
    if (mail) mail.href = 'mailto:' + BRAND.email + '?subject=' + encodeURIComponent('Consulta web') + '&body=' + encodeURIComponent(text);
    box.classList.add('is-visible');
  }

  function initForms() {
    $all('form[data-contact-form]').forEach(function (form) {
      var status = form.querySelector('[data-status]');
      var button = form.querySelector('button[type="submit"]');
      var t = form.querySelector('input[name="_t"]');
      var page = form.querySelector('input[name="pagina"]');
      if (t) t.value = String(Date.now());
      if (page) page.value = window.location.pathname;

      $all('input, select, textarea', form).forEach(function (el) {
        var evt = (el.type === 'checkbox' || el.tagName === 'SELECT') ? 'change' : 'input';
        el.addEventListener(evt, function () {
          var wrap = el.closest('.field, .consent');
          if (wrap) wrap.classList.remove('is-invalid');
        });
      });

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        status.className = 'form-status';
        if (!validate(form)) {
          status.textContent = 'Revisá los campos marcados, por favor.';
          status.classList.add('is-error');
          var first = form.querySelector('.is-invalid input, .is-invalid select, .is-invalid textarea');
          if (first) first.focus();
          return;
        }
        button.disabled = true;
        status.textContent = 'Enviando…';
        fetch(form.getAttribute('action'), {
          method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' }
        }).then(function (res) {
          return res.json().catch(function () { return { ok: false }; }).then(function (json) {
            if (!res.ok || !json.ok) throw new Error(json.error || 'envio');
          });
        }).then(function () {
          var motivo = form.querySelector('[name="motivo"]');
          track('consulta_enviada', { motivo: motivo ? motivo.value : '', pagina: window.location.pathname });
          window.location.href = '/gracias/';
        }).catch(function () {
          status.textContent = 'No pudimos enviar el formulario. Podés enviarnos la consulta por WhatsApp o por email:';
          status.classList.add('is-error');
          showFallback(form);
        }).then(function () { button.disabled = false; });
      });
    });
  }

  function initYear() {
    $all('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
  }

  function boot() {
    safe(initHeader, 'header');
    safe(initMenu, 'menu');
    safe(initReveal, 'reveal');
    safe(initFaq, 'faq');
    safe(initUtm, 'utm');
    safe(initMotivo, 'motivo');
    safe(initTracking, 'tracking');
    safe(initForms, 'forms');
    safe(initYear, 'year');
  }

  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
