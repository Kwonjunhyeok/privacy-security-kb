---
title: SonicWall SonicOS 보안 업데이트 권고 (2026-11-09, 2026-11-10)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-10
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72292
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72292&menuNo=205020
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72290&menuNo=205020
---

# SonicWall SonicOS 보안 업데이트 권고 (2026-11-09, 2026-11-10)

보호나라에 같은 제목 「SonicWall 제품 보안 업데이트 권고」 공지가 두 건 연달아 게시됨. 두 공지 모두 같은 SonicWall 권고(SNWLID-2026-0014)를 참고로 들고 영향·해결 버전이 같아 한 문서로 묶음(검증 시 두 공지 모두 원문 대조).

- nttId 72290 (2026-11-09): CVE-2026-19868, SonicOS Use of Single-factor Authentication
- nttId 72292 (2026-11-10): CVE-2026-82308 Heap-based Buffer Overflow, CVE-2026-107154 Reliance on IP Address for Authentication, CVE-2026-107155 Permissive Cross-domain Security Policy with Untrusted Domains

| 제품 | 영향받는 버전 | 해결 버전 |
|---|---|---|
| SonicOS (Gen7) | 7.3.3-7015 이하 | 7.3.4-7013 이상 |
| SonicOS (Gen8) | 8.2.2-8015 이하 | 8.2.3-8015 이상 |

(위 4개 CVE 모두 같은 버전 범위)
- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014, NVD