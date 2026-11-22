---
title: 국가사이버안보센터 지침·가이드 현행 목록
category: guides
doc_type: 가이드라인
issuer: 국가정보원 국가사이버안보센터
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-16   # 지침·가이드 게시판 최신 등록일 (2026-11-22 1~3쪽 재확인)
topics: [S09]
source_url: https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNsYfHBDSvLeAA55UtgT6j6-A
status: 현행
verified:
candidate:
  kind: revision
  replaces: kb/guides/ncsc-guides-current-list.md
  target_path: kb/guides/ncsc-guides-current-list.md
  found_at:
    - https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNsYfHBDSvLeAA55UtgT6j6-A   # 지침·가이드 목록 1~3쪽 (2026-11-22 Playwright, "총 26건의 게시물이 있습니다")
    - https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvJbI7a2mJqCMzoRfcssNBUj2tasxcpMwHpcsY6E5VIDw   # 신규 1번 「국가ㆍ공공기관 대민 웹사이트 설치형 보안SW 최소화 가이드」 (2026-11-16)
    - https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvPJyCCf3pbZp847WeNf63vZx3QaMO9fIZ48zJc-4sMcL   # 신규 2번 「국가ㆍ공공기관 암호 안전성 기준(Draft)(2026.11)」
    - https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvKO74QXTXworRMvwAlG8B3nQQCNFMa6tCsMZfwWhsfTb   # 신규 3번 「국가ㆍ공공기관 양자내성암호 전환 가이드북」(Draft)(2026.11)」
    - https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvNweQY_U_riHeJG4MbYAX_3cYu0dKvbkFyAgc_uNHfeX   # 11번(舊 8번) 「국가ㆍ공공기관 AI보안 가이드북」 게시물
    - https://www.ncsc.go.kr/api/usr/bbs/downloadFile   # 11번 첨부(downloadFileId=53abf493-6fe3-484f-9da1-038247d7098a), sha256 d4ed2902…df9f = 게시 해시. 원문 3쪽 "문서이력"
    - https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvNW9wnrsXcREF_zixwc3sj_du7Fw_EQfsAy0Fhg_EjyI   # 19번(舊 16번) 「챗GPT 등 생성형 AI 활용 보안 가이드라인(2023.6)」
  attempts: 1
---

# 국가사이버안보센터 지침·가이드 현행 목록 (수정 초안, 전체 재수집)

## 게시 정보

- 출처: 국가정보원 국가사이버안보센터 누리집 전체메뉴 > 자료실 > 지침·가이드. 2026-11-22 Playwright(`scripts/browser/`)로 "전체" 탭 1~3쪽을 쪽 번호 클릭 방식으로 전수 재수집했다(쪽 1: 1~10번, 쪽 2: 11~20번, 쪽 3: 21~26번). 게시판 표기 "총 26건의 게시물이 있습니다. (1/3페이지)".
- 2026-11-21 보고서가 전한 대로 2026.11.16 등록 신규 게시물 3건이 있고, 기존 23건의 번호가 모두 3씩 밀렸다(기존 n번 → n+3번). 번호·구분·제목·등록일을 새로 확인한 결과 n+3 대응이 23건 전부 맞았다.
- 신규 3건(모두 2026.11.16 등록, "가이드")을 게시물 본문까지 열어 확인:
  1. 「국가ㆍ공공기관 대민 웹사이트 설치형 보안SW 최소화 가이드」 — 본문: "국가정보원은 정부 정보보호 종합대책의 일환으로 관계기관 합동, 공공 웹사이트에서 배포하는 설치형 보안SW의 무설치 전환을 목표로 개선을 추진중"이며 "클라우드 공동인증서 전환, 보안SW 개발 시 고려 사항 등"을 담은 가이드라고 적혀 있다. 첨부 1건(설치형_보안SW_최소화_가이드.pdf, sha256 dc8871a5…98f 게시).
  2. 「국가ㆍ공공기관 암호 안전성 기준(Draft)(2026.11)」 — 본문: "「국가ㆍ공공기관 암호 안전성 기준」(Draft)을 배포하오니 업무에 참고하시기 바랍니다." 제목·본문 모두 "(Draft)" 표기. 첨부 1건(sha256 61253120…fa25 게시). 의견수렴·입법예고 절차인지는 본문에 적혀 있지 않아 확인필요.
  3. 「국가ㆍ공공기관 양자내성암호 전환 가이드북」(Draft)(2026.11)」 — 본문: "「국가ㆍ공공기관 양자내성암호 전환 가이드북」(Draft)을 배포하오니 업무에 참고하시기 바랍니다." (괄호 짝 안 맞음은 게시판 표기 그대로). 첨부 1건(sha256 b61db535…d358 게시). 마찬가지로 의견수렴 여부 확인필요.
  - 두 Draft 건은 "배포하오니 참고" 문구만 있고 입법예고·행정예고 절차 표시는 본문에 없다. 판단하지 않고 제목의 "(Draft)" 표기와 확인필요만 남긴다.
