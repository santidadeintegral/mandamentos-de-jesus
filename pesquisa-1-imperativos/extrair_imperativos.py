#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pesquisa 1 — extrai todos os verbos no modo imperativo dos Evangelhos com falante estimado.

Lê comum/dados (MorphGNT, letras vermelhas da WEB, Strong's) e grava em dados/:
  imperativos_brutos.json        todos os imperativos, com falante (Jesus / outro / revisar)
  complemento_subjuntivo.json    proibições μή + subjuntivo aoristo (2ª p.) nas falas de Jesus (bruto, p/ curadoria)

Uso: python3 pesquisa-1-imperativos/extrair_imperativos.py
"""
import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "comum"))
from biblia import TENSE, VOICE, morph_verses, norm, redletter, strongs_by_lemma  # noqa: E402

NEG = {"μή", "μηδέ", "μηδείς", "μηκέτι", "μήποτε"}


def main():
    red = redletter()
    lem2str = strongs_by_lemma()
    rows, subj = [], []
    for key, toks in morph_verses().items():
        book = key.split(" ")[0]
        gk = " ".join(t[2] for t in toks)
        r = red.get(key, {"wj": "", "nowj": "", "strongs_wj": [], "strongs_nowj": []})
        for i, (pos, parse, text, lemma) in enumerate(toks):
            if not pos.startswith("V"):
                continue
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
    (HERE / "dados").mkdir(exist_ok=True)
    json.dump(rows, open(HERE / "dados" / "imperativos_brutos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    json.dump(subj, open(HERE / "dados" / "complemento_subjuntivo.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("imperativos:", len(rows), dict(collections.Counter(x["speaker"] for x in rows)), "| proibições subj.:", len(subj))


if __name__ == "__main__":
    main()
