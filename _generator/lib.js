'use strict';
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const RM = matchMedia('(prefers-reduced-motion: reduce)');
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const EVA = {e: 'Eingabe', v: 'Verarbeitung', a: 'Ausgabe', ea: 'Ein- und Ausgabe'};

/* ---------------- Navigation ---------------- */
const STATIONS = $$('.station').map(s => s.id);
const LABEL = Object.fromEntries($$('.station').map(s => [s.id, s.dataset.label || s.id]));
const NEXT_LESSON = document.body.dataset.next ? JSON.parse(document.body.dataset.next) : null;
const onShow = [];
let cur = 0;
function go(id) { const i = STATIONS.indexOf(id); if (i >= 0 && i !== cur) { cur = i; render(true); } }
function render(scroll) {
  const id = STATIONS[cur];
  $$('.station').forEach(s => s.hidden = s.id !== id);
  $$('[data-go]', $('#tl')).forEach(b => b.dataset.go === id ? b.setAttribute('aria-current', 'step') : b.removeAttribute('aria-current'));
  const stops = $$('#tl li.m');
  const idx = stops.map(li => STATIONS.indexOf($('[data-go]', li).dataset.go));
  stops.forEach((li, i) => { li.classList.toggle('done', idx[i] < cur); li.classList.toggle('half', idx[i] === cur); });
  const prev = STATIONS[cur - 1], next = STATIONS[cur + 1];
  $('#prev').textContent = prev ? '← ' + LABEL[prev] : '←';
  $('#prev').disabled = !prev;
  if (next) { $('#next').textContent = LABEL[next] + ' →'; $('#next').disabled = false; }
  else if (NEXT_LESSON) { $('#next').textContent = NEXT_LESSON.label + ' →'; $('#next').disabled = false; }
  else { $('#next').textContent = '→'; $('#next').disabled = true; }
  $('#pos').textContent = `${cur + 1} / ${STATIONS.length}`;
  try { history.replaceState(null, '', '#' + id); } catch (e) {}
  if (scroll) {
    window.scrollTo({top: 0});
    const b = $(`#tl [data-go="${id}"]`);
    if (b) { const sc = $('.tl-scroll'); sc.scrollLeft = b.offsetLeft - sc.clientWidth / 2 + b.offsetWidth / 2; }
  }
  for (const f of onShow) f(id);
}
document.addEventListener('click', e => { const b = e.target.closest('[data-go]'); if (b) go(b.dataset.go); });
$('#prev').onclick = () => { if (cur > 0) { cur--; render(true); } };
$('#next').onclick = () => {
  if (cur < STATIONS.length - 1) { cur++; render(true); }
  else if (NEXT_LESSON) location.href = NEXT_LESSON.href;
};
document.addEventListener('keydown', e => {
  if (e.target.closest('input, select, textarea') || e.altKey || e.ctrlKey || e.metaKey) return;
  if (['ArrowRight', 'PageDown'].includes(e.key)) { e.preventDefault(); if (cur < STATIONS.length - 1) $('#next').click(); }
  else if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); $('#prev').click(); }
  else if (e.key === 'f' || e.key === 'F') toggleFs();
});
function toggleFs() {
  try {
    if (document.fullscreenElement) document.exitFullscreen();
    else { const p = document.documentElement.requestFullscreen && document.documentElement.requestFullscreen(); if (p && p.catch) p.catch(() => {}); }
  } catch (e) {}
}
$('#fs').onclick = toggleFs;
document.addEventListener('fullscreenchange', () => $('#fs').textContent = document.fullscreenElement ? 'Vollbild beenden' : 'Vollbild');
function startApp() {
  const h0 = (location.hash || '').slice(1);
  if (STATIONS.includes(h0)) cur = STATIONS.indexOf(h0);
  render(false);
  /* der Browser springt beim Laden zum Anker #station – wieder nach oben */
  window.scrollTo(0, 0); setTimeout(() => window.scrollTo(0, 0), 0); addEventListener('load', () => window.scrollTo(0, 0));
}

/* ================= Bausteine ================= */
/* Hefteintrag: Punkte nacheinander aufdecken */
$$('.heft').forEach(h => {
  const items = $$('[data-step]', h), btn = $('[data-heft-next]', h), all = $('[data-heft-all]', h);
  let k = 0;
  const upd = () => { items.forEach((it, i) => it.classList.toggle('shown', i < k)); if (btn) { btn.disabled = k >= items.length; btn.textContent = k >= items.length ? 'Alles aufgedeckt' : `Nächster Punkt (${k + 1}/${items.length})`; } if (all) all.textContent = k >= items.length ? 'Wieder verdecken' : 'Alles zeigen'; };
  if (btn) btn.onclick = () => { k = Math.min(items.length, k + 1); upd(); };
  if (all) all.onclick = () => { k = k >= items.length ? 0 : items.length; upd(); };
  upd();
});

/* Aufklappen: <button data-reveal="id"> zeigt/versteckt #id */
document.addEventListener('click', e => {
  const b = e.target.closest('[data-reveal]'); if (!b) return;
  const t = document.getElementById(b.dataset.reveal); t.hidden = !t.hidden;
  b.setAttribute('aria-expanded', !t.hidden);
});

/* Auswahl-Leiste: seg(root, [[wert, text], ...], onPick, start) */
function seg(root, opts, onPick, start) {
  root.classList.add('seg'); root.setAttribute('role', 'group');
  root.innerHTML = opts.map(([v, t]) => `<button data-v="${v}" aria-pressed="false">${t}</button>`).join('');
  const pick = v => { $$('button', root).forEach(b => b.setAttribute('aria-pressed', b.dataset.v === String(v))); onPick(v); };
  root.onclick = e => { const b = e.target.closest('button'); if (b) pick(b.dataset.v); };
  pick(start ?? opts[0][0]);
  return pick;
}

/* Karteikarten zum Umdrehen: [[Vorderseite, Rückseite], ...] */
function flipCards(root, cards) {
  root.classList.add('flips');
  root.innerHTML = cards.map(([f, b]) => `<button class="flip"><span class="f">${f}</span><span class="b">${b}</span></button>`).join('');
  root.addEventListener('click', e => { const c = e.target.closest('.flip'); if (c) c.classList.toggle('on'); });
}

/* Multiple-Choice-Quiz. qs: [{q, a:[...], ok: index, why}] */
function mcQuiz(root, qs, o = {}) {
  let list = [], i = 0, score = 0, answered = false;
  root.classList.add('mc');
  function start() { list = o.pick ? shuffle(qs.slice()).slice(0, o.pick) : qs.slice(); i = 0; score = 0; show(); }
  function show() {
    if (i >= list.length) {
      const pct = score / list.length;
      root.innerHTML = `<div class="mc-end"><p class="eyebrow">Ergebnis</p><p class="mc-big">${score} / ${list.length}</p>
        <p class="lead" style="margin:0 auto 1rem">${pct === 1 ? 'Perfekt! Alles richtig.' : pct >= .7 ? 'Sehr gut! Fast alles richtig.' : pct >= .4 ? 'Ordentlich. Schau dir die Fehler noch einmal an.' : 'Wiederhole die Inhalte und versuch es noch einmal.'}</p>
        <button class="btn primary" data-mc="again">Neue Runde</button></div>`;
      return;
    }
    const q = list[i]; answered = false;
    const order = shuffle(q.a.map((t, k) => k));
    root.innerHTML = `<div class="mc-head"><span class="eyebrow">Frage ${i + 1} von ${list.length}</span><span class="score">Punkte: <b>${score}</b></span></div>
      <div class="mc-bar"><i style="width:${100 * i / list.length}%"></i></div>
      <h3 class="mc-q">${q.q}</h3>
      <div class="mc-opts">${order.map(k => `<button class="mc-opt" data-k="${k}">${q.a[k]}</button>`).join('')}</div>
      <p class="mc-why" aria-live="polite"></p>
      <div class="controls"><button class="btn primary" data-mc="next" hidden>${i + 1 < list.length ? 'Nächste Frage →' : 'Ergebnis anzeigen'}</button></div>`;
  }
  root.addEventListener('click', e => {
    const b = e.target.closest('.mc-opt, [data-mc]'); if (!b) return;
    if (b.dataset.mc === 'again') return start();
    if (b.dataset.mc === 'next') { i++; return show(); }
    if (answered) return;
    answered = true;
    const q = list[i], k = +b.dataset.k, ok = k === q.ok;
    if (ok) score++;
    $$('.mc-opt', root).forEach(x => { x.disabled = true; if (+x.dataset.k === q.ok) x.classList.add('ok'); });
    if (!ok) b.classList.add('err');
    $('.mc-why', root).innerHTML = (ok ? '<b class="good">Richtig!</b> ' : '<b class="bad">Leider falsch.</b> ') + (q.why || '');
    $('[data-mc="next"]', root).hidden = false;
    $('.score b', root).textContent = score;
  });
  start();
}

/* Sortieren: Karte antippen, dann Spalte antippen. cats: [{id, name}], items: [{t, c, why}]
   Nach „Prüfen“ erscheint unter jeder Karte die Begründung (why). */
function sorter(root, cats, items) {
  let sel = null;
  function build() {
    const its = shuffle(items.map((it, k) => ({...it, k})));
    root.innerHTML = `<div class="sort-pool" data-pool>${its.map(it => `<button class="sort-card" data-k="${it.k}">${it.t}${it.why ? `<span class="why">${it.why}</span>` : ''}</button>`).join('')}</div>
      <div class="sort-cols" style="--n:${cats.length}">${cats.map(c => `<div class="sort-col" data-c="${c.id}"><h3>${c.name}</h3><div class="sort-drop"></div></div>`).join('')}</div>
      <div class="controls"><button class="btn primary" data-s="check">Prüfen</button><button class="btn" data-s="solve">Lösung</button><button class="btn" data-s="reset">Neu mischen</button><span class="sort-fb" aria-live="polite"></span></div>`;
  }
  function check() {
    let ok = 0;
    $$('.sort-col .sort-card', root).forEach(c => { const good = items[+c.dataset.k].c === c.closest('.sort-col').dataset.c; c.classList.toggle('ok', good); c.classList.toggle('err', !good); if (good) ok++; });
    const left = $$('[data-pool] .sort-card', root).length;
    $('.sort-fb', root).innerHTML = `<b>${ok}</b> von ${items.length} richtig${left ? ` · ${left} noch nicht einsortiert` : ''}${ok === items.length ? ' – perfekt!' : ''}`;
  }
  root.addEventListener('click', e => {
    const card = e.target.closest('.sort-card'), col = e.target.closest('.sort-col'), act = e.target.closest('[data-s]');
    if (act) {
      if (act.dataset.s === 'reset') { build(); sel = null; return; }
      if (act.dataset.s === 'solve') $$('.sort-card', root).forEach(c => $(`.sort-col[data-c="${items[+c.dataset.k].c}"] .sort-drop`, root).appendChild(c));
      return check();
    }
    if (card) {
      if (sel === card) { card.classList.remove('sel'); sel = null; return; }
      if (sel) sel.classList.remove('sel');
      sel = card; card.classList.add('sel'); card.classList.remove('ok', 'err');
      return;
    }
    if (col && sel) { $('.sort-drop', col).appendChild(sel); sel.classList.remove('sel'); sel = null; return; }
    if (e.target.closest('[data-pool]') && sel) { $('[data-pool]', root).appendChild(sel); sel.classList.remove('sel'); sel = null; }
  });
  build();
}

/* Paare finden: Begriff ↔ Erklärung. pairs: [[begriff, erklärung], ...] */
function matcher(root, pairs) {
  let selL = null, selR = null, done = 0, tries = 0;
  function build() {
    done = 0; tries = 0;
    const L = shuffle(pairs.map((p, k) => k)), R = shuffle(pairs.map((p, k) => k));
    root.innerHTML = `<div class="match"><div class="match-col">${L.map(k => `<button class="match-card term" data-k="${k}">${pairs[k][0]}</button>`).join('')}</div>
      <div class="match-col">${R.map(k => `<button class="match-card def" data-k="${k}">${pairs[k][1]}</button>`).join('')}</div></div>
      <div class="controls"><span class="score">Gefunden: <b>0</b> / ${pairs.length}</span><button class="btn" data-m="reset">Neu mischen</button><span class="sort-fb" aria-live="polite"></span></div>`;
  }
  root.addEventListener('click', e => {
    if (e.target.closest('[data-m="reset"]')) return build();
    const c = e.target.closest('.match-card'); if (!c || c.classList.contains('ok')) return;
    const isL = c.classList.contains('term');
    if (isL) { if (selL) selL.classList.remove('sel'); selL = selL === c ? null : c; } else { if (selR) selR.classList.remove('sel'); selR = selR === c ? null : c; }
    if (selL) selL.classList.add('sel'); if (selR) selR.classList.add('sel');
    if (selL && selR) {
      tries++;
      const a = selL, b = selR;
      if (a.dataset.k === b.dataset.k) { a.classList.add('ok'); b.classList.add('ok'); done++; $('.sort-fb', root).textContent = done === pairs.length ? `Alle Paare gefunden – mit ${tries} Versuchen!` : 'Passt!'; }
      else { a.classList.add('err'); b.classList.add('err'); setTimeout(() => { a.classList.remove('err'); b.classList.remove('err'); }, 650); $('.sort-fb', root).textContent = 'Passt nicht. Versuch es noch einmal.'; }
      a.classList.remove('sel'); b.classList.remove('sel'); selL = selR = null;
      $('.score b', root).textContent = done;
    }
  });
  build();
}

/* Richtig oder falsch? items: [{t, ok, why}] */
function trueFalse(root, items, o = {}) {
  function build() {
    const ks = shuffle(items.map((x, k) => k)).slice(0, o.pick || items.length);
    root.innerHTML = `<ol class="tf-list">${ks.map(k => `<li data-k="${k}"><p class="tf-t">${items[k].t}</p><div class="tf-btns"><button class="btn" data-v="1">stimmt</button><button class="btn" data-v="0">stimmt nicht</button></div><p class="tf-why"></p></li>`).join('')}</ol>
      <div class="controls"><span class="score">Richtig: <b>0</b> / ${ks.length}</span><button class="btn" data-tf="reset">Neue Runde</button></div>`;
  }
  root.addEventListener('click', e => {
    if (e.target.closest('[data-tf]')) return build();
    const b = e.target.closest('[data-v]'); if (!b) return;
    const li = b.closest('li'); if (li.dataset.done) return;
    li.dataset.done = 1;
    const it = items[+li.dataset.k], good = (b.dataset.v === '1') === it.ok;
    li.classList.add(good ? 'ok' : 'err'); b.classList.add(good ? 'ok' : 'err');
    $$('[data-v]', li).forEach(x => x.disabled = true);
    $('.tf-why', li).innerHTML = (good ? '<b class="good">Richtig erkannt.</b> ' : '<b class="bad">Leider nein.</b> ') + `Die Aussage ${it.ok ? 'stimmt' : 'stimmt nicht'}. ${it.why || ''}`;
    $('.score b', root).textContent = $$('li.ok', root).length;
  });
  build();
}

