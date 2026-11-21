---
title: Apache Juneau 보안 업데이트 권고 (CVE-2026-96677·73100, 2026-11-06)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-06
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72286&menuNo=205020
status: 현행
verified:
  date: 2026-11-21
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72286&menuNo=205020
---

# Apache Juneau 보안 업데이트 권고 (CVE-2026-96677·73100, 2026-11-06)

- 게시: KISA 보호나라 보안공지 「Apache 제품 보안 업데이트 권고」, 2026-11-06 (nttId=72286)
- 아래 표·값은 공지 본문 그대로 옮김. 제조사 원 권고 링크는 '참고사이트' 참조.


## 개요

- Apache 재단은 자사 제품에서 발생하는 취약점을 해결한 보안 업데이트 발표 [1]
- 영향을 받는 버전을 사용 중인 사용자는 해결 방안에 따라 최신 버전으로 업데이트 권고

## 설명

- Apache Juneau에서 발생하는 Cross-site Scripting (XSS) 취약점(CVE-2026-96677) [1][2]
- Apache Juneau에서 발생하는 Insertion of Sensitive Information into Log File 취약점(CVE-2026-73100) [1][3]

## 영향을 받는 제품 및 해결 방안

| 취약점 | 제품명 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-96677 | Apache Juneau | 9.2.1 미만 | 9.2.1 이상 |
| CVE-2026-73100 | Apache Juneau | 9.2.1 미만 | 9.2.1 이상 |

※ 하단의 참고 사이트를 확인하여 업데이트 수행 [1]

## 참고사이트

- [1] https://lists.apache.org/thread/j05q7vw08j48o96tdlzcsd4sozx1lyl6
- [2] https://nvd.nist.gov/vuln/detail/CVE-2026-96677
- [3] https://nvd.nist.gov/vuln/detail/CVE-2026-73100

## 연관

- ISMS-P 2.10.8 패치관리 — 영향 버전 업데이트(최신 패치 적용) 권고와 직접 대응
- ISMS-P 2.11.2 취약점 점검 및 조치 — 최신 보안취약점 발생 파악·영향 분석·조치 요구와 대응

## 검증 메모

- 2026-11-21 kb-fact-checker: 보호나라 보안공지 목록(pageIndex=4)에서 제목·등록일을 독립 확인하고 원문(nttId 72286)을 직접 열어 대조. 제목·게시일·제품·CVE·영향/해결 버전·참고사이트 일치. 연관 후보 중 「개인정보 보호법 제29조 … (조문 번호 확인필요)」는 조문을 확정하지 못해 삭제.
