---
name: kb-update
description: 정보보호·개인정보보호 지식베이스 저장소(privacy-security-kb)를 어떤 PC에서든 로컬에 구성하거나 최신화하고, UPDATE.md 주간 갱신(수집→검증→반영→보고→push)을 서브에이전트로 진행한다. "지식베이스 갱신해줘", "UPDATE.md 대로 주간 갱신", "kb 최신화", "새 PC에 정보보호 지식베이스 받아줘", "security-kms 에이전트 설정", "kb pull 하고 상담 에이전트 복사" 같은 요청이나, 법령·고시·처분·보안공지·가이드 현행화를 지식베이스에 반영하려는 요청이면 이 스킬을 쓴다. 지식베이스를 근거로 질문에 답하는 일은 security-kms 에이전트 몫이니 이 스킬을 쓰지 않는다.
---

# 정보보호 지식베이스 구성·갱신

이 스킬은 **순서를 잡는 메인 세션용**이다. 수집·취합·검증은 저장소의 서브에이전트(`kb-collector`, `kb-guide-curator`, `kb-fact-checker`)가 맡고, 세부 규칙은 저장소의 `UPDATE.md`·`CLAUDE.md`·`sources.md` 가 기준이다. 이 문서는 그 파일들을 대신하지 않는다. 둘이 다르면 저장소 파일을 따른다(저장소 쪽이 더 자주 고쳐진다).

**PC 로컬 세션용**이다. 클라우드 세션(claude.ai/code)에서는 저장소의 `kb-cloud-update` 스킬을 쓴다(작업 브랜치 → PR → 사용자 병합). 같은 날 두 곳에서 동시에 돌리지 않는다. 시작 전에 `git fetch` 로 원격 main 에 최근 1시간 안의 kb 커밋이 있는지 보고, 있으면 다른 곳에서 진행 중으로 보고 멈춘다.

메인 세션이 맡는 이유: 서브에이전트는 다른 서브에이전트를 부를 수 없고 사용자에게 묻지도 못한다. 수집과 검증을 다른 에이전트로 나누는 원칙, 삭제 전 확인, 체크포인트 push 는 메인 세션만 지킬 수 있다.

## 고정 값

