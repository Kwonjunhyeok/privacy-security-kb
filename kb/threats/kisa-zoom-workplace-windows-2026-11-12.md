---
title: Zoom Workplace for Windows 보안 업데이트 권고 (CVE-2026-108186·108187, 2026-11-12)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-12
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72301&menuNo=205020
status: 현행
verified:
  date: 2026-11-21
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72301&menuNo=205020
---

# Zoom Workplace for Windows 보안 업데이트 권고 (CVE-2026-108186·108187, 2026-11-12)

- 게시: KISA 보호나라 보안공지 「Zoom 제품 보안 업데이트 권고」, 2026-11-12 (nttId=72301)
- 아래 표·값은 공지 본문 그대로 옮김. 제조사 원 권고 링크는 '참고사이트' 참조.


## 개요

- Zoom社는 자사 제품에서 발생하는 취약점을 해결한 보안 업데이트 발표 [1][2]
- 영향을 받는 버전을 사용 중인 사용자는 해결 방안에 따라 최신 버전으로 업데이트 권고

## 설명

- Zoom Workplace for Windows에서 발생하는 Improper Input Validation 취약점(CVE-2026-108186) [1][3]
- Zoom Workplace for Windows에서 발생하는 Origin Validation Error 취약점(CVE-2026-108187) [2][4]

## 영향을 받는 제품 및 해결 방안

| 취약점 | 제품명 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-108186 | Zoom Workplace for Windows | 7.1.0 이상 7.1.8 미만 | 7.1.8 이상 |
| CVE-2026-108187 | Zoom Workplace for Windows | 7.1.5 미만 | 7.1.5 이상 |

※ 하단의 참고 사이트를 확인하여 업데이트 수행 [1][2]

## 참고사이트

- [1] https://www.zoom.com/en/trust/security-bulletin/zsb-26023
- [2] https://www.zoom.com/en/trust/security-bulletin/zsb-26024
- [3] https://nvd.nist.gov/vuln/detail/CVE-2026-108186
- [4] https://nvd.nist.gov/vuln/detail/CVE-2026-108187

## 연관

- ISMS-P 2.10.8 패치관리 — 영향 버전 업데이트(최신 패치 적용) 권고와 직접 대응
- ISMS-P 2.11.2 취약점 점검 및 조치 — 최신 보안취약점 발생 파악·영향 분석·조치 요구와 대응

## 검증 메모

- 2026-11-21 kb-fact-checker: 보호나라 보안공지 목록(pageIndex=2)에서 제목·등록일을 독립 확인하고 원문(nttId 72301)을 직접 열어 대조. 제목·게시일·제품·CVE·영향/해결 버전·참고사이트 일치. 연관 후보 중 「개인정보 보호법 제29조 … (조문 번호 확인필요)」는 조문을 확정하지 못해 삭제.
