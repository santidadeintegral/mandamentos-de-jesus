#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Constrói os produtos do projeto "Mandamentos de Jesus" (ONG Santidade Integral em Cristo):

  docs/Mandamentos_de_Jesus.docx/.pdf           — documento final para a prática (categorias priorizadas)
  docs/Projeto_e_Metodologia.docx/.pdf          — definição do projeto, metodologia e critérios
  docs/Observacoes_e_Reflexoes.docx/.pdf        — pontos de atenção metodológicos
  docs/Mandamentos_de_Jesus_Achados.xlsx        — todos os achados, julgamentos e ordenação

Uso: python3 construir.py   (requer dados/ já preparados por preparar_dados.py)
"""
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "dados"))
from timbrado import *  # noqa: E402,F401
from rotulos import ROTULOS  # noqa: E402
from glossario import GLOSSARIO  # noqa: E402
from complemento import COMPLEMENTO  # noqa: E402
from categorias import CATEGORIAS  # noqa: E402

from openpyxl import Workbook  # noqa: E402
from openpyxl.styles import Alignment, Font, PatternFill  # noqa: E402
from openpyxl.utils import get_column_letter  # noqa: E402

DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)
LIGHT_GREY = RGBColor(0x7A, 0x7A, 0x7A)
BOOK_PT = {"Mt": "Mt", "Mk": "Mc", "Lk": "Lc", "Jn": "Jo"}
BOOK_ORDER = {"Mt": 1, "Mk": 2, "Lk": 3, "Jn": 4}
DEST_PT = {"D": "discípulos", "M": "multidão/ouvintes", "I": "indivíduo", "O": "oponentes/autoridades",
           "P": "o Pai (oração)", "N": "natureza/enfermidade/espíritos", "B": "personagem de parábola",
           "C": "citação da Escritura", "E": "fala futura do Juiz", "S": "Satanás", "T": "leitor", "X": "não é Jesus"}
ALC_PT = {"U": "universal", "G": "generalizável", "S": "situacional", "X": "performativo", "B": "parábola",
          "P": "oração de Jesus", "E": "escatológico", "T": "ao leitor", "F": "falso positivo"}
ALC_EXPL = {
    "U": "Mandamento dirigido a discípulos/ouvintes em geral, sem limitação de ocasião: vale para todo cristão.",
    "G": "Ordem dada a pessoa ou ocasião específica, mas cujo princípio Jesus aplica a todos em outros lugares (ex.: 'siga-me').",
    "S": "Ordem presa à circunstância histórica (buscar o jumentinho, preparar a Páscoa, mostrar-se ao sacerdote); não é norma em si.",
    "X": "Palavra de poder: cura, exorcismo ou domínio sobre a natureza. Não é ordem a seres humanos para obedecer.",
    "B": "Imperativo na boca de um personagem de parábola. Não é mandamento direto, mas reforça o tema da categoria.",
    "P": "Jesus falando ao Pai. Serve de modelo de oração, não de ordem aos discípulos.",
    "E": "Sentença proferida pelo Juiz no futuro ('apartem-se de mim'). Não é ordem presente.",
    "T": "Instrução dirigida ao leitor do evangelho ('quem lê, entenda').",
    "F": "A marcação automática atribuiu o versículo a Jesus, mas o imperativo é de outra pessoa.",
}
PESO_COMP, PESO_ENF = 0.5, 1.0
EMINENCIA = {  # promoções explícitas, com a base textual
    "DEUS": "Jesus chama o amor a Deus de 'o grande e primeiro mandamento' (Mt 22:38) e manda 'buscar primeiro' o Reino (Mt 6:33).",
    "AMAR": "'O segundo, semelhante a este… destes dois mandamentos dependem toda a Lei e os Profetas' (Mt 22:39-40); 'mandamento novo' (Jo 13:34).",
    "ARREP": "Primeira palavra da pregação pública de Jesus (Mt 4:17; Mc 1:15): o arrependimento é a porta de todos os outros mandamentos.",
    "FE": "'A obra de Deus é esta: que creiam naquele que ele enviou' (Jo 6:29); 'arrependam-se e creiam' (Mc 1:15) é o par inaugural.",
}


# ----------------------------------------------------------------- dados
def ref_key(ref):
    b, cv = ref.split(" ")
    c, v = cv.split(":")
    return (BOOK_ORDER[b], int(c), int(v))


def ref_pt(ref):
    b, cv = ref.split(" ")
    return f"{BOOK_PT[b]} {cv}"


def load():
    rows = json.load(open(ROOT / "dados" / "imperativos_brutos.json", encoding="utf-8"))
    rows.sort(key=lambda r: ref_key(r["ref"]))
    versos = collections.OrderedDict()
    for r in rows:
        lab = ROTULOS.get(r["ref"])
        if r["speaker"] == "outro" and lab is None:
            continue
        v = versos.setdefault(r["ref"], dict(ref=r["ref"], greek=r["greek"], wj=r["wj"], imps=[], label=lab))
        v["imps"].append(r)
    return rows, versos


def stats(versos):
    st = {c: collections.Counter() for c in CATEGORIAS}
    refs = {c: collections.defaultdict(list) for c in CATEGORIAS}
    for ref, v in versos.items():
        dest, alc, cats, *_ = v["label"]
        for c in cats.split(";"):
            if c in st:
                st[c][alc] += 1
                refs[c][alc].append(ref)
    comp = collections.defaultdict(list)
    for ref, forma, tipo, cats, resumo, just in COMPLEMENTO:
        for c in cats.split(";"):
            comp[c].append(ref)
    score = {}
    for c in CATEGORIAS:
        n_norm = st[c]["U"] + st[c]["G"]
        score[c] = dict(U=st[c]["U"], G=st[c]["G"], norm=n_norm, S=st[c]["S"], B=st[c]["B"],
                        outros=st[c]["P"] + st[c]["E"] + st[c]["T"], comp=len(comp[c]),
                        enf=len(CATEGORIAS[c]["enfases"]),
                        score=n_norm + PESO_COMP * len(comp[c]) + PESO_ENF * len(CATEGORIAS[c]["enfases"]))
    por_contagem = sorted(CATEGORIAS, key=lambda c: (-score[c]["norm"], -score[c]["score"]))
    por_score = sorted(CATEGORIAS, key=lambda c: (-score[c]["score"], -score[c]["norm"]))
    promovidas = ["DEUS", "AMAR", "ARREP", "FE"]
    final = promovidas + [c for c in por_score if c not in promovidas]
    for i, c in enumerate(por_contagem, 1):
        score[c]["pos_contagem"] = i
    for i, c in enumerate(por_score, 1):
        score[c]["pos_score"] = i
    for i, c in enumerate(final, 1):
        score[c]["pos_final"] = i
    return st, refs, comp, score, final


def just_ordenacao(c, sc):
    base = (f"{sc['norm']} passagens normativas (U+G: {sc['U']} universais + {sc['G']} generalizáveis), "
            f"{sc['comp']} ordens no complemento († peso {PESO_COMP}), {sc['enf']} blocos de ênfase (parábolas/discursos, peso {PESO_ENF}) "
            f"→ pontuação {sc['score']:.1f}; posição por contagem bruta {sc['pos_contagem']}º, por pontuação {sc['pos_score']}º.")
    if c in EMINENCIA:
        return base + f" Promovida para {sc['pos_final']}º por eminência explícita: {EMINENCIA[c]}"
    return base + f" Posição final {sc['pos_final']}º (ordem de pontuação, após as quatro categorias promovidas)."


# ----------------------------------------------------------------- XLSX
def xlsx(rows, versos, st, refs, comp, score, final):
    wb = Workbook()
    H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor="2D5130")
    WRAP = Alignment(wrap_text=True, vertical="top")

    def sheet(title, headers, data, widths):
        ws = wb.create_sheet(title)
        ws.append(headers)
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        for c in ws[1]:
            c.font = H; c.fill = HF; c.alignment = WRAP
        for r in data:
            ws.append(list(r))
        for row in ws.iter_rows(min_row=2):
            for c in row:
                c.alignment = WRAP
        ws.freeze_panes = "A2"
        return ws

    wb.remove(wb.active)
    leia = wb.create_sheet("Leia-me")
    leia.column_dimensions["A"].width = 120
    for line in [
        "MANDAMENTOS DE JESUS — ACHADOS, JULGAMENTOS E ORDENAÇÃO (ONG Santidade Integral em Cristo)",
        "",
        "Abas:",
        "1. Imperativos — cada verbo no modo imperativo (análise morfológica SBLGNT/MorphGNT) em versículos com fala de Jesus nos quatro Evangelhos.",
        "2. Versículos — um registro por versículo, com os julgamentos: destinatário, alcance, categoria(s), resumo e justificativa.",
        "3. Categorias — definição de cada grupo, justificativa do agrupamento, correspondência com John Piper e ênfases.",
        "4. Ordenação — contagens, pontuação e justificativa da prioridade de cada categoria.",
        "5. Complemento — ordens de Jesus em formas que não são o imperativo (subjuntivo proibitivo, futuro, infinitivo, ἵνα, condição), marcadas † no documento.",
        "6. Excluídos — imperativos em versículos com fala de Jesus que NÃO são ordens dele (falas de terceiros) ou não são fala de Jesus.",
        "7. Glossário — sentido básico de cada lema grego.",
        "",
        "Códigos de destinatário: " + "; ".join(f"{k} = {v}" for k, v in DEST_PT.items()),
        "Códigos de alcance: " + "; ".join(f"{k} = {v}" for k, v in ALC_PT.items()),
        "",
        "Fonte do grego: SBLGNT com morfologia MorphGNT (CC BY-SA). Marcação das falas de Jesus: World English Bible (USFM, marcador \\wj, domínio público).",
        "Mapeamento grego↔inglês por números de Strong (Open Scriptures, CC BY-SA). Tradução de referência do documento final: Nova Almeida Atualizada (SBB).",
        "Gerado automaticamente por construir.py em " + __import__("datetime").date.today().isoformat() + ".",
    ]:
        leia.append([line])

    data = []
    for r in rows:
        lab = ROTULOS.get(r["ref"])
        if lab is None:
            continue
        dest, alc, cats, resumo, *nota = lab
        data.append((ref_pt(r["ref"]), r["ref"], r["form"].strip("⸀⸁⸂⸃,.·;"), r["lemma"], GLOSSARIO.get(r["lemma"], ""),
                     r["person"] + "ª", "plural" if r["number"] == "P" else "singular", r["tense"], r["voice"],
                     "Jesus" if alc != "F" else "outro", DEST_PT[dest], ALC_PT[alc], cats, resumo, r["wj"], r["greek"]))
    sheet("Imperativos",
          ["Ref. (PT)", "Ref. (código)", "Forma grega", "Lema", "Sentido básico", "Pessoa", "Número", "Tempo", "Voz",
           "Falante", "Destinatário", "Alcance", "Categoria(s)", "Resumo da ordem", "Texto (WEB, fala de Jesus)", "Texto grego (SBLGNT)"],
          data, [9, 9, 16, 14, 24, 7, 8, 9, 8, 8, 16, 13, 14, 40, 50, 60])

    data = []
    for ref, v in versos.items():
        dest, alc, cats, resumo, *nota = v["label"]
        forms = "; ".join(f"{i['form'].strip('⸀⸁⸂⸃,.·;')} ({i['lemma']}, {i['person']}ª {'pl' if i['number']=='P' else 'sg'}, {i['tense']})" for i in v["imps"])
        just = (f"Destinatário: {DEST_PT[dest]}. Alcance: {ALC_PT[alc]} — {ALC_EXPL[alc]} "
                + (f"Categoria(s): {', '.join(CATEGORIAS[c]['titulo'] for c in cats.split(';') if c in CATEGORIAS)}. " if cats != "-" else "Sem categoria: não é mandamento aos discípulos. ")
                + (f"Nota: {nota[0]}." if nota else ""))
        data.append((ref_pt(ref), ref, len(v["imps"]), forms, DEST_PT[dest], ALC_PT[alc], "sim" if alc in ("U", "G") else "não",
                     cats, resumo, nota[0] if nota else "", just, v["wj"]))
    sheet("Versículos",
          ["Ref. (PT)", "Ref. (código)", "Nº imperativos", "Formas (lema, pessoa, tempo)", "Destinatário", "Alcance",
           "Conta na prioridade?", "Categoria(s)", "Resumo da ordem", "Nota", "Justificativa do julgamento", "Texto (WEB, fala de Jesus)"],
          data, [9, 9, 7, 45, 16, 13, 10, 14, 42, 30, 70, 50])

    data = []
    for c in final:
        m = CATEGORIAS[c]
        data.append((score[c]["pos_final"], c, m["titulo"], m["demanda"], m["agrupamento"], m["piper"],
                     "\n".join(m["enfases"]), m["eminencia"], f"{m['rep_ref']} — {m['rep_naa']}",
                     "; ".join(ref_pt(r) for r in sorted(refs[c]["U"] + refs[c]["G"], key=ref_key)),
                     "; ".join(ref_pt(r) for r in sorted(refs[c]["S"] + refs[c]["B"] + refs[c]["P"] + refs[c]["E"] + refs[c]["T"], key=ref_key)),
                     "; ".join(comp[c])))
    sheet("Categorias",
          ["Prioridade", "Código", "Título", "Demanda", "Justificativa do agrupamento", "Correspondência (Piper)",
           "Ênfases (parábolas/discursos)", "Eminência explícita", "Versículo representativo (NAA)",
           "Passagens normativas (U+G)", "Passagens de apoio (S/B/P/E/T)", "Complemento †"],
          data, [8, 9, 30, 45, 60, 35, 50, 40, 50, 45, 40, 30])

    data = []
    for c in final:
        sc = score[c]
        data.append((sc["pos_final"], c, CATEGORIAS[c]["titulo"], sc["U"], sc["G"], sc["norm"], sc["comp"], sc["enf"],
                     round(sc["score"], 1), sc["pos_contagem"], sc["pos_score"], "sim" if c in EMINENCIA else "não", just_ordenacao(c, sc)))
    ws = sheet("Ordenação",
               ["Posição final", "Código", "Categoria", "Versículos U", "Versículos G", "Normativos (U+G)", "Complemento †",
                "Ênfases", "Pontuação", "Posição por contagem", "Posição por pontuação", "Promovida por eminência", "Justificativa da ordenação"],
               data, [8, 9, 30, 8, 8, 9, 9, 8, 9, 9, 9, 10, 90])
    ws.append([])
    ws.append(["Regra:", f"pontuação = versículos normativos (U+G) + {PESO_COMP} × ordens no complemento + {PESO_ENF} × blocos de ênfase. "
               "Quatro categorias são promovidas ao topo por eminência explícita do próprio Jesus (ver justificativas); as demais seguem a pontuação."])

    data = [(ref_pt(ref), ref, forma, tipo, cats, resumo, just) for ref, forma, tipo, cats, resumo, just in COMPLEMENTO]
    sheet("Complemento", ["Ref. (PT)", "Ref. (código)", "Forma grega", "Tipo gramatical", "Categoria(s)", "Resumo", "Justificativa"],
          data, [10, 10, 34, 26, 12, 50, 60])

    data = []
    for r in rows:
        lab = ROTULOS.get(r["ref"])
        if r["speaker"] == "outro" or (lab and lab[1] == "F"):
            data.append((ref_pt(r["ref"]), r["ref"], r["form"].strip("⸀⸁⸂⸃,.·;"), r["lemma"], GLOSSARIO.get(r["lemma"], ""),
                         "fala de terceiro no versículo" if r["speaker"] == "outro" else "falso positivo da marcação", r["nowj"][:160], r["wj"][:160]))
    sheet("Excluídos", ["Ref. (PT)", "Ref. (código)", "Forma", "Lema", "Sentido", "Motivo", "Texto fora da fala de Jesus (WEB)", "Fala de Jesus no versículo (WEB)"],
          data, [10, 10, 16, 14, 22, 26, 60, 50])

    cnt = collections.Counter(r["lemma"] for r in rows if ROTULOS.get(r["ref"]))
    sheet("Glossário", ["Lema grego", "Sentido básico", "Ocorrências (imperativo, fala de Jesus)"],
          [(l, GLOSSARIO.get(l, ""), n) for l, n in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))], [18, 40, 12])
    out = DOCS / "Mandamentos_de_Jesus_Achados.xlsx"
    wb.save(out)
    print("OK ->", out)


# ----------------------------------------------------------------- DOCX helpers
def refs_paragraph(doc, parts, size=8.5):
    """Parêntese em itálico cinza-claro com as demais passagens."""
    p = doc.add_paragraph()
    spacing(p, after=6)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(0.6)
    run(p, "(", italic=True, size=size, color=LIGHT_GREY)
    for i, (label, txt) in enumerate(parts):
        if i:
            run(p, "  •  ", italic=True, size=size, color=LIGHT_GREY)
        run(p, label + " ", italic=True, bold=True, size=size, color=LIGHT_GREY)
        run(p, txt, italic=True, size=size, color=LIGHT_GREY)
    run(p, ")", italic=True, size=size, color=LIGHT_GREY)


def finish(doc, name):
    out = DOCS / f"{name}.docx"
    doc.save(out)
    print("OK ->", out)
    print("OK ->", to_pdf(out))


# ----------------------------------------------------------------- DOCX 1: documento final
def doc_mandamentos(versos, st, refs, comp, score, final):
    n_versos = sum(1 for v in versos.values() if v["label"][1] not in ("F",))
    n_norm = sum(1 for v in versos.values() if v["label"][1] in ("U", "G"))
    n_tok = sum(len(v["imps"]) for v in versos.values() if v["label"][1] != "F")
    doc = new_document(
        header_meta="Estudo bíblico-prático    •    Base: imperativos gregos nas falas de Jesus (Mt, Mc, Lc, Jo)    •    Tradução: NAA",
        footer_label="Os Mandamentos de Jesus  •  grego: SBLGNT/MorphGNT  •  v1.0",
    )
    title_block(doc, "OS MANDAMENTOS DE JESUS",
                "Tudo o que Jesus ordenou nos Evangelhos, agrupado por tema e ordenado por prioridade, para ser praticado",
                "ensinando-os a guardar todas as coisas que tenho ordenado a vocês.\nE eis que estou com vocês todos os dias até o fim dos tempos.",
                "Mateus 28:20", after=6)

    section_title(doc, "", "Como usar este documento")
    body(doc, f"Este documento reúne as ordens de Jesus registradas nos quatro Evangelhos. Foram levantados, pela análise morfológica do grego, "
              f"{n_tok} verbos no modo imperativo em {n_versos} versículos de falas de Jesus. Depois de separar o que é palavra de poder (curas), "
              f"ordem de ocasião (buscar o jumentinho) e fala de personagem de parábola, restaram {n_norm} passagens com mandamentos válidos para "
              f"todo discípulo. Elas foram organizadas em {len(CATEGORIAS)} categorias, à maneira de John Piper em *What Jesus Demands from the World*, "
              f"e ordenadas por prioridade.", size=9.5)
    body(doc, "Em cada categoria: o título resume a ordem; o versículo em destaque é o que melhor a representa (texto da Nova Almeida Atualizada); "
              "a frase seguinte explica a demanda; e, entre parênteses, em letra menor, estão todas as demais passagens, para que nada do que "
              "Jesus ordenou fique de fora.", size=9.5)
    bullet(doc, "passagens em que o imperativo é dirigido a todos os discípulos, ou cujo princípio Jesus aplica a todos.", lead="Mandamentos —", size=9)
    bullet(doc, "ordens de ocasião, falas de personagens de parábola e orações de Jesus que iluminam o tema sem serem norma direta.", lead="Apoio —", size=9)
    bullet(doc, "parábolas, discursos e ditos onde o tema é ensinado sem verbo no imperativo.", lead="Ênfases —", size=9)
    bullet(doc, "ordens expressas por outras formas gramaticais (proibição no subjuntivo, futuro 'amarás', infinitivo, 'que vos ameis'), "
                "incluídas para completude.", lead="† Outras formas —", size=9)
    note(doc, "Abreviaturas: Mt = Mateus, Mc = Marcos, Lc = Lucas, Jo = João. A ordem de prioridade combina a quantidade de passagens com a "
              "eminência que o próprio Jesus atribui ao tema (ver quadro final e o documento de metodologia).", size=8.5)

    for c in final:
        m = CATEGORIAS[c]; sc = score[c]
        section_title(doc, f"{sc['pos_final']}.", m["titulo"])
        p = doc.add_paragraph()
        spacing(p, after=3)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        run(p, f"“{m['rep_naa']}”  ", size=10.5, bold=True, color=GREEN)
        run(p, f"({m['rep_ref']})", size=9.5, bold=True, color=GREEN)
        body(doc, m["demanda"], size=9.5, after=3)
        norm = sorted(refs[c]["U"] + refs[c]["G"], key=ref_key)
        apoio = sorted(refs[c]["S"] + refs[c]["B"] + refs[c]["P"] + refs[c]["E"] + refs[c]["T"], key=ref_key)
        parts = [("Mandamentos:", "; ".join(ref_pt(r) for r in norm) or "—")]
        if apoio:
            parts.append(("Apoio:", "; ".join(ref_pt(r) for r in apoio)))
        if m["enfases"]:
            parts.append(("Ênfases:", "; ".join(e.split(" — ")[0] for e in m["enfases"])))
        if comp[c]:
            parts.append(("† Outras formas:", "; ".join(ref_pt(r) if r[:2] in BOOK_PT and r[2] == " " else r for r in comp[c])))
        refs_paragraph(doc, parts)

    section_title(doc, "", "Quadro de priorização")
    tbl = [[str(score[c]["pos_final"]), CATEGORIAS[c]["titulo"], str(score[c]["norm"]), str(score[c]["comp"]), str(score[c]["enf"]),
            f"{score[c]['score']:.1f}", str(score[c]["pos_contagem"]), "sim" if c in EMINENCIA else ""] for c in final]
    table(doc, ["#", "Categoria", "Mandamentos", "†", "Ênfases", "Pontos", "Só contagem", "Eminência"],
          tbl, [0.8, 7.6, 2.0, 1.0, 1.4, 1.4, 1.6, 2.0], size=8)
    note(doc, f"Pontos = mandamentos + {PESO_COMP} × († outras formas) + {PESO_ENF} × ênfases. 'Só contagem' é a posição se apenas o número de passagens "
              "fosse considerado. As quatro categorias com 'eminência' foram colocadas no topo porque o próprio Jesus as hierarquiza: 'o grande e primeiro "
              "mandamento' e 'o segundo, semelhante a este' (Mt 22:37-40), e 'arrependam-se e creiam', primeira palavra da sua pregação (Mc 1:15).", size=8)
    body(doc, "Os textos da NAA foram transcritos para este estudo e devem ser conferidos com a edição oficial da Sociedade Bíblica do Brasil antes de "
              "publicação impressa. A planilha de achados e os documentos de metodologia e de observações acompanham este arquivo no repositório.",
         size=8.5, italic=True, color=GREY)
    finish(doc, "Mandamentos_de_Jesus")


# ----------------------------------------------------------------- DOCX 2: projeto e metodologia
def doc_metodologia(rows, versos, st, score, final):
    doc = new_document(header_meta="Documento de projeto    •    Definição, metodologia, critérios e reprodutibilidade",
                       footer_label="Mandamentos de Jesus — Projeto e Metodologia  •  v1.0")
    title_block(doc, "PROJETO E METODOLOGIA",
                "Levantamento dos imperativos de Jesus nos Evangelhos, agrupamento temático e priorização",
                "Se vocês me amam, guardarão os meus mandamentos.", "João 14:15")

    section_title(doc, "1", "Definição do projeto")
    body(doc, "O projeto consiste em identificar, a partir do texto grego do Novo Testamento, todas as ordens de Jesus nos quatro Evangelhos "
              "expressas no modo imperativo; organizá-las em categorias de sentido lógico, preservando o versículo exato de cada ocorrência; "
              "atribuir prioridade a cada categoria segundo a quantidade de passagens e a ênfase que Jesus lhes dá em parábolas e ensinos; e "
              "entregar um documento de uso prático, cujo fim declarado é promover a obediência a Cristo: 'ensinando-os a guardar todas as "
              "coisas que tenho ordenado a vocês' (Mt 28:20).")
    section_title(doc, "2", "O que foi entendido do pedido (reformulação em termos do estudo)")
    body(doc, "Em termos de exegese, o pedido é um levantamento sintático-morfológico das *ipsissima verba* imperativas de Jesus — não um "
              "estudo de tudo o que ele ensinou, mas daquilo que ele ordenou com a forma verbal própria da ordem. O critério formal é o modo "
              "imperativo (presente ou aoristo; 2ª ou 3ª pessoa) no texto crítico grego. O recorte de corpus é o conjunto dos ditos atribuídos a "
              "Jesus em Mateus, Marcos, Lucas e João (as chamadas 'letras vermelhas'). O trabalho seguinte é de teologia bíblica: agrupar as "
              "ordens em demandas coerentes, como fez John Piper ao reduzir o ensino de Jesus a cinquenta demandas organizadas por eixos "
              "(relação com Deus e com Jesus; vida interior; relações; dinheiro; missão; vigilância). Por fim, pede-se um juízo de "
              "proeminência: quais demandas Jesus mais repete e mais enfatiza, para que o discípulo saiba por onde começar.")
    body(doc, "Entendeu-se também que o produto deve servir à prática, e não apenas ao estudo: por isso o documento final cita um versículo "
              "representativo por categoria (na NAA), lista as demais passagens de forma discreta e usa linguagem direta.")

    section_title(doc, "3", "Fontes e ferramentas")
    bullet(doc, "SBLGNT (Society of Biblical Literature Greek New Testament) com análise morfológica do projeto MorphGNT — cada palavra traz "
                "classe, pessoa, tempo, voz, modo, caso, número e lema.", lead="Texto grego:")
    bullet(doc, "World English Bible em formato USFM, que marca as palavras de Jesus com o código \\wj (words of Jesus). Essa marcação, "
                "feita por editores humanos, foi usada para decidir se cada versículo contém fala de Jesus.", lead="Falas de Jesus:")
    bullet(doc, "Dicionário de Strong (Open Scriptures) para ligar o lema grego ao número de Strong presente no texto inglês e, assim, verificar "
                "se o verbo imperativo está dentro ou fora do trecho marcado como fala de Jesus.", lead="Ponte grego–inglês:")
    bullet(doc, "Nova Almeida Atualizada (SBB, 2017) para os versículos representativos do documento final.", lead="Tradução de referência:")
    bullet(doc, "Python 3 (python-docx, openpyxl) e LibreOffice para gerar DOCX, XLSX e PDF. Todo o código está no repositório.", lead="Ferramentas:")

    section_title(doc, "4", "Conceitos gramaticais usados")
    bullet(doc, "forma verbal da ordem, do pedido e da exortação. Em grego aparece na 2ª pessoa ('vigiem') e também na 3ª ('quem tem ouvidos, ouça'; "
                "'não se turbe o coração de vocês').", lead="Modo imperativo:")
    bullet(doc, "o imperativo presente tende a indicar ação contínua ou habitual ('continuem pedindo'); o aoristo, ação vista como um todo "
                "('arrependam-se'). A planilha registra o tempo de cada forma.", lead="Aspecto (presente × aoristo):")
    bullet(doc, "no grego, a proibição 'não façam' costuma usar μή + subjuntivo aoristo, não o imperativo. Essas proibições não entram na contagem "
                "principal, mas foram recolhidas no complemento, para que o documento de obediência não as omita.", lead="Proibições no subjuntivo:")
    bullet(doc, "citações do Antigo Testamento com força de mandamento usam o futuro ('amarás'); há ainda infinitivos ('não jurar'), particípios "
                "('batizando') e orações com ἵνα ('que vos ameis'). Também foram recolhidos no complemento, com marcação †.", lead="Outras formas imperativais:")

    section_title(doc, "5", "Etapas do método")
    etapas = [
        "Extração: filtrar no MorphGNT todos os verbos com modo = imperativo em Mt, Mc, Lc e Jo (843 formas em 614 versículos).",
        "Atribuição de falante: para cada versículo, verificar na WEB se há trecho marcado como fala de Jesus; nos versículos mistos "
        "('Jesus disse: siga-me'), usar os números de Strong para checar se o verbo está dentro do trecho de Jesus; casos ambíguos foram revisados um a um.",
        "Exclusão: imperativos ditos por terceiros (a multidão a Bartimeu, o Sinédrio, Marta) foram retirados e listados na aba 'Excluídos'.",
        "Julgamento de destinatário e alcance: cada versículo recebeu um código de destinatário (discípulos, multidão, indivíduo, oponentes, "
        "Pai, natureza, personagem de parábola, citação, Juiz futuro) e de alcance (universal, generalizável, situacional, performativo, "
        "parábola, oração, escatológico). Só 'universal' e 'generalizável' contam como mandamento.",
        "Categorização: cada versículo foi ligado a uma ou mais das 17 categorias, com resumo em português e nota quando necessário.",
        "Complemento: levantamento automático das proibições μή + subjuntivo aoristo nas falas de Jesus, seguido de curadoria manual, e "
        "acréscimo das ordens em futuro, infinitivo, particípio e ἵνα.",
        "Priorização: contagem de passagens normativas por categoria, acrescida do complemento (peso 0,5) e dos blocos de ênfase (peso 1); "
        "promoção das categorias que o próprio Jesus hierarquiza.",
        "Produção: planilha com todos os achados e julgamentos; documento final; este documento; documento de observações.",
    ]
    for i, e in enumerate(etapas, 1):
        bullet(doc, e, lead=f"{i}.")

    section_title(doc, "6", "Critérios de julgamento")
    for k, v in ALC_EXPL.items():
        bullet(doc, v, lead=f"{ALC_PT[k].capitalize()} ({k}):")
    body(doc, "Exemplos: 'Siga-me' dito a Mateus é generalizável, porque Jesus universaliza o mesmo chamado em Mt 16:24. 'Vão à aldeia e tragam "
              "o jumentinho' é situacional. 'Fique limpo' é performativo. 'Pague o que me deve', dito pelo servo da parábola, é parábola.")

    section_title(doc, "7", "Taxonomia e relação com John Piper")
    body(doc, "Piper organiza cinquenta demandas em grandes eixos: a conversão e a relação com Jesus (nascer de novo, arrepender-se, vir, crer, "
              "amar, ouvir, permanecer, seguir), a relação com Deus (amar, temer, adorar, orar, não ter ansiedade), a vida interior e as relações "
              "(humildade, ira, perdão, amor ao inimigo e ao próximo, juramentos, pureza, casamento), o dinheiro, a missão e a vigilância. "
              "As 17 categorias deste estudo seguem a mesma lógica, mas foram definidas a partir das ocorrências efetivas do imperativo, de modo "
              "que cada categoria tem ao menos um imperativo morfológico que a sustenta. A correspondência temática com Piper está na planilha.")
    for c in final:
        bullet(doc, CATEGORIAS[c]["agrupamento"], lead=f"{score[c]['pos_final']}. {CATEGORIAS[c]['titulo']} —", size=9)

    section_title(doc, "8", "Regra de priorização")
    body(doc, f"Pontuação = número de versículos normativos (U+G) + {PESO_COMP} × ordens do complemento + {PESO_ENF} × blocos de ênfase "
              "(parábolas e discursos listados por categoria). A ordenação por pontuação é a base. Sobre ela aplicou-se um único ajuste, "
              "documentado versículo a versículo: as categorias que o próprio Jesus declara primeiras — amar a Deus ('o grande e primeiro "
              "mandamento'), amar o próximo ('o segundo, semelhante'), arrepender-se e crer (primeira palavra da pregação) — foram promovidas ao "
              "topo. Sem esse ajuste, a contagem bruta privilegiaria 'vigiar' e 'missão', porque os discursos escatológico e de envio são longos "
              "e repetidos nos três sinóticos. A planilha mostra as três ordens (bruta, por pontuação e final) para quem preferir outro critério.")

    section_title(doc, "9", "Produtos")
    bullet(doc, "Mandamentos_de_Jesus.docx/.pdf — documento final para a prática.")
    bullet(doc, "Mandamentos_de_Jesus_Achados.xlsx — imperativos, versículos, julgamentos, categorias, ordenação, complemento, excluídos e glossário.")
    bullet(doc, "Projeto_e_Metodologia.docx/.pdf — este documento.")
    bullet(doc, "Observacoes_e_Reflexoes.docx/.pdf — pontos de atenção metodológicos.")
    bullet(doc, "dados/ e construir.py — dados brutos, rótulos e código que regenera tudo.")

    section_title(doc, "10", "Como reproduzir")
    body(doc, "No repositório: `python3 preparar_dados.py` baixa o MorphGNT, a WEB e o dicionário de Strong e gera os arquivos intermediários; "
              "`python3 construir.py` aplica os rótulos (dados/rotulos.py), o glossário, o complemento e a taxonomia e produz a planilha e os "
              "documentos. Alterar um julgamento é editar uma linha em rotulos.py e rodar de novo.", size=9.5)
    finish(doc, "Projeto_e_Metodologia")


# ----------------------------------------------------------------- DOCX 3: observações
def doc_observacoes(rows, versos, st, score, final):
    doc = new_document(header_meta="Documento de projeto    •    Pontos de atenção sobre a metodologia",
                       footer_label="Mandamentos de Jesus — Observações e Reflexões  •  v1.0")
    title_block(doc, "OBSERVAÇÕES E REFLEXÕES",
                "Pontos de atenção observados durante o levantamento, o agrupamento e a priorização",
                "Examinem tudo, retenham o que é bom.", "1 Tessalonicenses 5:21")
    n_norm = sum(1 for v in versos.values() if v["label"][1] in ("U", "G"))
    obs = [
        ("Imperativo não é sinônimo de mandamento.",
         "O recorte morfológico é objetivo e reprodutível, mas deixa de fora ordens célebres: 'amarás o Senhor, teu Deus' (futuro), "
         "'sejam perfeitos' (futuro), 'não jurem' (infinitivo), 'não se preocupem com o amanhã' (subjuntivo), 'amem-se uns aos outros' "
         "(ἵνα + subjuntivo), 'é necessário nascer de novo' (δεῖ). O complemento mitiga isso, mas quem usar só a contagem principal "
         "subestimará as categorias Deus, Amor, Humildade e Confiança."),
        ("O inverso também vale: nem todo imperativo é mandamento.",
         "Dos imperativos nas falas de Jesus, pouco mais da metade são normativos. O restante é palavra de poder ('fique limpo'), ordem "
         "de ocasião ('tragam o jumentinho'), fala de personagem de parábola ('pague o que me deve'), oração ao Pai ('passe de mim este "
         "cálice') ou sentença do Juiz ('apartem-se de mim'). O julgamento de alcance é a etapa mais sensível do método e está inteiramente "
         "documentado na planilha."),
        ("A fronteira entre 'situacional' e 'generalizável' exige juízo teológico.",
         "'Siga-me' a Mateus foi tratado como generalizável porque Jesus universaliza o chamado; 'mostre-se ao sacerdote' foi tratado como "
         "generalizável no princípio (cumprir a Lei), não na letra. Outros leitores podem decidir diferente; por isso cada decisão tem "
         "justificativa escrita e pode ser alterada em uma linha."),
        ("Os paralelos sinóticos inflam a contagem.",
         "'Negue-se a si mesmo, tome a sua cruz e siga-me' aparece em Mt, Mc e Lc e conta três vezes. O discurso escatológico (Mt 24, Mc 13, "
         "Lc 21) e o discurso de envio (Mt 10, Lc 9–10) são longos e repetidos, o que explica por que 'vigiar' e 'missão' lideram a contagem "
         "bruta. A repetição é, em parte, ênfase legítima dos evangelistas; em parte, efeito da tradição comum. A planilha permite contar por "
         "perícope se desejado."),
        ("A ordem final combina dois critérios e isso deve ficar explícito.",
         "A contagem é objetiva; a 'eminência' é um julgamento baseado em ditos explícitos de Jesus (Mt 22:37-40; Mc 1:15; Mt 6:33; Jo 6:29). "
         "Optou-se por promover apenas quatro categorias e manter todas as demais na ordem de pontuação, para limitar a subjetividade. As três "
         "ordens (bruta, pontuação, final) estão lado a lado na planilha."),
        ("As categorias se sobrepõem.",
         "'Vigiem e orem' pertence a Vigiar e a Orar; 'venda tudo, dê aos pobres e siga-me' pertence a Bens e a Seguir. Permitiu-se mais de "
         "uma categoria por versículo, o que faz a soma das categorias superar o número de versículos. Isso é intencional: perder a dupla "
         "pertença seria perder sentido."),
        ("Dependência da marcação de 'letras vermelhas' da WEB.",
         "A marcação \\wj é editorial, não original. Ela foi confiável para a grande maioria, mas gerou falsos positivos ('coragem' dito pela "
         "multidão a Bartimeu, Mc 10:49; 'diga, Mestre', Lc 7:40; 'tell us', Lc 22:67; 'vem e vê', Jo 11:34), corrigidos à mão e listados em "
         "'Excluídos'. Versículos em que a WEB não marca fala de Jesus não foram revistos; um erro de omissão ali passaria despercebido."),
        ("A ponte por números de Strong é aproximada.",
         "O cruzamento grego–inglês por Strong falhou em cerca de um quinto dos versículos mistos (lemas sem correspondência, variantes); esses "
         "casos foram revisados um a um. O método serviu bem para triagem, não substitui a leitura."),
        ("Texto crítico e passagens disputadas.",
         "O SBLGNT inclui o final longo de Marcos (16:9-20), por isso 'vão por todo o mundo e preguem' (Mc 16:15) entrou com nota de "
         "disputa; e omite a perícope da adúltera (Jo 7:53–8:11), por isso 'vá e não peque mais' ficou no complemento. Quem adota a Textus "
         "Receptus terá contagens ligeiramente diferentes."),
        ("Aspecto verbal foi registrado, não interpretado.",
         "A distinção presente/aoristo pode enriquecer a prática ('continuem pedindo' × 'arrependam-se de uma vez'), mas sua leitura "
         "pastoral exige cautela; a planilha a registra para estudo posterior, sem fazer dela critério de agrupamento."),
        ("Imperativos de 3ª pessoa.",
         "'Quem tem ouvidos, ouça', 'não se turbe o coração de vocês', 'o que Deus uniu não separe o homem' são ordens reais, embora não "
         "pareçam em português. Foram contados. Já 'venha o teu Reino' é imperativo dirigido a Deus dentro de uma oração que Jesus manda orar; "
         "contou-se como parte do mandamento de orar assim."),
        ("Os textos da NAA foram transcritos de memória.",
         "Não havia acesso a uma fonte digital licenciada da Nova Almeida Atualizada neste processo. Os versículos representativos devem ser "
         "conferidos com a edição da SBB antes de impressão definitiva. As demais passagens aparecem apenas por referência, justamente para "
         "não depender de texto transcrito."),
        ("Piper é analogia de método, não molde.",
         "As 50 demandas de Piper partem do ensino inteiro de Jesus, incluindo o que não está no imperativo. Aqui o ponto de partida é "
         "inverso: a forma gramatical. Por isso algumas demandas de Piper ('nascer de novo', 'adorar em espírito e verdade') só aparecem no "
         "complemento, e algumas categorias daqui (Comunhão, Justiça e deveres) não têm capítulo próprio em Piper."),
        ("Risco pastoral: legalismo.",
         "Um catálogo de ordens pode ser lido como lista de exigências para merecer algo. O próprio material contradiz essa leitura: a "
         "primeira ordem é 'arrependam-se e creiam', a mais repetida é 'não tenham medo', e o quadro inteiro se abre com 'eu estou com vocês "
         "todos os dias'. Recomenda-se ensinar o documento sempre a partir da graça que o precede (Mt 11:28-30)."),
        ("Achado que vale registrar.",
         f"Entre as {n_norm} passagens normativas, a ordem individual mais frequente de Jesus não é ética, mas pastoral: 'não tenham medo / não "
         "andem ansiosos / tenham bom ânimo'. Isso diz algo sobre o tom com que ele comanda."),
        ("Reprodutibilidade.",
         "Todo passo automatizado está em código aberto no repositório; todo passo humano está em tabelas editáveis com justificativa. "
         "Qualquer leitor pode discordar de um julgamento, alterá-lo e regenerar os documentos em minutos."),
    ]
    for i, (t, txt) in enumerate(obs, 1):
        p = doc.add_paragraph()
        spacing(p, before=4, after=1)
        p.paragraph_format.keep_with_next = True
        run(p, f"{i}. {t}", bold=True, size=10, color=GREEN)
        body(doc, txt, size=9.5, after=4)
    finish(doc, "Observacoes_e_Reflexoes")


# ----------------------------------------------------------------- main
if __name__ == "__main__":
    rows, versos = load()
    st, refs, comp, score, final = stats(versos)
    xlsx(rows, versos, st, refs, comp, score, final)
    doc_mandamentos(versos, st, refs, comp, score, final)
    doc_metodologia(rows, versos, st, score, final)
    doc_observacoes(rows, versos, st, score, final)
    print("\nOrdem final:", " > ".join(f"{score[c]['pos_final']}.{c}" for c in final))
