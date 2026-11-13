---
title: KISA 국내 SW 취약점 공지 — 일부 SW 제품 사용 주의(2026-08-19), 보안인증 SW 클리닝 서비스(INNORIX Agent, 2026-10-06)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-10-06
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72210
status: 현행
fact_check: 수정 후 통과
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72210&menuNo=205020
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72161&menuNo=205020
---

# 국내 SW 취약점 공지

## 「보안인증 소프트웨어 취약점 관련 클리닝 서비스 가동 안내」 (2026-10-06, nttId 72210)

- 대상: INNORIX Agent 1.1.1.001 이상 1.3.5.576 이하 — 로컬 권한 상승 취약점
- 클리닝 서비스: nProtect Online Security, VirusChaser, 엑소스피어, 터보백신 4종이 취약 구버전 자동 탐지, 이용자 동의 시 조치
- 이용자 조치: 해당 S/W 운용 기관 담당자·이용자는 소프트웨어 삭제 권고. 문의 INNORIX 02-557-2757
- 이전 같은 제목 공지: 2026-07-27 (nttId 72141, SGA솔루션즈 TrustPKI 대상, 90일 범위 밖이라 미수록)

## 「일부 SW 제품 사용 주의 권고」 (2026-08-19, nttId 72161)

| 제조사 | 제품 | 버전 |
|---|---|---|
| 펫누리 | F10 | "-" |
| 서진네트웍스 | TCAM-S30 | 24.09.25 |

- 취약점 상세·CVE 는 공지에 미표기. 제조사 보완 프로그램 배포·적용 시까지 사용 자제, 부득이하면 외부망(인터넷)이 차단된 폐쇄망에서 사용.
- 문의: 펫누리 070-8027-8220, 서진네트웍스 1588-2713

## 연관

- ISMS-P 2.10.8 패치관리 — 취약 버전 삭제·보완 프로그램 적용 권고와 직접 대응

## 검증 메모

- 2026-11-13 kb-fact-checker: 보호나라 원문 72210·72161·72141 직접 열람. "취약점 상세·CVE 미공개" → 원문에는 '미공개' 표현이 없어 "공지에 미표기"로 수정, "제거 권고" → 원문 "소프트웨어 삭제 권고", 72141 "대상 제품 미확인" → "SGA솔루션즈 TrustPKI". 72161 게시일 2026-08-19 는 90일 기준일(2026-08-15) 이후라 범위 안. 연관 후보 1.2.1 정보자산 식별은 원문 근거가 약해 삭제.
