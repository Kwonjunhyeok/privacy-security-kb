# 클라우드 루틴 설정

https://claude.ai/code/routines 에서 등록한다.

| 항목 | 값 |
|---|---|
| 이름 | 정보보호 지식베이스 일일 갱신 |
| 저장소 | Kwonjunhyeok/privacy-security-kb |
| 일정 | 매일 06:00 (Asia/Seoul) — UTC cron `0 21 * * *` |
| 모델 | Claude Opus 5.5 |
| 환경 | Default |
| 도구 | Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Agent |

## 프롬프트

아래 블록 안의 내용을 그대로 붙여넣는다.

```text
너는 정보보호·개인정보보호 지식베이스(이 저장소)의 일일 갱신 담당이다. 오늘 날짜는 KST 기준으로 `TZ=Asia/Seoul date +%Y-%m-%d` 를 실행해 구하고 TODAY 라 한다.

1. 저장소 루트의 CLAUDE.md, sources.md, UPDATE.md 를 먼저 끝까지 읽는다.
2. UPDATE.md 의 0~6단계를 순서대로 빠짐없이 실행한다.
   - 1단계 수집은 반드시 `kb-collector` 서브에이전트(Agent 도구, .claude/agents/kb-collector.md)에 맡긴다.
   - 1-2단계 가이드·안내서 취합은 `kb-collector` 가 끝난 뒤 `kb-guide-curator` 서브에이전트(.claude/agents/kb-guide-curator.md)에 맡긴다.
   - 2단계 검증은 반드시 별도의 `kb-fact-checker` 서브에이전트(.claude/agents/kb-fact-checker.md)에 맡긴다. 수집과 검증을 같은 에이전트가 하거나 네가 검증을 생략해서는 안 된다.
   - 3단계 반영은 검증 판정이 '통과' 또는 '수정 후 통과'인 항목만 한다. 보류·기각 항목은 절대 kb/_pending/ 밖으로 옮기지 않는다.
   - 개정이 확인된 문서는 구버전 본문을 통째로 교체하고 kb/CHANGELOG.md 에 한 줄만 남긴다.
3. kb/index.md 가 '미갱신'이면 첫 실행이다. 추적 대상 전부와 위협·동향 90일치를 수집하되, 한 번에 다 못 하면 법령·고시 → ISMS-P → 개인정보위 → 위협·동향 순으로 우선 처리하고 남은 것은 보고서의 '다음 실행 이월'에 적는다. 미완료여도 검증 통과분은 반영하고 커밋한다.
4. 원문에서 확인하지 못한 값은 절대 지어내지 않는다. 의심스러우면 보류한다.
5. 마지막에 kb/reports/TODAY.md 를 쓰고, `git add -A && git commit -m "kb: TODAY 갱신 (통과 n, 보류 n, 기각 n)" && git push origin HEAD:main` 으로 main 에 직접 push 한다. 브랜치나 PR 을 만들지 않는다. push 가 거부되면 `git pull --rebase origin main` 후 다시 push 한다.
6. 끝나면 보고서 요약표(통과/보류/기각 건수, 주요 개정 사항)를 최종 메시지로 남긴다.
```

## 주의

- 루틴 설정에서 저장소 브랜치 push 가 허용되어 있어야 한다. "Claude 브랜치로만 push" 같은 제한이 있으면 main 직접 push 를 허용하도록 바꾸거나, 프롬프트 5번을 PR 생성으로 바꾼다.
