#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baixa as fontes comuns às pesquisas e gera os arquivos intermediários em comum/dados/:

  6?-??-morphgnt.txt           SBLGNT + morfologia (MorphGNT) dos quatro Evangelhos
  web_usfm/                    World English Bible (USFM) — marcador \\wj = palavras de Jesus
  strongs-greek-dictionary.js  dicionário de Strong (Open Scriptures)
  web_redletter.json           por versículo: texto dentro/fora da fala de Jesus + números de Strong

Uso: python3 comum/preparar_dados.py
As pesquisas usam `comum/biblia.py` para ler esses arquivos.
"""
import collections
import json
import os
import re
import subprocess
from pathlib import Path

D = Path(__file__).resolve().parent / "dados"
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
    import glob
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
    print("versículos:", len(out), "| com fala de Jesus:", sum(1 for v in out.values() if v["wj"]))


if __name__ == "__main__":
    fetch()
    redletter()
