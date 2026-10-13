"""Put the LaTeX code copied from MathType into the numbered equations of the paper.

The lecturer requires every formula to be typed in MathType and its LaTeX copied into the paper. Paste what MathType
copies (Preferences -> Cut and Copy Preferences -> MathML or TeX -> "LaTeX 2.09 and later") between the BAT DAU and
KET THUC lines of huong_dan/MATHTYPE_DAN_VAO.txt, then run (from the Latex_FinalCapstone folder):

    python scripts/insert_mathtype.py --dry-run     # show what would change
    python scripts/insert_mathtype.py               # write the chapters

For every filled slot the script removes the \\[ \\] (or $$ $$) wrapper and MathType's comment lines, replaces the body of
the equation environment that carries the slot's \\label, keeps \\label and the equation number, and marks the body with
"% typed in MathType". Empty slots are skipped, so the equations can be done a few at a time. A slot whose braces do not
balance is reported and left out.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CHAPTERS = ["chapters/main/Chapter3.tex", "chapters/main/Chapter4.tex"]
SLOT = re.compile(r"^%%% \((\d+)\) (eq:[\w:-]+) BAT DAU[ \t]*\n(.*?)^%%% \(\1\) \2 KET THUC", re.S | re.M)
MARK = "% typed in MathType"


def clean(code: str) -> str:
    lines = [ln for ln in code.splitlines() if not ln.strip().startswith("%")]  # MathType translator / MTEF data
    s = "\n".join(ln.rstrip() for ln in lines).strip()
    for left, right in ((r"\[", r"\]"), ("$$", "$$"), ("$", "$")):
        if s.startswith(left) and s.endswith(right) and len(s) > len(left) + len(right):
            s = s[len(left):-len(right)].strip()
            break
    return re.sub(r"\\epsilon(?![A-Za-z])", r"\\varepsilon", s)  # same epsilon as the text of the paper


def problems(s: str) -> list[str]:
    out = []
    depth = 0
    for ch in re.sub(r"\\[{}]", "", s):
        depth += (ch == "{") - (ch == "}")
        if depth < 0:
            break
    if depth:
        out.append("ngoặc { } không cân")
    if re.search(r"\\\[|\\\]|\$", s):
        out.append("còn sót \\[, \\] hoặc $")
    if re.search(r"\\(begin|end)\{equation", s):
        out.append("không được chứa \\begin{equation}")
    if not s:
        out.append("rỗng")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--paste", type=Path, default=Path("huong_dan/MATHTYPE_DAN_VAO.txt"))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # Vietnamese messages on a cp1252 Windows console

    texts ={f: Path(f).read_text(encoding="utf-8") for f in CHAPTERS}
    done, skipped, failed = [], [], []
    for num, label, raw in SLOT.findall(a.paste.read_text(encoding="utf-8")):
        code = clean(raw)
        if not code:
            skipped.append(f"({num})")
            continue
        bad = problems(code)
        if bad:
            failed.append(f"({num}) {label}: " + "; ".join(bad))
            continue
        pat = re.compile(r"(\\begin\{equation\}[ \t]*\n)((?:(?!\\begin\{equation\}).)*?)(^([ \t]*)\\label\{"
                         + re.escape(label) + r"\}[ \t]*\n[ \t]*\\end\{equation\})", re.S | re.M)
        for f, t in texts.items():
            m = pat.search(t)
            if m:
                ind = m.group(4)
                body = "\n".join(ind + ln for ln in [MARK] + code.splitlines()) + "\n"
                texts[f] = t[:m.start(2)] + body + t[m.end(2):]
                old = " ".join(m.group(2).split())
                done.append(f"({num}) {label} in {f}\n      cũ: {old[:90]}\n      mới: {' '.join(code.split())[:90]}")
                break
        else:
            failed.append(f"({num}) {label}: không tìm thấy \\label{{{label}}} trong {', '.join(CHAPTERS)}")

    for line in done:
        print("THAY  " + line)
    for line in failed:
        print("LỖI   " + line)
    if skipped:
        print("Bỏ qua (chưa dán):", " ".join(skipped))
    if done and not a.dry_run:
        backup = Path("huong_dan/backup_truoc_mathtype")  # the LaTeX version, kept from the first run on
        backup.mkdir(parents=True, exist_ok=True)
        for f, t in texts.items():
            keep = backup / Path(f).name
            if not keep.exists():
                keep.write_text(Path(f).read_text(encoding="utf-8"), encoding="utf-8")
            Path(f).write_text(t, encoding="utf-8")
        print(f"Bản LaTeX trước lần chạy đầu tiên được giữ ở {backup.as_posix()}/.")
        print(f"Đã ghi {len(done)} công thức. Build lại trên Overleaf để kiểm tra số thứ tự và tràn lề.")
    elif done:
        print("--dry-run: chưa ghi gì.")


if __name__ == "__main__":
    main()
