# 매일 갱신 절차

이 PC의 데스크톱 예약 작업 `kb-daily-update` 가 매일 06:00 (KST) 이 문서를 그대로 실행하고 결과를 GitHub 에 push 한다(하이브리드 구성). 06:00 에 PC·앱이 꺼져 있으면 다음에 켤 때 실행된다. 클라우드 루틴(trig_01Qjd6uLw8oVCAZwP1cngtoz)은 클라우드 네트워크가 국내 기관 사이트를 막아 원문 검증이 안 되므로 꺼 두었다. 둘을 동시에 켜지 않는다. 수동으로 돌릴 때도 같은 순서를 따른다.

오늘 날짜를 `TODAY` (YYYY-MM-DD, KST) 라 한다.

## 0. 준비

1. `CLAUDE.md`, `sources.md`, `kb/index.md` 를 읽는다.
2. `kb/_pending/` 의 기존 항목 목록을 확인한다.
3. **1차 출처 접속 사전 점검**: 아래 명령으로 A 등급 출처 접속을 확인한다.
   ```bash
   for u in https://www.law.go.kr https://www.pipc.go.kr https://isms.kisa.or.kr https://www.boho.or.kr https://www.privacy.go.kr https://www.msit.go.kr; do
     echo "$u $(curl -sS -m 15 -o /dev/null -w '%{http_code}' "$u" 2>/dev/null)"
   done
   ```
   - 응답 코드가 `000` 이거나 연결 오류(CONNECT 403, DNS 실패 등)면 접속 실패로 본다.
   - **전부 실패하면 즉시 중단한다.** 수집·검증·반영을 하지 않고, `_pending` 의 `attempts` 도 올리지 않으며, 커밋·push 도 하지 않는다. 예약 실행이면 알림(PushNotification)으로 실패한 도메인과 응답 코드만 알리고 끝낸다. 클라우드 환경에서 실행됐다면 클라우드 루틴이 켜져 있다는 뜻이므로 알림에 그 사실도 적는다.
   - 일부만 실패하면 계속하되, 실패한 도메인 목록을 2단계 검증기에 넘기고 보고서 `## 출처 접근 문제` 에 적는다.

## 1. 수집 — `kb-collector` 에이전트

`kb-collector` 서브에이전트를 호출해 다음을 맡긴다.

- `sources.md` 의 각 출처에서 `kb/index.md` 의 마지막 검증일 이후 새로 나온 것 또는 바뀐 것을 찾는다.
  - 법령·고시: 공포번호 또는 시행일이 index 값과 다르면 개정 후보.
  - ISMS-P·가이드: 개정판·게시일이 index 값보다 새로우면 후보.
  - 위협·동향: 최근 24시간(첫 실행이면 90일) 게시물.
- 후보마다 `kb/_pending/TODAY-<slug>.md` 에 초안을 쓴다. frontmatter 는 `CLAUDE.md` 형식을 따르되 `verified` 는 비워 두고, 아래 필드를 추가한다.
  ```yaml
  candidate:
    kind: new | revision | repeal   # 신규 | 개정(교체 대상) | 폐지
    replaces: kb/laws/....md        # revision/repeal 일 때 교체할 기존 문서
    found_at: [수집 때 본 URL들]
    attempts: 0          # 원문을 열고도 확인 못 한 횟수 (3이면 기각)
    access_failures: 0   # 원문 접속 자체를 못 한 횟수 (기각 사유 아님)
  ```
- 수집기는 `kb/` 의 `_pending/` 밖 파일을 절대 수정하지 않는다.

## 2. 검증 — `kb-fact-checker` 에이전트

`kb-fact-checker` 서브에이전트를 호출해 `kb/_pending/` 의 **모든** 항목(오늘 것과 이전 대기분)을 검증하게 한다. 검증기는 항목별로 아래 판정 중 하나를 낸다.

