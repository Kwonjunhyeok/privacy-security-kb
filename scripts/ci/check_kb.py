#!/usr/bin/env python3
"""kb PR 검사. 형식만 본다(값의 진위는 kb-fact-checker 몫).

사용: check_kb.py <base-ref>   변경 파일은 git diff <base-ref>...HEAD 로 구한다.
출력: 마지막 줄에 PROTECTED=true|false, 실패 사유는 stderr, 실패 시 종료코드 1.
"""
import datetime, re, subprocess, sys
from urllib.parse import urlparse

# 이 경로를 건드린 PR 은 자동 병합하지 않는다(규칙·절차·출처 변경은 사람이 승인)
PROTECTED = ('.claude/', 'CLAUDE.md', 'UPDATE.md', 'sources.md', 'scripts/', '.github/', 'docs/')
# kb 안에서도 문서 형식을 따르지 않는 파일
NON_DOC = {'kb/CHANGELOG.md', 'kb/index.md', 'kb/catalog.md', 'kb/crossref.md', 'kb/topics.md'}
CATEGORIES = {'laws', 'isms-p', 'pipc', 'guides', 'threats'}
# 1차 출처(A) 도메인. sources.md 와 맞춘다. 법령 외 문서는 이 중 최소 1곳이 verified.sources 에 있어야 한다.
A_DOMAINS = ('law.go.kr', 'pipc.go.kr', 'privacy.go.kr', 'msit.go.kr', 'korea.kr', 'fsc.go.kr',
             'likms.assembly.go.kr', 'gwanbo.go.kr', 'kisa.or.kr', 'boho.or.kr', 'ncsc.go.kr')
# KISA 공지가 지정한 배포처. 같은 문서에 kisa.or.kr 출처가 함께 있을 때만 근거로 센다(sources.md)
KISA_DESIGNATED = ('data.go.kr',)
# 근거로 쓰지 않는 출처(C 등급)
C_DOMAINS = ('tistory.com', 'blog.naver.com', 'cafe.naver.com', 'brunch.co.kr', 'velog.io', 'medium.com',
             'wikipedia.org', 'namu.wiki', 'dcinside.com', 'reddit.com')
LAW_TYPES = ('법률', '시행령', '시행규칙', '고시')
REQUIRED = ('title', 'category', 'doc_type', 'issuer', 'source_url', 'status')


def changed(base):
    if base == 'ALL':  # 전수 시험용
        return [('A', f) for f in subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True).stdout.splitlines()]
    out = subprocess.run(['git', 'diff', '--name-status', f'{base}...HEAD'],
                         capture_output=True, text=True, check=True).stdout
    res = []
    for line in out.splitlines():
        parts = line.split('\t')
        res.append((parts[0][0], parts[-1]))  # (상태, 경로)
    return res


