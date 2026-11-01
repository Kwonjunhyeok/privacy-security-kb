---
title: PHP 신규 취약점(CVE-2026-115560) 임시 조치 권고
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 확인필요   # 검색 요약상 2026-10-24
source_url: 확인필요
status: 현행
verified:
candidate:
  kind: new
  target_path: kb/threats/2026-10-php-cve-2026-115560-temporary-measures.md
  found_at:
    - https://www.boho.or.kr/kr/bbs/list.do?menuNo=205020&bbsId=B0000133
  attempts: 2
---

> 수집 메모: 웹 검색 요약에 보호나라 보안공지(게시판 번호 2581로 표기)로 PHP 신규 취약점 CVE-2026-115560 임시 조치 권고가 2026-10-24 게시되었다고 나왔다. 상세 URL(nttId)을 찾지 못했고 boho.or.kr 은 DNS 차단. 제목·CVE·게시일 모두 원문 대조 필요.

## 요지

- 대상: PHP (영향 버전 확인필요)
- 취약점: CVE-2026-115560 (내용·CVSS 확인필요)
- 권고: 임시 조치 (세부 확인필요)

## 연관 후보

- ISMS-P 2.10.8 패치관리, 2.11.2 취약점 점검 및 조치
- 관련 후보 문서: 2026-11-02-kisa-php2shell-response-guide.md

## 보류 사유

- 2026-11-02 kb-fact-checker (attempts 1): www.boho.or.kr / krcert.or.kr 직접 열람 실패(ENOTFOUND). 상세 URL(nttId)이 없음.
- 확인 못 한 값: 제목, CVE-2026-115560, 게시일 2026-10-24, '게시판 번호 2581', 영향 버전, 임시 조치 내용. 본문 요지가 사실상 비어 있음.
- PHP2Shell 공지(nttId 72228/72230)와 같은 건인지 다른 건인지 원문으로 구분해야 함.
- 2026-11-02 2차 kb-fact-checker (attempts 2): www.boho.or.kr 재열람 ENOTFOUND(세션 네트워크 허용 목록 밖). 상세 URL 여전히 없음. 보류 유지. 다음 실행에서도 미확인이면 attempts 3 → 기각.
