---
title: Citrix 제품 보안 업데이트 권고 (2026-11-17)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-17
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72312&menuNo=205020
status: 현행
verified:
  date: 2026-11-22
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72312&menuNo=205020
---

# Citrix 제품 보안 업데이트 권고 (2026-11-17)

- 게시: KISA 보호나라 보안공지 「Citrix 제품 보안 업데이트 권고」, 2026-11-17 (nttId=72312)
- 아래 표·값은 공지 본문 그대로 옮김. 제조사 원 권고 링크는 '참고사이트' 참조.

## 개요

- Citrix社는 자사 제품에서 발생하는 취약점을 해결한 보안 업데이트 발표 [1]~[3]
- 영향을 받는 버전을 사용 중인 사용자는 해결 방안에 따라 최신 버전으로 업데이트 권고

## 설명

- NetScaler ADC, NetScaler Gateway에서 발생하는 Improper Restriction of Operations within the Bounds of a Memory Buffer 취약점(CVE-2026-120868) [1][4]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Improper Restriction of Operations within the Bounds of a Memory Buffer 취약점(CVE-2026-107407) [1][5]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Out-of-bounds Write 취약점(CVE-2026-107408) [1][6]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Double Free 취약점(CVE-2026-107409) [1][7]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Heap-based Buffer Overflow 취약점(CVE-2026-107410) [1][8]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Improper Restriction of Operations within the Bounds of a Memory Buffer 취약점(CVE-2026-107412) [1][9]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Heap-based Buffer Overflow 취약점(CVE-2026-107415) [1][10]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Improper Restriction of Operations within the Bounds of a Memory Buffer 취약점(CVE-2026-120864) [1][11]
- NetScaler Console에서 발생하는 Improper Authentication 취약점(CVE-2026-120869) [2][12]
- NetScaler ADC, NetScaler Gateway에서 발생하는 Improper Restriction of Operations within the Bounds of a Memory Buffer 취약점(CVE-2026-111334) [1][13]
- Secure Access Client for Windows에서 발생하는 Improper Privilege Management 취약점(CVE-2026-118268) [3][14]

## 영향을 받는 제품 및 해결 방안

| 취약점 | 제품명 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-120868 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-120868 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-120868 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-120868 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-120868 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-120868 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-107407 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107407 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107407 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107407 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107407 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-107407 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-107408 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107408 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107408 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107408 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107408 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-107408 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-107409 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107409 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107409 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107409 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107409 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-107409 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-107410 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107410 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107410 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107410 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107410 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-107410 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-107412 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107412 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107412 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107412 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107412 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-107412 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-107415 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107415 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107415 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-107415 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-107415 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-107415 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-120864 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-120864 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-120864 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-120864 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-120864 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-120864 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-120869 | NetScaler Console | 14.1-74.34 미만 | 14.1-74.34 이상 |
| CVE-2026-111334 | NetScaler ADC | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-111334 | NetScaler ADC | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-111334 | NetScaler Gateway | 14.1-73.57 미만 | 14.1-73.57 이상 |
| CVE-2026-111334 | NetScaler Gateway | 13.1-64.39 미만 | 13.1-64.39 이상 |
| CVE-2026-111334 | NetScaler ADC (FIPS) | 14.1-73.58(FIPS) 미만 | 14.1-73.58(FIPS) 이상 |
| CVE-2026-111334 | NetScaler ADC (FIPS/NDcPP) | 13.1-37.293(FIPS/NDcPP) 미만 | 13.1-37.293(FIPS/NDcPP) 이상 |
| CVE-2026-118268 | Secure Access Client (Windows) | 26.11.1.6 미만 | 26.11.1.6 이상 |

※ 하단의 참고 사이트를 확인하여 업데이트 수행 [1]~[3]

## 참고사이트

- [1] https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697305
- [2] https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697320
- [3] https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697280
- [4] https://nvd.nist.gov/vuln/detail/CVE-2026-120868
- [5] https://nvd.nist.gov/vuln/detail/CVE-2026-107407
- [6] https://nvd.nist.gov/vuln/detail/CVE-2026-107408
- [7] https://nvd.nist.gov/vuln/detail/CVE-2026-107409
- [8] https://nvd.nist.gov/vuln/detail/CVE-2026-107410
- [9] https://nvd.nist.gov/vuln/detail/CVE-2026-107412
- [10] https://nvd.nist.gov/vuln/detail/CVE-2026-107415
- [11] https://nvd.nist.gov/vuln/detail/CVE-2026-120864
- [12] https://nvd.nist.gov/vuln/detail/CVE-2026-120869
- [13] https://nvd.nist.gov/vuln/detail/CVE-2026-111334
- [14] https://nvd.nist.gov/vuln/detail/CVE-2026-118268

## 연관

- ISMS-P 2.10.8 패치관리
- ISMS-P 2.11.2 취약점 점검 및 조치

## 검증 기록

- 2026-11-22 kb-fact-checker: KISA 보호나라 원문(nttId=72312)을 브라우저로 재방문해 제목·게시일(2026-11-17)·개요·CVE 11건·제품명(NetScaler ADC/Gateway/Console, Secure Access Client 등)·영향받는 버전·해결 버전 표·참고사이트 링크를 전수 대조. 모든 값 일치, 수정 없음. 판정: 통과.
  - 대조 URL: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72312&menuNo=205020
  - 연관 ISMS-P 항목(2.10.8, 2.11.2)은 kb/isms-p/2-protection-measures.md 에 동일 제목으로 존재함을 확인.
