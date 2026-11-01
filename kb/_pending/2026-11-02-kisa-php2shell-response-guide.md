---
title: PHP 보안취약점(PHP2Shell) 관련 기업 보안 대응 수칙
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 확인필요   # 2026-10-21~22 무렵으로 검색 요약에 나옴, 원문 미열람
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&pageIndex=1&nttId=72230&menuNo=205020
status: 현행
verified:
candidate:
  kind: new
  target_path: kb/threats/2026-10-php2shell-response-guide.md
  found_at:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&pageIndex=1&nttId=72230&menuNo=205020
    - https://boho.or.kr/kr/bbs/view.do?bbsId=B0000133&categoryCode=&menuNo=205020&nttId=72228&pageIndex=1&searchCnd=&searchWrd=
    - https://knvd.krcert.or.kr/info/vuln/notice/detail?id=6ad8c80eb5290478048f38cf
  attempts: 1
---

> 수집 메모: boho.or.kr DNS 차단으로 원문 미열람. 같은 제목의 게시물이 nttId 72228, 72230 두 개로 검색됨(관계 확인필요). KNVD 「PHP 제품 보안 업데이트 권고」도 함께 있다. 아래 값은 검색 결과 요약에서 본 것이다.

## 요지 (검색 요약 표기, 확인필요)

- 취약점: CVE-2026-109618, CVE-2026-109619 (CVSS 9.2) — 인증 없이 원격 명령 실행 가능
- 보안 업데이트 배포 전 취약점 정보가 유출되었고 공격 시도가 보고됨
- 해결 버전: PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35 이상. PHP 8.1 이하는 공식 업데이트 미제공 → 지원 버전으로 전환
- 업데이트 후 웹 서비스 재시작 필요 (재시작 전에는 이전 버전이 메모리에 남음)
- 인터넷에 노출됐던 서버는 DB 비밀번호, 토큰, 외부 연동 API 키, 관리자 계정 비밀번호 교체 권장
- 즉시 업데이트가 어려우면 웹 방화벽에서 요청 크기 제한·파일 업로드 요청 차단 등 임시 조치. 임시 조치로는 공격을 완전히 막지 못한다고 명시

## 연관 후보

- ISMS-P 2.10.8 패치관리, 2.11.2 취약점 점검 및 조치, 2.11.3 이상행위 분석 및 모니터링
- 개인정보 보호법 제29조 / 안전성 확보조치 기준 (악성프로그램 등 방지 조항 — 조문 번호 확인필요)
- 관련 후보 문서: 2026-11-02-msit-cyber-alert-php-raised.md, 2026-11-02-kisa-php-new-vuln-temporary-measures.md

## 보류 사유

- 2026-11-02 kb-fact-checker (attempts 1): www.boho.or.kr, krcert.or.kr, knvd.krcert.or.kr 직접 열람 실패(모두 ENOTFOUND). A 등급 1곳도 열지 못함.
- 확인 못 한 값: 게시일, CVE 번호(CVE-2026-109618/109619), CVSS 9.2, 해결 버전(8.5.12/8.4.27/8.3.36/8.2.35), 8.1 이하 지원 종료 표기. nttId 72228 과 72230 의 관계(정정·재게시 여부)도 확인필요.
- 패치 버전·CVE 가 틀리면 실무 조치가 잘못되므로, 보호나라 원문(필요하면 php.net 공식 공지도 참고)으로 대조한 뒤에만 통과.
