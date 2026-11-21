---
title: Node.js 제품 보안 업데이트 권고
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-10-23
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72236&menuNo=205020
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72236&menuNo=205020
---

# Node.js 제품 보안 업데이트 권고 (2026-10-23, nttId 72236)

- 개요: OpenJS 재단이 Node.js 취약점을 해결한 보안 업데이트 발표. 영향 버전 사용자는 최신 버전으로 업데이트 권고.
- 취약점:
  - CVE-2026-105482 — Improper Access Control
  - CVE-2026-105483 — Improper Certificate Validation
  - CVE-2026-106069 — Improper Certificate Validation
- CVSS: 공지에 미표기

## 영향 버전 및 해결 버전

| CVE | 영향받는 버전 | 해결 버전 |
|---|---|---|
| CVE-2026-105482 | 22.23.4 미만 / 24.22.1 미만 / 26.12.1 미만 | 22.23.4 / 24.22.1 / 26.12.1 이상 |
| CVE-2026-105483 | 24.22.1 미만 / 26.12.1 미만 | 24.22.1 / 26.12.1 이상 (22.x 행 없음) |
| CVE-2026-106069 | 22.23.4 미만 / 24.22.1 미만 / 26.12.1 미만 | 22.23.4 / 24.22.1 / 26.12.1 이상 |

- 참고: nodejs.org/en/blog/vulnerability/october-2026-security-releases, NVD 각 CVE
- 작성: 디지털위협대응본부 취약점관리센터 / 문의 118

## 연관

- ISMS-P 2.10.8 패치관리 — 영향 버전 업데이트 권고와 직접 대응

## 검증 메모

- 2026-11-13 kb-fact-checker: 보호나라 원문 72236 직접 열람. 게시일 확인필요 → 2026-10-23, 취약점 유형 2종 일치, CVE 3건·영향/해결 버전을 원문 표로 채움. 연관 후보 중 "2.8.6 운영환경 이관"은 원문 근거가 없어 삭제.