/* EVA-Fließband: pipeline(root, statusEl, beispiele) mit {name, e:[icon, gerät, daten], v:[…], a:[…], text} */
function pipeline(root, segRoot, statusEl, ex) {
  root.classList.add('pipe');
  const stage = (k, t) => `<div class="pipe-stage ${k}" data-k="${k}"><span class="big">${k.toUpperCase()}</span><span class="nm">${t}</span><span class="dev"></span><span class="dv"></span><span class="dt"></span></div>`;
  root.innerHTML = stage('e', 'Eingabe') + '<div class="wire"><i class="pkt"></i></div>' + stage('v', 'Verarbeitung') + '<div class="wire"><i class="pkt"></i></div>' + stage('a', 'Ausgabe');
  let timer = null;
  function play(i) {
    const x = ex[i];
    for (const k of ['e', 'v', 'a']) { const s = $(`[data-k="${k}"]`, root); $('.dev', s).textContent = x[k][0]; $('.dv', s).textContent = x[k][1]; $('.dt', s).textContent = x[k][2]; }
    statusEl.innerHTML = x.text;
    clearTimeout(timer);
    const st = $$('.pipe-stage', root), wi = $$('.wire', root);
    st.forEach(s => s.classList.remove('lit')); wi.forEach(w => w.classList.remove('run'));
    const seq = [() => st[0].classList.add('lit'), () => wi[0].classList.add('run'), () => st[1].classList.add('lit'), () => wi[1].classList.add('run'), () => st[2].classList.add('lit')];
    let k = 0;
    const step = () => { if (k < seq.length) { seq[k++](); timer = setTimeout(step, RM.matches ? 0 : 700); } };
    step();
  }
  seg(segRoot, ex.map((x, i) => [i, x.name]), v => play(+v));
}

/* Zeitleiste. ev: [{y, lab, t, ic, cat, txt, eva}], cats: {id: name} */
function timeline(root, detail, ev, cats, o = {}) {
  const segs = o.segs; /* gestauchte Achse: [[jahr, anteil], …] stückweise linear */
  const minY = ev[0].y, maxY = o.end || 2030;
  const posBook = y => { for (let i = 0; i < segs.length - 1; i++) { const [y0, p0] = segs[i], [y1, p1] = segs[i + 1]; if (y <= y1) return p0 + (p1 - p0) * (y - y0) / (y1 - y0); } return segs[segs.length - 1][1]; };
  const posTrue = y => (y - minY) / (maxY - minY);
  let mode = 'book', sel = 0, filt = null;
  const order = ev.map((e, i) => i).sort((a, b) => ev[a].y - ev[b].y);
  root.innerHTML = `<div class="zl-tools"><div class="zl-filter"></div><div class="zl-scale"></div></div>
    <div class="zl-scroll"><div class="zl"><div class="zl-axis"></div><div class="zl-brace">↑ fast alle Erfindungen<br>liegen hier ganz rechts</div></div></div>`;
  const zl = $('.zl', root);
  /* Beschriftungen abwechselnd oben/unten in Etagen, damit sich nichts überlappt */
  const lanes = {up: [], dn: []};
  order.forEach((i, n) => {
    const e = ev[i], side = n % 2 ? 'dn' : 'up';
    const b = document.createElement('button');
    b.className = `zl-ev c-${e.cat}`; b.dataset.i = i;
    b.innerHTML = `<span class="lab"><span class="ic">${e.ic}</span><span>${e.lab}<b>${e.t}</b></span></span><span class="stem"></span><span class="pin"></span>`;
    b.setAttribute('aria-label', `${e.lab}, ${e.t}`);
    e.side = side; e.el = b; zl.appendChild(b);
  });
  ev.filter(e => e.keep).forEach(e => e.el.classList.add('keep'));
  const axis = $('.zl-axis', zl), brace = $('.zl-brace', zl);
  const ticks = (o.ticks || []).map(([y, t]) => { const d = document.createElement('span'); d.className = 'zl-tick'; d.textContent = t; d.dataset.y = y; zl.appendChild(d); return d; });
  function layout() {
    /* Etagenhöhe aus der tatsächlichen Beschriftungsgröße (Beamer skaliert die Schrift) */
    const lh = Math.max(...ev.map(e => $('.lab', e.el).offsetHeight || 0), 30), LH = lh + 8, LV = 6, TK = 24;
    const W = zl.clientWidth, pad = Math.max(W * .015, 80), span = W - 2 * pad;
    const P = y => pad + span * (mode === 'book' ? posBook(y) : posTrue(y));
    lanes.up = []; lanes.dn = [];
    const used = {up: 0, dn: 0};
    let last = 'dn';
    const laneOf = (L, x, w) => { let k = 0; while (L[k] !== undefined && L[k] > x - w / 2) k++; return k; };
    for (const i of order) {
      /* Seite mit der niedrigeren freien Etage wählen, bei Gleichstand abwechseln */
      const e = ev[i], x = P(e.y), w = ($('.lab', e.el).offsetWidth || 0) + 6;
      const ku = laneOf(lanes.up, x, w), kd = laneOf(lanes.dn, x, w);
      e.side = ku < kd ? 'up' : kd < ku ? 'dn' : (last === 'up' ? 'dn' : 'up'); last = e.side;
      const k = e.side === 'up' ? ku : kd;
      if (w > 6) { lanes[e.side][k] = x + w / 2; used[e.side] = Math.max(used[e.side], Math.min(k, LV - 1)); }
      e.x = x; e.k = Math.min(k, LV - 1);
    }
    const AX = 14 + used.up * LH + lh + 12, H = AX + TK + used.dn * LH + lh + 20;
    zl.style.height = H + 'px'; axis.style.top = (AX - 8) + 'px'; brace.style.top = (AX + 16) + 'px';
    ticks.forEach(t => { t.style.left = P(+t.dataset.y) + 'px'; t.style.top = (AX + 10) + 'px'; t.hidden = mode !== 'book'; });
    for (const i of order) {
      const e = ev[i], el = e.el;
      el.style.left = e.x + 'px';
      $('.stem', el).style.height = ((e.side === 'up' ? 12 : TK) + e.k * LH) + 'px';
      if (e.side === 'up') { el.style.flexDirection = 'column'; el.style.top = ''; el.style.bottom = (H - AX) + 'px'; $('.pin', el).style.cssText = 'bottom:-6px'; }
      else { el.style.flexDirection = 'column-reverse'; el.style.bottom = ''; el.style.top = AX + 'px'; $('.pin', el).style.cssText = 'top:-6px'; }
    }
  }
  function show(i) {
    sel = i; const e = ev[i];
    $$('.zl-ev', zl).forEach(b => b.classList.toggle('sel', +b.dataset.i === i));
    const k = order.indexOf(i);
    detail.className = `zl-detail c-${e.cat}`;
    detail.innerHTML = `<div class="ic">${e.ic}</div><div><span class="yr">${e.t}</span> <span class="tag">${cats[e.cat]}</span><h3>${e.lab}</h3><p>${e.txt}</p>${e.eva ? `<div class="eva"><b>EVA-Blick:</b> ${e.eva}</div>` : ''}
      <div class="nav"><button class="btn" data-zl="-1" ${k === 0 ? 'disabled' : ''}>◀ früher</button><button class="btn primary" data-zl="1" ${k === order.length - 1 ? 'disabled' : ''}>später ▶</button></div></div>`;
    const sc = $('.zl-scroll', root), el = e.el;
    sc.scrollTo({left: el.offsetLeft - sc.clientWidth / 2, behavior: RM.matches ? 'auto' : 'smooth'});
  }
  zl.addEventListener('click', e => { const b = e.target.closest('.zl-ev'); if (b) show(+b.dataset.i); });
  detail.addEventListener('click', e => { const b = e.target.closest('[data-zl]'); if (b) show(order[clamp(order.indexOf(sel) + +b.dataset.zl, 0, order.length - 1)]); });
  const fl = $('.zl-filter', root);
  fl.innerHTML = Object.entries(cats).map(([k, n]) => `<button class="c-${k}" data-f="${k}" aria-pressed="false">${n}</button>`).join('');
  fl.addEventListener('click', e => {
    const b = e.target.closest('[data-f]'); if (!b) return;
    filt = filt === b.dataset.f ? null : b.dataset.f;
    $$('[data-f]', fl).forEach(x => x.setAttribute('aria-pressed', x.dataset.f === filt));
    ev.forEach(x => x.el.classList.toggle('dim', !!filt && x.cat !== filt));
  });
  if (o.noScale) brace.remove(); else seg($('.zl-scale', root), [['book', 'Zeitachse gestaucht'], ['true', 'maßstabsgetreu']], v => {
    mode = v; zl.classList.toggle('true', v === 'true'); zl.style.minWidth = v === 'true' ? '100%' : '';
    layout();
    const sc = $('.zl-scroll', root); if (v === 'true') sc.scrollLeft = 0; else if (ev[sel]) sc.scrollLeft = ev[sel].el.offsetLeft - sc.clientWidth / 2;
    if (o.onMode) o.onMode(v);
  });
  onShow.push(id => { if (id === o.station) requestAnimationFrame(() => { layout(); if (!detail.innerHTML) show(order[0]); }); });
  const relayout = () => { if (!root.closest('.station').hidden) layout(); };
  addEventListener('resize', relayout);
  /* Schriften laden evtl. erst nach dem ersten Layout – dann neu messen */
  if (document.fonts) document.fonts.ready.then(() => requestAnimationFrame(relayout));
}

/* Reihenfolge-Puzzle: n zufällige Ereignisse in die richtige zeitliche Reihenfolge klicken */
function orderPuzzle(root, ev, n = 5) {
  let pick = [];
  const card = (e, i) => `<button class="pz-card c-${e.cat}" data-i="${i}"><span class="ic">${e.ic}</span>${e.lab}<small>${e.t}</small></button>`;
  function build() {
    const ys = new Set(); pick = [];
    for (const i of shuffle(ev.map((e, i) => i))) { if (pick.length >= n) break; if (ys.has(ev[i].y)) continue; ys.add(ev[i].y); pick.push(i); }
    root.innerHTML = `<p class="eyebrow">Ausgangslage</p><div class="pz-pool">${pick.map(i => card(ev[i], i)).join('')}</div>
      <p class="eyebrow" style="margin-top:.8rem">Deine Reihenfolge (früheste zuerst)</p><div class="pz-slots"></div>
      <div class="controls"><button class="btn primary" data-pz="check">Prüfen</button><button class="btn" data-pz="new">Neue Runde</button><span class="sort-fb" aria-live="polite"></span></div>`;
  }
  root.classList.add('puzzle');
  root.addEventListener('click', e => {
    const a = e.target.closest('[data-pz]');
    if (a && a.dataset.pz === 'new') return build();
    if (a) {
      const placed = $$('.pz-slots .pz-card', root);
      if (placed.length < pick.length) { $('.sort-fb', root).textContent = 'Lege zuerst alle Karten ab.'; return; }
      const sorted = pick.slice().sort((x, y) => ev[x].y - ev[y].y);
      let ok = 0; placed.forEach((c, k) => { const g = +c.dataset.i === sorted[k]; c.classList.toggle('ok', g); c.classList.toggle('err', !g); if (g) ok++; });
      $('.sort-fb', root).innerHTML = ok === pick.length ? '<b class="good">Perfekt – alles in der richtigen Reihenfolge!</b>' : `<b>${ok}</b> von ${pick.length} am richtigen Platz. Tippe Karten an, um sie zurückzulegen.`;
      return;
    }
    const c = e.target.closest('.pz-card'); if (!c) return;
    c.classList.remove('ok', 'err');
    (c.closest('.pz-pool') ? $('.pz-slots', root) : $('.pz-pool', root)).appendChild(c);
  });
  build();
}

/* Was war zuerst? Zwei Ereignisse, das frühere antippen */
function duel(root, ev) {
  let a, b, n = 0, ok = 0, streak = 0, lock = false;
  root.classList.add('puzzle');
  function next() {
    lock = false;
    do { a = Math.floor(Math.random() * ev.length); b = Math.floor(Math.random() * ev.length); } while (a === b || ev[a].y === ev[b].y || ev[a].t === ev[b].t);
    const c = i => `<button class="pz-card c-${ev[i].cat}" data-i="${i}"><span class="ic">${ev[i].ic}</span>${ev[i].lab}<small>${ev[i].t}</small></button>`;
    $('.duel', root).innerHTML = c(a) + '<span class="vs">oder</span>' + c(b);
    $('.sort-fb', root).textContent = '';
  }
  root.innerHTML = `<div class="mc-head"><b>Was wurde zuerst erfunden?</b><span class="score">Richtig: <b>0</b> / 0 · Serie: <b>0</b></span></div><div class="duel"></div>
    <div class="controls"><button class="btn primary" data-d="next">Nächstes Paar →</button><span class="sort-fb" aria-live="polite"></span></div>`;
  root.addEventListener('click', e => {
    if (e.target.closest('[data-d]')) return next();
    const c = e.target.closest('.pz-card'); if (!c || lock) return;
    lock = true; n++;
    const i = +c.dataset.i, j = i === a ? b : a, good = ev[i].y < ev[j].y;
    if (good) { ok++; streak++; } else streak = 0;
    $$('.pz-card', root).forEach(x => x.classList.add(+x.dataset.i === (good ? i : j) ? 'ok' : 'err'));
    $('.score', root).innerHTML = `Richtig: <b>${ok}</b> / ${n} · Serie: <b>${streak}</b>`;
    $('.sort-fb', root).innerHTML = good ? '<b class="good">Richtig!</b>' : `<b class="bad">Nein:</b> ${ev[j].lab} (${ev[j].t}) war früher.`;
  });
  next();
}

/* ================= weitere Bausteine (wie in den Chemie-Reihen) ================= */
const numDE = (v, d = 2) => (+v).toLocaleString('de-DE', {maximumFractionDigits: d});
const parseNum = s => parseFloat(String(s).trim().replace(/\s/g, '').replace(',', '.'));
const randInt = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
const pick = a => a[Math.floor(Math.random() * a.length)];

/* Lückentext: {richtig|falsch|falsch} wird zu einem Auswahlfeld */
function cloze(root, text) {
  const ans = [];
  const body = text.replace(/\{([^}]+)\}/g, (m, g) => {
    const opts = g.split('|'), k = ans.length; ans.push(opts[0]);
    return `<select data-k="${k}" aria-label="Lücke ${k + 1}"><option value="">…</option>${shuffle(opts.slice()).map(x => `<option>${x}</option>`).join('')}</select>`;
  });
  root.classList.add('cloze');
  root.innerHTML = `<div class="cloze-text">${body}</div>
    <div class="controls"><button class="btn primary" data-c="check">Prüfen</button><button class="btn" data-c="solve">Lösung zeigen</button><button class="btn" data-c="reset">Zurücksetzen</button><span class="sort-fb" aria-live="polite"></span></div>`;
  root.addEventListener('change', e => { if (e.target.matches('select')) e.target.className = ''; });
  root.addEventListener('click', e => {
    const b = e.target.closest('[data-c]'); if (!b) return;
    const sels = $$('select', root), fb = $('.sort-fb', root);
    if (b.dataset.c === 'reset') { sels.forEach(s => { s.value = ''; s.className = ''; }); fb.textContent = ''; return; }
    if (b.dataset.c === 'solve') sels.forEach(s => s.value = ans[+s.dataset.k]);
    let ok = 0, empty = 0;
    sels.forEach(s => { const g = s.value === ans[+s.dataset.k]; if (!s.value) empty++; s.className = s.value ? (g ? 'ok' : 'err') : ''; if (g) ok++; });
    fb.innerHTML = ok === sels.length ? '<b class="good">Alles richtig!</b>' : `<b>${ok}</b> von ${sels.length} Lücken richtig${empty ? ` · ${empty} noch leer` : ''}.`;
  });
}

