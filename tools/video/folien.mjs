// Rendert Folien (1920x1080) und Thumbnail (1280x720) aus schnittplan.json via Playwright.
// Aufruf: node tools/video/folien.mjs <videoordner>
import fs from 'node:fs'; import path from 'node:path'; import { createRequire } from 'node:module';
const require = createRequire(import.meta.url); const { chromium } = require('playwright');
const dir = process.argv[2]; const plan = JSON.parse(fs.readFileSync(path.join(dir, 'schnittplan.json'), 'utf8'));
const timing = JSON.parse(fs.readFileSync(path.join(dir, 'build/timing.json'), 'utf8'));
const out = path.join(dir, 'build/folien'); fs.mkdirSync(out, { recursive: true });
const MARKE = 'QM-Klartext';
const esc = s => String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const FARBE = { rot:'#C0392B', gruen:'#2E8B57', blau:'#1F3A5F', orange:'#E8730C', grau:'#6B7280' };
const CSS = `*{box-sizing:border-box;margin:0}body{width:1920px;height:1080px;font-family:Inter,sans-serif;background:#F7F8FA;color:#1F2937;overflow:hidden;position:relative}
.top{position:absolute;top:0;left:0;right:0;height:84px;display:flex;align-items:center;justify-content:space-between;padding:0 80px;font-size:26px;color:#6B7280}
.kap{color:#1F3A5F;font-weight:600}.marke{font-weight:700;color:#1F3A5F}.marke b{background:#1F3A5F;color:#fff;border-radius:8px;padding:4px 10px;margin-right:12px;font-size:22px}
.main{position:absolute;top:120px;left:120px;right:120px;bottom:120px;display:flex;flex-direction:column;justify-content:center}
h1{font-size:72px;line-height:1.1;color:#1F3A5F;font-weight:800;letter-spacing:-1px;margin-bottom:48px}
.unter{font-size:40px;color:#4B5563;max-width:1400px}.badge{display:inline-block;background:#E8730C;color:#fff;font-weight:700;font-size:30px;padding:10px 24px;border-radius:10px;margin-bottom:36px;align-self:flex-start}
ul{list-style:none;padding:0}li{font-size:46px;line-height:1.3;margin:0 0 28px 0;padding-left:56px;position:relative}li:before{content:"";position:absolute;left:0;top:20px;width:22px;height:22px;border-radius:50%;background:#E8730C}
.hinweis{margin-top:24px;font-size:38px;font-weight:700;color:#E8730C;border-left:10px solid #E8730C;padding-left:28px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:56px}.col{background:#fff;border-radius:20px;padding:44px;border-top:14px solid var(--f);box-shadow:0 6px 24px rgba(0,0,0,.06)}
.col h2{font-size:46px;color:var(--f);margin-bottom:28px}.col li{font-size:38px}.col li:before{background:var(--f);top:16px}
.zs{display:flex;gap:16px;align-items:stretch}.st{flex:1;background:#fff;border-radius:16px;padding:26px 10px;text-align:center;box-shadow:0 4px 16px rgba(0,0,0,.06);border:3px solid transparent}
.st .l{font-size:44px;font-weight:800;color:#1F3A5F}.st .t{font-size:22px;color:#4B5563;margin-top:10px;line-height:1.25}.st.akt{background:#1F3A5F;transform:scale(1.08)}.st.akt .l,.st.akt .t{color:#fff}.st.ok{opacity:.5}
.karten{display:grid;grid-template-columns:repeat(var(--n),1fr);gap:36px}.karte{background:#fff;border-radius:20px;padding:40px 32px;box-shadow:0 6px 24px rgba(0,0,0,.06)}
.karte .nr{width:64px;height:64px;border-radius:50%;background:#1F3A5F;color:#fff;font-size:32px;font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:24px}.karte h3{font-size:38px;color:#1F3A5F;margin-bottom:14px}.karte p{font-size:30px;color:#4B5563;line-height:1.35}
.xl{background:#fff;border:2px solid #CBD5E1;border-radius:6px;overflow:hidden;box-shadow:0 8px 30px rgba(0,0,0,.08)}.xlbar{background:#217346;color:#fff;font-size:24px;padding:12px 20px;font-weight:600}
table{border-collapse:collapse;width:100%;font-size:28px}th{background:#1F3A5F;color:#fff;text-align:left;padding:16px 18px;font-weight:600}td{padding:14px 18px;border-bottom:1px solid #E5E7EB;border-right:1px solid #F1F5F9}tr.m td{background:#FFF1E6;font-weight:700}
h1.k{font-size:58px;margin-bottom:36px}.cta{align-items:flex-start}.btn{margin-top:40px;background:#E8730C;color:#fff;font-size:44px;font-weight:800;padding:26px 52px;border-radius:16px}
.fiktiv{position:absolute;right:80px;bottom:44px;font-size:22px;color:#92400E;background:#FEF3C7;padding:6px 16px;border-radius:8px}
.prog{position:absolute;left:0;bottom:0;height:10px;background:#E8730C}`;
function body(s){const d=s.daten||{};switch(s.layout){
case 'titel': return `${d.badge?`<div class="badge">${esc(d.badge)}</div>`:''}<h1>${esc(d.ueberschrift)}</h1><div class="unter">${esc(d.unterzeile)}</div>`;
case 'punkte': return `<h1 class="k">${esc(d.ueberschrift)}</h1><ul>${(d.punkte||[]).map(p=>`<li>${esc(p)}</li>`).join('')}</ul>${d.hinweis?`<div class="hinweis">${esc(d.hinweis)}</div>`:''}`;
case 'zwei_spalten': {const c=x=>`<div class="col" style="--f:${FARBE[x?.farbe]||FARBE.blau}"><h2>${esc(x?.titel)}</h2><ul>${(x?.punkte||[]).map(p=>`<li>${esc(p)}</li>`).join('')}</ul></div>`;return `<h1 class="k">${esc(d.ueberschrift)}</h1><div class="cols">${c(d.links)}${c(d.rechts)}</div>`;}
case 'zeitstrahl': return `<h1 class="k">${esc(d.ueberschrift)}</h1><div class="zs">${(d.schritte||[]).map((x,i)=>`<div class="st ${d.aktiv===i?'akt':(d.aktiv!=null&&i<d.aktiv?'ok':'')}"><div class="l">${esc(x.label)}</div><div class="t">${esc(x.text)}</div></div>`).join('')}</div>`;
case 'tabelle': return `<h1 class="k">${esc(d.ueberschrift)}</h1><div class="xl"><div class="xlbar">8D-Report-Vorlage.xlsx · Blatt: ${esc(d.blatt||'')}</div><table><tr>${(d.spalten||[]).map(x=>`<th>${esc(x)}</th>`).join('')}</tr>${(d.zeilen||[]).map((z,i)=>`<tr class="${(d.markiert||[]).includes(i)?'m':''}">${z.map(x=>`<td>${esc(x)}</td>`).join('')}</tr>`).join('')}</table></div>${d.hinweis?`<div class="hinweis">${esc(d.hinweis)}</div>`:''}`;
case 'karten': return `<h1 class="k">${esc(d.ueberschrift)}</h1><div class="karten" style="--n:${(d.karten||[]).length||1}">${(d.karten||[]).map((k,i)=>`<div class="karte"><div class="nr">${i+1}</div><h3>${esc(k.titel)}</h3><p>${esc(k.text)}</p></div>`).join('')}</div>`;
case 'cta': return `<h1>${esc(d.ueberschrift)}</h1><div class="unter">${esc(d.text)}</div><div class="btn">${esc(d.button)}</div>`;
default: return `<h1>${esc(d.ueberschrift||s.kapitel)}</h1>`;}}
const total = timing.gesamt;
const browser = await chromium.launch(); const page = await browser.newPage({ viewport:{width:1920,height:1080} });
for (const s of plan.segmente) {
  const t = timing.segmente[s.id]; const pct = ((t.start + t.dauer) / total * 100).toFixed(2);
  const html = `<!doctype html><meta charset="utf-8"><style>${CSS}</style><div class="top"><span class="kap">${esc(s.kapitel)}</span><span class="marke"><b>QM</b>${MARKE}</span></div><div class="main ${s.layout==='cta'?'cta':''}">${body(s)}</div>${s.fiktiv?'<div class="fiktiv">Fiktives Beispiel</div>':''}<div class="prog" style="width:${pct}%"></div>`;
  await page.setContent(html); await page.screenshot({ path: path.join(out, `${s.id}.png`) });
}
// Thumbnail
const th = plan.thumbnail || { zeile1: '8D-Report', zeile2: 'richtig gemacht', badge: 'Gratis-Vorlage' };
await page.setViewportSize({ width:1280, height:720 });
await page.setContent(`<!doctype html><meta charset="utf-8"><style>*{margin:0;box-sizing:border-box}body{width:1280px;height:720px;font-family:Inter,sans-serif;background:linear-gradient(135deg,#1F3A5F 0%,#0F2238 100%);color:#fff;position:relative;overflow:hidden;padding:70px}
.z1{font-size:150px;font-weight:900;letter-spacing:-4px;line-height:1}.z2{font-size:86px;font-weight:800;color:#E8730C;margin-top:18px;line-height:1.05;max-width:760px}
.badge{position:absolute;left:70px;bottom:60px;background:#fff;color:#1F3A5F;font-size:40px;font-weight:800;padding:14px 28px;border-radius:14px}
.d{position:absolute;right:60px;top:70px;display:grid;grid-template-columns:repeat(3,120px);gap:16px}.d div{height:120px;border-radius:18px;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:800}.d div.a{background:#E8730C}</style>
<div class="z1">${esc(th.zeile1)}</div><div class="z2">${esc(th.zeile2)}</div><div class="badge">${esc(th.badge)}</div>
<div class="d">${['D1','D2','D3','D4','D5','D6','D7','D8','✓'].map(x=>`<div class="${x==='D4'?'a':''}">${x}</div>`).join('')}</div>`);
await page.screenshot({ path: path.join(dir, 'build/thumbnail.png') });
await browser.close(); console.log(`Folien: ${plan.segmente.length} + Thumbnail -> ${out}`);
