---
title: 국가 망 보안체계(N2SF) 이해 및 활용 안내
category: guides
doc_type: 가이드라인
issuer: 국가정보원 국가사이버안보센터   # 게시 기관. 원문에서 읽은 쪽(1·2·4·5·9·12쪽)에 발행 기관 표기는 보지 못함 → 확인필요
promulgation_no: 해당없음
effective_date: 해당없음
published_date: 2026-03-24
edition: 확인필요
topics: [S09]
source_url: https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvNj_uU6OMakPcrAhgWAjJq6eEvT3SmMyxg5hgnvZ2g1h
status: 현행
verified:
candidate:
  kind: new
  target_path: kb/guides/n2sf-overview.md
  found_at:
    - https://www.ncsc.go.kr/ko/main/PageLink.html?token=MDEyMzQ1Njc4OWFiY2RlZrBvBnCd4cC_Aqu-HrYk1bi4IwVbci5a1FamchlW1qNssCyKZu6ZLfUXAiW9SUOAvNj_uU6OMakPcrAhgWAjJq6eEvT3SmMyxg5hgnvZ2g1h   # 자료실 > 지침·가이드 4번(기타 공시), 작성일 2026.03.24 (2026-11-15 내장 브라우저)
    - https://www.ncsc.go.kr/api/usr/bbs/downloadFile   # POST downloadFileId=48175697-2b66-4979-a6cb-74cfc69c5d55, 「국가_망_보안체계(N2SF)_이해_및_활용_안내.pdf」 7,970,302바이트. sha256 af605dd1b82b444e691f5ed4303e7842e37390ac97e703c2d3b7e0a9ead3af06 = 게시물 게시 해시값과 일치
  attempts: 0
---

# 국가 망 보안체계(N2SF) 이해 및 활용 안내

## 게시 정보

- 국가사이버안보센터 자료실 > 지침·가이드, 번호 4, 구분 "기타 공시", 작성일 2026.03.24. 게시물 본문: "국가 망 보안체계(N2SF) 이해를 돕기위한 설명자료입니다".
- 첨부 1건 「국가_망_보안체계(N2SF)_이해_및_활용_안내.pdf」(13쪽). 받은 파일의 SHA-256 이 게시물에 적힌 해시값과 같다.
- 글자 추출이 되지 않아(Adobe-Korea1 글꼴) 1·2·4·5·9·12쪽을 렌더링해 읽었다. 3·6·7·8·10·11·13쪽은 원문 미확인.
- 판·발행일·발행 기관 표기는 읽은 쪽에서 보지 못했다(확인필요).

## 목적·적용 대상

- 성격: 「N2SF 보안가이드라인」 본문이 아니라 N2SF 이해를 돕는 설명자료(게시물 본문). 각 쪽 머리말의 구성: N2SF의 개념 / N2SF 활용효과(예시) / N2SF 적용 5단계 / N2SF 정책 카드뉴스.
- 대상: 원문 2쪽은 "각 기관"이 기관장 책임하에 등급 분류·위협 식별 후 보안대책을 수립·시행해야 한다고 적음. 적용 대상 기관의 범위는 kb/guides/n2sf-security-guideline.md(국가·공공기관, 각급기관)를 함께 본다.

## 목차

- N2SF(국가 망 보안체계)의 개념 (2쪽)
- N2SF 활용효과(예시) (3쪽, 원문 미확인)
- N2SF 적용 5단계 (4쪽 개관, 5~9쪽 단계별): 1. 준비(Prepare) / 2. C/S/O 등급분류(Classification) / 3. 위협 식별(Identify) / 4. 보안대책 수립(Select) / 5. 적절성 평가·조정(Assess)
- N2SF 정책 카드뉴스 (10~13쪽)

## 장별 요지

- 개념(2쪽): N2SF는 업무망을 획일적으로 인터넷과 분리하는 기존 '망 분리' 체계를 개선한 보안체계. 업무정보(데이터)의 중요도에 따라 기밀(Classified)·민감(Sensitive)·공개(Open) 등급으로 분류하고 등급별 차등 보안통제를 적용. 그림 예시: C등급(비밀·안보·국방·통일·외교·범죄·재판정보 등) 엄격 통제, S등급(감사·감독·시험·입찰·인사·개인정보 등) 제한 접근, O등급(공개 가능한 일반 정보) 공유·활용.
- 5단계 개관(4쪽): 준비(자산 식별) → 등급분류(C/S/O 분류) → 위협 식별(정보서비스 모델링) → 대책 수립(보안통제 선택) → 평가·조정(종합 검토).
- 1단계 준비(5쪽): 업무정보 식별은 정부기능분류체계(BRM)의 최소 '소기능(5레벨)' 수준에서 수행하고, 식별된 업무정보를 처리하는 정보시스템·서비스를 파악. 등급분류가 세부적으로 되도록 '과' 단위 미만 업무 수준인 5레벨을 적용한다고 적음.
- 2~4단계(6~8쪽): 원문 미확인 → 확인필요(추출 글자에 "N2SF-LP-" 형태의 보안통제 ID 표기가 보임).
- 5단계 적절성 평가·조정(9쪽): 가이드라인에 수록된 단계별 '적절성 평가지표'로 평가하고, 미비점은 조정·보완 후 기관 정보보안 담당관의 검토·승인을 거쳐 확정. 예시 지표(등급분류 단계): 업무정보 등급분류 기준 준수, 준비단계 식별 업무정보의 누락 없는 분류, 정보시스템 등급은 포함된 업무정보 중 최상위 등급, 하나의 시스템은 가급적 동일 등급 업무정보로 구성. 표 제목은 "평가지표(권고)".
- 카드뉴스(12쪽): 기밀·민감·공개 등급을 "강철 금고 방", "든든한 서재", "사랑방"에 비유.

## 근거 법령

- 읽은 쪽에서 법령 조문 인용은 보지 못했다(확인필요). 등급분류·보안대책·평가 절차의 세부 기준은 「N2SF 보안가이드라인 1.0」(kb/guides/n2sf-security-guideline.md)이 근거 문서다. 이 설명자료의 평가지표는 "권고"로 표기돼 있다.

## 연관 후보

- kb/guides/n2sf-security-guideline.md (국가 망 보안체계(N2SF) 보안가이드라인 1.0, 2025-09-30)
- 국가사이버안보센터 「국가 사이버보안 기본지침(5.1부 개정) 안내」(2026-07-20, 원문 미확인)
- 같은 분류(S09): 「2026년도 사이버보안 실태 평가지표」(2025-12-11)
- ISMS-P 후보: 1.2.1 정보자산 식별, 2.6.1 네트워크 접근, 2.6.7 인터넷 접속 통제