/* Aufgaben mit Eingabefeldern. make(i) -> {q, fields: [{l, a, unit, tol, wide}], hint, key, tag}
   a: Zahl (Toleranz tol) oder Text bzw. Liste erlaubter Texte (ohne Leerzeichen, Groß/klein egal) */
function taskSet(root, make, o = {}) {
  const n = o.n || 6;
  let tasks = [];
  root.innerHTML = `<div class="tasks-head"><div class="score"></div><div class="controls" style="margin:0"><button class="btn" data-ts="all">Alle prüfen</button>${o.fixed ? '' : '<button class="btn primary" data-ts="new">Neue Aufgaben</button>'}</div></div><div class="tasks"></div>`;
  const box = $('.tasks', root);
  const norm = s => String(s).toLowerCase().replace(/\s+/g, '').replace(/[–−‐]/g, '-');
  const isNum = f => typeof f.a === 'number';
  function okField(f, v) {
    if (String(v).trim() === '') return null;
    if (isNum(f)) { const x = parseNum(v); return isFinite(x) && Math.abs(x - f.a) <= (f.tol ?? 0) + 1e-9; }
    return (Array.isArray(f.a) ? f.a : [f.a]).some(a => norm(a) === norm(v));
  }
  const show = f => isNum(f) ? numDE(f.a, 3) : (Array.isArray(f.a) ? f.a[0] : f.a);
  function newTasks() {
    const seen = new Set(); tasks = []; let guard = 0;
    while (tasks.length < n && guard++ < 400) { const t = make(tasks.length); const key = t.key || t.q; if (seen.has(key) && guard < 300) continue; seen.add(key); tasks.push(t); }
    box.innerHTML = tasks.map((t, i) => `<div class="task" data-i="${i}"><header><span>Aufgabe ${i + 1}</span>${t.tag ? `<span>${t.tag}</span>` : ''}</header>
      <div class="task-q">${t.q}</div>
      <div class="fields">${t.fields.map((f, j) => `<label${f.wide || t.fields.length === 1 ? ' class="wide"' : ''}><i>${f.l}</i><span class="inrow"><input type="text" ${isNum(f) ? 'inputmode="decimal"' : ''} data-j="${j}" autocomplete="off" spellcheck="false">${f.unit ? `<small>${f.unit}</small>` : ''}</span></label>`).join('')}</div>
      <div class="actions"><button class="btn primary" data-act="check">Prüfen</button><button class="btn" data-act="solve">Lösung</button></div><p class="fb" aria-live="polite"></p></div>`).join('');
    score();
  }
  function check(i) {
    const t = tasks[i], card = $(`.task[data-i="${i}"]`, box), fb = $('.fb', card);
    const ins = $$('input', card), res = ins.map((x, j) => okField(t.fields[j], x.value));
    if (res.every(r => r === null)) { fb.className = 'fb'; fb.textContent = 'Trage zuerst deine Antwort ein.'; return; }
    ins.forEach((x, j) => x.className = res[j] === null ? '' : res[j] ? 'ok' : 'err');
    t.ok = res.every(r => r === true);
    fb.className = 'fb ' + (t.ok ? 'ok' : 'err');
    fb.innerHTML = t.ok ? (t.good || 'Richtig!') : (t.hint || 'Noch nicht richtig. Versuch es noch einmal.');
    card.classList.toggle('ok', t.ok); score();
  }
  function solve(i) { const t = tasks[i], card = $(`.task[data-i="${i}"]`, box); $$('input', card).forEach((x, j) => x.value = show(t.fields[j])); check(i); }
  function score() { $('.score', root).innerHTML = `Richtig gelöst: <b>${tasks.filter(t => t.ok).length}</b> von ${tasks.length}`; }
  box.addEventListener('click', e => { const b = e.target.closest('[data-act]'); if (!b) return; const i = +b.closest('.task').dataset.i; b.dataset.act === 'check' ? check(i) : solve(i); });
  box.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.matches('input')) check(+e.target.closest('.task').dataset.i); });
  root.addEventListener('click', e => { const b = e.target.closest('[data-ts]'); if (!b) return; if (b.dataset.ts === 'new') newTasks(); else tasks.forEach((t, i) => { if ($$(`.task[data-i="${i}"] input`, box).some(x => x.value !== '')) check(i); }); });
  newTasks();
  return {renew: newTasks};
}

/* Tabelle mit verdeckbaren Feldern (td.q): antippen deckt auf */
function quizTable(table, bQuiz, bAll) {
  table.classList.add('quiz');
  table.addEventListener('click', e => { const td = e.target.closest('td.q'); if (td) td.classList.add('shown'); });
  if (bQuiz) bQuiz.onclick = () => $$('td.q', table).forEach(td => td.classList.remove('shown'));
  if (bAll) bAll.onclick = () => $$('td.q', table).forEach(td => td.classList.add('shown'));
}

/* Schritt-für-Schritt-Ablauf: Buttons „Zurück / Weiter“ mit Zähler */
function stepper(root, n, onStep, o = {}) {
  let k = 0;
  root.innerHTML = `<button class="btn" data-st="-1">← Zurück</button><span class="st-pos score"></span><button class="btn primary" data-st="1">${o.next || 'Weiter'} →</button>${o.reset !== false ? '<button class="btn" data-st="0">Von vorn</button>' : ''}`;
  root.classList.add('controls');
  const upd = () => { $('.st-pos', root).textContent = `Schritt ${k + 1} / ${n}`; $('[data-st="-1"]', root).disabled = k === 0; $('[data-st="1"]', root).disabled = k === n - 1; onStep(k); };
  root.addEventListener('click', e => { const b = e.target.closest('[data-st]'); if (!b) return; const d = +b.dataset.st; k = d === 0 ? 0 : clamp(k + d, 0, n - 1); upd(); });
  upd();
  return {go(i) { k = clamp(i, 0, n - 1); upd(); }, get k() { return k; }};
}

/* „Ich kann …“-Liste zur Selbsteinschätzung: items [{t, href}] */
function selfCheck(root, items) {
  root.classList.add('selfcheck');
  root.innerHTML = items.map((it, k) => `<li><span>${it.t}</span><span class="sc-r"><span class="seg" data-k="${k}"><button aria-pressed="false" data-v="2">sicher</button><button aria-pressed="false" data-v="1">geht so</button><button aria-pressed="false" data-v="0">unsicher</button></span>${it.href ? `<a href="${it.href}">wiederholen →</a>` : ''}</span></li>`).join('') + '<li class="sc-sum"><span>Markiere ehrlich. Wo du unsicher bist, führt der Link zur passenden Station.</span><b class="sc-out score"></b></li>';
  root.addEventListener('click', e => {
    const b = e.target.closest('[data-v]'); if (!b) return;
    $$('button', b.parentElement).forEach(x => x.setAttribute('aria-pressed', x === b));
    const vals = $$('.seg', root).map(s => { const p = $('[aria-pressed="true"]', s); return p ? +p.dataset.v : null; }).filter(v => v !== null);
    $('.sc-out', root).textContent = `${vals.filter(v => v === 2).length} sicher · ${vals.filter(v => v === 1).length} geht so · ${vals.filter(v => v === 0).length} unsicher`;
  });
}

/* Reihenfolge herstellen: Karten nacheinander antippen. steps: [text, …] in richtiger Reihenfolge */
function orderSteps(root, steps, o = {}) {
  root.classList.add('puzzle');
  function build() {
    root.innerHTML = `<div class="pz-pool">${shuffle(steps.map((s, i) => i)).map(i => `<button class="pz-card step" data-i="${i}">${steps[i]}</button>`).join('')}</div>
      <p class="eyebrow" style="margin-top:.8rem">${o.label || 'Deine Reihenfolge'}</p><div class="pz-slots"></div>
      <div class="controls"><button class="btn primary" data-pz="check">Prüfen</button><button class="btn" data-pz="solve">Lösung</button><button class="btn" data-pz="new">Neu mischen</button><span class="sort-fb" aria-live="polite"></span></div>`;
  }
  root.addEventListener('click', e => {
    const a = e.target.closest('[data-pz]');
    if (a && a.dataset.pz === 'new') return build();
    if (a && a.dataset.pz === 'solve') { const sl = $('.pz-slots', root); steps.forEach((s, i) => sl.appendChild($(`.pz-card[data-i="${i}"]`, root))); }
    if (a) {
      const placed = $$('.pz-slots .pz-card', root);
      if (placed.length < steps.length) { $('.sort-fb', root).textContent = 'Lege zuerst alle Karten ab.'; return; }
      let ok = 0; placed.forEach((c, k) => { const g = +c.dataset.i === k; c.classList.toggle('ok', g); c.classList.toggle('err', !g); if (g) ok++; });
      $('.sort-fb', root).innerHTML = ok === steps.length ? '<b class="good">Perfekt – richtige Reihenfolge!</b>' : `<b>${ok}</b> von ${steps.length} am richtigen Platz.`;
      return;
    }
    const c = e.target.closest('.pz-card'); if (!c) return;
    c.classList.remove('ok', 'err');
    (c.closest('.pz-pool') ? $('.pz-slots', root) : $('.pz-pool', root)).appendChild(c);
  });
  build();
}

/* Klickbares Schaubild: Elemente mit data-part="id" im SVG/HTML. parts: [{id, n, t, tag}]
   o.find = true ergänzt einen Modus „Finden“: Ein Begriff wird genannt, das passende Teil muss angetippt werden. */
function explorer(fig, panel, parts, o = {}) {
  const P = Object.fromEntries(parts.map(p => [p.id, p]));
  let mode = 'explore', target = null, ok = 0, tries = 0, order = [];
  fig.classList.add('xp');
  const els = id => $$(`[data-part="${id}"]`, fig);
  $$('[data-part]', fig).forEach(el => { el.setAttribute('tabindex', '0'); el.setAttribute('role', 'button'); if (P[el.dataset.part]) el.setAttribute('aria-label', P[el.dataset.part].n); });
  const intro = o.intro || 'Tippe ein Bauteil an.';
  function mark(id) { $$('[data-part]', fig).forEach(el => el.classList.toggle('on', el.dataset.part === id)); }
  function nextTarget() {
    if (!order.length) order = shuffle(parts.map(p => p.id));
    target = order.pop();
    panel.innerHTML = `<span class="eyebrow">Finden</span><h3>Wo ist: ${P[target].n}?</h3><p class="score">Richtig: <b>${ok}</b> / ${tries}</p>`;
  }
  function pickPart(id) {
    if (!P[id]) return;
    if (mode === 'explore') { mark(id); const p = P[id]; panel.innerHTML = `<span class="eyebrow">${o.label || 'Bauteil'}</span><h3>${p.n}</h3>${p.tag ? `<span class="tag ${p.tagc || ''}">${p.tag}</span>` : ''}<p>${p.t}</p>`; return; }
    tries++;
    const good = id === target; if (good) ok++;
    mark(target);
    els(id).forEach(el => { el.classList.add(good ? 'hit' : 'miss'); setTimeout(() => el.classList.remove('hit', 'miss'), 700); });
    panel.innerHTML = `<span class="eyebrow">Finden</span><h3>${good ? '<span class="good">Richtig!</span>' : `<span class="bad">Das war: ${P[id].n}</span>`}</h3><p>${P[target].n}: ${P[target].t}</p><p class="score">Richtig: <b>${ok}</b> / ${tries}</p><div class="controls"><button class="btn primary" data-xp="next">Nächster Begriff →</button></div>`;
  }
  fig.addEventListener('click', e => { const el = e.target.closest('[data-part]'); if (el) pickPart(el.dataset.part); });
  fig.addEventListener('keydown', e => { const el = e.target.closest('[data-part]'); if (el && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); pickPart(el.dataset.part); } });
  panel.addEventListener('click', e => { if (e.target.closest('[data-xp="next"]')) { mark(null); nextTarget(); } });
  const start = () => { mark(null); panel.innerHTML = `<p><b>${intro}</b></p>`; };
  if (o.modeRoot) seg(o.modeRoot, [['explore', 'Erkunden'], ['find', 'Finden']], v => { mode = v; ok = tries = 0; order = []; v === 'find' ? (mark(null), nextTarget()) : start(); });
  else start();
}

/* Bewertungstabelle mit Punkten 1–5. rows: [Fähigkeit, …], cols: [Spaltenname, …] */
function rating(root, rows, cols, o = {}) {
  const val = rows.map(() => cols.map(() => 0));
  root.classList.add('rating');
  root.innerHTML = `<div class="table-wrap"><table class="cmp"><thead><tr><th>${o.head || 'Fähigkeit'}</th>${cols.map(c => `<th>${c}</th>`).join('')}</tr></thead><tbody>${rows.map((r, i) => `<tr><th>${r}</th>${cols.map((c, j) => `<td><span class="dots" data-r="${i}" data-c="${j}">${[1, 2, 3, 4, 5].map(v => `<button data-v="${v}" aria-label="${v} Punkte"></button>`).join('')}</span></td>`).join('')}</tr>`).join('')}</tbody>
    <tfoot><tr><th>Summe</th>${cols.map((c, j) => `<td class="sum" data-c="${j}">0</td>`).join('')}</tr></tfoot></table></div>`;
  root.addEventListener('click', e => {
    const b = e.target.closest('.dots button'); if (!b) return;
    const d = b.parentElement, i = +d.dataset.r, j = +d.dataset.c, v = +b.dataset.v;
    val[i][j] = val[i][j] === v ? 0 : v;
    $$('button', d).forEach(x => x.classList.toggle('on', +x.dataset.v <= val[i][j]));
    cols.forEach((c, k) => $(`.sum[data-c="${k}"]`, root).textContent = val.reduce((s, r) => s + r[k], 0));
  });
}

/* Canvas-Animation, die nur läuft, solange die Station sichtbar ist. draw(ctx, w, h, t) */
function loopCanvas(cv, station, draw) {
  let t = 0, last = performance.now();
  function frame(now) {
    const dt = Math.min(.05, (now - last) / 1000); last = now;
    if (STATIONS[cur] === station && cv.clientWidth) {
      t += RM.matches ? 0 : dt;
      const dpr = Math.min(devicePixelRatio || 1, 2), w = cv.clientWidth, h = cv.clientHeight;
      if (cv.width !== Math.round(w * dpr) || cv.height !== Math.round(h * dpr)) { cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); }
      const ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, w, h);
      draw(ctx, w, h, t);
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}

/* ================= Scratch-Simulator =================
   scratch(root, script, o): script = Liste von Blöcken, z. B.
   [{op:'flag'}, {op:'repeat', n:4, body:[{op:'move', n:100}, {op:'turn', n:90}]}]
   Blöcke: flag, move n, turn n, turnL n, goto x y, glide s (zu Zufallsposition), say text s, think text, wait s, costume, costume2,
           sound, bounce, show, hide, size n, repeat n body, forever body, until cond body, if cond body, ifelse cond body else, ask text
   Bedingungen: {c:'edge'} Rand berührt · {c:'mouse'} Mauszeiger berührt · {c:'answer', v} Antwort = v · {c:'var', name, v} Variable = v
   o: {pen: true} zeichnet eine Spur · {vars: {Ampel: ['Rot','Grün']}} Schalter für Variablen · {x, y, dir} Startwerte
   Klasse 7: Variablen mit Zahlen: o.nums {Punkte: 0} (Anzeige auf der Bühne) und Blöcke
     setvar name v · changevar name n · setrand name a b (Zufallszahl) · setans name (Antwort speichern) · sayvar name s · sayjoin text name s · changex n · changey n
   Vergleich als Bedingung: {c:'cmp', a:'Punkte'|'Antwort'|'x'|'y', op:'>'|'<'|'=', v} oder statt v eine Variable b:'Zahl' */
