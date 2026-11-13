---
title: 지란지교소프트 CrossUploader 보안 조치 권고 (2026-11-03)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-03
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72269
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72269&menuNo=205020
---

# 지란지교소프트 제품 보안 조치 권고 (2026-11-03)

- 게시: KISA 보호나라 보안공지, 2026-11-03
- 취약점: CrossUploader 부적절한 파일 업로드 취약점(CVE 번호 공지에 없음)
- 영향: CrossUploader 1.0.00 이상 3.0.09 이하
- 조치 방안: 샘플파일(UploadProcess.jsp) 삭제 및 보안 설정. 별도 보안 업데이트 버전은 안내되지 않음
- 보안 조치 방법(요지)
  1. 운영 환경의 샘플 폴더 /NamoCrossUploaderH5Samples, /NamoCrossUploaderJaSamples 삭제
  2. 기본 설치 경로 외에도 UploadProcess.jsp 존재 여부 확인 후 불필요 파일 삭제
  3. 웹 접근 로그에서 해당 파일 호출 이력, 업로드 경로의 비정상 JSP 등 스크립트 생성 여부 점검
  4. 샘플파일을 실서비스에 쓰는 경우: 필요한 확장자만 허용, 업로드 요청 인증·권한 검증, 서버 측 확장자·내용·파일명 검증, 웹 직접 접근 불가 경로에 저장, 업로드 폴더 스크립트 실행 차단
  - 샘플 폴더 삭제는 제품 정상 동작에 영향 없음. 실서비스 사용 중이면 삭제 전 영향 확인
- 참고(공지 인용): jiran.tistory.com/1752 (제조사 블로그)
