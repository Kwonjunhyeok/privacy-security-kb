// 사용법: node scripts/browser/attachments.js <저장폴더> <게시물URL> [게시물URL...]
// 게시물의 첨부를 모두 원래 파일 이름으로 받는다(개인정보위 fn_egov_downFile, KISA fnPostAttachDownload).
// 저장폴더/<게시물 순번>/<원래 파일명> 으로 저장하고, 줄마다 "순번\t게시물URL\t파일명\t크기\t상태" 를 출력한다.
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [out, ...posts] = process.argv.slice(2);
  const b = await chromium.launch();
  const ctx = await b.newContext({ locale: 'ko-KR' });
  let n = 0;
  for (const post of posts) {
    n++;
    const dir = `${out}/${String(n).padStart(2, '0')}`; fs.mkdirSync(dir, { recursive: true });
    const p = await ctx.newPage();
    try {
      await p.goto(post, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
      const urls = await p.$$eval('a', as => {
        const seen = new Set(), r = [];
        for (const a of as) {
          const s = (a.getAttribute('onclick') || '') + ' ' + (a.getAttribute('href') || '');
          let m = s.match(/fn_egov_downFile\('([^']+)'\s*,\s*'([^']+)'/);
          let u = m ? `/np/cmm/fms/FileDown.do?atchFileId=${m[1]}&fileSn=${m[2]}` : null;
          m = s.match(/fnPostAttachDownload\((\d+)\s*,\s*'?(\d+)'?\s*,\s*(\d+)\s*,\s*'(\w+)'\)/);
          if (m && m[1] !== '99999999') u = `/post/fileDownload?menuSeq=${m[1]}&postSeq=${m[2]}&attachSeq=${m[3]}&lang_type=${m[4]}`;
          if (u && !seen.has(u)) { seen.add(u); r.push(u); }
        }
        return r;
      });
      if (!urls.length) console.log(`${n}\t${post}\t-\t0\t첨부 없음`);
      for (const u of urls) {
        let res;
        for (let t = 0; t < 2; t++) {
          res = await p.evaluate(async (u) => {
            const r = await fetch(u, { credentials: 'include' });
            const buf = new Uint8Array(await r.arrayBuffer());
            let bin = ''; for (let i = 0; i < buf.length; i += 0x8000) bin += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000));
            return { status: r.status, disp: r.headers.get('content-disposition') || '', b64: btoa(bin) };
          }, u);
          if (res.status === 200) break;
        }
        let name = 'file';
        const m1 = res.disp.match(/filename\*=UTF-8''([^;]+)/i), m2 = res.disp.match(/filename="?([^";]+)"?/i);
        if (m1) name = decodeURIComponent(m1[1]);
        else if (m2) { name = m2[1]; try { name = decodeURIComponent(name); } catch (e) {} if (/[À-ÿ]/.test(name)) name = Buffer.from(name, 'latin1').toString('utf8'); }
        name = name.replace(/[\\/:*?"<>|]/g, '_').trim();
        const body = Buffer.from(res.b64, 'base64');
        if (res.status === 200) fs.writeFileSync(`${dir}/${name}`, body);
        console.log(`${n}\t${post}\t${name}\t${body.length}\t${res.status}`);
      }
    } catch (e) { console.log(`${n}\t${post}\t-\t0\tERR ${e.message.split('\n')[0]}`); }
    await p.close();
  }
  await b.close();
})();