function scratch(root, script, o = {}) {
  const CAT = {flag: 'ev', move: 'mo', turn: 'mo', turnL: 'mo', goto: 'mo', glide: 'mo', bounce: 'mo', say: 'lo', think: 'lo', costume: 'lo', costume2: 'lo', show: 'lo', hide: 'lo', size: 'lo', sound: 'so',
    wait: 'ct', repeat: 'ct', forever: 'ct', until: 'ct', if: 'ct', ifelse: 'ct', ask: 'se', setvar: 'va', changevar: 'va', setrand: 'va', setans: 'va', sayvar: 'lo', sayjoin: 'lo', changex: 'mo', changey: 'mo'};
  const inp = (b, k, w = 3) => `<input class="sb-v" data-k="${k}" value="${b[k]}" size="${w}" aria-label="${k}">`;
  const cond = c => !c ? '' : c.c === 'edge' ? '<span class="sb-cond se">wird <i>Rand</i> berührt?</span>' : c.c === 'mouse' ? '<span class="sb-cond se">wird <i>Mauszeiger</i> berührt?</span>'
    : c.c === 'answer' ? `<span class="sb-cond op"><span class="sb-rep se">Antwort</span> = <i>${c.v}</i></span>`
    : c.c === 'cmp' ? `<span class="sb-cond op"><span class="sb-rep ${c.a === 'Antwort' ? 'se' : c.a === 'x' || c.a === 'y' ? 'mo' : 'va'}">${c.a === 'x' ? 'x-Position' : c.a === 'y' ? 'y-Position' : c.a}</span> ${c.op === '<' ? '&lt;' : c.op === '>' ? '&gt;' : '='} ${c.b ? `<span class="sb-rep va">${c.b}</span>` : `<i>${c.v}</i>`}</span>`
    : `<span class="sb-cond op"><span class="sb-rep va">${c.name}</span> = <i>${c.v}</i></span>`;
  function html(list, path) {
    return list.map((b, i) => {
      const p = path + i, c = CAT[b.op];
      const body = k => `<div class="sb-in">${html(b[k] || [], p + '.' + k + '.')}</div>`;
      switch (b.op) {
        case 'flag': return `<div class="sb hat ev" data-p="${p}">Wenn <span class="flag">⚑</span> angeklickt wird</div>`;
        case 'move': return `<div class="sb ${c}" data-p="${p}">gehe ${inp(b, 'n')} er Schritt</div>`;
        case 'turn': return `<div class="sb ${c}" data-p="${p}">drehe dich ↻ um ${inp(b, 'n')} Grad</div>`;
        case 'turnL': return `<div class="sb ${c}" data-p="${p}">drehe dich ↺ um ${inp(b, 'n')} Grad</div>`;
        case 'goto': return `<div class="sb ${c}" data-p="${p}">gehe zu x: ${inp(b, 'x')} y: ${inp(b, 'y')}</div>`;
        case 'glide': return `<div class="sb ${c}" data-p="${p}">gleite in ${inp(b, 's', 2)} Sek. zu <i>Zufallsposition</i></div>`;
        case 'bounce': return `<div class="sb ${c}" data-p="${p}">pralle vom Rand ab</div>`;
        case 'say': return `<div class="sb ${c}" data-p="${p}">sage ${inp(b, 'text', 10)}${b.s != null ? ` für ${inp(b, 's', 2)} Sekunden` : ''}</div>`;
        case 'think': return `<div class="sb ${c}" data-p="${p}">denke ${inp(b, 'text', 10)}</div>`;
        case 'costume': return `<div class="sb ${c}" data-p="${p}">wechsle zum nächsten Kostüm</div>`;
        case 'costume2': return `<div class="sb ${c}" data-p="${p}">wechsle zu Kostüm <i>Kostüm2</i></div>`;
        case 'show': return `<div class="sb ${c}" data-p="${p}">zeige dich</div>`;
        case 'hide': return `<div class="sb ${c}" data-p="${p}">verstecke dich</div>`;
        case 'size': return `<div class="sb ${c}" data-p="${p}">setze Größe auf ${inp(b, 'n')} %</div>`;
        case 'sound': return `<div class="sb ${c}" data-p="${p}">spiele Klang <i>Miau</i></div>`;
        case 'wait': return `<div class="sb ${c}" data-p="${p}">warte ${inp(b, 's', 2)} Sekunden</div>`;
        case 'ask': return `<div class="sb ${c}" data-p="${p}">frage ${inp(b, 'text', 12)} und warte</div>`;
        case 'repeat': return `<div class="sb ${c} cb" data-p="${p}"><div class="sb-h">wiederhole ${inp(b, 'n')} mal</div>${body('body')}<div class="sb-f">↻</div></div>`;
        case 'forever': return `<div class="sb ${c} cb" data-p="${p}"><div class="sb-h">wiederhole fortlaufend</div>${body('body')}<div class="sb-f">↻</div></div>`;
        case 'until': return `<div class="sb ${c} cb" data-p="${p}"><div class="sb-h">wiederhole bis ${cond(b.cond)}</div>${body('body')}<div class="sb-f">↻</div></div>`;
        case 'if': return `<div class="sb ${c} cb" data-p="${p}"><div class="sb-h">falls ${cond(b.cond)}, dann</div>${body('body')}<div class="sb-f"></div></div>`;
        case 'ifelse': return `<div class="sb ${c} cb" data-p="${p}"><div class="sb-h">falls ${cond(b.cond)}, dann</div>${body('body')}<div class="sb-m">sonst</div>${body('else')}<div class="sb-f"></div></div>`;
        case 'setvar': return `<div class="sb ${c}" data-p="${p}">setze <i>${b.name}</i> auf ${inp(b, 'v', 4)}</div>`;
        case 'changevar': return `<div class="sb ${c}" data-p="${p}">ändere <i>${b.name}</i> um ${inp(b, 'n')}</div>`;
        case 'setrand': return `<div class="sb ${c}" data-p="${p}">setze <i>${b.name}</i> auf <span class="sb-rep op">Zufallszahl von ${inp(b, 'a', 2)} bis ${inp(b, 'b', 2)}</span></div>`;
        case 'setans': return `<div class="sb ${c}" data-p="${p}">setze <i>${b.name}</i> auf <span class="sb-rep se">Antwort</span></div>`;
        case 'sayvar': return `<div class="sb ${c}" data-p="${p}">sage <span class="sb-rep va">${b.name}</span>${b.s != null ? ` für ${inp(b, 's', 2)} Sekunden` : ''}</div>`;
        case 'sayjoin': return `<div class="sb ${c}" data-p="${p}">sage <span class="sb-rep op">verbinde ${inp(b, 'text', 10)} und <span class="sb-rep va">${b.name}</span></span>${b.s != null ? ` für ${inp(b, 's', 2)} Sekunden` : ''}</div>`;
        case 'changex': return `<div class="sb ${c}" data-p="${p}">ändere x um ${inp(b, 'n')}</div>`;
        case 'changey': return `<div class="sb ${c}" data-p="${p}">ändere y um ${inp(b, 'n')}</div>`;
      }
      return '';
    }).join('');
  }
  const vars = o.vars || {};
  const V = Object.fromEntries(Object.entries(vars).map(([k, v]) => [k, v[0]]));
  const nums = o.nums || {};
  Object.assign(V, nums);
  root.classList.add('scr');
  root.innerHTML = `<div class="scr-code"><div class="scr-script">${html(script, '')}</div></div>
    <div class="scr-right"><div class="scr-bar"><button class="scr-go" title="Grüne Fahne">⚑</button><button class="scr-stop" title="Stopp">⬣</button><span class="scr-xy mono"></span>
      ${Object.keys(vars).map(k => `<button class="btn scr-var" data-var="${k}">${k}: <b>${V[k]}</b></button>`).join('')}${Object.keys(nums).map(k => `<span class="scr-mon" data-mon="${k}">${k} <b>${V[k]}</b></span>`).join('')}</div>
      <div class="scr-stage"><canvas class="scr-pen"></canvas><div class="scr-sprite"><span class="scr-cat">🐈</span><span class="scr-bubble" hidden></span></div><form class="scr-ask" hidden><span></span><input aria-label="Antwort"><button class="btn primary">✓</button></form></div>
      <p class="status scr-status">Klicke auf die grüne Fahne.</p></div>`;
  const stage = $('.scr-stage', root), spr = $('.scr-sprite', root), cat = $('.scr-cat', root), bub = $('.scr-bubble', root), pen = $('.scr-pen', root), st = $('.scr-status', root);
  const S = {x: o.x ?? 0, y: o.y ?? 0, dir: o.dir ?? 90, cos: 0, size: 100, vis: true, answer: '', mouse: [9999, 9999]};
  let run = 0;
  const sleep = ms => new Promise(r => setTimeout(r, RM.matches ? Math.min(ms, 30) : ms));
  function draw() {
    const W = stage.clientWidth, H = stage.clientHeight;
    spr.style.left = (W / 2 + S.x * W / 480) + 'px'; spr.style.top = (H / 2 - S.y * H / 360) + 'px';
    const flip = S.dir < 0 || S.dir > 180 ? -1 : 1;
    /* Kostüm 2 = Schritt-Pose (leicht angehoben und gekippt) statt Emoji-Wechsel, sonst flackert die Figur */
    cat.style.transform = `translate(-50%,-50%) scale(${S.size / 100 * flip}, ${S.size / 100}) rotate(${(S.dir - 90) * flip}deg)${S.cos % 2 ? ' translateY(-6%) rotate(-7deg)' : ''}`;
    spr.style.opacity = S.vis ? 1 : 0;
    $('.scr-xy', root).textContent = `x: ${Math.round(S.x)}  y: ${Math.round(S.y)}  Richtung: ${Math.round(S.dir)}`;
    Object.keys(nums).forEach(k => { const m = $(`[data-mon="${k}"] b`, root); if (m) m.textContent = V[k]; });
  }
  function reset() {
    Object.assign(S, {x: o.x ?? 0, y: o.y ?? 0, dir: o.dir ?? 90, cos: 0, size: 100, vis: true}); Object.assign(V, nums);
    bub.hidden = true; const c = pen.getContext('2d'); pen.width = stage.clientWidth; pen.height = stage.clientHeight; c.clearRect(0, 0, pen.width, pen.height); draw();
  }
  function line(x1, y1, x2, y2) {
    if (!o.pen) return; const c = pen.getContext('2d'), W = pen.width, H = pen.height;
    c.strokeStyle = '#2563EB'; c.lineWidth = 3; c.lineCap = 'round'; c.beginPath(); c.moveTo(W / 2 + x1 * W / 480, H / 2 - y1 * H / 360); c.lineTo(W / 2 + x2 * W / 480, H / 2 - y2 * H / 360); c.stroke();
  }
  const edge = () => Math.abs(S.x) >= 225 || Math.abs(S.y) >= 165;
  function test(c) {
    if (c.c === 'edge') return edge();
    if (c.c === 'mouse') { const [mx, my] = S.mouse; return Math.hypot(mx - S.x, my - S.y) < 40; }
    if (c.c === 'answer') return String(S.answer).trim().toLowerCase() === String(c.v).toLowerCase();
    if (c.c === 'var') return V[c.name] === c.v;
    if (c.c === 'cmp') {
      const a = c.a === 'Antwort' ? S.answer : c.a === 'x' ? S.x : c.a === 'y' ? S.y : V[c.a], cv = c.b ? V[c.b] : c.v, na = parseFloat(String(a).replace(',', '.')), nv = parseFloat(String(cv).replace(',', '.'));
      const both = isFinite(na) && isFinite(nv);
      if (c.op === '<') return both ? na < nv : String(a) < String(cv);
      if (c.op === '>') return both ? na > nv : String(a) > String(cv);
      return both ? na === nv : String(a).trim().toLowerCase() === String(cv).trim().toLowerCase();
    }
    return false;
  }
  const num = (el, k, b) => { const v = parseFloat(String(b[k]).replace(',', '.')); return isFinite(v) ? v : 0; };
  async function moveTo(nx, ny, ms, id) {
    /* im Takt der Bildwiederholung bewegen, damit die Figur nicht ruckelt */
    const x0 = S.x, y0 = S.y, t0 = performance.now();
    for (let k = 0; k < 1;) {
      await new Promise(r => requestAnimationFrame(r)); if (id !== run) return;
      k = Math.min(1, (performance.now() - t0) / Math.max(ms, 1)); const px = S.x, py = S.y; S.x = x0 + (nx - x0) * k; S.y = y0 + (ny - y0) * k; line(px, py, S.x, S.y); draw();
    }
  }
  /* Dauer eines Blocks in ms: Nur Blöcke, die lange genug laufen, werden gelb markiert –
     sonst flackert die Markierung in schnellen Schleifen. */
  function dur(b, el) {
    if (b.body || b.op === 'ask') return Infinity;
    const s = () => num(el, 's', b) * 1000;
    return {move: clamp(Math.abs(num(el, 'n', b)) * 4, 30, 400), turn: 80, turnL: 80, goto: 60, glide: s(), say: b.s != null ? s() : 300, think: b.s != null ? s() : 300,
      costume: 50, costume2: 120, size: 120, sound: 500, wait: s(), sayvar: b.s != null ? s() : 300, sayjoin: b.s != null ? s() : 300}[b.op] || 0;
  }
  async function exec(list, path, id) {
    for (let i = 0; i < list.length; i++) {
      if (id !== run) return;
      const b = list[i], p = path + i, el = $(`[data-p="${p}"]`, root);
      if (dur(b, el) >= (RM.matches ? Infinity : 150)) el.classList.add('run');
      try {
        switch (b.op) {
          case 'move': { const n = num(el, 'n', b), r = S.dir * Math.PI / 180; await moveTo(clamp(S.x + n * Math.sin(r), -240, 240), clamp(S.y + n * Math.cos(r), -180, 180), clamp(Math.abs(n) * 4, 30, 400), id); break; }
          case 'turn': S.dir = ((S.dir + num(el, 'n', b)) % 360 + 360) % 360; draw(); await sleep(80); break;
          case 'turnL': S.dir = ((S.dir - num(el, 'n', b)) % 360 + 360) % 360; draw(); await sleep(80); break;
          case 'goto': await moveTo(num(el, 'x', b), num(el, 'y', b), 60, id); break;
          case 'glide': await moveTo(randInt(-200, 200), randInt(-140, 140), num(el, 's', b) * 1000, id); break;
          case 'bounce': if (Math.abs(S.x) >= 225) S.dir = (360 - S.dir) % 360; if (Math.abs(S.y) >= 165) S.dir = (540 - S.dir) % 360; draw(); break;
          case 'say': case 'think': bub.hidden = false; bub.textContent = b.text; bub.classList.toggle('think', b.op === 'think'); if (b.s != null) { await sleep(num(el, 's', b) * 1000); bub.hidden = true; } else await sleep(300); break;
          case 'costume': S.cos++; draw(); await sleep(50); break;
          case 'costume2': S.cos = 1; draw(); await sleep(120); break;
          case 'show': S.vis = true; draw(); break;
          case 'hide': S.vis = false; draw(); break;
          case 'size': S.size = num(el, 'n', b); draw(); await sleep(120); break;
          case 'sound': beep(); bub.hidden = false; bub.textContent = '♪ Miau'; await sleep(500); bub.hidden = true; break;
          case 'wait': await sleep(num(el, 's', b) * 1000); break;
          case 'ask': S.answer = await ask(b.text, id); break;
          case 'repeat': { const n = Math.min(500, Math.round(num(el, 'n', b))); for (let k = 0; k < n && id === run; k++) await exec(b.body, p + '.body.', id); break; }
          case 'forever': for (let k = 0; k < 100000 && id === run; k++) { await exec(b.body, p + '.body.', id); await sleep(10); } break;
          case 'until': for (let k = 0; k < 2000 && id === run && !test(b.cond); k++) { await exec(b.body, p + '.body.', id); await sleep(10); } break;
          case 'if': if (test(b.cond)) await exec(b.body, p + '.body.', id); break;
          case 'ifelse': if (test(b.cond)) await exec(b.body, p + '.body.', id); else await exec(b.else, p + '.else.', id); break;
          case 'setvar': { const v = parseFloat(String(b.v).replace(',', '.')); V[b.name] = isFinite(v) && String(b.v).trim() !== '' ? v : b.v; draw(); await sleep(60); break; }
          case 'changevar': V[b.name] = (+V[b.name] || 0) + num(el, 'n', b); draw(); await sleep(60); break;
          case 'setrand': { const lo = Math.round(num(el, 'a', b)), hi = Math.round(num(el, 'b', b)); V[b.name] = randInt(Math.min(lo, hi), Math.max(lo, hi)); draw(); await sleep(60); break; }
          case 'setans': { const v = parseFloat(String(S.answer).replace(',', '.')); V[b.name] = isFinite(v) ? v : S.answer; draw(); break; }
          case 'sayvar': case 'sayjoin': bub.hidden = false; bub.classList.remove('think'); bub.textContent = (b.op === 'sayjoin' ? b.text : '') + V[b.name]; if (b.s != null) { await sleep(num(el, 's', b) * 1000); bub.hidden = true; } else await sleep(300); break;
          case 'changex': { const n = num(el, 'n', b); await moveTo(clamp(S.x + n, -240, 240), S.y, clamp(Math.abs(n) * 4, 30, 300), id); break; }
          case 'changey': { const n = num(el, 'n', b); await moveTo(S.x, clamp(S.y + n, -180, 180), clamp(Math.abs(n) * 4, 30, 300), id); break; }
        }
      } finally { el.classList.remove('run'); }
    }
  }
  function ask(text, id) {
    return new Promise(res => {
      const f = $('.scr-ask', root); bub.hidden = false; bub.textContent = text; f.hidden = false; $('span', f).textContent = text; const i = $('input', f); i.value = ''; i.focus();
      const chk = setInterval(() => { if (id !== run) { clearInterval(chk); if (f.dataset.id === String(id)) f.hidden = true; res(''); } }, 200);
      f.dataset.id = id;
      f.onsubmit = e => { e.preventDefault(); clearInterval(chk); f.hidden = true; bub.hidden = true; res(i.value); };
    });
  }
  function beep() { try { const A = new (window.AudioContext || window.webkitAudioContext)(), g = A.createGain(), osc = A.createOscillator(); osc.frequency.value = 660; osc.connect(g); g.connect(A.destination); g.gain.setValueAtTime(.15, A.currentTime); g.gain.exponentialRampToValueAtTime(.001, A.currentTime + .4); osc.start(); osc.stop(A.currentTime + .4); } catch (e) {} }
  root.addEventListener('input', e => {
    const k = e.target.dataset.k; if (!k) return;
    /* Pfad wie „1.body.0“ → Block im Skript */
    let list = script, node;
    for (const part of e.target.closest('[data-p]').dataset.p.split('.')) { if (/^\d+$/.test(part)) node = list[+part]; else list = node[part]; }
    node[k] = e.target.value;
  });
  $('.scr-go', root).onclick = async () => { const id = ++run; reset(); st.innerHTML = 'Das Programm läuft …'; await exec(script, '', id); if (id === run) st.innerHTML = o.done || 'Programm beendet. Ändere Werte und starte erneut.'; };
  $('.scr-stop', root).onclick = () => { run++; st.innerHTML = 'Gestoppt.'; $$('.sb.run', root).forEach(x => x.classList.remove('run')); };
  $$('.scr-var', root).forEach(b => b.onclick = () => { const k = b.dataset.var, L = vars[k]; V[k] = L[(L.indexOf(V[k]) + 1) % L.length]; $('b', b).textContent = V[k]; });
  stage.addEventListener('pointermove', e => { const r = stage.getBoundingClientRect(); S.mouse = [(e.clientX - r.left - r.width / 2) * 480 / r.width, -(e.clientY - r.top - r.height / 2) * 360 / r.height]; });
  stage.addEventListener('pointerleave', () => S.mouse = [9999, 9999]);
  onShow.push(() => requestAnimationFrame(() => { if (root.offsetParent) { if (!pen.width) reset(); else draw(); } }));
  requestAnimationFrame(reset);
  return {state: S, reset, draw, vars: V};
}

