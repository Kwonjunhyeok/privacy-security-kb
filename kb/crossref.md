# 연관 매핑

ISMS-P 인증기준 항목을 축으로 관련 법 조항, 가이드, 처분 사례, 위협 동향을 잇는다. 연결은 양쪽 문서 본문에서 근거를 확인한 것만 적는다.

2026-11-15: ISMS-P 인증기준 문서가 kb/isms-p 에 반영됐다(2.11.5 연결 추가). 처분 사례 문서는 아직 검증 대기 중이라 kb 에 없다. 아래 2026-11-13 메모 참고.

2026-11-13 기준: ISMS-P 인증기준·처분 사례 문서는 아직 검증 대기 중이라 kb 에 없다. 그래서 해당 열은 `-` 로 두고, kb 에 실제로 있는 문서끼리의 연결만 적었다. 위협 문서 본문에 적힌 ISMS-P 항목(2.10.8 패치관리 등)은 인증기준 문서가 반영되면 이 표로 옮긴다.

| ISMS-P 항목 | 법 조항 | 고시·가이드 | 처분 사례 | 관련 위협·동향 |
|---|---|---|---|---|
| - | 개인정보 보호법 제31조 ([pipa](laws/pipa.md)) ↔ 시행령 제32조제4항 ([pipa-enforcement-decree](laws/pipa-enforcement-decree.md)) | - | - | - |
| [2.11.5 사고 대응 및 복구](isms-p/2-protection-measures.md) | 개인정보 보호법 제34조 ([pipa](laws/pipa.md)) ↔ 시행령 제39조의2·제39조의3 ([pipa-enforcement-decree](laws/pipa-enforcement-decree.md)) | [개인정보 유출등 대응 안내서(2026.9.)](pipc/pipc-guide-breach-response.md) | - | - |
| - | 개인정보 보호법 제64조의2 (제6항 투자 감경) ([pipa](laws/pipa.md)) ↔ 시행령 제60조의2제5항, 별표 1의5 ([pipa-enforcement-decree](laws/pipa-enforcement-decree.md)) | [과징금 투자감경제도 안내서](pipc/pipc-guide-penalty-investment-reduction.md) | - | [유출·침해 사건 신속 조사 및 조사역량 강화 방안](threats/2026-10-02-pipc-breach-investigation-reform.md) |
| - | 개인정보 보호법 제28조의2~제28조의5 ([pipa](laws/pipa.md)) | [가명정보 처리 가이드라인(2026.3.)](pipc/pseudonymization-guideline.md) | - | - |
| - | 개인정보 보호법 제28조의8제1항제5호, 제28조의9 ([pipa](laws/pipa.md)) | - | - | [영국 동등성 인정 검토 착수](threats/2026-10-01-pipc-uk-adequacy-review.md) |
| - | 개인정보 보호법 제25조의2제2항 ([pipa](laws/pipa.md)) | - | - | [스마트 글래스 이용 시 유의사항](threats/2026-11-09-pipc-smart-glasses.md) |
| - | 개인정보 보호법 제16조·제21조·제26조·제29조 ([pipa](laws/pipa.md)) | - | - | [외부 설문도구 이용 시 준수사항](threats/2026-10-16-pipc-external-survey-tools.md) |
| - | 개인정보 보호법 제28조의12~제28조의15 (시행예정, [pipa-amendment-21910](laws/pipa-amendment-21910.md)) ↔ 현행 제18조~제25조의2, 제30조 ([pipa](laws/pipa.md)) | - | - | - |
| - | 정보통신망법 제45조의3·제45조의4 ([network-act](laws/network-act.md)) ↔ 시행령 제36조의7·제36조의10·제36조의11 ([network-act-enforcement-decree](laws/network-act-enforcement-decree.md)) | - | - | - |
| - | 정보통신망법 제48조의7 ([network-act](laws/network-act.md)) ↔ 시행령 제60조의10 ([network-act-enforcement-decree](laws/network-act-enforcement-decree.md)) | - | - | - |
| - | 정보통신망법 제48조의8 ([network-act](laws/network-act.md)) ↔ 개인정보 보호법 제64조의2제1항제9호 ([pipa](laws/pipa.md)) | - | - | - |
| - | - | - | - | [PHP2Shell](threats/threat-php2shell-2026-10.md) ↔ [사이버위기 경보 '주의' 상향](threats/threat-cyber-alert-level-2026-10-22.md) (72233 공지가 상향 사유로 명시) |
| - | - | - | - | [금융권 해킹 대응체계 강화](threats/2026-10-msit-financial-hacking-response.md) ↔ [기업 보안강화 권고](threats/threat-kisa-enterprise-hardening-2026-09-10.md) |
| [2.11.5 사고 대응 및 복구](isms-p/2-protection-measures.md) | 정보통신망법 제48조의3(침해사고 신고, 24시간) ([network-act](laws/network-act.md)) | [정보통신분야 침해사고 대응 안내서](guides/incident-response-guide.md), [랜섬웨어 대응 가이드](guides/ransomware-response-guide.md) | - | - |
