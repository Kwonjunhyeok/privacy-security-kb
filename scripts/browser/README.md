# 브라우저 수집 도구

국내 기관 누리집(pipc.go.kr, kisa.or.kr, msit.go.kr 등)은 WebFetch 로는 열리지 않는 일이 많아, 실제 브라우저(Chromium, Playwright)로 연다. 결과 파일은 저장소 밖(임시 폴더)에 두고 `kb/_pending/` 초안의 재료로만 쓴다.

| 스크립트 | 용도 |
|---|---|
| `page.js` | 페이지 본문 텍스트와 링크 목록 저장. 메뉴 구조·게시물 본문 확인용 |
| `board.js` | 게시판 목록 표의 행 추출. 여러 쪽 URL을 한 번에 넘긴다 |
| `download.js` | 게시물 첨부(PDF 등) 내려받기. 게시물을 연 뒤 페이지 안에서 받는다. 첨부 주소 형식은 파일 머리 주석 참고 |

```bash
# Playwright 가 전역 설치된 환경(클라우드 세션 기본)
NODE_PATH=$(npm root -g) node scripts/browser/board.js /tmp/pipc.tsv \
  "https://www.pipc.go.kr/np/cop/bbs/selectBoardList.do?bbsId=BS217&mCode=D010030000&pageIndex=1"
```

PC(Windows)에서 Node·Playwright 가 없으면 Claude 데스크톱 앱의 내장 브라우저로 같은 페이지를 열어 읽는다.

## 게시판별 쪽 넘김 (2026-11-15 확인)

| 출처 | 목록 URL | 쪽 넘김 | 비고 |
|---|---|---|---|
| 개인정보위 안내서 | https://www.pipc.go.kr/np/cop/bbs/selectBoardList.do?bbsId=BS217&mCode=D010030000 | `&pageIndex=N` | `pipc.go.kr`(www 없음)로 넘어감. 쪽당 10건+공지 |
| KISA 가이드라인 | https://www.kisa.or.kr/2060207 | `?page=N` | 쪽당 10건 |
| KISA 안내서 | https://www.kisa.or.kr/2060307 | `?page=N` | 쪽당 10건 |
| 개인정보 포털 안내서 | https://www.privacy.go.kr/front/bbs/bbsList.do?bbsNo=BBSMSTR_000000000049 | `&pageIndex=N` | 표가 아니라 `page.js` 로 읽는다 |
| 과기정통부 보도자료 | https://www.msit.go.kr/bbs/list.do?sCode=user&mPid=208&mId=307&bbsSeqNo=94 | `&pageIndex=N`, 제목 검색 `&searchOpt=NTT_SJ&searchTxt=…` | 표가 아니라 `page.js` 로 읽는다 |

가끔 첫 시도에서 빈 결과(0행)가 나온다. 그 쪽만 다시 받는다.

첨부 원문(PDF)은 저장소에 넣지 않는다(.gitignore). 임시 폴더에 받아 `pdftotext` 나 Python `pypdf` 로 글자를 뽑아 읽는다.