- 메뉴 위치: "발간자료" 메뉴(자료실 > 발간자료, 국가정보보호백서)는 별도 게시판이다(기존 목록 문서 "발간자료(참고)" 절 참고, 이번에 다시 열지 않음).
- 쪽 넘김: URL 인자가 없다. `.paging` 쪽 번호 클릭 방식(자바스크립트).
- 번호 열은 최신 글이 1번(게시판 표기 그대로).
- 담당 부서: 목록·게시물에 담당 부서 칸이 없다(확인필요, 기존과 동일).
- 현행 표시: "舊 국가 정보보안 기본지침" 한 건에만 기관 표시(舊)가 있다. 나머지는 기관 표시 없음(A 기준).
- 분류 코드는 `kb/topics.md` 기준. 「병원정보시스템 보안가이드라인(2025.4)」은 맞는 코드가 없어 `미분류`(기존과 동일).
- 신규 3건 분류: 1번은 공공 웹사이트 설치형 보안SW·웹 보안이라 S09(국가·공공 망 보안), S03(기술적 보안: 웹 보안)로 달았다. 2·3번은 암호 관련 국가·공공기관 대상 자료라 기존 암호모듈류(S09, S03)와 같은 코드로 달았다. 확정이 아니라 후보다.
- 이번에 새로 원문을 연 자료: 위 신규 3건(목록 수준 확인, 장별 요지 요약 초안은 만들지 않음). 기존에 요약 초안이 있는 자료는 그대로 둔다: 「국가 망 보안체계(N2SF) 보안가이드라인 1.0」(kb/_pending/2026-11-15-guides-n2sf-security-guideline.md), 「국가 망 보안체계(N2SF) 이해 및 활용 안내」(kb/_pending/2026-11-15-guides-n2sf-overview.md), 「국가ㆍ공공기관 AI보안 가이드북」(kb/_pending/2026-11-15-guides-public-ai-security-guidebook.md).

## 변경 요지 (기존 kb/guides/ncsc-guides-current-list.md 대비)

- 신규 행 3건 추가(1~3번, 2026.11.16).
- 기존 23건의 번호가 모두 +3(예: 1→4, 8→11, 9→12, 16→19).
- 「이전 판 제외」에 다섯 번째 쌍 추가: 챗GPT 등 생성형 AI 활용 보안 가이드라인(2023.6) (舊 16번, 신 19번, 2023-06-29) → 국가ㆍ공공기관 AI보안 가이드북 (舊 8번, 신 11번, 2025.12.10). 근거: AI보안 가이드북 첨부 원문 3쪽 "문서이력" 표에 "2023.06. / 1.0 / 챗GPT 등 생성형 AI 활용 보안 가이드라인", "2025.12. / 2.0 / 국가·공공기관 AI보안 가이드북"이 적혀 있다(2026-11-15 수집 시 확인, 이번에 다시 열지 않음).
- published_date 를 2026-08-01 → 2026-11-16(최신 등록일)로 바꾼다.
- kb 에 16번(2023.6, 신 19번) 자료의 개별 문서는 없어 repeal 초안은 만들지 않는다(기존 판단 유지).

## 지침·가이드 게시 중 (이전 판 제외 후 21건)

