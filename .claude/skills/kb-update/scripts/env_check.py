"""지식베이스 갱신에 필요한 도구와 저장소 상태를 한 번에 보여 준다.

사용법: python env_check.py [저장소경로]
저장소경로를 주지 않으면 KB_REPO_DIR, 그다음 알려진 후보 경로를 찾는다.
아무것도 고치지 않는다(읽기 전용).
"""
import os, shutil, subprocess, sys
from pathlib import Path

CANDIDATES = [
    os.environ.get("KB_REPO_DIR", ""),
    r"D:\Jun\정보보호에이전트",
    str(Path.home() / "정보보호에이전트"),
    str(Path.home() / "privacy-security-kb"),
]
TOOL_DIRS = [
    Path(os.environ.get("LOCALAPPDATA", "")) / "kb-tools",
    Path.home() / ".cache" / "kb-tools",
]


_print = print


def print(*a):  # Windows 콘솔·오래된 Python 에서도 한글이 깨지지 않게 UTF-8 바이트로 쓴다
    sys.stdout.buffer.write((" ".join(str(x) for x in a) + "\n").encode("utf-8"))
    sys.stdout.flush()


def run(cmd, cwd=None):
    try:  # Python 3.6 호환(capture_output·text 없음)
        r = subprocess.run(cmd, cwd=str(cwd) if cwd else None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        out = r.stdout or r.stderr
        return out.decode("utf-8", errors="replace").strip()
    except Exception as e:  # 도구가 없거나 실행 실패
        return "(실패: %s)" % e.__class__.__name__


def tool(name, *args):
    p = shutil.which(name)
    return f"{name}: " + (run([p, *args]).splitlines()[0] if p else "없음")


def find_repo(arg):
    for c in ([arg] if arg else []) + CANDIDATES:
        if c and (Path(c) / ".git").exists() and (Path(c) / "UPDATE.md").exists():
            return Path(c)
    return None


def main():
    print("== 도구")
    print(tool("git", "--version"))
    print(tool("gh", "--version"))
    print(tool("node", "-v"))
    print(tool("npm", "-v"))
    print(tool("pdftotext", "-v"))
    try:
        import pypdf  # noqa
        print("pypdf:", pypdf.__version__)
    except ImportError:
        print("pypdf: 없음")
    pw = [d for d in TOOL_DIRS if (d / "node_modules" / "playwright").exists()]
    print("playwright 도구 폴더:", pw[0] if pw else "없음 (SKILL.md '브라우저 도구 준비')")

    print("\n== 저장소")
    repo = find_repo(sys.argv[1] if len(sys.argv) > 1 else "")
    if not repo:
        print("찾지 못함 → '구성' 모드")
        return
    print("경로:", repo)
    print("브랜치:", run(["git", "branch", "--show-current"], repo))
    print("마지막 커밋:", run(["git", "log", "--oneline", "-1"], repo))
    st = run(["git", "status", "--short"], repo)
    print("커밋 안 된 변경:", "없음" if not st else "\n" + st)
    idx = repo / "kb" / "index.md"
    if idx.exists():
        for line in idx.read_text(encoding="utf-8").splitlines():
            if line.startswith("마지막 갱신:"):
                print(line[:120]); break
    pend = repo / "kb" / "_pending"
    if pend.exists():
        files = [f for f in pend.glob("*.md") if f.name != "README.md"]
        hi = [f.name for f in files if "attempts: 2" in f.read_text(encoding="utf-8")]
        print(f"_pending: {len(files)}건 (attempts 2: {len(hi)}건)")
    reports = sorted((repo / "kb" / "reports").glob("*.md"))
    if reports:
        print("최신 보고서:", reports[-1].name)
    src = repo / ".claude" / "agents" / "security-kms.md"
    for dst in [Path(r"D:\Jun\.claude\agents\security-kms.md"), Path.home() / ".claude" / "agents" / "security-kms.md"]:
        if dst.exists():
            same = src.exists() and src.read_bytes() == dst.read_bytes()
            print(f"상담 에이전트 사본 {dst}: {'같음' if same else '다름'}")


if __name__ == "__main__":
    main()
