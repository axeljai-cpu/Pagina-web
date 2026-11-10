/* Estudio J, C & S — Calculadora de indemnización (despido y ART).
   Patrón IIFE, sin dependencias. Los resultados son estimativos y en montos brutos. */
(function () {
  'use strict';

  var doc = document;
  var WA = (window.__BRAND__ && window.__BRAND__.whatsapp) || '5491149734492';
  var DAY = 86400000;
  var money = new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 });

  function safe(fn, name) {
    try { fn(); } catch (err) { if (window.console) console.warn('[JCS calculadora] ' + name + ':', err); }
  }
  function $(sel, ctx) { return (ctx || doc).querySelector(sel); }
  function $all(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }
  function track(event, data) {
    window.dataLayer = window.dataLayer || [];
    var payload = { event: event };
    for (var k in data) if (Object.prototype.hasOwnProperty.call(data, k)) payload[k] = data[k];
    window.dataLayer.push(payload);
  }

  /* Fechas en hora local, sin desfases por zona horaria */
  function parseDate(value) {
    if (!value) return null;
    var p = value.split('-');
    if (p.length !== 3) return null;
    var d = new Date(+p[0], +p[1] - 1, +p[2]);
    return isNaN(d.getTime()) ? null : d;
  }
  function daysBetween(a, b) { return Math.round((b - a) / DAY); }
  function lastDayOfMonth(d) { return new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate(); }
  function addMonths(d, n) {
    var r = new Date(d.getFullYear(), d.getMonth() + n, d.getDate());
    if (r.getDate() !== d.getDate()) r.setDate(0);
    return r;
  }
  /* Diferencia en años, meses y días */
  function diffYMD(a, b) {
    var y = b.getFullYear() - a.getFullYear();
    var m = b.getMonth() - a.getMonth();
    var d = b.getDate() - a.getDate();
    if (d < 0) { m -= 1; d += new Date(b.getFullYear(), b.getMonth(), 0).getDate(); }
    if (m < 0) { y -= 1; m += 12; }
    return { y: y, m: m, d: d };
  }
  function num(input) {
    var v = (input.value || '').toString().replace(/\./g, '').replace(',', '.').replace(/[^\d.]/g, '');
    return v ? parseFloat(v) : 0;
  }
  function plural(n, s, p) { return n + ' ' + (n === 1 ? s : p); }

  function setError(form, msg) {
    var box = $('[data-calc-error]', form);
    box.textContent = msg || '';
    box.hidden = !msg;
  }

  function renderRows(table, rows) {
    var tbody = $('tbody', table);
    tbody.innerHTML = '';
    rows.forEach(function (r) {
      if (!r.amount) return;
      var tr = doc.createElement('tr');
      var th = doc.createElement('th');
      th.scope = 'row';
      th.innerHTML = '<span>' + r.label + '</span>' + (r.note ? '<small>' + r.note + '</small>' : '');
      var td = doc.createElement('td');
      td.textContent = money.format(r.amount);
      tr.appendChild(th); tr.appendChild(td);
      tbody.appendChild(tr);
    });
  }

  function waLink(text) {
    return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(text);
  }

  /* ---------- Despido sin causa ---------- */
  function calcDespido(form) {
    var ingreso = parseDate($('[name="ingreso"]', form).value);
    var egreso = parseDate($('[name="egreso"]', form).value);
    var sueldo = num($('[name="sueldo"]', form));
    var tope = num($('[name="tope"]', form));
    var preavisoDado = $('[name="preaviso"]', form).value === 'si';
    var tomadas = num($('[name="vacaciones"]', form));

    if (!ingreso || !egreso) return setError(form, 'Completá la fecha de ingreso y la fecha del despido.');
    if (egreso <= ingreso) return setError(form, 'La fecha del despido tiene que ser posterior a la de ingreso.');
    if (!sueldo) return setError(form, 'Ingresá tu mejor remuneración mensual bruta.');
    setError(form, '');

    var ant = diffYMD(ingreso, egreso);
    var enPrueba = egreso < addMonths(ingreso, 6);
    var fraccionMayor3 = ant.m > 3 || (ant.m === 3 && ant.d > 0);
    var anios245 = ant.y + (fraccionMayor3 ? 1 : 0);

    /* Art. 245: base con tope de convenio y piso Vizzoti (67 %) */
    var base245 = sueldo;
    var topeAplicado = false;
    if (tope > 0 && tope < sueldo) { base245 = Math.max(tope, sueldo * 0.67); topeAplicado = true; }
    var indemnizacion = enPrueba ? 0 : base245 * Math.max(anios245, 1);

    /* Art. 231/232: preaviso */
    var preaviso = 0, preavisoNota = '';
    if (!preavisoDado) {
      if (enPrueba) { preaviso = sueldo / 2; preavisoNota = '15 días (período de prueba)'; }
      else if (daysBetween(ingreso, egreso) > 5 * 365.25) { preaviso = sueldo * 2; preavisoNota = '2 meses (más de 5 años de antigüedad)'; }
      else { preaviso = sueldo; preavisoNota = '1 mes (hasta 5 años de antigüedad)'; }
    }

    /* Art. 233: integración del mes de despido */
    var integracion = 0, diasInteg = 0;
    var ultimo = lastDayOfMonth(egreso);
    if (!preavisoDado && egreso.getDate() !== ultimo) {
      diasInteg = ultimo - egreso.getDate();
      integracion = sueldo / 30 * diasInteg;
    }

    /* Días trabajados del mes */
    var diasMes = Math.min(egreso.getDate(), 30);
    var trabajados = sueldo / 30 * diasMes;

    /* SAC proporcional del semestre */
    var semInicio = new Date(egreso.getFullYear(), egreso.getMonth() < 6 ? 0 : 6, 1);
    var semFin = new Date(egreso.getFullYear(), egreso.getMonth() < 6 ? 6 : 12, 1);
    var desde = ingreso > semInicio ? ingreso : semInicio;
    var diasSem = daysBetween(desde, egreso) + 1;
    var sac = sueldo / 2 * diasSem / daysBetween(semInicio, semFin);

    /* Art. 150/156: vacaciones proporcionales */
    var finAnio = new Date(egreso.getFullYear(), 11, 31);
    var antDic = diffYMD(ingreso, finAnio).y;
    var diasAnuales = antDic < 5 ? 14 : antDic < 10 ? 21 : antDic < 20 ? 28 : 35;
    var inicioAnio = new Date(egreso.getFullYear(), 0, 1);
    var desdeAnio = ingreso > inicioAnio ? ingreso : inicioAnio;
    var diasAnio = daysBetween(desdeAnio, egreso) + 1;
    /* Mínimo de 14 días de vacaciones (criterio indicado por el estudio) */
    var VAC_MIN = 14;
    var diasProp = Math.max(VAC_MIN, diasAnuales * diasAnio / 365);
    var diasVac = Math.max(0, Math.round((diasProp - tomadas) * 10) / 10);
    var vacaciones = sueldo / 25 * diasVac;
    var minAplicado = diasAnuales * diasAnio / 365 < VAC_MIN;
    var vacNota = minAplicado
      ? (tomadas ? ' (mínimo de 14, menos ' + tomadas + ' ya tomados)' : ' (mínimo de 14)')
      : (tomadas ? ' (descontados ' + tomadas + ' ya tomados)' : '');

    var rows = [
      { label: 'Indemnización por antigüedad', note: 'Art. 245 LCT · ' + plural(Math.max(anios245, 1), 'año', 'años') + (topeAplicado ? ' · con tope de convenio' : ''), amount: indemnizacion },
      { label: 'Preaviso omitido', note: 'Arts. 231 y 232 LCT · ' + preavisoNota, amount: preaviso },
      { label: 'SAC sobre preaviso', note: 'Aguinaldo proporcional al preaviso', amount: preaviso / 12 },
      { label: 'Integración del mes de despido', note: 'Art. 233 LCT · ' + plural(diasInteg, 'día', 'días'), amount: integracion },
      { label: 'SAC sobre integración', note: 'Aguinaldo proporcional a la integración', amount: integracion / 12 },
      { label: 'Días trabajados del mes', note: plural(diasMes, 'día', 'días'), amount: trabajados },
      { label: 'SAC proporcional', note: 'Aguinaldo del semestre · ' + plural(diasSem, 'día', 'días'), amount: sac },
      { label: 'Vacaciones no gozadas', note: 'Arts. 150 y 156 LCT · ' + diasVac.toString().replace('.', ',') + ' días' + vacNota, amount: vacaciones },
      { label: 'SAC sobre vacaciones', note: 'Aguinaldo proporcional a las vacaciones', amount: vacaciones / 12 }
    ];
    var total = rows.reduce(function (s, r) { return s + r.amount; }, 0);

    var result = $('[data-result="despido"]');
    renderRows($('table', result), rows);
    $('[data-total]', result).textContent = money.format(total);
    $('[data-antiguedad]', result).textContent = 'Antigüedad: ' + plural(ant.y, 'año', 'años') + ', ' + plural(ant.m, 'mes', 'meses') + ' y ' + plural(ant.d, 'día', 'días') + '.';
    $('[data-prueba]', result).hidden = !enPrueba;

    var resumen = 'Hola, usé la calculadora de indemnización del sitio y me gustaría que revisen mi liquidación.\n\n' +
      'Ingreso: ' + $('[name="ingreso"]', form).value.split('-').reverse().join('/') + '\n' +
      'Despido: ' + $('[name="egreso"]', form).value.split('-').reverse().join('/') + '\n' +
      'Mejor remuneración: ' + money.format(sueldo) + '\n' +
      'Total estimado: ' + money.format(total);
    $('[data-wa-result]', result).href = waLink(resumen);

    result.hidden = false;
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
    track('calculadora_usada', { tipo: 'despido', pagina: window.location.pathname });
  }

  /* ---------- ART: incapacidad permanente ---------- */
  function calcArt(form) {
    var ingreso = num($('[name="ibm"]', form));
    var edad = num($('[name="edad"]', form));
    var pct = num($('[name="incapacidad"]', form));
    var lugar = $('[name="lugar"]', form).value;

    if (!ingreso) return setError(form, 'Ingresá tu ingreso mensual promedio del último año.');
    if (!edad || edad < 16 || edad > 99) return setError(form, 'Ingresá una edad válida.');
    if (!pct || pct <= 0 || pct > 100) return setError(form, 'Ingresá un porcentaje de incapacidad entre 1 y 100.');
    setError(form, '');

    var total66 = pct >= 66;
    var pctCalc = total66 ? 100 : pct;
    var coef = 65 / edad;
    var base = 53 * ingreso * (pctCalc / 100) * coef;
    var adicional = lugar === 'trabajo' ? base * 0.2 : 0;

    var rows = [
      { label: 'Indemnización por incapacidad', note: 'Ley 24.557 · 53 × ingreso × ' + pctCalc + ' % × 65/' + edad, amount: base },
      { label: 'Adicional del 20 %', note: 'Ley 26.773 · accidente en el lugar de trabajo', amount: adicional }
    ];
    var total = base + adicional;

    var result = $('[data-result="art"]');
    renderRows($('table', result), rows);
    $('[data-total]', result).textContent = money.format(total);
    $('[data-total66]', result).hidden = !total66;
    $('[data-itinere]', result).hidden = lugar === 'trabajo';

    var resumen = 'Hola, usé la calculadora de ART del sitio y me gustaría que revisen mi caso.\n\n' +
      'Ingreso mensual promedio: ' + money.format(ingreso) + '\n' +
      'Edad: ' + edad + '\n' +
      'Incapacidad: ' + pct + ' %\n' +
      'Total estimado: ' + money.format(total);
    $('[data-wa-result]', result).href = waLink(resumen);

    result.hidden = false;
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
    track('calculadora_usada', { tipo: 'art', pagina: window.location.pathname });
  }

  /* ---------- Pestañas ---------- */
  function selectTab(name) {
    $all('[data-calc-tab]').forEach(function (t) {
      var on = t.getAttribute('data-calc-tab') === name;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
    });
    $all('[data-calc-panel]').forEach(function (p) {
      p.hidden = p.getAttribute('data-calc-panel') !== name;
    });
  }

  function init() {
    var tabs = $all('[data-calc-tab]');
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { selectTab(tab.getAttribute('data-calc-tab')); });
      tab.addEventListener('keydown', function (e) {
        var dir = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!dir) return;
        e.preventDefault();
        var next = tabs[(i + dir + tabs.length) % tabs.length];
        next.focus(); next.click();
      });
    });
    if (window.location.hash === '#art') selectTab('art');
    $all('a[href="#art"]').forEach(function (a) {
      a.addEventListener('click', function () { selectTab('art'); });
    });

    var fd = $('form[data-calc="despido"]');
    if (fd) fd.addEventListener('submit', function (e) { e.preventDefault(); safe(function () { calcDespido(fd); }, 'despido'); });
    var fa = $('form[data-calc="art"]');
    if (fa) fa.addEventListener('submit', function (e) { e.preventDefault(); safe(function () { calcArt(fa); }, 'art'); });

    /* Fecha de despido por defecto: hoy */
    var eg = $('form[data-calc="despido"] [name="egreso"]');
    if (eg && !eg.value) {
      var t = new Date();
      eg.value = t.getFullYear() + '-' + String(t.getMonth() + 1).padStart(2, '0') + '-' + String(t.getDate()).padStart(2, '0');
    }
  }

  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', function () { safe(init, 'init'); });
  else safe(init, 'init');
})();
