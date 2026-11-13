---
title: Zyxel 제품 보안 업데이트 권고 (GS1900 스위치·AP·FWA7·Security Router, 2026-11-05)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-11-05
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72279
status: 현행
verified:
  date: 2026-11-13
  by: kb-fact-checker
  sources:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72279&menuNo=205020
---

# Zyxel 제품 보안 업데이트 권고 (2026-11-05)

- 게시: KISA 보호나라 보안공지, 2026-11-05
- 취약점
  - CVE-2026-107441: GS1900 시리즈 스위치 Out-of-bounds Write
  - CVE-2026-76955: AP, FWA7, Security Router Classic Buffer Overflow
- 영향·해결(요지, 모델별 상세는 원문 표)
  - GS1900-8/8HP/10HP/16/24/24E/24EP/24HPv2/48/48HPv2: 펌웨어 2.90(xxxx.2)C0 이하 → 2.90(xxxx.3)C0 이상
  - NWA·WAX·WBE·IAP500BE 등 AP, FWA7 Leaf Plus/Root/Root Plus: 7.12(xxxx.0)C0 이하 → 7.12(xxxx.1)C0 이상, 7.40(xxxx.1)C0 이하 → 7.40(xxxx.2)C0 이상 (모델별 코드 상이)
  - WAC500H: 6.70(ABWA.7)C0 이하 → 핫픽스 적용(벤더 문의)
  - 원문 표기 불일치: 공지 설명과 참고 링크[2] 제목에는 "Security Router"가 포함되나, 영향 표에는 Security Router 모델이 없음(AP·FWA7 모델만 기재). 이 문서는 영향 표 값을 따르며, Security Router 사용 시 Zyxel 원 권고([2])에서 해당 모델을 직접 확인해야 함
- 권고 조치: 해결 버전으로 업데이트
- 참고(공지 인용): zyxel.com security-advisories(GS1900 Out-of-bounds Write 11-03-2026, AP·FWA7·Security Router Buffer Overflow 11-03-2026), NVD
