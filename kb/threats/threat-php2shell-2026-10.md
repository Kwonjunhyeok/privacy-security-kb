---
title: PHP 원격 코드 실행 취약점(PHP2Shell, CVE-2026-109618·109619) 및 후속 CVE-2026-115560
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA) / 개인정보보호위원회
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-10-21
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72227
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72227
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72230
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72237
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000342&menuNo=205024&nttId=72233
    - https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12588
---

# PHP2Shell 및 후속 PHP 취약점

## KISA 「PHP 제품 보안 업데이트 권고」 (2026-10-21, nttId 72227)

- CVE-2026-109618 (Improper Handling of Exceptional Conditions), CVE-2026-109619 (Use After Free)
- 영향/해결 버전: 8.2.35 미만→8.2.35 이상, 8.3.36 미만→8.3.36 이상, 8.4.27 미만→8.4.27 이상, 8.5.12 미만→8.5.12 이상
- PHP 8.1 이하는 공식 보안 지원 종료 → 지원 버전으로 전환. 7.4·8.0·8.1은 벤더별 해결 버전·완화 조치 상이.
- 참고: php.net/archive/2026.php#2026-10-21-5, GHSA-w8hw-w9fx-j79w, GHSA-6wmf-4rv5-p3rp

## KISA 「PHP 보안취약점(PHP2Shell) 관련 기업 보안 대응 수칙」 (2026-10-22, nttId 72230, 공지 고정, 작성 디지털위협대응본부 취약점관리센터)

- CVSS 9.2. 로그인 없이 원격 명령 실행. 공격 성공 시 웹셸 설치·고객정보 유출·홈페이지 변조·내부망 침투 가능. 보안 업데이트 배포 전 취약점 정보가 유출되었고, 해외 보안업체를 중심으로 공격 시도 보고.
- PHP 8.2 보안 지원 2026.12.31. 종료 예정 → 8.3 이상 이전 권장.
- 점검 대상: 외주 제작·방치 사이트, 이벤트·테스트 서버, 관리자 페이지 포함. PHP 내장 장비·솔루션(네트워크 장비 관리 화면 등), PHP 포함 윈도우용 설치 패키지, 컨테이너 이미지도 별도 확인. 자산 목록보다 실제 가동 서버 기준.
- 조치 요지: 인터넷 노출 PHP 자산 전수 파악 → 업데이트 후 PHP 실행 웹 서비스 재시작(컨테이너는 신규 이미지 재배포) → 실제 구동 버전 확인 → 8.1 이하 이전 → 즉시 패치 불가 시 임시완화(PHP 앞단 요청 크기 제한, 불필요한 파일 업로드(multipart) 요청 차단, 웹 방화벽 최신 차단 규칙 적용 확인, `session.upload_progress.enabled = 0`, post_max_size·upload_max_filesize 축소 등 — 완전 차단은 아니므로 업데이트 필요) → 로그 점검: 최소 10.20.(취약점 정보 유출일) 이후 기록 전체(비정상적으로 큰 요청 뒤 반복된 HTTP 500, PHP 크래시, 셸 실행, 웹 디렉터리 신규 PHP 파일, 비정상 외부 연결) → 업데이트 전 노출 서버의 DB 비밀번호·API 키·관리자 비밀번호 교체 → 침해 시 격리·신고·증거 확보 → 출처 불명 PoC 실행 금지(필요 시 업무망 분리 환경에서만).

## KISA 「PHP 신규 취약점(CVE-2026-115560) 임시 조치 권고」 (2026-10-24, nttId 72237)

- PHP 세션 처리 과정 원격 코드 실행. CVSS 미표기. 영향 버전 "제조사 미공개"(공개 시 업데이트 예정).
- 10.21 배포 업데이트(8.5.12/8.4.27/8.3.36/8.2.35)로 해결되지 않음. 해결 버전 "미배포(차기 정기 업데이트 예정)".
- 영향 조건(모두 충족): `session.serialize_handler` 가 php_binary 또는 php_serialize, `session_start()` 전 `ini_set()` 으로 php 로 변경, `session.upload_progress.enabled` 활성(기본값).
- 임시조치: php.ini·PHP-FPM pool 설정 등에서 `session.upload_progress.enabled=0` 후 모든 PHP 워커 재시작.

## 관계기관 발표

- KISA 보호나라 경보단계 공지 (2026-10-22, nttId 72233): 10.22. 12:00부로 민간 분야 사이버위기 경보 '관심'→'주의' 상향. 사유는 PHP 취약점으로 인한 대규모 해킹 가능성.
- 개인정보위 (2026-10-22, nttId 12588, 사전실태점검과): PHP 버전 확인·패치, phpMyAdmin 등 DB 관리도구 인터넷 직접 접근 제한, 웹서비스 계정 DB 접근권한 최소화, DB 대량조회·반출 등 비정상 접근 점검, 외주 개발·운영 시스템·수탁업체·호스팅 환경의 PHP 확인·조치 당부.

## 연관

- ISMS-P 2.10.8 패치관리, 2.11.2 취약점 점검 및 조치, 2.9.4 로그 및 접속기록 관리 — 72230 공지의 패치·로그 점검 권고와 직접 대응
- kb/threats 경보 단계 문서(threat-cyber-alert-level-2026-10-22) — 72233 공지가 PHP 취약점을 상향 사유로 명시

## 검증 메모

- 2026-11-02 kb-fact-checker 수정 내용: 로그 점검 시작일 "10.20. 불완전, 확인필요" → 원문 "최소 10.20.(취약점 정보 유출일) 이후 기록 전체"; "관리 콘솔" → "네트워크 장비 관리 화면"; "패치 전 상세정보 유출" → "보안 업데이트 배포 전 취약점 정보 유출"; 정책브리핑(korea.kr)에만 있던 문장(해외기관 평가, 긴급 전파 대상, 문의 번호)은 삭제.
