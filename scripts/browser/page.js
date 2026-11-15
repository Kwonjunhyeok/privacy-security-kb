// 사용법: node scripts/browser/page.js <저장폴더> <URL> [URL...]  → 폴더/NN.txt 에 제목·최종 URL·본문·링크 저장
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [out, ...urls] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const ctx = await b.newContext({ locale: 'ko-KR' });
  let i = 0;
  for (const u of urls) {
    i++;
    const p = await ctx.newPage();
    let s = '';
    try {
      const r = await p.goto(u, { waitUntil: 'networkidle', timeout: 45000 }).catch(async e => { await p.waitForTimeout(3000); return null; });
      const text = await p.innerText('body');
      const links = await p.$$eval('a', as => as.map(a => (a.innerText||a.title||'').replace(/\s+/g,' ').trim() + ' | ' + (a.getAttribute('href')||'') + ' | ' + (a.getAttribute('onclick')||'')));
      s = `URL: ${u}\nFINAL: ${p.url()}\nSTATUS: ${r && r.status()}\nTITLE: ${await p.title()}\n\n${text}\n\n#LINKS\n${links.join('\n')}\n`;
    } catch (e) { s = `URL: ${u}\nERR: ${e.message.split('\n')[0]}\n`; }
    const f = `${out}/${String(i).padStart(2,'0')}.txt`;
    fs.writeFileSync(f, s);
    console.log(f, s.split('\n').slice(0,4).join(' / '));
    await p.close();
  }
  await b.close();
})();
