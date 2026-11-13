---
title: WordPress 플러그인 보안 업데이트 권고 (WPML·LiteSpeed Cache·Elementor·Ninja Forms, 2026-11-12)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-12
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72303
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72303&menuNo=205020
---

# WordPress 플러그인 보안 업데이트 권고 (2026-11-12)

- 게시: KISA 보호나라 보안공지, 2026-11-12

| CVE | 플러그인 | 유형 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|---|
| CVE-2026-76877 | WPML Multilingual CMS | Improper Authentication | 4.9.7 이하 | 5.0.0 이상 |
| CVE-2026-93389 | LiteSpeed Cache | Exposure of Sensitive Information to an Unauthorized Actor | 7.9.1 이하 | 7.9.2 이상 |
| CVE-2026-109883 | Elementor Website Builder | Cross-site Scripting | 4.3.5 이하 | 4.3.6 이상 |
| CVE-2026-126537 | Ninja Forms - File Uploads | Path Traversal | 3.3.36 이하 | 3.3.37 이상 |

- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): Wordfence 위협 정보 4건, NVD
- LiteSpeed Cache 건의 참고 링크[2] 주소에 "woocommerce-store-api-cartcheckout-pii-cart-token" 표기가 있음(공지 본문에는 이 설명 없음, Wordfence 원문은 대조하지 않음)
- 원문 표기 불일치: 공지 개요는 "WPML Multilingual CMS 플러그인"만 언급하나, 설명·영향 표는 플러그인 4종을 다룸. 이 문서는 설명·표 값을 따름
