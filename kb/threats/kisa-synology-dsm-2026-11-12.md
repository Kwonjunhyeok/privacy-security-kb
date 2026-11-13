---
title: Synology 제품 보안 업데이트 권고 (DSM 10건, 2026-11-12)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-12
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72300
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72300&menuNo=205020
---

# Synology DSM 보안 업데이트 권고 (2026-11-12)

- 게시: KISA 보호나라 보안공지, 2026-11-12
- 대상: Synology DiskStation Manager(DSM), 취약점 10건
  - SQL Injection: CVE-2026-76954, CVE-2026-81584
  - Authorization Bypass Through User-Controlled Key: CVE-2026-13672
  - Path Traversal: CVE-2026-18792 / Link Following: CVE-2026-19048
  - Missing Critical Step in Authentication: CVE-2026-74857
  - Authentication Bypass Using an Alternate Path or Channel: CVE-2026-85101, CVE-2026-18596
  - Access of Uninitialized Pointer: CVE-2026-18633 / OS Command Injection: CVE-2026-75785

| 제품 | 영향받는 버전 | 해결 버전 | 해당 CVE |
|---|---|---|---|
| DSM 7.2.1 | 7.2.1-69057-13 미만 | 7.2.1-69057-13 이상 | CVE-2026-76954, 85101 |
| DSM 7.2.2 | 7.2.2-72806-10 미만 | 7.2.2-72806-10 이상 | CVE-2026-76954, 85101 |
| DSM 7.3 | 7.3.2-86009-5 미만 | 7.3.2-86009-5 이상 | 10건 전부 |
| DSM 7.4 | 7.4.1-90080-1 미만 | 7.4.1-90080-1 이상 | 10건 전부 |

- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): synology.com/en-global/security/advisory/Synology_SA_26_19, Synology_SA_26_18, NVD
- 관련: 같은 달 「Synology NAS 대상 랜섬웨어 공격 주의 권고」(nttId 72267, 2026-11-03), 72267 공지가 참고자료로 든 이전 「Synology 제품 보안 업데이트 권고」(nttId 72254, 본문은 이번에 대조하지 않음)