/* Statische Scratch-Blöcke (z. B. für Sortieraufgaben): sblock('mo', 'gehe 10 er Schritt') */
const sblock = (c, t, hat) => `<span class="sb ${hat ? 'hat ' : ''}${c} inline">${t}</span>`;

/* Programmier-Labyrinth: Fahrzeug mit Befehlen (vor, links, rechts) zum Ziel steuern.
   grid: Strings mit '#' Wand, '.' Weg, 'S' Start (Blick nach rechts), 'Z' Ziel */
function gridBot(root, grid, o = {}) {
  const H = grid.length, W = grid[0].length;
  let prog = [], sx, sy;
  grid.forEach((r, y) => [...r].forEach((ch, x) => { if (ch === 'S') { sx = x; sy = y; } }));
  root.classList.add('gbot');
  root.innerHTML = `<div class="gb-grid" style="--w:${W};--h:${H}">${grid.map(r => [...r].map(ch => `<span class="gb-c ${ch === '#' ? 'wall' : ch === 'Z' ? 'goal' : ''}">${ch === 'Z' ? (o.goal || '🏠') : ''}</span>`).join('')).join('')}<span class="gb-bot">${o.bot || '🚜'}</span></div>
    <div class="gb-side"><div class="controls" style="margin-top:0"><button class="btn" data-c="F">⬆ fahre 1 Feld</button><button class="btn" data-c="L">↺ drehe links</button><button class="btn" data-c="R">↻ drehe rechts</button></div>
    <ol class="gb-prog"></ol><div class="controls"><button class="btn primary" data-a="run">▶ Ausführen</button><button class="btn" data-a="undo">⌫ Letzten löschen</button><button class="btn" data-a="clear">Neu</button></div><p class="status gb-st">Baue eine Befehlsfolge, die den Traktor zum Ziel bringt.</p></div>`;
  const bot = $('.gb-bot', root), list = $('.gb-prog', root), st = $('.gb-st', root);
  const NAME = {F: 'Fahre 1 Feld vorwärts.', L: 'Drehe dich nach links.', R: 'Drehe dich nach rechts.'};
  const place = (x, y, d) => { bot.style.left = `calc(${x} * 100% / ${W})`; bot.style.top = `calc(${y} * 100% / ${H})`; bot.style.transform = `rotate(${d * 90}deg) scaleX(-1)`; };
  const show = () => list.innerHTML = prog.map((c, i) => `<li data-i="${i}">${NAME[c]}</li>`).join('');
  place(sx, sy, 0);
  root.addEventListener('click', async e => {
    const c = e.target.closest('[data-c]')?.dataset.c, a = e.target.closest('[data-a]')?.dataset.a;
    if (c) { prog.push(c); show(); }
    if (a === 'undo') { prog.pop(); show(); }
    if (a === 'clear') { prog = []; show(); place(sx, sy, 0); st.textContent = 'Baue eine Befehlsfolge, die den Traktor zum Ziel bringt.'; }
    if (a === 'run') {
      let x = sx, y = sy, d = 0; place(x, y, d);
      for (let i = 0; i < prog.length; i++) {
        $$('li', list).forEach((li, k) => li.classList.toggle('on', k === i));
        await new Promise(r => setTimeout(r, 380));
        if (prog[i] === 'L') d = (d + 3) % 4; else if (prog[i] === 'R') d = (d + 1) % 4;
        else { const nx = x + [1, 0, -1, 0][d], ny = y + [0, 1, 0, -1][d]; if (!grid[ny] || !grid[ny][nx] || grid[ny][nx] === '#') { st.innerHTML = `<b class="bad">Befehl ${i + 1}: Da ist kein Weg!</b> Korrigiere die Befehlsfolge.`; return; } x = nx; y = ny; }
        place(x, y, d);
      }
      st.innerHTML = grid[y][x] === 'Z' ? `<b class="good">Geschafft!</b> Der Traktor ist mit ${prog.length} Befehlen am Ziel.` : 'Der Traktor ist noch nicht am Ziel. Ergänze weitere Befehle.';
    }
  });
}

/* Ablaufplan-Baukasten: Anweisungen antippen oder eintippen, Start/Stopp werden automatisch ergänzt.
   o: {pool: [Anweisungen], start: [vorgegebene Anweisungen], free: true, check: [richtige Reihenfolge]} */
function flowBuilder(root, o = {}) {
  let steps = (o.start || []).slice();
  root.classList.add('fb-wrap');
  root.innerHTML = `<div class="fb-side">${o.pool ? `<p class="eyebrow">Anweisungen</p><div class="fb-pool">${o.pool.map((p, i) => `<button class="btn fb-add" data-i="${i}">+ ${p}</button>`).join('')}</div>` : ''}
    ${o.free !== false ? `<p class="eyebrow" style="margin-top:.8rem">Eigene Anweisung (Imperativ!)</p><form class="fb-form"><input class="text-in" placeholder="z. B. Gehe zur Tür." aria-label="Anweisung"><button class="btn primary">+</button></form>` : ''}
    <div class="controls">${o.check ? '<button class="btn primary" data-f="check">Prüfen</button>' : ''}<button class="btn" data-f="clear">Leeren</button><span class="sort-fb" aria-live="polite"></span></div></div>
    <div class="fb-chart"></div>`;
  const chart = $('.fb-chart', root);
  function draw() {
    chart.innerHTML = `<div class="fc term">Start</div>` + steps.map((s, i) => `<div class="fc-ar">↓</div><div class="fc step" data-i="${i}"><span>${s}</span><span class="fc-tools"><button data-m="-1" aria-label="nach oben">↑</button><button data-m="x" aria-label="entfernen">✕</button></span></div>`).join('') + `<div class="fc-ar">↓</div><div class="fc term">Stopp</div>`;
  }
  root.addEventListener('click', e => {
    const a = e.target.closest('.fb-add'); if (a) { steps.push(o.pool[+a.dataset.i]); draw(); return; }
    const m = e.target.closest('[data-m]');
    if (m) { const i = +m.closest('.fc').dataset.i; if (m.dataset.m === 'x') steps.splice(i, 1); else if (i > 0) [steps[i - 1], steps[i]] = [steps[i], steps[i - 1]]; draw(); return; }
    const f = e.target.closest('[data-f]'); if (!f) return;
    if (f.dataset.f === 'clear') { steps = []; draw(); $('.sort-fb', root).textContent = ''; }
    if (f.dataset.f === 'check') { const ok = steps.length === o.check.length && steps.every((s, i) => s === o.check[i]); $('.sort-fb', root).innerHTML = ok ? '<b class="good">Richtig!</b>' : `<b class="bad">Noch nicht.</b> ${steps.length !== o.check.length ? `Es fehlen oder sind zu viele Anweisungen (${o.check.length} nötig).` : 'Prüfe die Reihenfolge.'}`; }
  });
  const form = $('.fb-form', root);
  if (form) form.addEventListener('submit', e => { e.preventDefault(); const i = $('input', form); if (i.value.trim()) { steps.push(i.value.trim()); i.value = ''; draw(); } });
  draw();
}

/* Pixelraster zum Anklicken. o: {w, h, data: ['0101…', …] (0 = schwarz, 1 = weiß), palette: [Farben] für Farbbilder,
   code: Element für den Binärcode, onChange(data)} */
function pixelGrid(root, o = {}) {
  const W = o.w || 8, H = o.h || 8;
  let data = (o.data || Array(H).fill('1'.repeat(W))).map(r => r.split(''));
  let pen = o.pen ?? '0';
  root.classList.add('pxg');
  root.style.setProperty('--w', W);
  const color = v => o.palette ? o.palette[v] : v === '0' ? '#111' : '#fff';
  function draw() {
    root.innerHTML = data.map((r, y) => r.map((v, x) => `<button class="px" data-x="${x}" data-y="${y}" style="background:${color(v)}" aria-label="Pixel ${x + 1},${y + 1}"></button>`).join('')).join('');
    if (o.code) o.code.innerHTML = data.map(r => `<span>${r.join(' ')}</span>`).join('');
    if (o.onChange) o.onChange(data.map(r => r.join('')));
  }
  let down = false;
  /* Beim Drücken wird die Stiftfarbe festgelegt (Schwarz-Weiß: Gegenteil des angeklickten Pixels), beim Ziehen weitergemalt */
  const paint = el => { const x = +el.dataset.x, y = +el.dataset.y; data[y][x] = pen; el.style.background = color(pen); if (o.code) o.code.children[y].textContent = data[y].join(' '); if (o.onChange) o.onChange(data.map(r => r.join(''))); };
  root.addEventListener('pointerdown', e => { const p = e.target.closest('.px'); if (!p || o.readonly) return; down = true; if (!o.palette) pen = data[+p.dataset.y][+p.dataset.x] === '0' ? '1' : '0'; paint(p); });
  root.addEventListener('pointerover', e => { if (!down) return; const p = e.target.closest('.px'); if (p) paint(p); });
  addEventListener('pointerup', () => down = false);
  draw();
  return {set(d) { data = d.map(r => r.split('')); draw(); }, get: () => data.map(r => r.join('')), setPen(v) { pen = v; }, clear() { data = Array(H).fill((o.palette ? '0' : '1').repeat(W)).map(r => r.split('')); draw(); }};
}
/* Lauflängencodierung: „AAAAABB“ → „5A2B“ */
function rle(s) { let out = '', i = 0; while (i < s.length) { let j = i; while (j < s.length && s[j] === s[i]) j++; out += (j - i) + s[i]; i = j; } return out; }

/* Bildschirmtastatur (deutsches Layout, vereinfacht). o: {marks: {Taste: Nummer}, mac: true für cmd/option, onKey(taste, el)}
   Tasten werden über ihren Namen angesprochen (z. B. 'Strg', 'C', '←'). Rückgabe: {press(namen), clear()} */
