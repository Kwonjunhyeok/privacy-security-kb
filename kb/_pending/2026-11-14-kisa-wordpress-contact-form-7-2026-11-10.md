---
title: WordPress Contact Form 7 플러그인 보안 업데이트 권고 (CVE-2026-114432, 2026-11-10)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-10
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72293&menuNo=205020
status: 현행
verified:
candidate:
  kind: new
  target_path: kb/threats/kisa-wordpress-contact-form-7-2026-11-10.md
  found_at:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72293&menuNo=205020
  attempts: 0
---

# WordPress Contact Form 7 플러그인 보안 업데이트 권고 (CVE-2026-114432, 2026-11-10)

- 게시: KISA 보호나라 보안공지 「WordPress 플러그인 보안 업데이트 권고」, 2026-11-10 (nttId=72293)
- 아래 표·값은 공지 본문 그대로 옮김. 제조사 원 권고 링크는 '참고사이트' 참조.


## 개요

- WordPress의 Contact Form 7 플러그인 취약점을 해결한 보안 업데이트 발표 [1]
- 영향을 받는 버전을 사용 중인 사용자는 해결 방안에 따라 최신 버전으로 업데이트 권고

## 설명

- Contact Form 7에서 발생하는 Unrestricted Upload of File with Dangerous Type 취약점(CVE-2026-114432) [1][2]

## 영향을 받는 제품 및 해결 방안

| 취약점 | 제품명 | 영향받는 버전 | 해결 버전 |
|---|---|---|---|
| CVE-2026-114432 | Contact Form 7 | 6.2.0 이상 6.2.4 미만 | 6.2.4 이상 |

※ 하단의 참고 사이트를 확인하여 업데이트 수행 [1]

## 참고사이트

- [1] https://wpscan.com/vulnerability/6b0a5d1f-84fb-425f-8d37-ddde5703937c/
- [2] https://nvd.nist.gov/vuln/detail/CVE-2026-114432

## 연관 후보

- ISMS-P 2.10.8 패치관리
- ISMS-P 2.11.2 취약점 점검 및 조치
- 개인정보 보호법 제29조(안전조치의무) — 안전성 확보조치 기준의 보안 업데이트 관련 조항(조문 번호 확인필요)
