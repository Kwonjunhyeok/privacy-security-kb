#!/usr/bin/env python3
"""공공기관 게시판 감시. 새 게시물을 찾아 보고만 한다(AI 미사용).

사용: watch.py --state <상태폴더> --out <결과.json> [--probe]
- 게시판 HTML 에서 링크(제목+식별번호)를 뽑아 상태 파일과 비교한다. 처음 보는 게시판은 기준선만 저장한다.
- --probe: 접속 가능 여부와 추출 결과만 출력하고 상태를 바꾸지 않는다(항상 종료코드 0).
- 판독 실패(접속 차단·구조 변경)는 결과의 errors 에 담는다. 모든 게시판이 실패하면 종료코드 1.
"""
import argparse, html, json, os, re, ssl, sys, urllib.request
from urllib.parse import urljoin

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/124.0 Safari/537.36')
ANCHOR = re.compile(r'<a\b([^>]*)>(.*?)</a>', re.S | re.I)
TAG = re.compile(r'<[^>]+>')
HANGUL = re.compile(r'[가-힣]')
# 게시물 링크처럼 보이는 것: 쿼리의 seq/ntt/idx/id/no 번호 또는 onclick 호출의 번호(메뉴 링크와 구분)
LISTLIKE = re.compile(r'(?:[?&;][A-Za-z_]*(?:seq|ntt|idx|id|no|sn)[A-Za-z_]*=\d{3,})|(?:onclick=["\'][^"\']*\(\s*["\']?\d{3,})', re.I)
MAX_NEW = 25  # 한 번에 이만큼 넘게 새로 보이면 목록 구조 변경으로 본다


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'ko-KR,ko;q=0.9'})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=40, context=ctx) as r:
        raw = r.read()
        enc = r.headers.get_content_charset() or 'utf-8'
    try:
        return r.status, raw.decode(enc, 'replace')
    except LookupError:
        return r.status, raw.decode('utf-8', 'replace')


def extract(page, base):
    items = {}
    for attrs, inner in ANCHOR.findall(page):
        text = html.unescape(TAG.sub(' ', inner))
        text = re.sub(r'\s+', ' ', text).strip()
        if len(text) < 6 or not HANGUL.search(text) or 'attr(' in text or "\\'" in text:
            continue
        href = re.search(r'href=["\']([^"\']*)["\']', attrs)
        href = href.group(1) if href else ''
        ids = re.findall(r'\d{3,}', attrs)
        if href and not href.startswith(('#', 'javascript')):
            link = urljoin(base, html.unescape(href))
        else:
            link = base
        key = text + '|' + ','.join(ids) + ('|' + link if link != base else '')
        items.setdefault(key, {'title': text, 'url': link, 'ids': ids, 'listlike': bool(LISTLIKE.search(attrs))})
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--state', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--probe', action='store_true')
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    boards = json.load(open(os.path.join(here, 'boards.json'), encoding='utf-8'))['boards']
    os.makedirs(a.state, exist_ok=True)
    result = {'new': [], 'errors': [], 'baseline': [], 'probe': []}
    ok = 0
    for b in boards:
        sp = os.path.join(a.state, b['id'] + '.json')
        try:
            status, page = fetch(b['url'])
            items = extract(page, b['url'])
            if not items:
                raise ValueError(f'HTTP {status}, 추출된 링크 0건(구조 변경 또는 차단 페이지 의심)')
            rows = {k: v for k, v in items.items() if v['listlike']}
            if not rows and not a.probe:
                raise ValueError(f'HTTP {status}, 게시물 목록으로 보이는 링크 0건: 목록이 자바스크립트로 나중에 불러와지는 게시판일 수 있어 감시가 새 글을 볼 수 없음')
            ok += 1
        except Exception as e:  # noqa
            result['errors'].append({'board': b['id'], 'name': b['name'], 'error': f'{type(e).__name__}: {e}'})
            result['probe'].append({'board': b['id'], 'ok': False, 'error': str(e)[:160]})
            continue
        result['probe'].append({'board': b['id'], 'ok': True, 'http': status, 'links': len(items), 'listlike': len(rows),
                                'sample': [v['title'][:40] for v in list(rows.values())[:3]]})
        if a.probe:
            continue
        seen = json.load(open(sp, encoding='utf-8')) if os.path.exists(sp) else None
        if seen is None:
            result['baseline'].append(b['id'])
            seen = {}
        fresh = {k: v for k, v in rows.items() if k not in seen}
        if result['baseline'] and result['baseline'][-1] == b['id']:
            fresh = {}
        kws = b.get('keywords')
        if kws:
            fresh = {k: v for k, v in fresh.items() if any(w in v['title'] for w in kws)}
        if len(fresh) > MAX_NEW:
            result['errors'].append({'board': b['id'], 'name': b['name'],
                                     'error': f'새 링크 {len(fresh)}건: 목록 구조가 바뀐 것으로 보여 기준선을 다시 잡음'})
            fresh = {}
        for k, v in fresh.items():
            result['new'].append({'board': b['id'], 'name': b['name'], **v})
        seen.update({k: {'title': v['title']} for k, v in items.items()})
        json.dump(seen, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    json.dump(result, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for p in result['probe']:
        print(p)
    print(f"새 항목 {len(result['new'])}건, 오류 {len(result['errors'])}건, 기준선 {len(result['baseline'])}곳")
    sys.exit(0 if a.probe or ok else 1)


main()
