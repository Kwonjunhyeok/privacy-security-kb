// 사용법: node scripts/browser/board.js <결과.tsv> <목록URL> [URL...]  → 게시판 표의 행을 TSV(출처URL, 칸들, 링크)로 저장
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [out, ...urls] = process.argv.slice(2);
  const b = await chromium.launch();
  const ctx = await b.newContext({ locale: 'ko-KR' });
  const p = await ctx.newPage();
  const lines = [];
  for (const u of urls) {
    try {
      await p.goto(u, { waitUntil: 'networkidle', timeout: 45000 }).catch(()=>p.waitForTimeout(3000));
      const rows = await p.$$eval('table tbody tr, ul.board_list li, .board-list li, .bbs_list li', trs => trs.map(tr => {
        const cells = [...tr.querySelectorAll('td, th, span, p, strong')].length && tr.tagName==='TR'
          ? [...tr.querySelectorAll('td, th')].map(td => td.innerText.replace(/\s+/g,' ').trim())
          : [tr.innerText.replace(/\s+/g,' ').trim()];
        const a = tr.querySelector('a');
        return cells.concat([a ? (a.getAttribute('href')||'') + ' ' + (a.getAttribute('onclick')||'') : '']).join('\t');
      }));
      rows.forEach(r => lines.push(u + '\t' + r));
      console.error(u, rows.length);
    } catch (e) { console.error(u, 'ERR', e.message.split('\n')[0]); lines.push(u + '\tERR'); }
  }
  fs.writeFileSync(out, lines.join('\n') + '\n');
  await b.close();
})();