function keyboard(root, o = {}) {
  const ctl = o.mac ? 'cmd ⌘' : 'Strg', alt = o.mac ? 'option' : 'Alt';
  const rows = [
    ['Esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'Entf'],
    ['^', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'ß', '⌫:w2'],
    ['Tab:w15', 'Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 'P', 'Ü', '+', 'Enter:w15'],
    ['⇩:w2', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä', '#'],
    ['Shift:w15', '<', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-', 'Shift:w25'],
    [ctl + ':w15', o.mac ? 'ctrl' : 'Win', alt, 'Leertaste:w6', o.mac ? 'cmd ⌘' : 'Alt Gr', '←', '↑', '↓', '→']
  ];
  root.classList.add('kb');
  root.innerHTML = rows.map(r => `<div class="kb-row">${r.map(k => { const [n, w] = k.split(':'), m = o.marks && o.marks[n];
    return `<button class="kb-k${w ? ' ' + w : ''}${m ? ' mark' : ''}" data-k="${n}" tabindex="-1">${n === 'Leertaste' ? '' : n}${m ? `<span class="n">${m}</span>` : ''}</button>`; }).join('')}</div>`).join('');
  root.addEventListener('click', e => { const b = e.target.closest('.kb-k'); if (b && o.onKey) o.onKey(b.dataset.k, b); });
  const api = {
    press(names, cls = 'down') { names.forEach(n => $$(`.kb-k[data-k="${n}"]`, root).forEach(b => b.classList.add(cls))); },
    clear() { $$('.kb-k', root).forEach(b => b.classList.remove('down', 'hit', 'miss')); },
    ctl
  };
  return api;
}

/* ================= Klasse 7/8 ================= */
/* Graph mit (gewichteten) Kanten für Netzwerke, Routing und kürzeste Wege.
   nodes: {id: [x, y, name, icon]}, edges: [[a, b, gewicht], …]
   draw(st): st = {on: [ids], done: [ids], path: [ids], bad: [ids], sub: {id: text}, edgeOn: [[a,b], …], pkt: id}
   o: {w, h, weights: true, onNode(id), r} */
function graphView(svg, nodes, edges, o = {}) {
  const W = o.w || 460, H = o.h || 300, R = o.r || 22;
  svg.setAttribute('viewBox', `0 0 ${W} ${H}`); svg.classList.add('net-svg', 'graph');
  const key = (a, b) => [a, b].sort().join('|');
  function draw(st = {}) {
    const on = new Set(st.on || []), done = new Set(st.done || []), bad = new Set(st.bad || []);
    const pe = new Set((st.edgeOn || []).map(([a, b]) => key(a, b)));
    (st.path || []).forEach((id, i, p) => { if (i) pe.add(key(p[i - 1], id)); });
    const deadE = new Set((st.deadEdges || []).map(([a, b]) => key(a, b)));
    let s = '';
    for (const [a, b, w] of edges) {
      const [x1, y1] = nodes[a], [x2, y2] = nodes[b], k = key(a, b), dead = bad.has(a) || bad.has(b) || deadE.has(k);
      s += `<line class="edge${pe.has(k) ? ' on' : ''}${dead ? ' dead' : ''}" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}"/>`;
      if (o.weights !== false && w !== undefined) {
        const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
        s += `<g class="wt${pe.has(k) ? ' on' : ''}"><rect x="${mx - 11}" y="${my - 9}" width="22" height="18" rx="3"/><text x="${mx}" y="${my + 4}" text-anchor="middle">${w}</text></g>`;
      }
    }
    for (const [id, [x, y, name, icon]] of Object.entries(nodes)) {
      const cls = ['node', on.has(id) && 'on', done.has(id) && 'done', bad.has(id) && 'bad', (st.path || []).includes(id) && 'onpath'].filter(Boolean).join(' ');
      s += `<g class="${cls}" data-n="${id}" tabindex="0" role="button" aria-label="${name || id}"><circle cx="${x}" cy="${y}" r="${R}"/>`
        + `<text x="${x}" y="${y + (icon ? 6 : 5)}" text-anchor="middle" class="${icon ? 'ic' : 'nm'}">${icon || name || id}</text>`
        + (icon && name ? `<text x="${x}" y="${y + R + 14}" text-anchor="middle" class="lb">${name}</text>` : '')
        + (st.sub && st.sub[id] !== undefined ? `<text x="${x + R - 2}" y="${y - R + 2}" class="sub">${st.sub[id]}</text>` : '') + '</g>';
    }
    if (st.pkt && nodes[st.pkt]) { const [x, y] = nodes[st.pkt]; s += `<rect class="pkt" x="${x - 7}" y="${y - R - 12}" width="14" height="10" rx="2"/>`; }
    svg.innerHTML = s;
  }
  if (o.onNode) {
    svg.addEventListener('click', e => { const g = e.target.closest('[data-n]'); if (g) o.onNode(g.dataset.n); });
    svg.addEventListener('keydown', e => { const g = e.target.closest('[data-n]'); if (g && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); o.onNode(g.dataset.n); } });
  }
  /* kürzester Weg (Dijkstra) – liefert {dist, prev, order} */
  function dijkstra(src, skip = []) {
    const dist = {}, prev = {}, seen = new Set(skip), order = [];
    Object.keys(nodes).forEach(n => dist[n] = Infinity); dist[src] = 0;
    while (true) {
      let u = null; for (const n in dist) if (!seen.has(n) && dist[n] < Infinity && (u === null || dist[n] < dist[u])) u = n;
      if (u === null) break; seen.add(u); order.push(u);
      for (const [a, b, w] of edges) { const v = a === u ? b : b === u ? a : null; if (v && !seen.has(v) && dist[u] + (w ?? 1) < dist[v]) { dist[v] = dist[u] + (w ?? 1); prev[v] = u; } }
    }
    return {dist, prev, order};
  }
  function path(src, dst, skip = []) { const {dist, prev} = dijkstra(src, skip); if (dist[dst] === Infinity) return null; const p = [dst]; while (p[0] !== src) p.unshift(prev[p[0]]); return {path: p, cost: dist[dst]}; }
  draw();
  return {draw, dijkstra, path};
}

/* Mini-Fenster mit Code (nur Anzeige), Zeilen werden nummeriert. hl: Zeilennummern zum Hervorheben */
function codeView(root, code, hl = []) {
  root.classList.add('codeview');
  root.innerHTML = code.split('\n').map((l, i) => `<span class="cl${hl.includes(i + 1) ? ' hl' : ''}"><i>${i + 1}</i>${l.replace(/&/g, '&amp;').replace(/</g, '&lt;') || ' '}</span>`).join('');
}

/* Struktogramm (Nassi-Shneiderman). nodes: [{t:'s', text} | {t:'loop', head, body} (kopfgesteuert/Zählschleife)
   | {t:'foot', foot, body} (fußgesteuert) | {t:'if', cond, yes:[], no:[]} | {t:'forever', body}] */
function nsd(root, nodes, o = {}) {
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const R = list => list.map(n => {
    if (n.t === 's') return `<div class="ns-s">${o.html ? n.text : esc(n.text)}</div>`;
    if (n.t === 'loop') return `<div class="ns-loop"><div class="ns-h">${esc(n.head)}</div><div class="ns-b">${R(n.body)}</div></div>`;
    if (n.t === 'forever') return `<div class="ns-loop"><div class="ns-h">wiederhole fortlaufend</div><div class="ns-b">${R(n.body)}</div></div>`;
    if (n.t === 'foot') return `<div class="ns-loop foot"><div class="ns-b">${R(n.body)}</div><div class="ns-h">${esc(n.foot)}</div></div>`;
    if (n.t === 'if') return `<div class="ns-if"><div class="ns-cond"><svg viewBox="0 0 100 30" preserveAspectRatio="none"><polyline points="0,0 50,30 100,0" fill="none" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke"/></svg><span class="c">${esc(n.cond)}</span><span class="y">ja</span><span class="n">nein</span></div><div class="ns-br"><div>${R(n.yes || []) || '<div class="ns-s ns-empty">∅</div>'}</div><div>${R(n.no || []) || '<div class="ns-s ns-empty">∅</div>'}</div></div></div>`;
    return '';
  }).join('');
  root.classList.add('nsd');
  root.innerHTML = (o.title ? `<div class="ns-title">${esc(o.title)}</div>` : '') + R(nodes);
}

/* ================= Calliope-Simulator (Klasse 8) =================
   calliope(root, {blocks: [[einrückung, kategorie, 'Text'], …], run: async c => {…}, sensors: {licht, temp, laut}, channel, label})
   Kategorien: st Start, ak Aktion, se Sensor, ko Kontrolle, lo Logik, ma Mathe, va Variable, na Nachrichten
   API im Programm: c.show(text) · c.image(name|[5 Zeilen]) · c.clear() · c.plot(x,y,on) · c.rgb(farbe|null) · c.tone(hz, ms) · await c.wait(ms)
     c.sensor('licht'|'temp'|'laut') · c.pressed('A'|'B'|'AB') (seit letzter Abfrage gedrückt?) · c.held('A') · c.pin(0–3) · c.shaken()
     c.set(name, wert) (Variablenanzeige) · c.send(text) · c.receive() → Text oder null · c.running · c.log(text) */
const CAL_FONT = {
  '0': [14, 19, 21, 25, 14], '1': [4, 12, 4, 4, 14], '2': [30, 1, 14, 16, 31], '3': [30, 1, 6, 1, 30], '4': [18, 18, 31, 2, 2], '5': [31, 16, 30, 1, 30], '6': [14, 16, 30, 17, 14], '7': [31, 2, 4, 8, 8], '8': [14, 17, 14, 17, 14], '9': [14, 17, 15, 1, 14],
  A: [14, 17, 31, 17, 17], B: [30, 17, 30, 17, 30], C: [15, 16, 16, 16, 15], D: [30, 17, 17, 17, 30], E: [31, 16, 30, 16, 31], F: [31, 16, 30, 16, 16], G: [15, 16, 19, 17, 15], H: [17, 17, 31, 17, 17], I: [14, 4, 4, 4, 14], J: [7, 2, 2, 18, 12],
  K: [18, 20, 24, 20, 18], L: [16, 16, 16, 16, 31], M: [17, 27, 21, 17, 17], N: [17, 25, 21, 19, 17], O: [14, 17, 17, 17, 14], P: [30, 17, 30, 16, 16], Q: [14, 17, 21, 18, 13], R: [30, 17, 30, 18, 17], S: [15, 16, 14, 1, 30], T: [31, 4, 4, 4, 4],
  U: [17, 17, 17, 17, 14], V: [17, 17, 17, 10, 4], W: [17, 17, 21, 27, 17], X: [17, 10, 4, 10, 17], Y: [17, 10, 4, 4, 4], Z: [31, 2, 4, 8, 31], ' ': [0, 0, 0, 0, 0], '!': [4, 4, 4, 0, 4], '?': [14, 1, 6, 0, 4], '-': [0, 0, 14, 0, 0], '+': [0, 4, 14, 4, 0],
  ':': [0, 4, 0, 4, 0], '%': [25, 26, 4, 11, 19], '°': [12, 18, 12, 0, 0], '.': [0, 0, 0, 0, 4], ',': [0, 0, 0, 4, 8], '=': [0, 31, 0, 31, 0]
};
const CAL_IMG = {HERZ: [10, 31, 31, 14, 4], SMILEY: [0, 10, 0, 17, 14], TRAURIG: [0, 10, 0, 14, 17], HAKEN: [0, 1, 2, 20, 8], KREUZ: [17, 10, 4, 10, 17], PFEIL_HOCH: [4, 14, 21, 4, 4], PFEIL_RUNTER: [4, 4, 21, 14, 4], SONNE: [21, 14, 31, 14, 21], MOND: [6, 12, 12, 12, 6], GLOCKE: [4, 14, 14, 31, 4]};
const CAL_RADIO = {};
function calliope(root, o = {}) {
  const sens = Object.assign({licht: 50, temp: 21, laut: 10}, o.sensors || {});
  const ch = o.channel || 'kanal1', id = Math.random().toString(36).slice(2);
  root.classList.add('cal');
  root.innerHTML = `<div class="cal-code">${(o.blocks || []).map(([ind, cat, t]) => `<div class="nb ${cat}" style="margin-left:${ind * 1.2}rem">${t}</div>`).join('')}</div>
    <div class="cal-right">
      <div class="cal-bar"><button class="btn primary cal-go">▶ Programm starten</button><button class="btn cal-stop">■ Stopp</button>${o.label ? `<span class="tag info">${o.label}</span>` : ''}</div>
      <div class="cal-board">
        <svg viewBox="0 0 260 230" class="cal-svg">
          <path class="cal-pcb" d="M130 8 L170 40 L236 40 L236 112 L252 160 L200 222 L60 222 L8 160 L24 112 L24 40 L90 40 Z"/>
          ${[[130, 28, '+'], [36, 58, '0'], [224, 58, '1'], [36, 172, '2'], [224, 172, '3'], [130, 208, '−']].map(([x, y, t]) => `<g class="cal-pin" data-pin="${t}"><circle cx="${x}" cy="${y}" r="14"/><text x="${x}" y="${y + 5}" text-anchor="middle">${t}</text></g>`).join('')}
          <g class="cal-mx">${[...Array(25)].map((_, i) => `<rect class="cal-led" data-i="${i}" x="${85 + (i % 5) * 19}" y="${70 + Math.floor(i / 5) * 19}" width="13" height="13" rx="2"/>`).join('')}</g>
          <g class="cal-btn" data-b="A"><circle cx="55" cy="118" r="16"/><text x="55" y="124" text-anchor="middle">A</text></g>
          <g class="cal-btn" data-b="B"><circle cx="205" cy="118" r="16"/><text x="205" y="124" text-anchor="middle">B</text></g>
          <circle class="cal-rgb" cx="130" cy="185" r="9"/><text x="150" y="189" class="cal-lbl">RGB</text>
          <text x="96" y="58" class="cal-lbl">5×5-LED-Matrix</text>
        </svg>
        <p class="cal-note mono" aria-live="polite"></p>
      </div>
      <div class="cal-sens">
        ${[['licht', '☀ Licht', 0, 100, '%'], ['temp', '🌡 Temperatur', -10, 40, '°C'], ['laut', '🎤 Lautstärke', 0, 100, '%']].filter(s => !o.only || o.only.includes(s[0])).map(([k, n, a, b, u]) => `<label class="slider-row">${n} <input type="range" min="${a}" max="${b}" value="${sens[k]}" data-s="${k}"><output class="mono">${sens[k]} ${u}</output></label>`).join('')}
        <div class="controls" style="margin:.2rem 0 0"><button class="btn cal-shake">📳 Schütteln</button><button class="btn cal-ab">A+B</button></div>
      </div>
      <div class="cal-vars mono"></div>
    </div>`;
  const leds = $$('.cal-led', root), note = $('.cal-note', root);
  let grid = Array(25).fill(0), run = 0, flags = {}, held = {}, inbox = [], shake = false, vars = {}, audio = null;
  const draw = () => leds.forEach((l, i) => l.classList.toggle('on', !!grid[i]));
  const rows = r => { grid = r.flatMap(v => [16, 8, 4, 2, 1].map(b => v & b ? 1 : 0)); draw(); };
  const sleep = ms => new Promise(r => setTimeout(r, RM.matches ? Math.min(ms, 40) : ms));
  CAL_RADIO[ch] = CAL_RADIO[ch] || {}; CAL_RADIO[ch][id] = m => { inbox.push(m); };
  const api = {
    get running() { return api._id === run; }, _id: 0,
    show: async t => { const s = String(t).toUpperCase(); note.textContent = '▸ ' + t; for (const chr of s) { if (!api.running) return; rows(CAL_FONT[chr] || CAL_FONT['?']); await sleep(420); rows([0, 0, 0, 0, 0]); await sleep(60); } },
    image: n => { rows(Array.isArray(n) ? n.map(r => typeof r === 'string' ? parseInt(r.replace(/[^01]/g, ''), 2) : r) : CAL_IMG[n] || CAL_IMG.KREUZ); note.textContent = '▸ Bild ' + (Array.isArray(n) ? '' : n); },
    clear: () => { grid = Array(25).fill(0); draw(); },
    plot: (x, y, on = 1) => { if (x >= 0 && x < 5 && y >= 0 && y < 5) { grid[y * 5 + x] = on ? 1 : 0; draw(); } },
    rgb: c => { $('.cal-rgb', root).style.fill = c || ''; $('.cal-rgb', root).classList.toggle('on', !!c); },
    tone: async (hz = 440, ms = 300) => { try { audio = audio || new (window.AudioContext || window.webkitAudioContext)(); const g = audio.createGain(), osc = audio.createOscillator(); osc.frequency.value = hz; osc.connect(g); g.connect(audio.destination); g.gain.setValueAtTime(.12, audio.currentTime); g.gain.exponentialRampToValueAtTime(.001, audio.currentTime + ms / 1000); osc.start(); osc.stop(audio.currentTime + ms / 1000); } catch (e) {} note.textContent = `♪ ${hz} Hz`; await sleep(ms); },
    wait: ms => sleep(ms),
    sensor: k => sens[k],
    pressed: b => { const v = !!flags[b]; flags[b] = false; return v; },
    held: b => !!held[b],
    pin: n => { const v = !!flags['P' + n]; flags['P' + n] = false; return v; },
    shaken: () => { const v = shake; shake = false; return v; },
    set: (k, v) => { vars[k] = v; $('.cal-vars', root).innerHTML = Object.entries(vars).map(([a, b]) => `<span class="scr-mon">${a} <b>${b}</b></span>`).join(' '); },
    send: m => { Object.entries(CAL_RADIO[ch]).forEach(([k, f]) => { if (k !== id) f(m); }); note.textContent = `📡 gesendet: ${m}`; },
    receive: () => inbox.length ? inbox.shift() : null,
    log: t => note.textContent = t
  };
  const press = (b, down) => { if (down) { flags[b] = true; held[b] = true; } else held[b] = false; $$(`.cal-btn[data-b="${b}"]`, root).forEach(x => x.classList.toggle('down', down)); };
  root.addEventListener('pointerdown', e => { const b = e.target.closest('.cal-btn'); if (b) press(b.dataset.b, true); const p = e.target.closest('.cal-pin'); if (p) { flags['P' + p.dataset.pin] = true; p.classList.add('down'); setTimeout(() => p.classList.remove('down'), 250); } });
  root.addEventListener('pointerup', () => { press('A', false); press('B', false); });
  $('.cal-ab', root).onclick = () => { flags.AB = true; flags.A = flags.B = false; };
  $('.cal-shake', root).onclick = () => { shake = true; $('.cal-board', root).classList.remove('shake'); void root.offsetWidth; $('.cal-board', root).classList.add('shake'); };
  root.addEventListener('input', e => { const k = e.target.dataset.s; if (!k) return; sens[k] = +e.target.value; e.target.nextElementSibling.textContent = `${sens[k]} ${k === 'temp' ? '°C' : '%'}`; });
  $('.cal-go', root).onclick = async () => {
    api._id = ++run; grid = Array(25).fill(0); draw(); api.rgb(null); flags = {}; inbox = []; vars = {}; $('.cal-vars', root).innerHTML = ''; note.textContent = 'Programm läuft …';
    try { await o.run(api); } catch (err) { note.textContent = 'Fehler: ' + err.message; }
    if (api.running) note.textContent = note.textContent.startsWith('▸') || note.textContent.startsWith('📡') ? note.textContent : 'Programm beendet.';
  };
  $('.cal-stop', root).onclick = () => { run++; note.textContent = 'Gestoppt.'; };
  return api;
}

/* ================= Code-Labor JavaScript (Klasse 8) =================
   codeLab(root, {code, h, globals, examples: {Name: code}, console: true})
   Im Code verfügbar: Canvas.init([xmin,xmax],[ymin,ymax],{width, background}) · Canvas.circle(x,y,r,{fill,stroke}) · Canvas.rect(x,y,b,h,{fill}) (Mittelpunkt)
     Canvas.line(x1,y1,x2,y2,{stroke,width}) · Canvas.text(x,y,"…",{fill,size}) · Canvas.clear() · Console.print(…) · random(a,b) · randint(a,b)
     Ereignisse: function on_frame(t) {…} (Animation) · function on_mouse_down(x,y) · function on_key_down(key) ("UP","DOWN","LEFT","RIGHT","SPACE", Buchstaben) */
function codeLab(root, o = {}) {
  root.classList.add('lab');
  root.innerHTML = `<div class="lab-ed"><div class="lab-bar"><button class="btn primary lab-run">▶ Ausführen</button><button class="btn lab-stop">■ Stopp</button>${o.examples ? `<select class="lab-ex" aria-label="Beispiel"><option value="">Beispiel laden …</option>${Object.keys(o.examples).map(k => `<option>${k}</option>`).join('')}</select>` : ''}<button class="btn lab-reset" title="Ursprünglichen Code wiederherstellen">↺</button></div>
    <textarea class="code-in lab-code" spellcheck="false" aria-label="JavaScript-Code"></textarea></div>
    <div class="lab-out"><canvas class="lab-cv" tabindex="0"></canvas>${o.console === false ? '' : '<pre class="lab-con" aria-live="polite"></pre>'}</div>`;
  const ta = $('.lab-code', root), cv = $('.lab-cv', root), con = $('.lab-con', root);
  ta.value = o.code || ''; ta.style.minHeight = (o.h || 14) + 'rem';
  ta.addEventListener('keydown', e => { if (e.key === 'Tab') { e.preventDefault(); const s = ta.selectionStart; ta.value = ta.value.slice(0, s) + '  ' + ta.value.slice(ta.selectionEnd); ta.selectionStart = ta.selectionEnd = s + 2; } });
  let V = {x: [0, 20], y: [0, 12], bg: '#F3F4F6'}, run = 0, hooks = {};
  const W = () => cv.width, H = () => cv.height;
  const X = x => (x - V.x[0]) / (V.x[1] - V.x[0]) * W(), Y = y => H() - (y - V.y[0]) / (V.y[1] - V.y[0]) * H(), S = r => r / (V.x[1] - V.x[0]) * W();
  const ctx = () => cv.getContext('2d');
  const Canvas = {
    init(xr = [0, 20], yr = [0, 12], opt = {}) { V = {x: xr, y: yr, bg: opt.background || '#F3F4F6'}; const w = opt.width || 480; cv.width = w; cv.height = Math.round(w * (yr[1] - yr[0]) / (xr[1] - xr[0])); Canvas.clear(); },
    clear() { const c = ctx(); c.fillStyle = V.bg; c.fillRect(0, 0, W(), H()); },
    circle(x, y, r, opt = {}) { const c = ctx(); c.beginPath(); c.arc(X(x), Y(y), Math.abs(S(r)), 0, 2 * Math.PI); c.fillStyle = opt.fill || 'black'; if (opt.fill !== 'none') c.fill(); if (opt.stroke) { c.strokeStyle = opt.stroke; c.lineWidth = opt.width || 2; c.stroke(); } },
    rect(x, y, b, h, opt = {}) { const c = ctx(); c.save(); c.translate(X(x), Y(y)); if (opt.rotate) c.rotate(-opt.rotate * Math.PI / 180); c.fillStyle = opt.fill || 'black'; c.fillRect(-S(b) / 2, -S(h) / 2, S(b), S(h)); if (opt.stroke) { c.strokeStyle = opt.stroke; c.lineWidth = opt.width || 2; c.strokeRect(-S(b) / 2, -S(h) / 2, S(b), S(h)); } c.restore(); },
    line(x1, y1, x2, y2, opt = {}) { const c = ctx(); c.beginPath(); c.moveTo(X(x1), Y(y1)); c.lineTo(X(x2), Y(y2)); c.strokeStyle = opt.stroke || opt.fill || 'black'; c.lineWidth = opt.width || 2; c.lineCap = 'round'; c.stroke(); },
    text(x, y, t, opt = {}) { const c = ctx(); c.fillStyle = opt.fill || 'black'; c.font = `600 ${opt.size || 18}px "Atkinson Hyperlegible", sans-serif`; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText(String(t), X(x), Y(y)); },
    pixel(x, y, rgb) { const c = ctx(), x0 = Math.floor(X(x)), x1 = Math.ceil(X(x + 1)), y0 = Math.floor(Y(y + 1)), y1 = Math.ceil(Y(y)); c.fillStyle = `rgb(${rgb.join(',')})`; c.fillRect(x0, y0, x1 - x0, y1 - y0); },
    get width() { return V.x[1] - V.x[0]; }, get height() { return V.y[1] - V.y[0]; }, _cv: cv
  };
  const fmt = v => Array.isArray(v) ? '[' + v.map(fmt).join(', ') + ']' : typeof v === 'number' ? String(Math.round(v * 1000) / 1000) : typeof v === 'object' && v ? JSON.stringify(v) : String(v);
  const Console = {print: (...a) => { if (con) { con.textContent += a.map(fmt).join(' ') + '\n'; con.scrollTop = con.scrollHeight; } }, clear: () => { if (con) con.textContent = ''; }};
  const random = (a = 0, b = 1) => a + Math.random() * (b - a), randint = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  function exec() {
    const id = ++run; hooks = {}; Console.clear(); Canvas.init();
    const g = Object.assign({Canvas, Console, random, randint}, o.globals ? o.globals(Canvas) : {});
    try {
      const f = new Function(...Object.keys(g), `"use strict";\n${ta.value}\n;return {on_frame: typeof on_frame === 'function' ? on_frame : null, on_mouse_down: typeof on_mouse_down === 'function' ? on_mouse_down : null, on_key_down: typeof on_key_down === 'function' ? on_key_down : null};`);
      hooks = f(...Object.values(g)) || {};
    } catch (err) {
      const m = String(err.stack || '').match(/<anonymous>:(\d+):\d+/); const line = m ? +m[1] - 3 : null;
      Console.print('⚠ Fehler' + (line > 0 ? ` in Zeile ${line}` : '') + ': ' + err.message); return;
    }
    if (hooks.on_frame) { const t0 = performance.now(); const step = now => { if (id !== run) return; try { if (cv.offsetParent) hooks.on_frame((now - t0) / 1000); } catch (err) { Console.print('⚠ Fehler: ' + err.message); run++; return; } requestAnimationFrame(step); }; requestAnimationFrame(step); }
  }
  const pos = e => { const r = cv.getBoundingClientRect(); return [V.x[0] + (e.clientX - r.left) / r.width * (V.x[1] - V.x[0]), V.y[0] + (1 - (e.clientY - r.top) / r.height) * (V.y[1] - V.y[0])]; };
  cv.addEventListener('pointerdown', e => { cv.focus(); if (hooks.on_mouse_down) try { hooks.on_mouse_down(...pos(e)); } catch (err) { Console.print('⚠ Fehler: ' + err.message); } });
  cv.addEventListener('keydown', e => { if (!hooks.on_key_down) return; const k = {ArrowUp: 'UP', ArrowDown: 'DOWN', ArrowLeft: 'LEFT', ArrowRight: 'RIGHT', ' ': 'SPACE'}[e.key] || e.key.toUpperCase(); e.preventDefault(); e.stopPropagation(); try { hooks.on_key_down(k); } catch (err) { Console.print('⚠ Fehler: ' + err.message); } });
  $('.lab-run', root).onclick = exec;
  $('.lab-stop', root).onclick = () => { run++; Console.print('■ gestoppt'); };
  $('.lab-reset', root).onclick = () => { ta.value = o.code || ''; exec(); };
  const ex = $('.lab-ex', root); if (ex) ex.onchange = () => { if (ex.value) { ta.value = o.examples[ex.value]; exec(); } ex.value = ''; };
  onShow.push(() => {}); requestAnimationFrame(exec);
  return {exec, set code(c) { ta.value = c; }, get code() { return ta.value; }, Canvas};
}

/* ---------------- Tabellenkalkulation ----------------
   sheet(root, {cols, rows, cells: {A1: 'Text', B4: '=SUMME(B1:B3)'}, fmt: {B: 'eur'|'num'|'pct'|'int'}, w: {A: '9rem'},
                cls: {A1: 'h'}, lock: ['A1', …] | true, sel: 'B4', onChange(api)})
   Formeln (deutsch): + − * / & ^ %, absolute Bezüge mit $ (B$8), Vergleiche = <> < > <= >=, Bereiche A1:B3, Argumente mit ;
   Funktionen: SUMME, MITTELWERT, MIN, MAX, ANZAHL, ANZAHL2, ZÄHLENWENN, RUNDEN, WENN, UND, ODER */
const SHEET_FN = {
  SUMME: a => a.flat().filter(v => typeof v === 'number').reduce((s, v) => s + v, 0),
  MITTELWERT: a => { const n = a.flat().filter(v => typeof v === 'number'); if (!n.length) throw '#DIV/0!'; return n.reduce((s, v) => s + v, 0) / n.length; },
  MIN: a => Math.min(...a.flat().filter(v => typeof v === 'number')), MAX: a => Math.max(...a.flat().filter(v => typeof v === 'number')),
  ANZAHL: a => a.flat().filter(v => typeof v === 'number').length, ANZAHL2: a => a.flat().filter(v => v !== '').length,
  'ZÄHLENWENN': ([r, c]) => { const m = String(c).match(/^(<=|>=|<>|<|>|=)?(.*)$/), op = m[1] || '=', x = isFinite(parseNum(m[2])) && m[2] !== '' ? parseNum(m[2]) : m[2].toLowerCase();
    return [r].flat().filter(v => sheetCmp(op, typeof v === 'string' ? v.toLowerCase() : v, x)).length; },
  RUNDEN: ([x, n = 0]) => Math.round(x * 10 ** n) / 10 ** n,
  WENN: ([c, a = true, b = false]) => (c === true || (typeof c === 'number' && c !== 0)) ? a : b,
  UND: a => a.flat().every(v => v === true), ODER: a => a.flat().some(v => v === true)
};
function sheetCmp(op, a, b) { return {'=': a === b, '<>': a !== b, '<': a < b, '>': a > b, '<=': a <= b, '>=': a >= b}[op]; }
function sheetVal(raw) {
  const s = String(raw ?? '').trim();
  if (s === '') return '';
  const t = s.replace(/\s*[€%]$/, '');
  if (/^-?\d{1,3}(\.\d{3})+(,\d+)?$/.test(t)) return +t.replace(/\./g, '').replace(',', '.') / (s.endsWith('%') ? 100 : 1);
  if (/^-?\d+([.,]\d+)?$/.test(t)) return +t.replace(',', '.') / (s.endsWith('%') ? 100 : 1);
  if (/^\d{1,2}\.\d{1,2}\.\d{4}$/.test(s)) { const [d, m, y] = s.split('.').map(Number); return Math.round((Date.UTC(y, m - 1, d) - Date.UTC(1899, 11, 30)) / 864e5); }
  return s;
}
function sheet(root, o = {}) {
  const NC = o.cols || 4, NR = o.rows || 8, L = i => String.fromCharCode(65 + i);
  const raw = {}; Object.entries(o.cells || {}).forEach(([k, v]) => raw[k.toUpperCase()] = String(v));
  const style = {}; let sel = o.sel || 'A1', cache = {};
  const locked = r => o.lock === true || (o.lock || []).includes(r);
  root.classList.add('sheet');
  root.innerHTML = `<div class="sh-bar"><span class="sh-ref"></span><span class="sh-fx">fx</span><input class="sh-in" spellcheck="false" autocomplete="off" aria-label="Inhalt der markierten Zelle"></div>
    <div class="sh-wrap"><table class="sh"><thead><tr><th class="sh-c"></th>${[...Array(NC)].map((_, c) => `<th${o.w && o.w[L(c)] ? ` style="min-width:${o.w[L(c)]}"` : ''}>${L(c)}</th>`).join('')}</tr></thead>
    <tbody>${[...Array(NR)].map((_, r) => `<tr><th class="sh-c">${r + 1}</th>${[...Array(NC)].map((_, c) => `<td data-r="${L(c)}${r + 1}"></td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
  const inp = $('.sh-in', root), td = r => $(`td[data-r="${r}"]`, root);
  const split = r => { const m = /^([A-Z])(\d+)$/.exec(r); return m ? [m[1].charCodeAt(0) - 65, +m[2] - 1] : null; };
  function value(ref, stack = []) {
    ref = ref.toUpperCase();
    const p = split(ref); if (!p || p[0] >= NC || p[1] >= NR) throw '#BEZUG!';
    if (ref in cache) return cache[ref];
    if (stack.includes(ref)) throw '#ZIRKEL!';
    const s = raw[ref] ?? '';
    let v;
    if (s.startsWith('=')) { try { v = evalF(s.slice(1), [...stack, ref]); } catch (e) { v = {err: typeof e === 'string' ? e : '#WERT!'}; } }
    else v = sheetVal(s);
    if (v && v.err && stack.length) throw v.err;
    return cache[ref] = v;
  }
  function evalF(src, stack) {
    const tk = []; const re = /\s*(?:(\d+(?:,\d+)?)|("(?:[^"]*)")|([A-Za-z]\d+:[A-Za-z]\d+)|([A-Za-zÄÖÜäöü][A-Za-zÄÖÜäöü0-9]*)|(<=|>=|<>|[-+*/&=<>();^%]))/y;
    let m, i = 0; src = src.replace(/\$/g, '').trim();
    while (i < src.length) { re.lastIndex = i; m = re.exec(src); if (!m) throw '#NAME?'; i = re.lastIndex; tk.push(m[1] ? {n: +m[1].replace(',', '.')} : m[2] ? {s: m[2].slice(1, -1)} : m[3] ? {rg: m[3].toUpperCase()} : m[4] ? {id: m[4].toUpperCase()} : {op: m[5]}); if (/^\s*$/.test(src.slice(i))) break; }
    let k = 0; const peek = () => tk[k], eat = op => { if (tk[k] && tk[k].op === op) { k++; return true; } return false; };
    const num = v => { if (v === '') return 0; if (typeof v === 'number') return v; if (typeof v === 'boolean') return +v; throw '#WERT!'; };
    function cmp() { let a = add(); for (const op of ['<=', '>=', '<>', '=', '<', '>']) if (eat(op)) { const b = add(); return sheetCmp(op, typeof a === 'string' ? a.toLowerCase() : a, typeof b === 'string' ? b.toLowerCase() : b); } return a; }
    function add() { let a = mul(); for (;;) { if (eat('+')) a = num(a) + num(mul()); else if (eat('-')) a = num(a) - num(mul()); else if (eat('&')) a = String(a) + String(mul()); else return a; } }
    function mul() { let a = un(); for (;;) { if (eat('*')) a = num(a) * num(un()); else if (eat('/')) { const b = num(un()); if (b === 0) throw '#DIV/0!'; a = num(a) / b; } else return a; } }
    function un() { if (eat('-')) return -num(un()); if (eat('+')) return num(un()); let v = pr(); if (eat('%')) v = num(v) / 100; if (eat('^')) v = num(v) ** num(un()); return v; }
    function range(rg) { const [a, b] = rg.split(':').map(split); if (!a || !b) throw '#BEZUG!'; const out = []; for (let c = Math.min(a[0], b[0]); c <= Math.max(a[0], b[0]); c++) for (let r = Math.min(a[1], b[1]); r <= Math.max(a[1], b[1]); r++) out.push(value(L(c) + (r + 1), stack)); return out; }
    function pr() {
      const t = tk[k++]; if (!t) throw '#WERT!';
      if ('n' in t) return t.n; if ('s' in t) return t.s; if (t.rg) return range(t.rg);
      if (t.op === '(') { const v = cmp(); if (!eat(')')) throw '#WERT!'; return v; }
      if (t.id) {
        if (t.id === 'WAHR') return true; if (t.id === 'FALSCH') return false;
        if (peek() && peek().op === '(') {
          k++; const f = SHEET_FN[t.id]; if (!f) throw '#NAME?';
          const args = []; if (!eat(')')) { do { args.push(peek() && (peek().op === ';' || peek().op === ')') ? '' : cmp()); } while (eat(';')); if (!eat(')')) throw '#WERT!'; }
          return f(args);
        }
        if (/^[A-Z]\d+$/.test(t.id)) return value(t.id, stack);
        throw '#NAME?';
      }
      throw '#WERT!';
    }
    const v = cmp(); if (k < tk.length) throw '#WERT!';
    if (Array.isArray(v)) throw '#WERT!';
    return v;
  }
  function show(ref, v) {
    if (v && v.err) return v.err;
    if (typeof v === 'boolean') return v ? 'WAHR' : 'FALSCH';
    if (typeof v !== 'number') return v;
    const f = (o.fmt || {})[ref] || (o.fmt || {})[ref[0]];
    if (f === 'eur') return v.toLocaleString('de-DE', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' €';
    if (f === 'pct') return numDE(v * 100, 1) + ' %';
    if (f === 'int') return numDE(v, 0);
    if (f === 'date') { const d = new Date(Date.UTC(1899, 11, 30) + v * 864e5); return d.toLocaleDateString('de-DE', {timeZone: 'UTC', day: '2-digit', month: '2-digit', year: 'numeric'}); }
    return numDE(v, f === 'num' ? 2 : 4);
  }
  function refsOf(s) { if (!s.startsWith('=')) return []; const out = []; s.replace(/\$/g, '').replace(/([A-Za-z])(\d+):([A-Za-z])(\d+)|([A-Za-z])(\d+)/g, (m, a, b, c, d, e, f) => { if (a) { const p = split(a.toUpperCase() + b), q = split(c.toUpperCase() + d); if (p && q) for (let x = Math.min(p[0], q[0]); x <= Math.max(p[0], q[0]); x++) for (let y = Math.min(p[1], q[1]); y <= Math.max(p[1], q[1]); y++) out.push(L(x) + (y + 1)); } else out.push(e.toUpperCase() + f); }); return out; }
  function paint() {
    cache = {};
    $$('td', root).forEach(c => {
      const r = c.dataset.r, v = value(r), s = raw[r] ?? '';
      c.textContent = show(r, v);
      c.className = [(o.cls || {})[r] || '', typeof v === 'number' || typeof v === 'boolean' ? 'n' : '', v && v.err ? 'err' : '', s.startsWith('=') ? 'f' : '', r === sel ? 'sel' : '', locked(r) ? 'lk' : ''].filter(Boolean).join(' ');
      c.removeAttribute('style'); if (style[r]) Object.assign(c.style, style[r]);
    });
    const refs = refsOf(raw[sel] || ''); refs.forEach(r => { const c = td(r); if (c) c.classList.add('ref'); });
    $('.sh-ref', root).textContent = sel; inp.value = raw[sel] ?? ''; inp.readOnly = locked(sel);
  }
  function select(r, focus) { sel = r; paint(); if (focus && !locked(r)) { inp.focus(); inp.select(); } }
  function commit() { if (locked(sel)) return; const v = inp.value.trim(); if (v === '') delete raw[sel]; else raw[sel] = v; paint(); if (o.onChange) o.onChange(api); }
  root.addEventListener('click', e => { const c = e.target.closest('td[data-r]'); if (c) select(c.dataset.r, true); });
  inp.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === 'Tab') { e.preventDefault(); commit(); const [c, r] = split(sel); const nx = e.key === 'Tab' ? L(Math.min(NC - 1, c + 1)) + (r + 1) : L(c) + Math.min(NR, r + 2); select(nx, true); }
    else if (e.key === 'Escape') { inp.value = raw[sel] ?? ''; inp.blur(); }
  });
  inp.addEventListener('blur', () => { if ((raw[sel] ?? '') !== inp.value.trim()) commit(); });
  const api = {
    get: r => { cache = {}; return value(r); }, text: r => { cache = {}; return show(r.toUpperCase(), value(r)); }, raw: r => raw[r.toUpperCase()] ?? '',
    set(r, v) { r = r.toUpperCase(); if (v === '' || v == null) delete raw[r]; else raw[r] = String(v); paint(); },
    load(cells) { Object.keys(raw).forEach(k => delete raw[k]); Object.entries(cells).forEach(([k, v]) => raw[k.toUpperCase()] = String(v)); Object.keys(style).forEach(k => delete style[k]); paint(); },
    style(r, st) { style[r.toUpperCase()] = st; paint(); }, select: r => select(r.toUpperCase()),
    sortRows(r1, r2, col, desc) { const rows = []; for (let r = r1; r <= r2; r++) rows.push([...Array(NC)].map((_, c) => raw[L(c) + r])); const ci = col.charCodeAt(0) - 65; cache = {};
      const key = row => sheetVal(row[ci]); rows.sort((a, b) => { const x = key(a), y = key(b); const d = typeof x === 'number' && typeof y === 'number' ? x - y : String(x).localeCompare(String(y), 'de'); return desc ? -d : d; });
      rows.forEach((row, k) => row.forEach((v, c) => { const ref = L(c) + (r1 + k); if (v == null) delete raw[ref]; else raw[ref] = v; })); paint(); },
    refresh: paint, get sel() { return sel; }
  };
  paint();
  return api;
}

/* Diagramm als SVG: chart(root, {type: 'bar'|'hbar'|'line'|'pie', data: [[Beschriftung, Wert], …], min, max, unit, title, step}) → {set(o)} */
const CHART_COLORS = ['#0E7490', '#C2410C', '#65A30D', '#7C3AED', '#CA8A04', '#BE123C', '#2563EB', '#64748B', '#0D9488', '#DB2777', '#78716C', '#9333EA'];
function chart(root, o = {}) {
  root.classList.add('chart');
  function draw() {
    const W = 420, H = 250, d = o.data || [], u = o.unit || '', fmt = v => numDE(v, 1) + u;
    let s = o.title ? `<text x="${W / 2}" y="14" text-anchor="middle" class="ch-t">${o.title}</text>` : '';
    if (o.type === 'pie') {
      const tot = d.reduce((a, x) => a + x[1], 0) || 1; let a0 = -Math.PI / 2; const cx = 120, cy = 135, r = 95;
      d.forEach(([l, v], i) => {
        const a1 = a0 + v / tot * 2 * Math.PI, big = a1 - a0 > Math.PI ? 1 : 0, c = CHART_COLORS[i % 12];
        s += d.length === 1 ? `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${c}"/>` : `<path d="M${cx},${cy} L${cx + r * Math.cos(a0)},${cy + r * Math.sin(a0)} A${r},${r} 0 ${big} 1 ${cx + r * Math.cos(a1)},${cy + r * Math.sin(a1)} Z" fill="${c}" class="ch-sl"><title>${l}: ${numDE(v / tot * 100, 1)} %</title></path>`;
        const am = (a0 + a1) / 2; if (v / tot > .06) s += `<text x="${cx + r * .65 * Math.cos(am)}" y="${cy + r * .65 * Math.sin(am) + 4}" text-anchor="middle" class="ch-in">${numDE(v / tot * 100, 0)} %</text>`;
        s += `<rect x="250" y="${30 + i * 19}" width="11" height="11" fill="${c}"/><text x="267" y="${40 + i * 19}" class="ch-l">${l}</text>`;
        a0 = a1;
      });
    } else if (o.type === 'hbar') {
      const mx = o.max ?? Math.max(...d.map(x => x[1])) * 1.1, x0 = 150, bw = W - x0 - 50, bh = Math.min(26, (H - 30) / d.length - 6);
      d.forEach(([l, v], i) => { const y = 24 + i * (bh + 6); s += `<text x="${x0 - 6}" y="${y + bh / 2 + 4}" text-anchor="end" class="ch-l">${l}</text><rect x="${x0}" y="${y}" width="${Math.max(0, v / mx * bw)}" height="${bh}" class="ch-bar"/><text x="${x0 + v / mx * bw + 4}" y="${y + bh / 2 + 4}" class="ch-v">${fmt(v)}</text>`; });
    } else {
      const vals = d.map(x => x[1]), mn = o.min ?? 0, mx = o.max ?? Math.max(...vals, mn + 1) * 1.12, x0 = 46, y0 = H - 30, y1 = 26, pw = W - x0 - 10;
      const Y = v => y0 - (v - mn) / (mx - mn) * (y0 - y1), st = o.step || niceStep((mx - mn) / 5);
      for (let v = Math.ceil(mn / st) * st; v <= mx + 1e-9; v += st) s += `<line x1="${x0}" x2="${W - 10}" y1="${Y(v)}" y2="${Y(v)}" class="ch-g"/><text x="${x0 - 5}" y="${Y(v) + 4}" text-anchor="end" class="ch-l">${numDE(v, 2)}${u}</text>`;
      const n = d.length, bw = pw / n;
      if (o.type === 'line') s += `<polyline points="${d.map(([l, v], i) => `${x0 + bw * (i + .5)},${Y(Math.max(mn, v))}`).join(' ')}" class="ch-line"/>`;
      d.forEach(([l, v], i) => {
        const x = x0 + bw * i, cv = Math.max(mn, Math.min(mx, v));
        if (o.type === 'line') s += `<circle cx="${x + bw / 2}" cy="${Y(cv)}" r="3.5" class="ch-dot"/>`;
        else s += `<rect x="${x + bw * .15}" y="${Y(cv)}" width="${bw * .7}" height="${Math.max(0, y0 - Y(cv))}" class="ch-bar"/>`;
        if (o.labels !== false) s += `<text x="${x + bw / 2}" y="${Y(cv) - 5}" text-anchor="middle" class="ch-v">${fmt(v)}</text>`;
        s += `<text x="${x + bw / 2}" y="${y0 + 15}" text-anchor="middle" class="ch-l">${l}</text>`;
      });
      s += `<line x1="${x0}" x2="${x0}" y1="${y1 - 8}" y2="${y0}" class="ch-ax"/><line x1="${x0}" x2="${W - 10}" y1="${y0}" y2="${y0}" class="ch-ax"/>`;
      if (mn > 0) s += `<path d="M${x0 - 6},${y0 - 10} l12,-4 M${x0 - 6},${y0 - 5} l12,-4" class="ch-brk"/>`;
    }
    root.innerHTML = `<svg viewBox="0 0 420 250" role="img" aria-label="${o.title || 'Diagramm'}">${s}</svg>`;
  }
  draw();
  return {set(p) { Object.assign(o, p); draw(); }};
}
function niceStep(x) { const p = 10 ** Math.floor(Math.log10(x)), m = x / p; return (m <= 1 ? 1 : m <= 2 ? 2 : m <= 5 ? 5 : 10) * p; }
