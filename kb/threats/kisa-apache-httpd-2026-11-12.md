---
title: Apache HTTP Server 보안 업데이트 권고 (2026-11-12)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-12
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72304
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72304&menuNo=205020
---

# Apache HTTP Server 보안 업데이트 권고 (2026-11-12)

- 게시: KISA 보호나라 보안공지 「Apache 제품 보안 업데이트 권고」, 2026-11-12

| CVE | 유형 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-119618 | Race Condition | 2.4.55 이상 2.4.71 미만 | 2.4.71 이상 |
| CVE-2026-106023 | NULL Pointer Dereference | 2.4.30 이상 2.4.71 미만 | 2.4.71 이상 |
| CVE-2026-109163 | Stack-based Buffer Overflow | 2.4.69 이상 2.4.71 미만 | 2.4.71 이상 |

- 권고 조치: 2.4.71 이상으로 업데이트
- 참고(공지 인용): httpd.apache.org/security/vulnerabilities_24.html, NVD
