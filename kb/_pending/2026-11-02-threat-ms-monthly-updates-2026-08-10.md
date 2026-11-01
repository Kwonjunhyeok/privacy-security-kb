---
title: KISA MS 정기 보안 업데이트 권고 (2026년 8월·9월·10월)
category: threats
doc_type: 보안공지
issuer: 한국인터넷진흥원(KISA)
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-10-15   # 가장 최근 공지 기준. 개별 게시일은 본문 표
source_url: https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72216
status: 현행
verified:
candidate:
  kind: new
  target_path: kb/threats/threat-ms-monthly-updates-2026-08-10.md
  found_at:
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72160
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72180
    - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72216
  attempts: 0
---

# MS 정기 보안 업데이트 (2026.8~10)

| 월 | KISA 게시일 | MS 배포일 | 업데이트 수 (긴급/중요) | 취약점 수(페이지 표기) | nttId |
|---|---|---|---|---|---|
| 8월 | 2026-08-19 | 2026-08-11 | 13 (8/5) | 423 | 72160 |
| 9월 | 2026-09-09 | 2026.09.08 | 13 (10/3) | 996 ("취약점 요약 정보 (총 996개)") | 72180 |
| 10월 | 2026-10-15 | 2026-10-13 | 14 (10/4) | 1,417 (페이지 표기, 목록 일부만 읽어 미대조 → 확인필요) | 72216 |

- 대상: Windows 11, Windows Server 2025/2022/2019/2016, Office, SharePoint, Exchange Server, SQL Server, .NET, Visual Studio, Dynamics 365, Azure, Defender(월별 포함 여부·등급 상이)
- 제로데이·실제 악용 CVE: 읽은 범위에서 언급 없음. 10월 공지는 본문 일부(앞 10만 자)만 읽음 → 확인필요
- 9월 취약점 수 996, 10월 1,417은 통상 규모보다 커 보여 원문 재확인 필요 → 확인필요
- 참고: MSRC Update Guide, 릴리스노트 2026-Aug / 2026-Sep / 2026-Oct

## 연관 후보

- ISMS-P 2.10.8 패치관리