| 분류 | 자료명 (게시판 제목 그대로) | 번호 | 구분 | 등록일 | 비고 |
|---|---|---|---|---|---|
| S09, S03 | 국가ㆍ공공기관 대민 웹사이트 설치형 보안SW 최소화 가이드 | 1 | 가이드 | 2026-11-16 | 신규. 첨부 「설치형_보안SW_최소화_가이드.pdf」, sha256 dc8871a5…98f 게시. 원문 미확인(목록 수준만 확인) |
| S09, S03 | 국가ㆍ공공기관 암호 안전성 기준(Draft)(2026.11) | 2 | 가이드 | 2026-11-16 | 신규. 제목·본문 "(Draft)". 첨부 sha256 61253120…fa25 게시. 의견수렴 절차 여부 확인필요. 원문 미확인 |
| S09, S03 | 국가ㆍ공공기관 양자내성암호 전환 가이드북」(Draft)(2026.11) | 3 | 가이드 | 2026-11-16 | 신규(「 없는 」 는 게시판 표기 그대로). 첨부 sha256 b61db535…d358 게시. 의견수렴 절차 여부 확인필요. 원문 미확인 |
| S04, S09 | [국가·공공기관 민간클라우드 컴퓨팅서비스 도입 가능 목록(2026.9.30)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvBL0bbZO5HiVN9vMjIKidIGinjESc-bO9B3A3DTpW0SM) | 4 | 기타 공시 | 2026-08-01 | 첨부 「20260930_국가공공기관_민간클라우드_컴퓨팅서비스_도입_가능목록(20260930_기준).pdf」. 제목 기준일(2026.9.30)이 작성일(2026.08.01)보다 늦음 → 게시판 표기 그대로 |
| S09 | [국가 사이버보안 기본지침(5.1부 개정) 안내](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvMBQ9yji1O0uKiPsS2aFQM07mQ5u7yGVw572DcM-zepU) | 5 | 지침 | 2026-07-20 | 게시물: "2026년 5월 1일부로 국가 사이버보안 기본지침(舊 국가 정보보안 기본지침)을 개정". 첨부 「국가사이버보안기본지침.pdf」 1건. 원문 미확인 |
| S04, X01 | [SW 공급망 보안 강화 로드맵](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvMmE7Jz3x_Huja3jsX_79Kjr-BFqUyc8mzWR7QUAp0D-) | 6 | 기타 공시 | 2026-07-03 | 게시물: "관계부처 합동으로 발간". 첨부 「SW 공급망 보안 강화 로드맵(2026년 6월).pdf」. KISA 지식플랫폼 「SW 공급망 보안 강화 로드맵 발표(2026.06.)」(가이드라인 72번)과 같은 자료인지 확인필요 |
| S09 | [국가 망 보안체계(N2SF) 이해 및 활용 안내](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvNj_uU6OMakPcrAhgWAjJq6eEvT3SmMyxg5hgnvZ2g1h) | 7 | 기타 공시 | 2026-03-24 | N2SF 설명자료(13쪽). 원문 열람 |
| S08 | [지능형 전력망 사이버보안 가이드라인(2026.03)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvLVRScxAP7e6jeBCRF3hXUiVuzOi3FNpsh9hOhVTcmLY) | 9 | 가이드 | 2026-03-11 |  |
| S09 | [2026년도 사이버보안 실태 평가지표](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvH4D27_lndraxOrzvh9YmIvJ_eJWtU2132BbQuPrDilQ) | 10 | 기타 공시 | 2025-12-11 |  |
| S08, S09 | [국가ㆍ공공기관 AI보안 가이드북](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvNweQY_U_riHeJG4MbYAX_3cYu0dKvbkFyAgc_uNHfeX) | 11 | 가이드 | 2025-12-10 | 원문 문서이력: 「챗GPT 등 생성형 AI 활용 보안 가이드라인」 1.0(2023.06.)의 2.0. 요약 초안 kb/_pending/2026-11-15-guides-public-ai-security-guidebook.md |
| S09 | [국가 망 보안체계(N2SF) 보안가이드라인 1.0](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvKlgmp4pbcUcyETJn6NrHSIACCUP_xvUj35ZGb7sJqI4) | 12 | 가이드 | 2025-09-30 | 게시물: "기존 Draft 버전을 보완·개정한 … 1.0". 본문·부록1·부록2(zip) 3건. 요약 초안 kb/_pending/2026-11-15-guides-n2sf-security-guideline.md |
| S08 | [우주시스템 사이버보안 가이드라인 V1.0(국 · 영문)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvJodhzvS2M9TedPmloAFoAGnOsd3tNQK4iCJQgCDFDFg) | 13 | 가이드 | 2025-09-09 |  |
| S02, S03 | [관제기술 플랫폼(SIEM/SOAR) 구축 가이드라인(25.5)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvFzM5mNyA454egeZn0YzoQBB8MIAM0m9PkW_2a_CDWnT) | 14 | 가이드 | 2025-06-20 |  |
| S09, S03 | [암호모듈 시험 및 검증지침(2025.6.1부)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvKcQbyRHaulf1awVnDFAlNbWO8NgMZZSCNgNXo13u9W6) | 15 | 지침 | 2025-05-30 | 첨부 HWP 1건(원문 미확인) |
| 미분류 | [병원정보시스템 보안가이드라인(2025.4)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvD10NTv7jzfU2GzEhHBs5LhAkv8lbZbtgr73szxJRfUc) | 16 | 가이드 | 2025-04-03 | 분류: 보건의료 분야 정보보호에 맞는 S 코드 없음 |
| S04 | [SW 공급망 보안 가이드라인(v1.0)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvI6DXWnxR4wxUsEwN57ThTn8uHzPDjaAHwhGzHILF1Ys) | 18 | 가이드 | 2024-05-13 | 게시물: 국가정보원·과학기술정보통신부·디지털플랫폼정부위원회 합동, 전체본·요약본 2건. KISA 지식플랫폼 「SW 공급망 보안 가이드라인 1.0 (전체본, 요약본)」(2024-05-13)과 같은 날짜. 같은 자료인지 확인필요 |
| S04, S09 | [국가 클라우드 컴퓨팅 보안 가이드라인(2023.01)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvMbrfd5kR0-lqj8TEr3qHESwn6A1voTj_GLzwyg5SD5x) | 22 | 가이드 | 2023-01-31 |  |
| S09, S03 | [암호모듈 제출물 작성 안내서(2022.08)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvJVn8qmhKw0MIdR-IY6gitS0ohKoKn-a1agz9phCyLZ2) | 23 | 가이드 | 2022-08-31 |  |
| S09, S03 | [암호모듈 구현안내서(2022.05)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvFk5qS1IdH68aiOpm7wk10OJn70SThFi9Yoqi5fWjdn4) | 24 | 가이드 | 2022-05-17 |  |
| S09, S03 | [검증필 암호모듈 운용가이드(2022.03)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvH1jhV4M1OeWCIjtLzlWfrwRD7f76wcgOyzdOlP6mc1C) | 25 | 가이드 | 2022-03-25 |  |
| S03, S09 | [국가ㆍ공공기관 도입을 위한 블록체인 암호기술 가이드라인(20.12)](https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvJFDIeiLbKBRCExqbnRsQrVylvf-KY7TVFMyWcr3saQP) | 26 | 가이드 | 2020-12-30 |  |

