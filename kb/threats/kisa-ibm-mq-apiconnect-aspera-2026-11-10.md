---
title: IBM 제품 보안 업데이트 권고 (MQ·API Connect·Aspera Faspex, 2026-11-10)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-10
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72294
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72294&menuNo=205020
---

# IBM 제품 보안 업데이트 권고 (2026-11-10)

- 게시: KISA 보호나라 보안공지, 2026-11-10
- 취약점
  - CVE-2026-11724: IBM MQ Improper Input Validation
  - CVE-2026-17399: API Connect Unrestricted Upload of File with Dangerous Type
  - CVE-2026-16720: API Connect Improper Authentication
  - CVE-2026-123218: Aspera Faspex Incorrect Authorization

| CVE | 제품 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-11724 | MQ | 9.2.0.0~9.2.0.44 LTS | 9.2.0.46 이상 |
| CVE-2026-11724 | MQ | 9.3.0.0~9.3.0.42 LTS | 9.3.0.43 이상 |
| CVE-2026-11724 | MQ | 9.4.0.0~9.4.0.26 LTS | 9.4.0.30 이상 |
| CVE-2026-11724 | MQ | 9.4.0.0~9.4.5.1 CD | 10.0.1.0 이상 |
| CVE-2026-11724 | MQ | 10.0.0.0~10.0.0.5 LTS | 10.0.0.6 이상 |
| CVE-2026-11724 | MQ | 10.0.0.0~10.0.0.5 CD | 10.0.1.0 이상 |
| CVE-2026-17399, CVE-2026-16720 | API Connect | 10.0.8.0~10.0.8.12 | 10.0.8.13 이상 |
| CVE-2026-17399, CVE-2026-16720 | API Connect | 12.1.0.0~12.1.1.2 | 12.1.1.3 이상 |
| CVE-2026-123218 | Aspera Faspex | 5.0.0~5.0.19 | 5.0.19 PL1 이상 |

(범위는 원문 표의 "이상 ~ 이하" 그대로)
- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): ibm.com/support/pages/node 7294503, 7295637, 7295635, 7295921, NVD
