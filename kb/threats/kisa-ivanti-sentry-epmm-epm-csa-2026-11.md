---
title: Ivanti 제품 보안 업데이트 권고 (Sentry·EPMM·EPM·CSA, 2026-11-11)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-11
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72297
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72297&menuNo=205020
---

# Ivanti 제품 보안 업데이트 권고 (2026-11-11)

- 게시: KISA 보호나라 보안공지, 2026-11-11
- 취약점
  - CVE-2026-105425: Ivanti Sentry, Endpoint Manager Mobile(EPMM) OS Command Injection
  - CVE-2026-121653: Endpoint Manager(EPM) SQL Injection
  - CVE-2026-121683: Cloud Services Application(CSA) Missing Authentication for Critical Function

| CVE | 제품 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-105425 | Sentry | 10.7.4 미만 | 10.7.4 이상 또는 11.0.0 |
| CVE-2026-105425 | Sentry | 10.8.0 이상 10.8.3 미만 | 10.8.3 이상 또는 11.0.0 |
| CVE-2026-105425 | EPMM | 12.9.0.3 미만 | 12.9.0.3 이상 또는 12.11.0.0 |
| CVE-2026-105425 | EPMM | 12.10.0.0 | 12.10.0.1 이상 또는 12.11.0.0 |
| CVE-2026-121653 | EPM | 2024 SU8 미만 | 2024 SU8 이상 |
| CVE-2026-121683 | CSA | 5.0.8 | 5.0.8.1 이상 |

- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): hub.ivanti.com 보안 권고 4건(Sentry, EPMM November-2026, EPM November-2026, CSA), NVD
- 같은 달 Ivanti Connect Secure 공지(nttId 72263, 2026-11-02)는 별도 초안