## 이전 판 제외

- 국가·공공기관 민간클라우드 컴퓨팅서비스 도입 가능 목록(2026.6.23) (8번, 기타 공시, 2026-03-12) → 국가·공공기관 민간클라우드 컴퓨팅서비스 도입 가능 목록(2026.9.30) (4번, 2026.08.01). 사유: 같은 목록의 더 늦은 기준일 판이 같은 게시판에 있음
- 국가 망 보안체계 보안 가이드라인(Draft) (17번, 가이드, 2025-01-23) → 국가 망 보안체계(N2SF) 보안가이드라인 1.0 (12번, 2025.09.30). 사유: 1.0 게시물 본문 "기존 Draft 버전을 보완·개정", 1.0 원문 문서이력(2025.1. Draft → 2025.9. 1.0)
- 챗GPT 등 생성형 AI 활용 보안 가이드라인(2023.6) (19번, 가이드, 2023-06-29) → 국가ㆍ공공기관 AI보안 가이드북 (11번, 2025.12.10). 사유: AI보안 가이드북 첨부 원문 3쪽 "문서이력" 표에 "2023.06. / 1.0 / 챗GPT 등 생성형 AI 활용 보안 가이드라인", "2025.12. / 2.0 / 국가·공공기관 AI보안 가이드북"이 적혀 있음(2026-11-15 수집 확인)
- 암호모듈 시험 및 검증지침(2023.3.9부) (20번, 지침, 2023-03-09) → 암호모듈 시험 및 검증지침(2025.6.1부) (15번, 2025.05.30). 사유: 같은 지침의 더 늦은 시행 기준일 판이 같은 게시판에 있음
- 舊 국가 정보보안 기본지침 (21번, 지침, 2023-01-31) → 국가 사이버보안 기본지침(5.1부 개정) 안내 (5번, 2026.07.20). 사유: 기관 표시 "舊". 게시물 본문 "2026년 5월 1일부 개정된 '국가 사이버보안 기본지침' 관련하여 '국가 정보보안 기본지침' 과거버전 파일을 첨부". 첨부 4건(23.1.31, 21.11.1, 20.7.1, 19.3.22판 PDF)

## 발간자료(참고): 국가정보보호백서

- 이번 재수집에서 다시 열지 않았다. 기존 kb/guides/ncsc-guides-current-list.md 의 "발간자료(참고)" 절 그대로 둔다.

## 연관 후보

- kb/_pending/2026-11-15-guides-public-ai-security-guidebook.md
- kb/_pending/2026-11-15-guides-n2sf-overview.md
- kb/_pending/2026-11-15-guides-n2sf-security-guideline.md
- kb/guides/n2sf-security-guideline.md