def frontmatter(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    return m.group(1) if m else None


def top_keys(fm):
    return {m.group(1): m.group(2).strip() for m in re.finditer(r'^([A-Za-z_]+):[ \t]*(.*)$', fm, re.M)}


def host_match(host, domains):
    return any(host == d or host.endswith('.' + d) for d in domains)


def source_hosts(fm):
    m = re.search(r'^verified:\n((?:[ \t]+.*\n?)+)', fm + '\n', re.M)
    block = m.group(1).split('sources:')[-1] if m and 'sources:' in m.group(1) else ''
    return [urlparse(u).hostname or '' for u in re.findall(r'https?://[^\s\]\)\'",]+', block)]


def verified_sources(fm):
    m = re.search(r'^verified:\n((?:[ \t]+.*\n?)+)', fm + '\n', re.M)
    if not m:
        return None, 0
    block = m.group(1)
    date = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', block)
    by = re.search(r'by:\s*(\S+)', block)
    n = len(re.findall(r'https?://', block.split('sources:')[-1])) if 'sources:' in block else 0
    return (date, by), n


def main():
    base = sys.argv[1]
    errors, protected = [], False
    for status, path in changed(base):
        if path.startswith(PROTECTED):
            protected = True
        if status == 'D':
            continue
        if path.startswith('kb/_pending/') and path != 'kb/_pending/README.md':
            continue  # 초안은 형식 제한 없음
        if not (path.startswith('kb/') and path.endswith('.md')):
            if not path.startswith(PROTECTED) and not path.startswith('kb/'):
                errors.append(f'{path}: 허용 경로(kb/ 또는 보호 경로) 밖의 변경')
            continue
        if path in NON_DOC or path.startswith('kb/reports/') or path.endswith('README.md'):
            continue
        text = open(path, encoding='utf-8').read()
        fm = frontmatter(text)
        if fm is None:
            errors.append(f'{path}: frontmatter 없음'); continue
        keys = top_keys(fm)
        for k in REQUIRED:
            if not keys.get(k):
                errors.append(f'{path}: 필수 필드 {k} 없음')
        cat = path.split('/')[1]
        if keys.get('category') and keys['category'] != cat:
            errors.append(f'{path}: category({keys["category"]}) 가 폴더({cat}) 와 다름')
        for bad in ('candidate', 'fact_check'):
            if bad in keys:
                errors.append(f'{path}: 초안 전용 필드 {bad} 가 남아 있음(검증 전 초안이 kb 로 들어옴)')
        if '## 보류 사유' in text:
            errors.append(f'{path}: "## 보류 사유" 절이 남아 있음(보류 항목은 _pending 에만)')
        v, n = verified_sources(fm)
        if v is None:
            errors.append(f'{path}: verified 블록 없음'); continue
        date, by = v
        if not date:
            errors.append(f'{path}: verified.date 없음')
        if not by or by.group(1) != 'kb-fact-checker':
            errors.append(f'{path}: verified.by 가 kb-fact-checker 가 아님')
        hosts = source_hosts(fm)
        for h in hosts:
            if host_match(h, C_DOMAINS):
                errors.append(f'{path}: 근거로 쓸 수 없는 출처(C 등급) {h}')
        has_a = any(host_match(h, A_DOMAINS) for h in hosts)
        if cat != 'threats' and not has_a:
            errors.append(f'{path}: verified.sources 에 1차 출처(A 등급 기관 도메인)가 없음')
        if any(host_match(h, KISA_DESIGNATED) for h in hosts) and not any(host_match(h, ('kisa.or.kr',)) for h in hosts):
            errors.append(f'{path}: data.go.kr 출처는 KISA 공지(kisa.or.kr)와 함께일 때만 인정')
        if keys.get('doc_type') in LAW_TYPES and cat == 'laws':
            if not any(host_match(h, ('law.go.kr',)) for h in hosts):
                errors.append(f'{path}: 법령·고시는 law.go.kr 출처가 필수')
            for k in ('promulgation_no', 'effective_date'):
                v = keys.get(k, '')
                if not v or '확인필요' in v:
                    errors.append(f'{path}: 법령·고시 {k} 가 비었거나 확인필요')
        if date:
            try:
                d = datetime.date.fromisoformat(date.group(1))
                if d > datetime.date.today() + datetime.timedelta(days=1):
                    errors.append(f'{path}: verified.date({d}) 가 미래 날짜')
            except ValueError:
                errors.append(f'{path}: verified.date 형식 오류')
        # threats·처분 사례는 출처 1곳 허용(CLAUDE.md), 그 밖은 2곳 이상
        one_ok = cat == 'threats' or keys.get('doc_type') in ('처분', '보안공지', '동향')
        if n < (1 if one_ok else 2):
            errors.append(f'{path}: verified.sources {n}곳 (필요 {1 if one_ok else 2}곳 이상)')
    for e in errors:
        print('ERROR', e, file=sys.stderr)
    print(f'PROTECTED={"true" if protected else "false"}')
    sys.exit(1 if errors else 0)


main()
