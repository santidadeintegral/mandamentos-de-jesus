# -*- coding: utf-8 -*-
"""Acesso aos dados comuns (grego MorphGNT, letras vermelhas da WEB, Strong's) e utilitários de referência."""
import collections
import json
import unicodedata
from pathlib import Path

D = Path(__file__).resolve().parent / "dados"
BOOKS = [("61-Mt", "MAT", "Mt"), ("62-Mk", "MRK", "Mk"), ("63-Lk", "LUK", "Lk"), ("64-Jn", "JHN", "Jn")]
BOOK_PT = {"Mt": "Mt", "Mk": "Mc", "Lk": "Lc", "Jn": "Jo"}
BOOK_ORDER = {"Mt": 1, "Mk": 2, "Lk": 3, "Jn": 4}
TENSE = {"P": "presente", "A": "aoristo", "F": "futuro", "X": "perfeito", "Y": "mais-que-perfeito", "I": "imperfeito"}
VOICE = {"A": "ativa", "M": "média", "P": "passiva"}
MOOD = {"I": "indicativo", "D": "imperativo", "S": "subjuntivo", "O": "optativo", "N": "infinitivo", "P": "particípio"}


def ref_key(ref):
    b, cv = ref.split(" ")
    c, v = cv.split(":")
    return (BOOK_ORDER[b], int(c), int(v.split("-")[0]))


def ref_pt(ref):
    b, cv = ref.split(" ")
    return f"{BOOK_PT[b]} {cv}"


def redletter():
    return json.load(open(D / "web_redletter.json", encoding="utf-8"))


def morph_verses():
    """{ 'Mt 5:3': [(pos, parse, text, lemma), ...] } — parse = pessoa,tempo,voz,modo,caso,número,gênero,grau."""
    out = collections.OrderedDict()
    for mg, _, book in BOOKS:
        for line in open(D / f"{mg}-morphgnt.txt", encoding="utf-8"):
            ref, pos, parse, text, word, nrm, lemma = line.rstrip("\n").split(" ")
            out.setdefault(f"{book} {int(ref[2:4])}:{int(ref[4:6])}", []).append((pos, parse, text, lemma))
    return out


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return s.lower().replace("ς", "σ")


def strongs_by_lemma():
    js = open(D / "strongs-greek-dictionary.js", encoding="utf-8").read()
    sd = json.loads(js[js.index("{"): js.rindex("}") + 1])
    m = collections.defaultdict(set)
    for k, v in sd.items():
        m[norm(v["lemma"])].add(k[1:])
    return m


def jesus_verses():
    """Versículos com fala de Jesus, em ordem canônica: [(ref, texto_wj, texto_fora)]."""
    red = redletter()
    refs = sorted((r for r, v in red.items() if v["wj"]), key=ref_key)
    return [(r, red[r]["wj"], red[r]["nowj"]) for r in refs]