| 판정 | 조건 | 처리 |
|---|---|---|
| 통과 | 1차 출처 원문을 직접 다시 열어 조문 번호·시행일·공포번호·수치가 모두 일치하고, A 등급 출처 2곳 이상이 일치 (threats 는 A 1곳) | 3단계로 반영 |
| 수정 후 통과 | 일부 값이 틀렸으나 원문에서 정확한 값을 확인함 | 검증기가 값을 고친 뒤 통과 처리, 보고서에 고친 내용 기록 |
| 보류(접근) | 네트워크 차단·DNS 실패·타임아웃 등으로 필요한 A 등급 원문을 열지 못함 | `_pending` 에 남기고 `attempts` 는 **올리지 않는다**. `access_failures` +1, 사유 기록 |
| 보류(내용) | 원문은 열었으나 출처 간 불일치, 값 미확인, B 등급 단서만 있음 | `_pending` 에 남기고 `attempts` +1, 사유 기록 |
| 기각 | 원문과 명백히 다름, 존재하지 않는 개정, 통과 전 개정안을 개정으로 오인 등 | `_pending` 에서 삭제, 보고서에 사유 기록 |

`attempts` 가 3이 된 보류 항목은 기각으로 처리한다. `attempts` 는 원문을 실제로 열고도 확인하지 못한 경우만 센다. 접속하지 못해 생긴 보류는 `access_failures` 로 따로 세고, 이것으로는 기각하지 않는다. `access_failures` 가 계속 쌓이면 보고서 `## 출처 접근 문제` 에 적어 사람이 판단하게 한다.

## 3. 반영 (통과 항목만)

- `new`: 해당 카테고리 폴더에 문서를 만든다.
- `revision`: `replaces` 문서를 **통째로 덮어쓴다**. 구버전 본문을 다른 곳에 남기지 않는다.
- `repeal`: 해당 문서를 삭제하고 `crossref.md` 에서 연결을 지운다.
- 반영한 항목마다 `kb/CHANGELOG.md` 맨 위에 한 줄을 추가한다.
  ```
  - TODAY | 개정 | 개인정보의 안전성 확보조치 기준 | 고시 제2026-x호, 시행 2026-xx-xx | 제8조(접속기록) 보관기간 변경 | 대조: law.go.kr, pipc.go.kr
  ```
- 반영이 끝난 `_pending` 파일은 삭제한다.
- 개정 검증이 보류된 경우 기존 현행본은 그대로 두고 CHANGELOG 에 `- TODAY | 개정 의심(검증 대기) | 문서명 | 사유` 를 남긴다.

## 4. 정리

1. `kb/threats/` 에서 `published_date` 가 90일보다 오래된 문서를 삭제한다.
2. `kb/crossref.md` 를 갱신한다. 반영·삭제된 문서와 연결된 행을 고치고, 새 문서의 연관 항목(ISMS-P 항목, 법 조항, 가이드, 처분 사례)을 추가한다. 연결은 양쪽 문서 본문에서 근거를 확인한 것만 적는다.
3. `kb/index.md` 를 갱신한다. 문서별 시행일·마지막 검증일을 고치고, 맨 위 `마지막 갱신:` 을 TODAY 로 바꾼다. 아무 변경이 없어도 날짜는 갱신한다.

## 5. 보고서

`kb/reports/TODAY.md` 를 쓴다.

```markdown
# 검증 보고서 TODAY

| 구분 | 건수 |
|---|---|
| 수집 후보 | n |
| 통과 / 수정 후 통과 | n / n |
| 보류 | n |
| 기각 | n |
| threats 만료 삭제 | n |

## 반영 내역
- (CHANGELOG 와 같은 줄)

## 수정 후 통과 내역
- 문서 | 틀린 값 → 원문 값 | 근거 URL

## 보류·기각 사유
- 문서 | 판정 | 사유 | attempts

## 출처 접근 문제
- (접속 실패·사이트 개편 등)
```

## 6. 커밋

```
git add -A
git commit -m "kb: TODAY 갱신 (통과 n, 보류 n, 기각 n)"
git push
```

변경이 보고서와 index 날짜뿐이어도 커밋한다. 상담 에이전트가 "마지막 갱신일"로 신선도를 판단하기 때문이다.
