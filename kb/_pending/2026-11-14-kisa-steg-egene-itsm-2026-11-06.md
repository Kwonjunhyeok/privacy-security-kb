---
title: 에스티이지 E-GENE ITSM 보안 조치 권고 (2026-11-06)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-06
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72284&menuNo=205020
status: 현행
verified:
candidate:
  kind: new
  target_path: kb/threats/kisa-steg-egene-itsm-2026-11-06.md
  found_at:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72284&menuNo=205020
  attempts: 0
---

# 에스티이지 E-GENE ITSM 보안 조치 권고 (2026-11-06)

- 게시: KISA 보호나라 보안공지 「에스티이지 제품 보안 조치 권고」, 2026-11-06 (nttId=72284)
- 아래 표·값은 공지 본문 그대로 옮김. 제조사 원 권고 링크는 '참고사이트' 참조.


## 개요

- 에스티이지社는 자사 제품에서 발견된 보안 취약점에 대한 조치 권고
- 해당 제품을 사용 중인 사용자는 제조사 권고에 따라 파일업로드 확장자 제한 등 보안 조치 권고

## 설명

- E-GENE ITSM에서 발생하는 비인가 회원가입 및 부적절한 파일 업로드 취약점
- CVE 번호: 공지 본문에 기재 없음. 해결 버전: 공지에 기재 없음(조치 방안만 제시)

## 영향을 받는 제품 및 조치 방안

| 제조사 | 제품명 | 영향받는 버전 | 조치 방안 |
|---|---|---|---|
| 에스티이지 | E-GENE ITSM | 7.0 이하 | 회원가입 기능 및 파일업로드 확장자 제한 |


## 패치 적용 전 임시 조치 방법

1. 회원가입 기능 제한 설정
- 회원가입 기능을 임시 차단 후 신규 사용자 등록은 수동으로 등록하는 방식으로 대체
2. 파일 업로드 확장자 제한
- 허용할 확장자에 대한 화이트리스트 방식의 검증 적용
※ 그 외 보안 조치는 제조사 안내에 따라 보안패치 적용

## 연관 후보

- ISMS-P 2.10.8 패치관리
- ISMS-P 2.11.2 취약점 점검 및 조치
- 개인정보 보호법 제29조(안전조치의무) — 안전성 확보조치 기준의 보안 업데이트 관련 조항(조문 번호 확인필요)
- ISMS-P 2.5.1 사용자 계정 관리(비인가 회원가입 관련)
