---
title: SAP 제품 보안 업데이트 권고 (2026년 11월, 2026-11-10)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-10
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72295
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72295&menuNo=205020
---

# SAP 11월 보안 업데이트 권고 (2026-11-10)

- 게시: KISA 보호나라 보안공지, 2026-11-10

| CVE | 제품 | 유형 | 영향 버전(요지) | 조치 |
|---|---|---|---|---|
| CVE-2026-120017 | NetWeaver AS ABAP and ABAP Platform (SAML2 Service Provider) | Improper Verification of Cryptographic Signature | SAP_BASIS 702, 731, 740, 750~758, 816, 920, 921, 922 | 보안 패치(SAP Note 3849308) |
| CVE-2026-76964 | NetWeaver AS ABAP (Internet Communication Manager) | Improper Validation of Specified Type of Input | KRNL64UC 7.53, KERNEL 7.53, 7.54, 7.77, 7.93, 9.16, 9.18, 9.20 | 보안 패치(Note 3778530) |
| CVE-2026-89126 | SAP Web Dispatcher | Heap-based Buffer Overflow | HDB 2.00, KRNL64UC 7.53, WEBDISP 7.53/7.54/7.77/7.93/9.16, XS_ADVANCED_RUNTIME 1.00, SAP_EXTENDED_APP_SERVICES 1, KERNEL 7.53/9.18/9.20 | 보안 패치(Note 3778556) |
| CVE-2026-89103 | SAP Gateway | Incorrect Authorization | KRNL64NUC 7.22, 7.22EXT, KRNL64UC 7.22/7.53/8.04, KERNEL 7.22/7.54/7.77/7.93/9.16/9.20/9.21 | 보안 패치(Note 3798345) |

- 권고 조치: SAP가 제공하는 별도 보안 패치 적용
- 참고(공지 인용): support.sap.com security-notes-news/november-2026, me.sap.com notes, NVD
