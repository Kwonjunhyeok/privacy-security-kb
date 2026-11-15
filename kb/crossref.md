# 연관 매핑

ISMS-P 인증기준 항목을 축으로 관련 법 조항, 가이드, 처분 사례, 위협 동향을 잇는다. 연결은 양쪽 문서 본문에서 근거를 확인한 것만 적는다.

2026-11-15(주간 갱신): 법령·고시 5건과 개인정보위 처분·점검 사례 15건이 반영돼, 각 문서의 `## 연관`(검증기가 양쪽 근거를 확인한 것)으로 아래 표 끝에 행을 추가했다.

2026-11-15: ISMS-P 인증기준 문서가 kb/isms-p 에 반영됐다(2.11.5 연결 추가). 아래 2026-11-13 메모 참고.

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
| [ISMS-P 인증기준](isms-p/certification-criteria.md) | 개인정보 보호법 제32조의2 ([pipa](laws/pipa.md)), 정보통신망법 제47조의7 ([network-act](laws/network-act.md)) ↔ 시행령 제55조의7 ([network-act-enforcement-decree](laws/network-act-enforcement-decree.md)) | [ISMS-P 인증 고시](laws/isms-p-certification-notice.md) (별표 7, 제23조) | - | - |
| [2.6.1 네트워크 접근](isms-p/2-protection-measures.md) | [안전성 확보조치 기준](laws/safety-measures-standard.md) 제6조(접근통제) | [안전성 확보조치 기준 안내서(2026.11.)](pipc/safety-measures-guide.md) | [KT](pipc/pipc-disposition-2026-07-29-kt.md), [HD건설기계 등](pipc/pipc-disposition-2026-08-26-hd-hyundai.md), [대교·영훈](pipc/pipc-disposition-2026-10-28-daekyo-younghoon.md), [에듀테크 점검](pipc/pipc-inspection-2026-11-11-edutech.md), [락앤락 등](pipc/pipc-disposition-2026-07-08-locknlock.md) | - |
| [2.7.1 암호정책 적용](isms-p/2-protection-measures.md) | [안전성 확보조치 기준](laws/safety-measures-standard.md) 제7조(암호화) | [안전성 확보조치 기준 안내서(2026.11.)](pipc/safety-measures-guide.md) | [대교·영훈](pipc/pipc-disposition-2026-10-28-daekyo-younghoon.md), [국가아동권리보장원](pipc/pipc-disposition-2026-08-26-ncrc.md), [알뜰폰 8개사](pipc/pipc-disposition-2026-11-11-mvno-8.md), [삼양 4개사](pipc/pipc-disposition-2026-11-11-samyang.md) | - |
| [2.9.4 로그 및 접속기록 관리](isms-p/2-protection-measures.md) | [안전성 확보조치 기준](laws/safety-measures-standard.md) 제8조(접속기록) | [안전성 확보조치 기준 안내서(2026.11.)](pipc/safety-measures-guide.md) | [락앤락 등](pipc/pipc-disposition-2026-07-08-locknlock.md), [알뜰폰 8개사](pipc/pipc-disposition-2026-11-11-mvno-8.md), [고객센터 점검](pipc/pipc-inspection-2026-10-28-call-center.md), [에듀테크 점검](pipc/pipc-inspection-2026-11-11-edutech.md), [쿠팡](pipc/sanction-coupang-breach.md) | - |
| [2.11.2 취약점 점검 및 조치 / 2.11.3 이상행위 분석 및 모니터링](isms-p/2-protection-measures.md) | - | - | [KT](pipc/pipc-disposition-2026-07-29-kt.md), [지에스리테일](pipc/pipc-disposition-2026-08-26-gs-retail.md), [HD건설기계 등](pipc/pipc-disposition-2026-08-26-hd-hyundai.md), [대교·영훈](pipc/pipc-disposition-2026-10-28-daekyo-younghoon.md), [에듀테크 점검](pipc/pipc-inspection-2026-11-11-edutech.md) | - |
| [2.11.5 사고 대응 및 복구](isms-p/2-protection-measures.md) | 개인정보 보호법 제34조 ([pipa](laws/pipa.md)) | [개인정보 유출등 대응 안내서(2026.9.)](pipc/pipc-guide-breach-response.md) | [지에스리테일](pipc/pipc-disposition-2026-08-26-gs-retail.md), [국가아동권리보장원](pipc/pipc-disposition-2026-08-26-ncrc.md), [쿠팡](pipc/sanction-coupang-breach.md) | - |
| [2.8.2 보안 요구사항 검토 및 시험](isms-p/2-protection-measures.md) | [개인정보 영향평가에 관한 고시](laws/pia-notice.md) | [개인정보 영향평가 수행안내서](pipc/pipc-guide-pia-manual.md) | - | - |
| [1.1.2 최고책임자의 지정](isms-p/1-management-system.md) | - | - | [KT](pipc/pipc-disposition-2026-07-29-kt.md), [지에스리테일](pipc/pipc-disposition-2026-08-26-gs-retail.md), [대교·영훈](pipc/pipc-disposition-2026-10-28-daekyo-younghoon.md) | - |
| [3.1.3 주민등록번호 처리 제한](isms-p/3-personal-info-lifecycle.md) | - | - | [국가아동권리보장원](pipc/pipc-disposition-2026-08-26-ncrc.md), [알뜰폰 8개사](pipc/pipc-disposition-2026-11-11-mvno-8.md), [삼양 4개사](pipc/pipc-disposition-2026-11-11-samyang.md) | - |
| [3.3.2 개인정보 처리 업무 위탁](isms-p/3-personal-info-lifecycle.md) | - | - | [알뜰폰 8개사](pipc/pipc-disposition-2026-11-11-mvno-8.md), [삼양 4개사](pipc/pipc-disposition-2026-11-11-samyang.md), [고객센터 점검](pipc/pipc-inspection-2026-10-28-call-center.md), [에듀테크 점검](pipc/pipc-inspection-2026-11-11-edutech.md) | - |
| [3.3.4 개인정보 국외이전](isms-p/3-personal-info-lifecycle.md) | - | - | [틱톡·애플](pipc/pipc-disposition-2026-07-22-tiktok-apple.md), [로봇청소기 점검](pipc/pipc-inspection-2026-09-09-robot-vacuum.md) | - |
| [3.5.1 개인정보 처리방침 공개](isms-p/3-personal-info-lifecycle.md) | - | [개인정보 처리방침 작성지침](pipc/pipc-guide-privacy-policy-writing.md) | [처리방침 사후점검](pipc/pipc-disposition-2026-09-09-privacy-policy-followup.md), [틱톡·애플](pipc/pipc-disposition-2026-07-22-tiktok-apple.md) | - |
| - | 개인정보 보호법 제31조의2(국내대리인) ([pipa](laws/pipa.md)) | [개인정보 처리방침 작성지침](pipc/pipc-guide-privacy-policy-writing.md) Ⅲ-19 | [처리방침 사후점검](pipc/pipc-disposition-2026-09-09-privacy-policy-followup.md), [로봇청소기 점검](pipc/pipc-inspection-2026-09-09-robot-vacuum.md) | - |
| - | 개인정보 보호법 제35조의2·제35조의3 ([pipa](laws/pipa.md)) ↔ 시행령 제42조의2~제42조의15 ([pipa-enforcement-decree](laws/pipa-enforcement-decree.md)) | [개인정보관리 전문기관 지정 안내서](pipc/pipc-guide-mydata-specialist-agency.md) | - | - |
| - | [정보통신기반 보호법](laws/ciip-act.md) 제9조(취약점 분석·평가) | [기술적 상세가이드](guides/ciip-technical-vulnerability-assessment-guide.md), [관리·물리적 안내서](guides/ciip-managerial-physical-vulnerability-assessment-guide.md) | - | - |
| - | [신용정보법](laws/credit-information-act.md) 제39조의4(누설통지) | [개인정보 유출등 대응 안내서(2026.9.)](pipc/pipc-guide-breach-response.md) | - | - |
