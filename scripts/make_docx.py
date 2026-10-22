"""Word version of the paper in the conference template (csnt_format-1.doc, converted to .docx by Word).

The text comes from the LaTeX sources, so the two versions say the same: chapters/main/*.tex and chapters/front/thanks.tex for the
body, main.bbl for the references (as formatted by IEEEtran.bst in the last LaTeX build) and main.aux for the numbers of sections,
tables, figures and equations. The body uses the template's own styles (Heading 1/2 numbering, Body Text, figure caption, table head,
references). Inline math is written as formatted text; the nine numbered equations are written below in linear UnicodeMath and built
up by Word (scripts/finish_docx.ps1), so they are native Word equations that the team can retype in MathType.

Figures: Fig. 3-4 are redrawn at 600 dpi by scripts/make_paper_figures.py; Fig. 1-2 (ConceptDraw PDFs) are rendered to PNG by
scripts/pdf_to_png.ps1 (Windows PDF renderer) and cropped to their content.

Usage (from the Latex_FinalCapstone folder, Windows, Microsoft Word installed; first save csnt_format-1.doc as .docx in Word):
    python scripts/make_docx.py --template <csnt_format-1.docx> --work <scratch folder> --prepare-figures
    powershell -File scripts/finish_docx.ps1 PPFedData.docx      # builds the equations, saves, exports a PDF, counts pages
The figures are made once with --prepare-figures; drop the flag when only the text changed. Rebuild main.aux and main.bbl with
LaTeX first if sections, labels or citations changed.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ["Abstract", "Chapter1", "Chapter2", "Chapter3", "Chapter4", "Chapter5", "Chapter6"]
TEXT_W, COL_W = 10080, 4860                     # twips: text width (7 in) and one column of the template (3.375 in)
EMU = 635                                       # EMU per twip
TABLE_PT, NOTE_PT = 7, 7                        # table text and notes: 7 pt, as \scriptsize in the LaTeX version
# Word has no floats: a figure or table that does not fit the rest of a column jumps to the next one and leaves a gap. As LaTeX
# would, these floats are placed after the given number of following paragraphs, so that text fills the column first (tuned on
# the PDF exported by scripts/finish_docx.ps1; check again after any change of the text).
DEFER: dict[str, int] = {"fig:tstr_eps": 1}

# The nine numbered equations in linear UnicodeMath (Word builds them up); keep them in step with chapters/main/Chapter3-4.tex.
EQUATIONS = {
    "eq:dirichlet": "𝐩_c=(p_(c,1),…,p_(c,K))∼\"Dir\"(α_(\"dir\") 𝟏_K ),",
    "eq:chow_liu": "T^⋆=\"arg max\"┬T ∑_((i,j)∈T)▒〖Î(X_i;X_j)〗,",
    "eq:tree_factorization": "P̂(𝐱∣c)=P̂(x_r∣c) ∏_((u,v)∈T^⋆)▒〖P̂(x_v∣x_u,c)〗,",
    "eq:sensitivity": "Δ_(1,r)=m M_r,  Δ_(2,r)=m√(M_r ).",
    "eq:skellam_rdp": "■(&ε_r (λ)≤(λΔ_(2,r)^2)/(2μ_r )@&  +min(((2λ−1)Δ_(2,r)^2+6Δ_(1,r))/(4μ_r^2 ),(3Δ_(1,r))/(2μ_r ))).",
    "eq:rdp_conversion": "ε=min┬λ [∑_(r=1)^3▒〖ε_r (λ)〗−(ln δ+ln λ)/(λ−1)+ln((λ−1)/λ)],",
    "eq:secagg": "S=∑_(k∈𝒦)▒〖(𝐱_k+𝛏_k)〗 \" mod \" 2^32,",
    "eq:dpsgd": "g̃=1/b (∑_(i=1)^b▒〖g_i/max(1,‖g_i ‖_2/G)〗+𝒩(0,σ_k^2 G^2 𝐈)),",
    "eq:decision_rule": "0∉\"CI\"_(95%) (Δ̅)  \"and\"  |Δ̅|>max(\"sd\"_A,\"sd\"_B ),",
}

# ---------------------------------------------------------------------------------------------------------------- symbols
GREEK = {"alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε", "zeta": "ζ", "eta": "η",
         "theta": "θ", "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π", "rho": "ρ", "sigma": "σ",
         "tau": "τ", "phi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω", "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ",
         "Xi": "Ξ", "Pi": "Π", "Sigma": "Σ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω"}
SYM = {"le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠", "times": "×", "pm": "±", "approx": "≈", "sim": "∼",
       "in": "∈", "notin": "∉", "cup": "∪", "cap": "∩", "infty": "∞", "dots": "…", "ldots": "…", "cdots": "⋯", "cdot": "·",
       "star": "⋆", "to": "→", "rightarrow": "→", "mid": "∣", "ell": "ℓ", "circ": "∘", "dagger": "†", "prod": "∏", "sum": "∑",
       "lvert": "|", "rvert": "|", "|": "‖", "{": "{", "}": "}", "%": "%", "#": "#", "&": "&", "_": "_", "partial": "∂"}
FUNCS = {"ln", "log", "min", "max", "exp", "arg", "det", "lim", "sin", "cos", "Pr"}
SKIP_MATH = {"left", "right", "big", "Big", "bigl", "bigr", "Bigl", "Bigr", "bigg", "Bigg", "displaystyle", "nonumber", "!"}
SPACES = {",": "\u2009", ";": " ", ":": " ", "quad": "\u2003", "qquad": "\u2003\u2003", " ": " "}
ACCENT = {"hat": "\u0302", "widehat": "\u0302", "tilde": "\u0303", "bar": "\u0305", "overline": "\u0305"}
CAL = {"K": "𝒦", "D": "𝒟", "N": "𝒩", "L": "ℒ", "B": "ℬ", "E": "ℰ", "F": "ℱ", "H": "ℋ", "I": "ℐ", "M": "ℳ", "R": "ℛ"}
BB = {"Z": "ℤ", "R": "ℝ", "N": "ℕ", "Q": "ℚ", "C": "ℂ", "E": "𝔼"}
SUPER = str.maketrans("0123456789+-=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ")
SUB = str.maketrans("0123456789+-=()", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎")
REL, BIN = set("=<>≤≥≈∼∈∉→≠"), set("+−×±∪∩")
MATH_FONT_CHARS = set("⋆∣∉∪∩ℓ𝒦𝒟𝒩ℤℝ∏∑√‖∘∼✓✗")       # glyphs Times New Roman may lack: Cambria Math has them
TEXT_ACCENT = {'"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303", "c": "\u0327", "v": "\u030C", "=": "\u0304"}

warnings: list[str] = []


def R(t, **k):
    """One run: text plus formatting (i, b, mono, va = 'sub' / 'sup', font, sz in half points, sc)."""
    return {"t": t, **k}


# --------------------------------------------------------------------------------------------------------------- parsing helpers
def group(s: str, i: int) -> tuple[str, int]:
    """Content of the balanced {...} starting at s[i] (skipping spaces) and the index after it."""
    while i < len(s) and s[i] in " \n\t":
        i += 1
    if i >= len(s) or s[i] != "{":
        return (s[i], i + 1) if i < len(s) else ("", i)
    depth, j = 0, i
    while j < len(s):
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced braces near: " + s[i:i + 60])


def opt(s: str, i: int) -> tuple[str | None, int]:
    """Optional [..] argument at s[i]."""
    if i < len(s) and s[i] == "[":
        j = s.index("]", i)
        return s[i + 1:j], j + 1
    return None, i


def strip_comments(t: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in t.split("\n"))


# ------------------------------------------------------------------------------------------------------------------ math
def parse_math(s: str, i: int, va, style: str, out: list, stop: str | None = None) -> int:
    while i < len(s):
        c = s[i]
        if stop and c == stop:
            return i + 1
        if c in " \t\n":
            i += 1
        elif c == "{":
            i = parse_math(s, i + 1, va, style, out, "}")
        elif c in "^_":
            nva = "sup" if c == "^" else "sub"
            sub: list = []
            j = i + 1
            while s[j] == " ":
                j += 1
            if s[j] == "{":
                j = parse_math(s, j + 1, nva, style, sub, "}")
            elif s[j] == "\\":
                j = math_cmd(s, j, nva, style, sub)
            else:
                parse_math(s[j], 0, nva, style, sub)
                j += 1
            if va is not None:                                 # a script inside a script: Unicode super- / subscript digits
                table = SUPER if nva == "sup" else SUB
                sub = [(t.translate(table), k, va) for t, k, _ in sub]
            out.extend(sub)
            i = j
        elif c == "\\":
            i = math_cmd(s, i, va, style, out)
        elif c.isalpha():
            out.append(letter(c, style, va))
            i += 1
        elif c.isdigit() or c == ".":
            out.append((c, "bf" if style in ("bf", "bfit") else "rm", va))
            i += 1
        elif c == "-":
            out.append(("−", "op", va))
            i += 1
        elif c == "'":
            out.append(("′", "rm", va))
            i += 1
        else:
            out.append((c, "op" if c in "=<>+" else "rm", va))
            i += 1
    return i


def letter(c: str, style: str, va):
    if style == "cal":
        return (CAL.get(c, c), "sym", va)
    if style == "bb":
        return (BB.get(c, c), "sym", va)
    return (c, {"rm": "rm", "bf": "bf", "bfit": "bfit"}.get(style, "it"), va)


def math_cmd(s: str, i: int, va, style: str, out: list) -> int:
    m = re.match(r"\\([A-Za-z]+|.)", s[i:])
    name = m.group(1)
    i += m.end()
    if name in GREEK:
        g = GREEK[name]
        kind = ("bfit" if g.islower() else "bf") if style in ("bf", "bfit") else ("it" if g.islower() else "rm")
        out.append((g, kind, va))
    elif name in ("mathrm", "text", "textrm", "operatorname", "mathit", "mathbf", "boldsymbol", "mathcal", "mathbb", "textit"):
        arg, i = group(s, i)
        st = {"mathrm": "rm", "text": "rm", "textrm": "rm", "operatorname": "rm", "mathit": "it", "textit": "it", "mathbf": "bf",
              "boldsymbol": "bfit", "mathcal": "cal", "mathbb": "bb"}[name]
        parse_math(arg, 0, va, st, out)
    elif name in ACCENT:
        arg, i = group(s, i)
        tmp: list = []
        parse_math(arg, 0, va, style, tmp)
        t, k, v = tmp[-1]
        tmp[-1] = (t + ACCENT[name], k, v)
        out.extend(tmp)
    elif name == "sqrt":
        arg, i = group(s, i)
        out.append(("√", "sym", va))
        parse_math(arg, 0, va, style, out)
    elif name in ("frac", "binom"):
        a, i = group(s, i)
        b, i = group(s, i)
        ta: list = []
        tb: list = []
        parse_math(a, 0, va, style, ta)
        parse_math(b, 0, va, style, tb)
        if name == "binom":
            out.extend([("C(", "rm", va), *ta, (", ", "rm", va), *tb, (")", "rm", va)])
        else:
            paren = lambda x: [("(", "rm", va), *x, (")", "rm", va)]  # noqa: E731
            num = paren(ta) if any(k == "op" for _, k, _ in ta) else ta
            den = paren(tb) if len(tb) > 1 else tb
            out.extend([*num, ("/", "rm", va), *den])
    elif name in FUNCS:
        out.append((name, "fn", va))
    elif name == "bmod":
        out.append((" mod ", "rm", va))
    elif name == "numcomma":
        out.append((",", "num", va))
    elif name in SKIP_MATH:
        if i < len(s) and s[i] == ".":
            i += 1
    elif name in SPACES:
        out.append((SPACES[name], "rm", va))
    elif name in SYM:
        out.append((SYM[name], "op" if SYM[name] in REL | BIN else "sym", va))
    elif name == "\\":
        pass
    else:
        warnings.append("math command \\" + name)
        out.append((name, "rm", va))
    return i


def math_runs(src: str) -> list[dict]:
    atoms: list = []
    parse_math(src.replace("{,}", "\\numcomma "), 0, None, "it", atoms)       # 88{,}500: a comma inside a number
    spaced: list = []
    nb = "\u00a0"                                            # no line break before an operator, as inside LaTeX math
    fn_pending = False
    for n, (t, k, va) in enumerate(atoms):
        prev = next((a for a in reversed(spaced) if a[0].strip()), None)
        has_next = n + 1 < len(atoms)
        if va is None:
            if fn_pending and k in ("it", "bfit"):           # \ln \delta, \max_k \varepsilon_k: a thin space after the name
                spaced.append(("\u2009", "rm", None))
            fn_pending = k == "fn"
        if va is None and k == "op" and (t in REL or t in BIN):
            unary = t in BIN and (prev is None or prev[0][-1] in "([{,=" or prev[0] in REL | BIN)
            if t in BIN and not (prev and has_next):         # 1.39\times: an operator at the end of a formula
                unary = True
            if not unary:                                    # spaces only between atoms of this formula, not at its ends
                spaced += ([(nb, "rm", None)] if prev else []) + [(t, k, va)] + \
                          ([(" " if t in REL else nb, "rm", None)] if has_next else [])
                continue
        spaced.append((t, k, va))
        if va is None and t == "," and k != "num" and has_next and atoms[n + 1][2] is None:
            spaced.append((" ", "rm", None))
    runs = []
    for t, k, va in spaced:
        r = R(t, va=va)
        if k == "it":
            r["i"] = True
        elif k == "bf":
            r["b"] = True
        elif k == "bfit":
            r["b"] = r["i"] = True
        if any(ch in MATH_FONT_CHARS for ch in t):
            r["font"] = "Cambria Math"
        r["math"] = True                                     # never small caps (the table-head style would turn ε into Ε)
        runs.append(r)
    return runs


# ------------------------------------------------------------------------------------------------------------------ text
class Ctx:
    def __init__(self, labels: dict[str, str], cites: dict[str, int]):
        self.labels, self.cites = labels, cites

    def ref(self, key: str) -> str:
        if key not in self.labels:
            warnings.append("undefined label " + key)
            return "??"
        return self.labels[key]

    def cite(self, keys: str, note: str | None) -> str:
        nums = sorted(self.cites[k.strip()] for k in keys.split(","))
        if note:
            return f"[{nums[0]}, {note}]"
        parts, j = [], 0
        while j < len(nums):
            k = j
            while k + 1 < len(nums) and nums[k + 1] == nums[k] + 1:
                k += 1
            if k - j >= 2:
                parts.append(f"[{nums[j]}]–[{nums[k]}]")
            else:
                parts += [f"[{x}]" for x in nums[j:k + 1]]
            j = k + 1
        return ", ".join(parts)


def text_runs(s: str, ctx: Ctx, fmt: dict | None = None) -> list[dict]:
    fmt = dict(fmt or {})
    out: list[dict] = []
    i = 0
    buf = ""

    def flush():
        nonlocal buf
        if buf:
            out.append(R(buf, **fmt))
            buf = ""

    while i < len(s):
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", s[i:])
            name = m.group(1)
            j = i + m.end()
            if name in ("textit", "emph", "textbf", "texttt", "textsc", "mbox", "textrm", "url", "textnormal"):
                arg, j = group(s, j)
                flush()
                f = dict(fmt)
                f.update({"textit": {"i": True}, "emph": {"i": True}, "textbf": {"b": True}, "texttt": {"mono": True},
                          "textsc": {"sc": True}, "url": {"mono": False}}.get(name, {}))
                out.extend(text_runs(arg, ctx, f))
            elif name == "cite":
                note, j = opt(s, j)
                keys, j = group(s, j)
                buf += ctx.cite(keys, note.replace("~", "\u00a0") if note else None)
            elif name in ("ref", "eqref"):
                key, j = group(s, j)
                buf += f"({ctx.ref(key)})" if name == "eqref" else ctx.ref(key)
            elif name in ("label", "vspace", "hspace"):
                _, j = group(s, j)
            elif name in ("centering", "scriptsize", "footnotesize", "small", "raggedright", "noindent", "relax", "newblock",
                          "BIBentryALTinterwordspacing", "BIBentrySTDinterwordspacing", "par", "arraybackslash", "protect"):
                pass
            elif name == "hskip":
                mm = re.match(r"\s*[\d.]+em(\s+plus\s+[\d.]+em)?(\s+minus\s+[\d.]+em)?\s*\\relax", s[j:])
                j += mm.end() if mm else 0
                buf += " "
            elif name in TEXT_ACCENT and j < len(s):
                arg, j = group(s, j) if s[j] == "{" else (s[j], j + 1)
                buf += unicodedata.normalize("NFC", arg + TEXT_ACCENT[name])
            elif name in ("ldots", "dots"):
                buf += "…"
            elif name == "yes":
                flush()
                out.append(R("✓", **fmt, font="Segoe UI Symbol"))
            elif name == "no":
                flush()
                out.append(R("✗", **fmt, font="Segoe UI Symbol"))
            elif name == "partly":
                flush()
                out.append(R("∘", **fmt, font="Cambria Math"))
            elif name in ("%", "&", "_", "#", "$", "{", "}"):
                buf += name
            elif name == ",":
                buf += "\u2009"
            elif name in (" ", "\n"):
                buf += " "
            elif name == "\\":
                buf += " "
            elif name == "textendash":
                buf += "–"
            else:
                warnings.append("text command \\" + name)
            i = j
        elif c == "$":
            j = s.index("$", i + 1)
            flush()
            for r in math_runs(s[i + 1:j]):
                out.append({**fmt, **r})
            i = j + 1
        elif c in "{}":
            i += 1
        elif c == "~":
            buf += "\u00a0"
            i += 1
        elif s.startswith("---", i):
            buf += "—"
            i += 3
        elif s.startswith("--", i):
            buf += "–"
            i += 2
        elif s.startswith("``", i):
            buf += "“"
            i += 2
        elif s.startswith("''", i):
            buf += "”"
            i += 2
        elif c == "`":
            buf += "‘"
            i += 1
        elif c == "'":
            buf += "’"
            i += 1
        elif c in " \t\n":
            if not buf.endswith(" ") and not (not buf and out and out[-1]["t"].endswith(" ")):
                buf += " "
            i += 1
        else:
            buf += c
            i += 1
    flush()
    return out


def trim(runs: list[dict]) -> list[dict]:
    while runs and not runs[0]["t"].strip():
        runs.pop(0)
    while runs and not runs[-1]["t"].strip():
        runs.pop()
    if runs:
        runs[0] = {**runs[0], "t": runs[0]["t"].lstrip()}
        runs[-1] = {**runs[-1], "t": runs[-1]["t"].rstrip()}
    return runs


# ------------------------------------------------------------------------------------------------------------------- XML
def run_xml(r: dict) -> str:
    pr = ""
    font = "Courier New" if r.get("mono") else r.get("font")
    if font:
        pr += f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
    if r.get("b"):
        pr += "<w:b/><w:bCs/>"
    if r.get("i"):
        pr += "<w:i/><w:iCs/>"
    if r.get("sc"):
        pr += "<w:smallCaps/>"
    elif r.get("math"):
        pr += '<w:smallCaps w:val="0"/>'
    sz = r.get("sz")
    if r.get("mono") and not sz:
        sz = r.get("monosz")
    if sz:
        pr += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    if r.get("va"):
        pr += f'<w:vertAlign w:val="{"superscript" if r["va"] == "sup" else "subscript"}"/>'
    rpr = f"<w:rPr>{pr}</w:rPr>" if pr else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(r["t"])}</w:t></w:r>'


def para(runs, style=None, ppr_extra="", jc=None, size=None, keep_next=False, sect="") -> str:
    ppr = f'<w:pStyle w:val="{style}"/>' if style else ""
    if keep_next:
        ppr += "<w:keepNext/>"
    ppr += ppr_extra
    if jc:
        ppr += f'<w:jc w:val="{jc}"/>'
    if size:
        ppr += f'<w:rPr><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>'
    ppr += sect
    body = "".join(run_xml({**r, "sz": r.get("sz") or size} if size else r) for r in runs)
    return f"<w:p><w:pPr>{ppr}</w:pPr>{body}</w:p>"


def sect_xml(cols: int, continuous: bool) -> str:
    c = f'<w:cols w:num="2" w:space="360"/>' if cols == 2 else '<w:cols w:space="720"/>'
    t = '<w:type w:val="continuous"/>' if continuous else ""
    return (f'<w:sectPr>{t}<w:pgSz w:w="12240" w:h="15840" w:code="1"/><w:pgMar w:top="1440" w:right="1080" w:bottom="1440" '
            f'w:left="1080" w:header="720" w:footer="720" w:gutter="0"/>{c}<w:docGrid w:linePitch="360"/></w:sectPr>')


class Doc:
    def __init__(self, figs: dict[str, Path]):
        self.parts: list[str] = []
        self.figs = figs
        self.media: list[tuple[str, Path]] = []
        self.pic = 0

    def image(self, key: str, width_tw: int) -> str:
        from PIL import Image

        path = self.figs[key]
        w, h = Image.open(path).size
        cx = width_tw * EMU
        cy = int(cx * h / w)
        self.pic += 1
        rid = f"rIdFig{self.pic}"
        self.media.append((rid, path))
        n = self.pic
        a = "http://schemas.openxmlformats.org/drawingml/2006/main"
        p = "http://schemas.openxmlformats.org/drawingml/2006/picture"
        return (f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
                f'<wp:docPr id="{100 + n}" name="Figure {n}"/><wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="{a}" '
                f'noChangeAspect="1"/></wp:cNvGraphicFramePr><a:graphic xmlns:a="{a}"><a:graphicData uri="{p}"><pic:pic '
                f'xmlns:pic="{p}"><pic:nvPicPr><pic:cNvPr id="{100 + n}" name="{path.name}"/><pic:cNvPicPr/></pic:nvPicPr>'
                f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr>'
                f'<a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/>'
                f'</a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')


# ---------------------------------------------------------------------------------------------------------------- blocks
ENV_RE = re.compile(r"\\(section\*?|subsection)\s*\{|\\begin\{(itemize|enumerate|equation|table|figure\*?|abstract|IEEEkeywords)\}")


def find_end(s: str, i: int, env: str) -> tuple[int, int]:
    depth, j = 1, i
    pat = re.compile(r"\\(begin|end)\{" + re.escape(env) + r"\}")
    for m in pat.finditer(s, i):
        depth += 1 if m.group(1) == "begin" else -1
        if depth == 0:
            return m.start(), m.end()
    raise ValueError("no end of " + env)


def split_paras(text: str, cont_first: bool):
    chunks = re.split(r"\n\s*\n", text)
    out = []
    for n, ch in enumerate(chunks):
        if ch.strip():
            out.append(("p", ch, cont_first and n == 0))
    return out


def blocks(text: str):
    """Block list of one chapter: ('h1'|'h2'|'h5', title), ('p', text, continues), ('eq', label), ('list', kind, items),
    ('table', body), ('figure', body, wide), ('abstract', text), ('keywords', text)."""
    out = []
    i, cont = 0, False
    while True:
        m = ENV_RE.search(text, i)
        pre = text[i:m.start() if m else len(text)]
        out += split_paras(pre, cont)
        cont = False
        if not m:
            return out
        if m.group(1):
            title, j = group(text, m.end() - 1)
            out.append(("h5" if m.group(1) == "section*" else "h1" if m.group(1) == "section" else "h2", title))
            lab = re.match(r"\s*\\label\{[^}]*\}", text[j:])
            i = j + (lab.end() if lab else 0)
            continue
        env = m.group(2)
        a, b = find_end(text, m.end(), env)
        body = text[m.end():a]
        if env == "equation":
            out.append(("eq", re.search(r"\\label\{([^}]*)\}", body).group(1)))
            cont = not re.match(r"[ \t]*\n[ \t]*\n", text[b:])
        elif env in ("itemize", "enumerate"):
            items = [it for it in re.split(r"\\item\s", body)[1:]]
            out.append(("list", env, items))
        elif env == "table":
            out.append(("table", body))
        elif env.startswith("figure"):
            out.append(("figure", body, env == "figure*"))
        else:
            out.append((env, body))
        i = b


# ---------------------------------------------------------------------------------------------------------------- tables
def split_top(s: str, sep: str) -> list[str]:
    parts, depth, cur, i = [], 0, "", 0
    while i < len(s):
        if s[i] == "\\" and s.startswith(sep, i) and depth == 0 and sep == "\\\\":
            parts.append(cur)
            cur = ""
            i += 2
            continue
        if s[i] == "\\":
            cur += s[i:i + 2]
            i += 2
            continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
        if s[i] == sep and depth == 0 and sep != "\\\\":
            parts.append(cur)
            cur = ""
        else:
            cur += s[i]
        i += 1
    parts.append(cur)
    return parts


def col_spec(spec: str) -> list[str]:
    spec = re.sub(r">\{[^}]*\}", "", spec)
    spec = re.sub(r"p\{[^}]*\}", "X", spec)
    return [c for c in spec if c in "lcrX"]


def table_xml(body: str, ctx: Ctx, doc: Doc) -> str:
    cap = re.search(r"\\caption\{", body)
    caption, _ = group(body, cap.end() - 1)
    m = re.search(r"\\begin\{(tabularx?)\}", body)
    env = m.group(1)
    j = m.end()
    if env == "tabularx":
        _, j = group(body, j)
    spec, j = group(body, j)
    a, b = find_end(body, j, env)
    tab, after = body[j:a], body[b:]
    cols = col_spec(spec)
    note = re.search(r"\\parbox\{\\columnwidth\}\{", after)
    note_text = group(after, note.end() - 1)[0] if note else None

    rows, rule_before, shade = [], [], []                   # rule_before: booktabs rule above each row ('top', 'mid' or None)
    pending_rule = "top"
    for raw in split_top(tab, "\\\\"):
        line = raw.strip()
        while True:
            mm = re.match(r"\\(toprule|midrule|bottomrule)\s*", line)
            if not mm:
                break
            pending_rule = {"toprule": "top", "midrule": "mid", "bottomrule": None}[mm.group(1)]
            line = line[mm.end():].strip()
        sh = re.match(r"\\rowcolor\{[^}]*\}\s*", line)
        if sh:
            line = line[sh.end():]
        if not line.strip():
            continue
        cells = []
        for cell in split_top(line, "&"):
            cell = cell.strip()
            span, merge = 1, None
            mc = re.match(r"\\multicolumn\{(\d+)\}", cell)
            if mc:
                span = int(mc.group(1))
                _, k = group(cell, mc.end())
                cell, _ = group(cell, k)
            mr = re.match(r"\\multirow\{(\d+)\}\{[^}]*\}", cell)
            if mr:
                merge = int(mr.group(1))
                cell, _ = group(cell, mr.end())
            cells.append({"text": cell, "span": span, "merge": merge})
        rows.append(cells)
        rule_before.append(pending_rule)
        shade.append(bool(sh))
        pending_rule = None

    # column widths from the visible length of the cells (spanning cells excluded)
    def vis(t: str) -> int:
        return len("".join(r["t"] for r in text_runs(t, ctx)))

    nat = [0] * len(cols)
    for cells in rows:
        k = 0
        for c in cells:
            if c["span"] == 1:
                nat[k] = max(nat[k], vis(c["text"]))
            k += c["span"]
    tw = [n * 74 + 140 for n in nat]                        # 8 pt Times: about 74 twips per character, plus cell margins
    if "X" in cols:
        fixed = sum(w for w, c in zip(tw, cols) if c != "X")
        nx = cols.count("X")
        for k, c in enumerate(cols):
            if c == "X":
                tw[k] = max(900, (COL_W - fixed) // nx)
    total = sum(tw)
    if total > COL_W:
        tw = [w * COL_W // total for w in tw]
    total = sum(tw)

    def border(kind: str | None) -> str:
        return {"top": '<w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>',
                "mid": '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'}.get(kind or "", "")

    # widths are a first guess: scripts/finish_docx.ps1 lets Word fit every table to its content and then to the column
    xml = [f'<w:tbl><w:tblPr><w:tblW w:w="{total}" w:type="dxa"/><w:jc w:val="center"/>'
           f'<w:tblCellMar><w:left w:w="50" w:type="dxa"/><w:right w:w="50" w:type="dxa"/></w:tblCellMar>'
           f'<w:tblLook w:val="0000"/></w:tblPr><w:tblGrid>' + "".join(f'<w:gridCol w:w="{w}"/>' for w in tw) + "</w:tblGrid>"]
    open_merge: dict[int, int] = {}
    for r, cells in enumerate(rows):
        last = r == len(rows) - 1
        xml.append(f'<w:tr><w:trPr><w:cantSplit/>{"<w:tblHeader/>" if r == 0 else ""}</w:trPr>')
        k = 0
        for c in cells:
            w = sum(tw[k:k + c["span"]])
            b = border(rule_before[r])
            if last:
                b += '<w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
            vm = ""
            if c["merge"]:
                vm = '<w:vMerge w:val="restart"/>'
                open_merge[k] = c["merge"] - 1
            elif open_merge.get(k):
                vm = "<w:vMerge/>"
                open_merge[k] -= 1
            shd = '<w:shd w:val="clear" w:color="auto" w:fill="E6E6E6"/>' if shade[r] else ""
            span = f'<w:gridSpan w:val="{c["span"]}"/>' if c["span"] > 1 else ""
            jc = {"l": "left", "c": "center", "r": "right", "X": "left"}[cols[k]] if c["span"] == 1 else "both"
            runs = trim(text_runs(c["text"], ctx))
            sz = NOTE_PT * 2 if c["span"] > 1 else TABLE_PT * 2
            xml.append(f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{span}{vm}<w:tcBorders>{b}</w:tcBorders>{shd}'
                       f'<w:vAlign w:val="center"/></w:tcPr>'
                       + para(runs if not vm.endswith("<w:vMerge/>") else [], "tablecopy", jc=jc, size=sz, keep_next=True)
                       + "</w:tc>")                         # keepNext in every row: the table stays in one piece with its note
            k += c["span"]
        xml.append("</w:tr>")
    xml.append("</w:tbl>")
    cap_xml = para(trim(text_runs(caption, ctx)), "tablehead", keep_next=True)
    note_xml = ""
    if note_text:
        note_xml = para(trim(text_runs(note_text, ctx)), None, jc="both", size=NOTE_PT * 2,
                        ppr_extra='<w:spacing w:before="40" w:after="160"/>')
    else:
        note_xml = para([], None, size=8, ppr_extra='<w:spacing w:before="0" w:after="120"/>')
    return cap_xml + "".join(xml) + note_xml


# ---------------------------------------------------------------------------------------------------------------- figures
FIGMAP = {"fig1_architecture": "fig1", "Fig2": "fig2", "Fig3_python": "fig3", "Fig4_python": "fig4"}


def figure_xml(body: str, ctx: Ctx, doc: Doc, wide: bool, fig2_one_column: bool) -> tuple[str, bool]:
    m = re.search(r"graphics/paper/([A-Za-z0-9_]+)", body)
    key = FIGMAP[m.group(1)]
    cap = re.search(r"\\caption\{", body)
    caption, _ = group(body, cap.end() - 1)
    if key == "fig2" and fig2_one_column:
        wide = False
    width = TEXT_W if wide else COL_W
    img = para([], None, jc="center", keep_next=True, ppr_extra='<w:spacing w:before="60" w:after="0"/>').replace(
        "</w:pPr>", "</w:pPr>" + doc.image(key, width))
    return img + "\n@@CAPTION@@" + para(trim(text_runs(caption, ctx)), "figurecaption"), wide


# ------------------------------------------------------------------------------------------------------------------ main
def load_labels(aux: Path) -> dict[str, str]:
    """Label -> printed number from the last LaTeX build (subsections are written as \\mbox {III-A})."""
    t = aux.read_text(encoding="utf-8", errors="replace")
    return {k: (mb or v) for k, v, mb in re.findall(r"\\newlabel\{([^}]+)\}\{\{(\\mbox\s*\{([^}]*)\}|[^}]*)\}", t)}


def load_bib(bbl: Path) -> list[tuple[str, str]]:
    t = bbl.read_text(encoding="utf-8")
    t = t[t.index("\\bibitem"):t.index("\\end{thebibliography}")]
    items = re.split(r"\\bibitem\{([^}]+)\}", t)[1:]
    return [(items[k], items[k + 1].strip()) for k in range(0, len(items), 2)]


def author_table(ctx: Ctx, main: str) -> str:
    blk = main[main.index("\\author{"):main.index("\\begin{document}")]
    names = re.findall(r"\\IEEEauthorblockN\{([^}]*)\}", blk)
    affs = [group(blk, m.end() - 1)[0] for m in re.finditer(r"\\IEEEauthorblockA\{", blk)]
    cells = []
    for n, a in zip(names, affs):
        lines = [x.strip() for x in a.split("\\\\")]
        ps = para(trim(text_runs(n, ctx)), "Author", ppr_extra='<w:spacing w:before="0" w:after="20"/>', size=21)
        ps += "".join(para(trim(text_runs(x, ctx)), "Affiliation", size=18) for x in lines)
        cells.append(ps)
    ncol = 4                                                 # eight authors in two rows of four (LaTeX: 3 + 2 + 3)
    w = TEXT_W // ncol
    xml = [f'<w:tbl><w:tblPr><w:tblW w:w="{w * ncol}" w:type="dxa"/><w:jc w:val="center"/><w:tblLayout w:type="fixed"/>'
           f'<w:tblCellMar><w:top w:w="160" w:type="dxa"/><w:left w:w="0" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/>'
           f'<w:right w:w="0" w:type="dxa"/></w:tblCellMar>'      # top / bottom margins: gaps above, between and below the rows
           f'<w:tblLook w:val="0000"/></w:tblPr><w:tblGrid>' + f'<w:gridCol w:w="{w}"/>' * ncol + "</w:tblGrid>"]
    for r in range(0, len(cells), ncol):
        xml.append("<w:tr><w:trPr><w:cantSplit/></w:trPr>")
        for c in cells[r:r + ncol]:
            xml.append(f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/></w:tcPr>{c}</w:tc>')
        xml.append("</w:tr>")
    xml.append("</w:tbl>")
    return "".join(xml)


def build(args) -> None:
    labels = load_labels(ROOT / "main.aux")
    bib = load_bib(ROOT / "main.bbl")
    ctx = Ctx(labels, {k: n + 1 for n, (k, _) in enumerate(bib)})
    main = strip_comments((ROOT / "main.tex").read_text(encoding="utf-8"))
    work = Path(args.work)
    figs = {"fig1": work / "fig1_crop.png", "fig2": work / "fig2_crop.png", "fig3": work / "Fig3_python.png",
            "fig4": work / "Fig4_python.png"}
    doc = Doc(figs)
    title, _ = group(main, main.index("\\title{") + 6)
    out = [para(text_runs(title, ctx), "papertitle"), author_table(ctx, main),
           para([], None, size=4, ppr_extra='<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="exact"/>',
                sect=sect_xml(1, False))]                    # a 12 pt line: the gap between the authors and both columns

    text = "\n\n".join(strip_comments((ROOT / "chapters" / "main" / f"{c}.tex").read_text(encoding="utf-8")) for c in CHAPTERS)
    text += "\n\n" + strip_comments((ROOT / "chapters" / "front" / "thanks.tex").read_text(encoding="utf-8"))
    blist = blocks(text)
    eq_n = 0
    pending: list[list] = []                                 # deferred floats: [paragraphs still to wait for, xml]

    def flush(all_: bool) -> None:
        for item in list(pending):
            if all_ or item[0] <= 0:
                out.append(item[1])
                pending.remove(item)

    def place(label: str | None, xml: str) -> None:
        n = DEFER.get(label or "", 0)
        if n > 0:
            pending.append([n, xml])
        else:
            out.append(xml)

    for bl in blist:
        kind = bl[0]
        if kind == "abstract":
            out.append(para([R("Abstract", i=True), R("—")] + trim(text_runs(bl[1], ctx)), "Abstract"))
        elif kind == "IEEEkeywords":
            out.append(para([R("Keywords—", i=True)] + trim(text_runs(bl[1], ctx)), "keywords"))
        elif kind in ("h1", "h2", "h5"):
            flush(True)                                      # a deferred float stays in its own subsection
            style = {"h1": "Heading1", "h2": "Heading2", "h5": "Heading5"}[kind]
            out.append(para(trim(text_runs(bl[1], ctx)), style, keep_next=True))
        elif kind == "p":
            runs = trim(text_runs(bl[1], ctx))
            if runs:
                out.append(para(runs, "BodyText", ppr_extra='<w:ind w:firstLine="0"/>' if bl[2] else ""))
                for item in pending:
                    item[0] -= 1
                flush(False)
        elif kind == "eq":
            eq_n += 1
            lin = EQUATIONS[bl[1]] + f"#({labels[bl[1]]})"
            out.append('<w:p><w:pPr><w:spacing w:before="60" w:after="60"/><w:jc w:val="center"/></w:pPr><m:oMathPara><m:oMath>'
                       f'<m:r><m:t>{escape(lin)}</m:t></m:r></m:oMath></m:oMathPara></w:p>')
        elif kind == "list":
            numbered = bl[1] == "enumerate"
            for n, item in enumerate(bl[2], 1):
                sub = blocks(item)
                first = True
                for sb in sub:
                    if sb[0] == "p":
                        runs = trim(text_runs(sb[1], ctx))
                        if first:
                            if numbered:
                                out.append(para([R(f"{n})\t")] + runs, "bulletlist",
                                                ppr_extra='<w:numPr><w:ilvl w:val="0"/><w:numId w:val="0"/></w:numPr>'
                                                          '<w:ind w:left="360" w:hanging="360"/>'))
                            else:
                                out.append(para(runs, "bulletlist"))
                            first = False
                        else:
                            left = 360 if numbered else 648
                            out.append(para(runs, "BodyText", ppr_extra=f'<w:ind w:left="{left}" w:firstLine="0"/>'))
                    elif sb[0] == "eq":
                        lin = EQUATIONS[sb[1]] + f"#({labels[sb[1]]})"
                        out.append('<w:p><w:pPr><w:spacing w:before="60" w:after="60"/><w:jc w:val="center"/></w:pPr>'
                                   f'<m:oMathPara><m:oMath><m:r><m:t>{escape(lin)}</m:t></m:r></m:oMath></m:oMathPara></w:p>')
        elif kind == "table":
            lab = re.search(r"\\label\{([^}]*)\}", bl[1])
            place(lab.group(1) if lab else None, table_xml(bl[1], ctx, doc))
        elif kind == "figure":
            xml, wide = figure_xml(bl[1], ctx, doc, bl[2], args.fig2_one_column)
            img, cap = xml.split("\n@@CAPTION@@")
            lab = re.search(r"\\label\{([^}]*)\}", bl[1])
            if not wide and lab and DEFER.get(lab.group(1)):
                place(lab.group(1), img + cap)
            elif wide:
                # close the two-column section with an empty one-point paragraph (a section break inside a justified
                # paragraph would stretch its last line), then put the figure and its caption in a one-column section
                out.append(para([], None, size=2, ppr_extra='<w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/>',
                                sect=sect_xml(2, True)))
                out.append(img)
                out.append(cap.replace("</w:pPr>", sect_xml(1, True) + "</w:pPr>", 1))
            else:
                out += [img, cap]
    flush(True)
    out.append(para([R("References")], "Heading5", keep_next=True))
    for _, t in bib:
        out.append(para(trim(text_runs(t, ctx)), "references"))
    # a continuous section break after the references balances the two columns of the last page, as in LaTeX
    out.append(para([], None, size=2, ppr_extra='<w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/>',
                    sect=sect_xml(2, True)))
    body = "".join(out) + sect_xml(1, True)
    write_docx(Path(args.template), Path(args.out), body, doc)
    if warnings:
        print("WARNINGS:", *sorted(set(warnings)), sep="\n  ")
    print("written:", args.out, f"({eq_n} equations, {doc.pic} figures, {len(bib)} references)")


def write_docx(template: Path, out: Path, body: str, doc: Doc) -> None:
    with zipfile.ZipFile(template) as z:
        files = {n: z.read(n) for n in z.namelist()}
    d = files["word/document.xml"].decode("utf-8")
    head = d[:d.index("<w:body>") + len("<w:body>")]
    files["word/document.xml"] = (head + body + "</w:body></w:document>").encode("utf-8")
    rels = files["word/_rels/document.xml.rels"].decode("utf-8")
    rels = re.sub(r'<Relationship [^>]*relationships/image"[^>]*/>', "", rels)
    rels = re.sub(r'<Relationship [^>]*Target="media/[^"]*"[^>]*/>', "", rels)
    for name in [n for n in files if n.startswith("word/media/")]:
        del files[name]
    add = "".join(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
                  f'Target="media/{rid}.png"/>' for rid, _ in doc.media)
    files["word/_rels/document.xml.rels"] = rels.replace("</Relationships>", add + "</Relationships>").encode("utf-8")
    for rid, path in doc.media:
        files[f"word/media/{rid}.png"] = path.read_bytes()
    ct = files["[Content_Types].xml"].decode("utf-8")
    if 'Extension="png"' not in ct:
        ct = ct.replace("<Default ", '<Default Extension="png" ContentType="image/png"/><Default ', 1)
    files["[Content_Types].xml"] = ct.encode("utf-8")
    core = files.get("docProps/core.xml")
    if core:
        c = core.decode("utf-8")
        c = re.sub(r"<dc:title>.*?</dc:title>", "<dc:title>PP-FedData</dc:title>", c)
        c = re.sub(r"<dc:creator>.*?</dc:creator>", "<dc:creator>PP-FedData team</dc:creator>", c)
        files["docProps/core.xml"] = c.encode("utf-8")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for n, data in files.items():
            z.writestr(n, data)


def prepare_figures(work: Path) -> None:
    """PNG copies of the figures in `work`: Fig. 1-2 rendered from their PDFs by Windows and cropped to the drawing,
    Fig. 3-4 redrawn at 600 dpi by make_paper_figures.py from the results of the PP-FedData repository."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from PIL import Image, ImageOps

    work.mkdir(parents=True, exist_ok=True)
    for src, name in (("fig1_architecture.pdf", "fig1"), ("Fig2.pdf", "fig2")):
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(ROOT / "scripts" / "pdf_to_png.ps1"),
                        "-In", str(ROOT / "graphics" / "paper" / src), "-Out", str(work / f"{name}.png"), "-Dpi", "600"], check=True)
        im = Image.open(work / f"{name}.png").convert("RGB")
        x0, y0, x1, y1 = ImageOps.invert(im).getbbox()          # bounding box of the non-white drawing
        pad = 30
        im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad))).save(
            work / f"{name}_crop.png", dpi=(600, 600))
    sys.path.insert(0, str(ROOT / "scripts"))
    import make_paper_figures as mpf

    orig = plt.Figure.savefig
    plt.Figure.savefig = lambda self, fname, *a, **k: orig(self, work / (Path(fname).stem + ".png"), dpi=600)
    try:
        mpf.style()
        rows, refs = mpf.load(ROOT.parent / "results")
        mpf.fig3(rows, refs, work, [])
        mpf.fig4(rows, work, [])
    finally:
        plt.Figure.savefig = orig


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--template", required=True, help="the conference template saved as .docx")
    ap.add_argument("--work", required=True, help="folder with fig1_crop.png, fig2_crop.png, Fig3_python.png, Fig4_python.png")
    ap.add_argument("--prepare-figures", action="store_true", help="first (re)make those PNG files in --work")
    ap.add_argument("--out", default=str(ROOT / "PPFedData.docx"))
    ap.add_argument("--fig2-two-columns", dest="fig2_one_column", action="store_false",
                    help="keep Fig. 2 across both columns as in LaTeX (default: one column, cropped)")
    a = ap.parse_args()
    if a.prepare_figures:
        prepare_figures(Path(a.work))
    build(a)


if __name__ == "__main__":
    sys.exit(main())
