"""가이드·안내서 원본을 보관 폴더에 분류별로 넣고 수집목록.csv 를 갱신한다.

사용법: python -I archive_originals.py <manifest.json> <보관폴더>

manifest.json 은 항목 배열이다.
[
  {
    "file": "C:/tmp/kb-dl/p12611.bin",       # 받은 파일(저장소 밖)
    "category": "P02_안전조치",               # 보관폴더 아래 분류 폴더
    "org": "개인정보위",                       # 기관 약칭
    "title": "개인정보의 안전성 확보조치 기준 안내서",
    "edition": "2026.11.",                    # 판. 없으면 ""
    "posted": "2026-11-05",                   # 게시일 YYYY-MM-DD
    "url": "https://www.pipc.go.kr/...nttId=12611",
    "original_name": "개인정보의 안전성 확보조치 기준 안내서(2026.11).pdf",
    "official_sha256": null                   # 게시물에 해시가 있으면 적는다
  }
]

- 파일명: <기관>_<자료명>_<판 또는 게시일(YYYY.MM.DD)>.<확장자>. 판 끝 마침표는 확장자 앞에서 겹치지 않게 뗀다.
- 폴더 어디든 같은 sha256 파일이 있으면 복사하지 않는다.
- official_sha256 과 다르면 복사하지 않고 보고한다.
- 같은 기관·자료명의 다른 판 파일이 이미 있으면 "이전 판 후보"로 출력만 한다. 지우지 않는다.
- 수집목록.csv 는 UTF-8 BOM. 열: 분류,기관,자료명,판,게시일,게시물 URL,파일명,크기(바이트),sha256,수집일,원본 첨부 파일명
"""
import csv, hashlib, json, os, re, shutil, sys
from datetime import date

HEADER = ["분류", "기관", "자료명", "판", "게시일", "게시물 URL", "파일명", "크기(바이트)", "sha256", "수집일", "원본 첨부 파일명"]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def ext_of(name, path):
    e = os.path.splitext(name or "")[1].lower()
    if e:
        return e
    head = open(path, "rb").read(4)
    return ".pdf" if head.startswith(b"%PDF") else ".zip" if head.startswith(b"PK") else ".bin"


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    items = json.load(open(sys.argv[1], encoding="utf-8"))
    root = sys.argv[2]
    os.makedirs(root, exist_ok=True)
    csv_path = os.path.join(root, "수집목록.csv")
    rows = []
    if os.path.exists(csv_path):
        with open(csv_path, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))[1:]

    existing = {}
    for dp, _, fs in os.walk(root):
        for fn in fs:
            if not fn.lower().endswith(".csv"):
                existing.setdefault(sha(os.path.join(dp, fn)), os.path.join(dp, fn))

    done, skipped, missing, mismatch, old = [], [], [], [], []
    for it in items:
        src = it["file"]
        if not os.path.exists(src) or os.path.getsize(src) < 1024:
            missing.append(it["title"]); continue
        h = sha(src)
        if it.get("official_sha256") and h != it["official_sha256"].lower():
            mismatch.append((it["title"], h)); continue
        ver = (it.get("edition") or it["posted"].replace("-", ".")).rstrip(".")
        fname = re.sub(r'[<>:"/\\|?*]', "_", f'{it["org"]}_{it["title"]}_{ver}{ext_of(it.get("original_name"), src)}')
        if h in existing:
            skipped.append((fname, existing[h])); continue
        folder = os.path.join(root, it["category"])
        os.makedirs(folder, exist_ok=True)
        prefix = f'{it["org"]}_{it["title"]}_'
        for fn in os.listdir(folder):
            if fn.startswith(prefix) and fn != fname:
                old.append(os.path.join(folder, fn))
        dst = os.path.join(folder, fname)
        shutil.copyfile(src, dst)
        existing[h] = dst
        size = os.path.getsize(dst)
        rows.append([it["category"], it["org"], it["title"], it.get("edition", ""), it["posted"], it["url"],
                     fname, size, h, date.today().isoformat(), it.get("original_name", "")])
        done.append((it["category"], fname, size))

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)

    out = {"saved": done, "skipped_same_sha256": skipped, "missing": missing,
           "hash_mismatch": mismatch, "older_edition_candidates": old}
    sys.stdout.buffer.write((json.dumps(out, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()
