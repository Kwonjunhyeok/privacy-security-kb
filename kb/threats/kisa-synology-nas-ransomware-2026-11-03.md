---
title: Synology NAS 대상 랜섬웨어 공격 주의 권고 (2026-11-03)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-03
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72267
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72267&menuNo=205020
---

# Synology NAS 대상 랜섬웨어 공격 주의 권고 (2026-11-03)

- 게시: KISA 보호나라 보안공지, 2026-11-03 (첨부 PDF 「Synology NAS 대상 랜섬웨어 공격 주의 권고.pdf」 — 첨부 내용 미열람)
- 상황: Synology NAS 대상 랜섬웨어로 저장 파일이 암호화되는 피해 발생
- 감염 의심 징후: 파일이 열리지 않거나 파일명·확장자 비정상 변경(L0CK3D, locked, lock3d, lock3D 등), 복구 대가 금전 요구 안내문
- 예방 조치(요지)
  - 보안 업데이트: 최신 DSM·설치 패키지 적용, 세부 업데이트 번호 확인, 지원 종료 버전은 전환·장비 교체 검토
  - 외부 접근 제한: 관리화면 인터넷 직접 노출 최소화, 불필요한 포트포워딩·원격접속·서비스 비활성화, 원격접속은 VPN 등 통제 경로
  - 계정 보호: 기본 관리자 계정 비활성화, 강력한 비밀번호, 다중인증
  - 백업 보호: NAS와 분리된 오프라인 또는 변경·삭제 제한 백업, 정기 복원 점검(동기화된 데이터도 피해 가능)
- 감염 의심 시: 네트워크 차단·동기화/백업 중단, 랜섬노트·로그 보존 및 기록, 초기화·포맷·재설치·암호화 파일 삭제·덮어쓰기 금지, 불필요한 전원 종료·재부팅·업데이트 회피, KISA 침해사고 신고 후 안내에 따라 조치, 출처 불명 복구 프로그램·사설 복구업체 주의
- 신고 경로: 보호나라 → 침해사고 신고 → 신고하기 → 랜섬웨어
- 참고(공지 인용): 보호나라 Synology 보안 업데이트 권고(nttId 72254), Synology 뉴스(구버전 DSM 대상 랜섬웨어 공격 및 PHP2Shell 수정 확대 안내)
