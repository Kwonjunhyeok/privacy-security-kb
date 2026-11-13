---
title: Apache 제품 보안 업데이트 권고 (Tomcat·Fineract, 2026-11-03)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-03
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72270
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72270&menuNo=205020
---

# Apache Tomcat·Fineract 보안 업데이트 권고 (2026-11-03)

- 게시: KISA 보호나라 보안공지 「Apache 제품 보안 업데이트 권고」, 2026-11-03
- Apache Fineract: SQL Injection CVE-2026-64618, CVE-2026-65874 — 1.15.0 이하 → 1.16.1 이상
- Apache Tomcat 취약점 6건

| CVE | 유형 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-80353 | TOCTOU Race Condition | 9.0.47 이상 9.0.123 미만 | 9.0.123 이상 |
| CVE-2026-88041 | Incomplete Cleanup | 11.0.0-M23~11.0.27 미만 / 10.1.27~10.1.61 미만 / 9.0.92~9.0.123 미만 | 11.0.27 / 10.1.61 / 9.0.123 이상 |
| CVE-2026-93446 | Incomplete Cleanup | 11.0.0-M21~11.0.27 미만 / 10.1.25~10.1.61 미만 / 9.0.90~9.0.123 미만 | 11.0.27 / 10.1.61 / 9.0.123 이상 |
| CVE-2026-101296 | Missing Critical Step in Authentication | 11.0.0-M1~11.0.27 미만 / 10.1.0-M1~10.1.61 미만 / 9.0.0.M1~9.0.123 미만 | 11.0.27 / 10.1.61 / 9.0.123 이상 |
| CVE-2026-101356 | Race Condition | 11.0.22~11.0.27 미만 / 10.1.55~10.1.61 미만 / 9.0.118~9.0.123 미만 | 11.0.27 / 10.1.61 / 9.0.123 이상 |
| CVE-2026-103119 | Buffer Under-read | 11.0.0-M25 이상 11.0.27 미만 | 11.0.27 이상 |

- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): lists.apache.org 스레드 8건, NVD