| 항목 | 값 |
|---|---|
| 저장소 | `https://github.com/Kwonjunhyeok/privacy-security-kb.git` (branch `main`) |
| 로컬 경로 | 환경변수 `KB_REPO_DIR` → 없으면 아래 후보 중 `.git` 과 `UPDATE.md` 가 있는 곳 → 없으면 사용자에게 묻는다 |
| 경로 후보 | `D:\Jun\정보보호에이전트`, `~/정보보호에이전트`, `~/privacy-security-kb` |
| 상담 에이전트 사본 | 저장소 `.claude/agents/security-kms.md` → 사용자 에이전트 폴더(기본 `~/.claude/agents/`, 이 사용자의 주 PC는 `D:\Jun\.claude\agents\`) |
| 원본 보관 폴더(선택) | `D:\Jun\101. 정보보호 자료집` (Google Drive 데스크톱 앱이 동기화. 다른 PC면 사용자에게 묻고, 없으면 이 단계를 건너뛴다) |

## 먼저 할 일: 모드 고르기

`python scripts/env_check.py [저장소경로]` 로 도구와 저장소 상태를 본다(Python이 없으면 `git --version`, `node -v`, `git -C <경로> status --short` 로 대신한다). 그다음 요청에 맞는 모드를 고른다.

| 모드 | 언제 | 하는 일 |
|---|---|---|
| **구성** | 저장소가 이 PC에 없다 | clone → 상담 에이전트 복사 → 브라우저 도구 준비 |
| **동기화** | 저장소는 있고 최신본만 필요하다 | pull → 상담 에이전트가 바뀌었으면 복사 |
| **주간 갱신** | "갱신", "UPDATE.md 대로" | 동기화 → UPDATE.md 0~6단계 → 원본 보관(선택) → 보고 |

## 구성

1. `git` 이 없으면 설치를 안내하고 멈춘다(설치는 사용자가 한다).
2. 경로를 정한다. 사용자가 말하지 않았으면 경로 후보 첫 번째의 상위 폴더가 있는지 보고, 없으면 묻는다.
3. `git clone <저장소> <경로>`. 비공개 저장소라 인증이 필요하면 `gh auth status` 를 확인하고, 로그인은 사용자에게 맡긴다(토큰을 대신 입력하지 않는다).
4. 상담 에이전트 사본을 복사하고 같은지 확인한다(아래 "상담 에이전트 사본").
5. 주간 갱신까지 할 PC면 "브라우저 도구"를 준비한다. 상담만 할 PC면 생략한다.
6. 결과를 짧게 보고한다: 경로, `git log --oneline -1`, 에이전트 사본 위치, 브라우저 도구 상태.

## 동기화

1. `git -C <경로> status --short`. 커밋 안 된 변경이 있으면 **지우지 말고** 파일 목록을 보여 주고 멈춘다. 예외: `UPDATE.md` "사용량 한도 대비"에 따라 `kb/` 아래 변경은 이전 실행 중단분일 수 있다. 주간 갱신 모드에서는 내용을 보여 주고 사용자가 동의하면 먼저 커밋·push 한다.
2. `git -C <경로> checkout main` → `git -C <경로> pull --ff-only`. 실패하면 이유를 보여 주고 멈춘다(merge·rebase·reset 을 임의로 하지 않는다).
3. `git log --oneline -1` 을 보여 준다.
4. 상담 에이전트 사본을 맞춘다.

### 상담 에이전트 사본

저장소의 `.claude/agents/security-kms.md` 와 사본을 비교한다. 다르면 차이(`diff -u 사본 원본`)를 몇 줄로 요약해 보여 주고, 덮어써 복사한 뒤 `cmp`(또는 sha256)로 같은지 확인한다. 사본이 없으면 새로 복사한다. 이 복사는 사용자가 이 스킬을 부른 것 자체가 요청이므로 따로 묻지 않는다.

## 주간 갱신

먼저 "동기화"를 한다. 그다음 저장소의 `UPDATE.md` 를 처음부터 끝까지 읽고 그대로 따른다. 아래는 UPDATE.md 를 실제로 돌리면서 막혔던 점과 그 해법이다.

### 시작 순서

1. 최신 `kb/reports/*.md` 의 "다음 실행 이월" 을 읽는다. **이월 항목을 새 수집보다 먼저** 처리한다.
2. `kb/_pending/` 의 항목 수와 `attempts` 를 센다: `grep -H "attempts:" kb/_pending/*.md`. `attempts: 2` 인 항목은 이번에도 보류되면 기각된다는 뜻이니 우선 검증한다.
3. 처리량 제한(UPDATE.md, 현재 검증 25건·새 수집 20건)으로 이번 실행의 범위를 정해 사용자에게 한 줄로 알린다. 우선순위: 이월 항목 → attempts 높은 순 → 오래된 순. 나머지는 보고서 "다음 실행 이월"로 넘긴다.

### 서브에이전트 부르기

- 항상 **포그라운드**로, `kb-collector` → `kb-guide-curator` → `kb-fact-checker` 순서로 하나씩 부른다(동시에 띄우면 `_pending` 이 겹친다).
- 세션 작업 폴더가 저장소이면 프로젝트 에이전트가 이름으로 잡힌다. 아니면(에이전트 목록에 없으면) `general-purpose` 에이전트를 부르고 프롬프트 첫머리에 "저장소의 `.claude/agents/<이름>.md` 를 읽고 그 역할과 규칙을 그대로 따르라"고 적는다. 모델은 역할 파일의 `model:` 을 따른다(수집기·가이드 취합기 sonnet, 검증기 opus). 단, 보안공지(threats)만 검증하는 묶음은 Agent 호출에 `model: sonnet` 을 지정한다(UPDATE.md '모델' 표). general-purpose 로 대신 부를 때도 같은 모델을 지정한다.
- 프롬프트에 넣을 것: 저장소 절대경로, TODAY, 이번 범위(검증할 파일 목록 또는 수집 한도), 원문 여는 방법(아래), 임시 폴더 경로(저장소 밖), "`kb/_pending/` 밖은 고치지 말 것", 끝나면 돌려줄 표 형식.
- 검증기에는 수집기가 무엇을 봤는지 설명하지 않는다. 독립 검증이 이 저장소의 핵심이다.

### 원문 여는 방법

국내 기관 누리집은 WebFetch 로 자주 실패하고(ENOTFOUND), 검색 요약은 근거가 아니다. 그래서:

- **메인 세션**: 앱 내장 브라우저(`mcp__Claude_Browser__*`)로 연다. 게시판 목록·첨부 ID는 페이지 안 `fetch` 와 DOMParser 로 여러 쪽을 한 번에 읽을 수 있다(같은 출처일 때).
- **서브에이전트**: 2026-11-15 실행에서는 서브에이전트(`general-purpose`)도 내장 브라우저 도구를 그대로 썼다. 프롬프트에 "필요하면 ToolSearch 로 `mcp__Claude_Browser__` 를 한 번에 불러온다"고 적는다. 내장 브라우저는 창 하나를 같이 쓰므로 검증·수집 에이전트는 한 번에 하나씩 돌린다. 내장 브라우저가 없는 환경에서만 `scripts/browser/`(Playwright)를 쓴다. 준비는 아래.
- **개인정보위 첨부**: curl 로 받을 때 게시물 페이지를 먼저 받아 쿠키(`-c`/`-b`)를 쓰고 브라우저 User-Agent·Referer 를 붙인다. 쿠키가 없으면 400 이 온다.
- **한글이 안 뽑히는 PDF**(회의록·속기록 등): `pdftotext` 결과가 비면 PowerShell 의 `Windows.Data.Pdf` 로 필요한 쪽을 PNG 로 렌더링해 읽는다.
- **이 PC 의 Python 3.6**: 한글이 든 스크립트를 `python - <<EOF` 로 넘기면 깨진다. 스크립트를 `# -*- coding: utf-8 -*-` 파일로 저장해 실행한다.
- 기관별 쪽 넘김·첨부 주소 형식은 저장소 `scripts/browser/README.md` 에 있다. 개인정보위는 `pipc.go.kr`(www 없음)로 넘어간다. 국가사이버안보센터는 token 주소이고 첨부는 `POST /api/usr/bbs/downloadFile`(`downloadFileId`)이며 게시물에 SHA-256 이 적혀 있다.
- 첨부가 0바이트·502 로 오면 한 번 더 받는다. 그래도 안 되면 보류 사유로 적는다.

### 브라우저 도구 준비 (Playwright)

저장소 안에 `node_modules` 를 만들지 않는다. 저장소 밖 도구 폴더(예: `~/.cache/kb-tools`, Windows 는 `%LOCALAPPDATA%\kb-tools`)에 설치한다.

```bash
mkdir -p ~/.cache/kb-tools && cd ~/.cache/kb-tools
npm init -y >/dev/null && npm install playwright
npx playwright install chromium     # 수백 MB. 2026-11-15 PC 에서는 headless shell 받기가 끝나지 않고 실패했다(내장 브라우저로 대신함)
# 사용: NODE_PATH=~/.cache/kb-tools/node_modules node <저장소>/scripts/browser/board.js <출력> <URL...>
```

PDF 글자 추출은 `pdftotext` 나 Python `pypdf` 로 한다. 내려받은 파일은 각자 새 빈 폴더에 두고, 그 폴더 안에서 인터프리터를 실행하지 않는다.

### 체크포인트

UPDATE.md 의 A(기존 `_pending` 검증·반영 후), B(새 수집 후), C(보고서 후)마다 `git add -A` → 커밋 → `git push`. 커밋 메시지는 UPDATE.md 6단계 형식을 따른다. push 가 거부되면(원격이 앞섬) `pull --ff-only` 후 다시 push 하고, 충돌하면 멈추고 보고한다.

### 반영 규칙에서 자주 틀리는 것

- 반영은 검증기가 **통과·수정 후 통과**로 판정한 것만. 메인 세션이 판정을 바꾸지 않는다.
- `attempts` 가 3이 된 보류는 기각이다(`_pending` 에서 지우고 보고서에 사유).
- `revision` 은 기존 문서를 통째로 덮어쓴다. 새 판이 파일명이 다르면 이전 판 파일을 지우고 `index.md`·`catalog.md`·`crossref.md` 링크를 바꾼다.
- `kb/threats/` 는 `published_date` 90일 지난 것을 지운다.
- `index.md`·`catalog.md` 의 `마지막 갱신:` 은 변경이 없어도 TODAY 로 바꾼다.

## 원본 보관 (선택)

이번에 kb 에 **새로 반영되거나 판이 바뀐 가이드·안내서**만 원본을 보관 폴더에 둔다.

1. 각 자료의 공식 게시물 첨부를 받는다(다른 사이트 사본 금지). 받은 파일 정보를 manifest JSON 으로 적는다. 형식은 `scripts/archive_originals.py` 머리 주석.
2. `python scripts/archive_originals.py <manifest.json> <보관폴더>` — 파일명 `<기관>_<자료명>_<판 또는 게시일>.<확장자>`, 같은 sha256 이 이미 있으면 건너뛰고, `수집목록.csv`(UTF-8 BOM)에 줄을 더한다. 공식 SHA-256 이 있으면 대조한다.
3. 스크립트가 출력한 "이전 판 후보"(같은 기관·자료명, 다른 판)는 **지우지 말고** 목록을 보여 준 뒤 사용자 확인을 받고 지운다. CSV 의 해당 줄도 함께 지운다.
4. 보관 폴더가 Drive 동기화 폴더여도 드라이브 커넥터로 따로 올리지 않는다.

## 마지막 보고

아래 표를 그대로 채워 보여 준다.

| 구분 | 건수 |
|---|---|
| 수집 후보 | n |
| 통과 / 수정 후 통과 | n / n |
| 보류 | n |
| 기각 | n |
| threats 만료 삭제 | n |

이어서 짧게:
- **주요 개정 사항**: 법령·고시 공포번호·시행일 변경, 가이드 새 판(구 판 → 신 판)
- **이월 항목**: 다음 실행으로 넘긴 것과 이유(처리량 한도, 원문 접근 실패 등)
- **push 결과**: 마지막 커밋 해시
- **원본 보관**: 받은 파일 / 받지 못한 것 / 지운 이전 판
- **상담 에이전트 사본**: 바뀌었으면 복사·일치 확인 결과
