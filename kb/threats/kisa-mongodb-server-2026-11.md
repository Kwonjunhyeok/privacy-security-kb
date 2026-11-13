---
title: MongoDB 제품 보안 업데이트 권고 (MongoDB Server 18건, 2026-11-11)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-11
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72296
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72296&menuNo=205020
---

# MongoDB 제품 보안 업데이트 권고 (2026-11-11)

- 게시: KISA 보호나라 보안공지, 2026-11-11
- 대상: MongoDB Server, 취약점 18건
  - Use After Free: CVE-2026-118383, 120824, 120821, 120818, 120803
  - Incorrect Authorization: CVE-2026-120826, 120822, 120815 / Missing Authorization: CVE-2026-120825
  - Allocation of Resources Without Limits or Throttling: CVE-2026-120828, 120810
  - Race Condition: CVE-2026-120817 / Execution with Unnecessary Privileges: CVE-2026-120814 / Interpretation Conflict: CVE-2026-120813
  - Improper Certificate Validation: CVE-2026-120808 / Improper Check for Unusual or Exceptional Conditions: CVE-2026-120807
  - Incomplete Cleanup: CVE-2026-120806 / Missing Release of Resource after Effective Lifetime: CVE-2026-120804
- 영향·해결 버전(분기별, CVE마다 해당 분기 다름 — 상세는 원문 표)

| 분기 | 영향받는 버전 | 해결 버전 |
|---|---|---|
| 4.4 | 4.4.0 이상 4.4.32 미만 | 4.4.32 이상 |
| 5.0 | 5.0.0 이상 5.0.35 미만 | 5.0.35 이상 |
| 6.0 | 6.0.0 이상 6.0.30 미만 | 6.0.30 이상 |
| 7.0 | 7.0.0 이상 7.0.48 미만 | 7.0.48 이상 |
| 8.0 | 8.0.0 이상 8.0.37 미만 | 8.0.37 이상 |
| 8.3 | 8.3.0 이상 8.3.16 미만 | 8.3.16 이상 |
| 9.0 | 9.0.0 이상 9.0.7 미만 | 9.0.7 이상 |

- CVE별 해당 분기(공지 표 기준, 해결 버전은 위 표의 분기별 값)
  - 4.4·5.0·6.0·7.0·8.0·8.3·9.0 전 분기: CVE-2026-118383, 120828
  - 7.0·8.0·8.3·9.0: CVE-2026-120824, 120822, 120817, 120815, 120813, 120810, 120808, 120807, 120806, 120804
  - 7.0·8.0·8.3: CVE-2026-120818
  - 8.0·8.3·9.0: CVE-2026-120814
  - 8.3·9.0: CVE-2026-120803
  - 9.0 만: CVE-2026-120826, 120825, 120821
- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): mongodb.com/resources/products/alerts, NVD
