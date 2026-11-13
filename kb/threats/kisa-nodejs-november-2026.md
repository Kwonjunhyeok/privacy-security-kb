---
title: Node.js 제품 보안 업데이트 권고 (2026-11-12)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-12
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72302
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72302&menuNo=205020
---

# Node.js 제품 보안 업데이트 권고 (2026-11-12)

- 게시: KISA 보호나라 보안공지, 2026-11-12 (기존 초안 `2026-11-02-kisa-nodejs-security-update.md` 의 nttId 72236 공지와 다른 별개 공지)
- 취약점 10건
  - Reachable Assertion: CVE-2026-123863 / Race Condition: CVE-2024-27983
  - Use After Free: CVE-2026-123864, 123866, 123874
  - Uncontrolled Resource Consumption: CVE-2026-123865, CVE-2026-48937
  - NULL Pointer Dereference: CVE-2026-126051 / Improper Authentication: CVE-2026-123872
  - Exposure of Private Personal Information to an Unauthorized Actor: CVE-2026-48615
- 해결 버전(공지 표 요지): 22.23.5 이상, 24.22.3 이상, 26.13.1 이상이 이번 릴리스의 주요 해결 버전
  - CVE-2026-123864·123865·123866·123872: 22.23.5 미만 / 23.0.0~24.22.3 미만 / 25.0.0~26.13.1 미만
  - CVE-2026-123863·123874: 24.22.0~24.22.3 미만 / 26.9.0~26.13.1 미만
  - CVE-2026-126051: 24.0.0~24.22.3 미만 / 25.0.0~26.13.1 미만
  - CVE-2026-48937: 22.0.0~22.23.0 미만(→22.23.0), 24.0.0~24.17.0 미만(→24.17.0)
  - CVE-2026-48615: 22.22.3 이하(→22.23.0), 24.16.0 이하(→24.17.0), 26.3.1 미만(→26.3.1)
  - CVE-2024-27983: 18.20.1 / 20.12.1 / 21.7.2 미만(→ 각 해당 버전 이상)
- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): nodejs.org november-2026-security-releases, april-2024-security-releases, june-2026-security-releases, github.com/nodejs/node 릴리스 v18.20.1·v20.12.1·v21.7.2, NVD
- 원문 표기 불일치: 본문 각주 번호가 참고사이트 목록 번호와 맞지 않음(예: CVE-2026-123863 의 [4]는 v20.12.1 릴리스 링크, NVD 링크는 [7]; CVE-2026-48937·48615 의 [3]은 v18.20.1 릴리스 링크). 설명의 CVE·유형과 영향 표의 버전 값은 서로 일치하므로 이 문서는 본문·표 값을 따름
