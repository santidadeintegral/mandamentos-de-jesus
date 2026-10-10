#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baixa as fontes e gera os arquivos intermediários em dados/:

  6?-??-morphgnt.txt         SBLGNT + morfologia (MorphGNT) dos quatro Evangelhos
  web_usfm/                  World English Bible (USFM) — marcador \\wj = palavras de Jesus
  strongs-greek-dictionary.js dicionário de Strong (Open Scriptures)
  web_redletter.json         por versículo: texto dentro/fora da fala de Jesus + números de Strong
  imperativos_brutos.json    todos os verbos no imperativo, com falante estimado
  complemento_subjuntivo.json  proibições μή + subjuntivo aoristo (2ª p.) nas falas de Jesus (bruto, para curadoria)

Uso: python3 preparar_dados.py
"""
import collections
import glob
import json
import os
import re
import subprocess
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D = ROOT / "dados"
D.mkdir(exist_ok=True)
os.chdir(D)

BOOKS = [("61-Mt", "MAT", "Mt"), ("62-Mk", "MRK", "Mk"), ("63-Lk", "LUK", "Lk"), ("64-Jn", "JHN", "Jn")]


def fetch():
    for mg, _, _ in BOOKS:
        f = f"{mg}-morphgnt.txt"
        if not Path(f).exists():
            subprocess.run(["curl", "-sS", "-L", "-o", f, f"https://raw.githubusercontent.com/morphgnt/sblgnt/master/{f}"], check=True)
    if not Path("web_usfm").exists():
        subprocess.run(["curl", "-sS", "-L", "-o", "eng-web_usfm.zip", "https://ebible.org/Scriptures/eng-web_usfm.zip"], check=True)
        subprocess.run(["unzip", "-o", "-q", "eng-web_usfm.zip", "-d", "web_usfm"], check=True)
    if not Path("strongs-greek-dictionary.js").exists():
        subprocess.run(["curl", "-sS", "-L", "-o", "strongs-greek-dictionary.js",
                        "https://raw.githubusercontent.com/openscriptures/strongs/master/greek/strongs-greek-dictionary.js"], check=True)


def redletter():
    out = {}
    for _, code, ab in BOOKS:
        f = glob.glob(f"web_usfm/*{code}*.usfm")[0]
        txt = open(f, encoding="utf-8").read()
        chap = verse = 0
        in_wj = False
        cur = collections.defaultdict(lambda: {"in": [], "out": []})
        for m in re.finditer(r"\\c (\d+)|\\v (\d+)|\\(\+?)([a-z]+\*?)|([^\\]+)", txt):
            c, v, plus, mk, text = m.groups()
            if c:
                chap, verse, in_wj = int(c), 0, False
                continue
            if v:
                verse = int(v)
                continue
            if mk:
                if mk == "wj":
                    in_wj = True
                elif mk == "wj*":
                    in_wj = False
                continue
            if text and chap and verse:
                cur[(chap, verse)]["in" if in_wj else "out"].append(text)

        def clean(parts):
            s = " ".join(parts)
            strongs = re.findall(r'strong="G(\d+)"', s)
            s = re.sub(r'\|strong="G\d+"', "", s)
            return re.sub(r"\s+", " ", s).strip(), strongs

        for (c, v), d in cur.items():
            si, sti = clean(d["in"])
            so, sto = clean(d["out"])
            out[f"{ab} {c}:{v}"] = {"wj": si, "nowj": so, "strongs_wj": sti, "strongs_nowj": sto}
    json.dump(out, open("web_redletter.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    return out


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return s.lower().replace("ς", "σ")


def imperativos(red):
    js = open("strongs-greek-dictionary.js", encoding="utf-8").read()
    sd = json.loads(js[js.index("{"): js.rindex("}") + 1])
    lem2str = collections.defaultdict(set)
    for k, v in sd.items():
        lem2str[norm(v["lemma"])].add(k[1:])
    TENSE = {"P": "presente", "A": "aoristo", "F": "futuro", "X": "perfeito", "Y": "mais-que-perfeito", "I": "imperfeito"}
    VOICE = {"A": "ativa", "M": "média", "P": "passiva"}
    rows, subj = [], []
    NEG = {"μή", "μηδέ", "μηδείς", "μηκέτι", "μήποτε"}
    for mg, _, book in BOOKS:
        verses = collections.defaultdict(list)
        for line in open(f"{mg}-morphgnt.txt", encoding="utf-8"):
            ref, pos, parse, text, word, nrm, lemma = line.rstrip("\n").split(" ")
            verses[ref].append((pos, parse, text, lemma))
        for ref, toks in verses.items():
            key = f"{book} {int(ref[2:4])}:{int(ref[4:6])}"
            gk = " ".join(t[2] for t in toks)
            r = red.get(key, {"wj": "", "nowj": "", "strongs_wj": [], "strongs_nowj": []})
            for i, (pos, parse, text, lemma) in enumerate(toks):
                if not pos.startswith("V"):
                    continue
                # parse: pessoa, tempo, voz, modo, caso, número, gênero, grau
                if parse[3] == "D":
                    st = lem2str.get(norm(lemma), set())
                    in_wj = bool(st & set(r["strongs_wj"]))
                    in_out = bool(st & set(r["strongs_nowj"]))
                    if not r["wj"]:
                        speaker = "outro"
                    elif in_wj and not in_out:
                        speaker = "Jesus"
                    elif in_out and not in_wj:
                        speaker = "outro"
                    elif not r["nowj"].strip():
                        speaker = "Jesus"
                    else:
                        speaker = "revisar"
                    rows.append(dict(ref=key, book=book, form=text, lemma=lemma, person=parse[0], tense=TENSE[parse[1]],
                                     voice=VOICE[parse[2]], number=parse[5], strongs=sorted(st), speaker=speaker,
                                     wj=r["wj"], nowj=r["nowj"], greek=gk))
                elif parse[3] == "S" and parse[1] == "A" and parse[0] == "2" and r["wj"]:
                    if NEG & {t[3] for t in toks[max(0, i - 4):i]}:
                        subj.append(dict(ref=key, form=text, lemma=lemma, number=parse[5], wj=r["wj"][:120]))
    json.dump(rows, open("imperativos_brutos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    json.dump(subj, open("complemento_subjuntivo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    c = collections.Counter(x["speaker"] for x in rows)
    print("imperativos:", len(rows), dict(c), "| proibições subj.:", len(subj))


if __name__ == "__main__":
    fetch()
    imperativos(redletter())
