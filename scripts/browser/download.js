// 사용법: node scripts/browser/download.js <저장파일> <게시물URL> <첨부 다운로드URL>
// 게시물을 브라우저로 연 뒤(쿠키·리퍼러 확보) 첨부 주소를 같은 세션으로 받아 저장한다.
// 첨부 주소 형식 (2026-11-15 확인)
//   개인정보위: https://www.pipc.go.kr/np/cmm/fms/FileDown.do?atchFileId=<FILE_...>&fileSn=<n>   (게시물의 fn_egov_downFile 인자)
//   KISA     : https://www.kisa.or.kr/post/fileDownload?menuSeq=<게시판>&postSeq=<번호>&attachSeq=<n>&lang_type=KO
//   국가사이버안보센터·보호나라처럼 첨부가 자바스크립트(downFile 등)로만 받아지는 곳은 세 번째 인자를
//   click:<첨부 링크 글자> 로 준다. 게시물에서 그 글자를 가진 링크를 눌러 브라우저 다운로드로 저장한다(2026-11-15 추가).
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [out, page, file] = process.argv.slice(2);
  const b = await chromium.launch();
  const ctx = await b.newContext({ locale: 'ko-KR' });
  const p = await ctx.newPage();
  await p.goto(page, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  if (file.startsWith('click:')) {
    const text = file.slice(6);
    const [dl] = await Promise.all([
      p.waitForEvent('download', { timeout: 120000 }),
      p.locator('a', { hasText: text }).first().click(),
    ]);
    const fail = await dl.failure();
    if (fail) { console.error('ERR download', fail); await b.close(); process.exit(1); }
    await dl.saveAs(out);
    console.log('download', dl.url(), dl.suggestedFilename(), fs.statSync(out).size, out);
    await b.close();
    return;
  }
  // 페이지 안에서 fetch 해야 브라우저와 같은 프록시·쿠키를 쓴다(ctx.request 는 프록시를 거치지 않는다)
  const res = await p.evaluate(async (u) => {
    const r = await fetch(u, { credentials: 'include' });
    const buf = new Uint8Array(await r.arrayBuffer());
    let bin = ''; for (let i = 0; i < buf.length; i += 0x8000) bin += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000));
    return { status: r.status, type: r.headers.get('content-type'), disp: r.headers.get('content-disposition'), b64: btoa(bin) };
  }, file);
  const body = Buffer.from(res.b64, 'base64');
  fs.writeFileSync(out, body);
  console.log(res.status, res.type, res.disp || '', body.length, out);
  await b.close();
})().catch(e => { console.error('ERR', e.message.split('\n')[0]); process.exit(1); });
