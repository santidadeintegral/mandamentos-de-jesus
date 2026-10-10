#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pesquisa 2 — Deveres sociais ensinados por Jesus. Constrói:

  docs/01-levantamento-inicial/Deveres_Sociais_Documento_Institucional.docx/.pdf  — documento consolidado da ONG (categorias priorizadas + atividades)
  docs/01-levantamento-inicial/Deveres_Sociais_Achados.xlsx                        — triagem dos 1.955 versículos, julgamentos, categorias, ordenação, atividades
  docs/Projeto_e_Metodologia.docx/.pdf
  docs/Observacoes_e_Reflexoes.docx/.pdf

Uso: python3 pesquisa-2-deveres-sociais/construir.py   (requer comum/preparar_dados.py já executado)
"""
import collections
import datetime
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "comum"))
sys.path.insert(0, str(ROOT / "dados"))
from timbrado import *  # noqa: E402,F401
from biblia import jesus_verses, ref_key, ref_pt  # noqa: E402
from rotulos import ROTULOS  # noqa: E402
from categorias import CATEGORIAS  # noqa: E402
from atividades_ong import ATIVIDADES  # noqa: E402

ROOT = Path(__file__).resolve().parent  # reafirma: o star-import de timbrado traz outro ROOT

from openpyxl import Workbook  # noqa: E402
from openpyxl.styles import Alignment, Font, PatternFill  # noqa: E402
from openpyxl.utils import get_column_letter  # noqa: E402

DOCS = ROOT / "docs" / "01-levantamento-inicial"  # etapa 1: levantamento, categorias, documento institucional
DOCS.mkdir(exist_ok=True)
LIGHT_GREY = RGBColor(0x7A, 0x7A, 0x7A)
TIPO_PT = {"O": "ordem direta", "E": "ensino normativo", "P": "parábola/ilustração", "J": "juízo escatológico",
           "B": "bem-aventurança", "A": "advertência/'ai'", "M": "modelo de Jesus", "C": "citação da Escritura"}
FORCA_PT = {"D": "direta", "I": "indireta", "S": "situacional"}
FORCA_EXPL = {
    "D": "O dever é explícito na fala de Jesus e vale para todo discípulo; conta integralmente na prioridade.",
    "I": "O dever está implicado: pressuposto por uma parábola, ilustrado pelo exemplo de Jesus, ou derivado de uma declaração; conta com peso 0,5.",
    "S": "Ordem presa à ocasião histórica (missão dos Doze, apresentação ao sacerdote); listada por completude, não conta na prioridade.",
}
DEST_PT = {"D": "discípulos", "M": "multidão/ouvintes", "I": "indivíduo", "O": "oponentes/autoridades", "B": "personagem de parábola"}
PESO_I, PESO_ENF = 0.5, 1.0
EMINENCIA = {
    "AMAR": "Mt 22:39-40: amar o próximo é 'o segundo, semelhante' ao maior mandamento, de que 'dependem toda a Lei e os Profetas'; Jo 13:35: é a marca do discípulo.",
    "ALIM": "Mt 25:35,42: dar de comer e de beber é o primeiro critério nomeado no juízo das nações.",
    "ENF": "Mt 25:36,43: visitar o enfermo e o preso é critério do juízo das nações.",
    "ESTR": "Mt 25:35,43: hospedar o forasteiro é critério do juízo das nações.",
}
STATUS_MARK = {"Praticada": "●", "Em implantação": "◐", "A definir": "○"}


# ----------------------------------------------------------------- dados
def load():
    corpus = jesus_verses()  # [(ref, wj, nowj)]
    textos = {r: wj for r, wj, _ in corpus}
    versos = collections.OrderedDict()
    for ref in sorted(ROTULOS, key=ref_key):
        if ref not in textos:
            raise SystemExit(f"rótulo sem versículo no corpus: {ref}")
        cats, tipo, forca, dest, det, resumo, *nota = ROTULOS[ref]
        versos[ref] = dict(ref=ref, cats=cats.split(";"), tipo=tipo, forca=forca, dest=dest, det=det,
                           resumo=resumo, nota=nota[0] if nota else "", wj=textos[ref])
    return corpus, versos


def blocos(refs):
    """Conta passagens = blocos de versículos contíguos no mesmo capítulo."""
    keys = sorted(ref_key(r) for r in refs)
    n, prev = 0, None
    for k in keys:
        if prev is None or k[0] != prev[0] or k[1] != prev[1] or k[2] != prev[2] + 1:
            n += 1
        prev = k
    return n


def stats(versos):
    st = {c: collections.Counter() for c in CATEGORIAS}
    refs = {c: collections.defaultdict(list) for c in CATEGORIAS}
    for ref, v in versos.items():
        for c in v["cats"]:
            st[c][v["forca"]] += 1
            st[c]["det"] += v["det"]
            st[c]["tipo_" + v["tipo"]] += 1
            refs[c][v["forca"]].append(ref)
    score = {}
    for c in CATEGORIAS:
        s = st[c]
        norm = s["D"] + s["I"]
        score[c] = dict(D=s["D"], I=s["I"], S=s["S"], norm=norm, det=s["det"], enf=len(CATEGORIAS[c]["enfases"]),
                        blocos=blocos(refs[c]["D"] + refs[c]["I"]),
                        score=s["D"] + PESO_I * s["I"] + PESO_ENF * len(CATEGORIAS[c]["enfases"]))
    por_contagem = sorted(CATEGORIAS, key=lambda c: (-score[c]["norm"], -score[c]["score"]))
    por_score = sorted(CATEGORIAS, key=lambda c: (-score[c]["score"], -score[c]["norm"]))
    mt25 = sorted(["ALIM", "ENF", "ESTR"], key=lambda c: -score[c]["score"])
    promovidas = ["AMAR"] + mt25
    final = promovidas + [c for c in por_score if c not in promovidas]
    for i, c in enumerate(por_contagem, 1):
        score[c]["pos_contagem"] = i
    for i, c in enumerate(por_score, 1):
        score[c]["pos_score"] = i
    for i, c in enumerate(final, 1):
        score[c]["pos_final"] = i
    return st, refs, score, final


def just_ordenacao(c, sc):
    base = (f"{sc['D']} versículos com dever direto + {sc['I']} com dever indireto (peso {PESO_I}) = {sc['norm']} versículos em {sc['blocos']} passagens; "
            f"{sc['S']} situacionais (não contam); {sc['enf']} blocos de ênfase (peso {PESO_ENF}); {sc['det']} versículos com detalhe prático "
            f"→ pontuação {sc['score']:.1f}; posição por contagem bruta {sc['pos_contagem']}º, por pontuação {sc['pos_score']}º.")
    if c in EMINENCIA:
        return base + f" Promovida para {sc['pos_final']}º por eminência explícita: {EMINENCIA[c]}"
    return base + f" Posição final {sc['pos_final']}º (ordem de pontuação, após as quatro categorias promovidas)."


# ----------------------------------------------------------------- XLSX
def xlsx(corpus, versos, st, refs, score, final):
    wb = Workbook()
    H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor="2D5130")
    WRAP = Alignment(wrap_text=True, vertical="top")

    def sheet(title, headers, data, widths):
        ws = wb.create_sheet(title)
        ws.append(headers)
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        for cell in ws[1]:
            cell.font = H; cell.fill = HF; cell.alignment = WRAP
        for r in data:
            ws.append(list(r))
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = WRAP
        ws.freeze_panes = "A2"
        return ws

    wb.remove(wb.active)
    leia = wb.create_sheet("Leia-me")
    leia.column_dimensions["A"].width = 120
    for line in [
        "DEVERES SOCIAIS ENSINADOS POR JESUS — ACHADOS, JULGAMENTOS E ORDENAÇÃO (ONG Santidade Integral em Cristo)",
        "",
        "Pergunta: em que falas de Jesus nos quatro Evangelhos ele descreve um dever do ouvinte para com outras pessoas / a sociedade?",
        "Corpus: todos os versículos com fala de Jesus (marcação \\wj da World English Bible). Sem filtro gramatical: ordens, ensinos, parábolas, juízos, 'ais', modelo de Jesus.",
        "",
        "Abas:",
        "1. Triagem — os 1.955 versículos com fala de Jesus, com a indicação de selecionado/não selecionado e a(s) categoria(s).",
        "2. Versículos — os versículos selecionados, com tipo, força normativa, destinatário, detalhe prático, resumo e justificativa do julgamento.",
        "3. Categorias — definição de cada dever, justificativa do agrupamento, ênfases, eminência e versículo representativo (NAA).",
        "4. Ordenação — contagens, pontuação e justificativa da prioridade de cada categoria.",
        "5. Atividades da ONG — o que a Santidade Integral em Cristo pratica ou planeja em obediência a cada dever (proposta a validar pela diretoria).",
        "",
        "Tipos: " + "; ".join(f"{k} = {v}" for k, v in TIPO_PT.items()),
        "Força: " + "; ".join(f"{k} = {v}" for k, v in FORCA_PT.items()),
        "Destinatário: " + "; ".join(f"{k} = {v}" for k, v in DEST_PT.items()),
        "",
        "Fonte das falas de Jesus: World English Bible (USFM, domínio público). Tradução de referência do documento final: Nova Almeida Atualizada (SBB).",
        "Gerado por construir.py em " + datetime.date.today().isoformat() + ".",
    ]:
        leia.append([line])

    data = []
    for ref, wj, _ in corpus:
        v = versos.get(ref)
        if v:
            data.append((ref_pt(ref), ref, "sim", "; ".join(v["cats"]), FORCA_PT[v["forca"]], v["resumo"], wj))
        else:
            data.append((ref_pt(ref), ref, "não", "", "", "não descreve dever do ouvinte para com outras pessoas", wj))
    sheet("Triagem", ["Ref. (PT)", "Ref. (código)", "Selecionado", "Categoria(s)", "Força", "Resumo / motivo", "Texto (WEB, fala de Jesus)"],
          data, [9, 9, 9, 14, 10, 50, 90])

    data = []
    for ref, v in versos.items():
        just = (f"Tipo: {TIPO_PT[v['tipo']]}. Força: {FORCA_PT[v['forca']]} — {FORCA_EXPL[v['forca']]} "
                f"Destinatário: {DEST_PT[v['dest']]}. Categoria(s): {', '.join(CATEGORIAS[c]['titulo'] for c in v['cats'])}. "
                + ("Jesus entra em detalhe prático de execução. " if v["det"] else "")
                + (f"Nota: {v['nota']}." if v["nota"] else ""))
        data.append((ref_pt(ref), ref, "; ".join(v["cats"]), TIPO_PT[v["tipo"]], FORCA_PT[v["forca"]], DEST_PT[v["dest"]],
                     "sim" if v["det"] else "", v["resumo"], v["nota"], just, v["wj"]))
    sheet("Versículos", ["Ref. (PT)", "Ref. (código)", "Categoria(s)", "Tipo", "Força", "Destinatário", "Detalhe prático",
                         "Resumo do dever", "Nota", "Justificativa do julgamento", "Texto (WEB, fala de Jesus)"],
          data, [9, 9, 14, 16, 10, 16, 8, 45, 30, 70, 60])

    data = []
    for c in final:
        m = CATEGORIAS[c]
        data.append((score[c]["pos_final"], c, m["titulo"], m["demanda"], m["agrupamento"], "\n".join(m["enfases"]), m["eminencia"],
                     f"{m['rep_ref']} — {m['rep_naa']}",
                     "; ".join(ref_pt(r) for r in sorted(refs[c]["D"], key=ref_key)),
                     "; ".join(ref_pt(r) for r in sorted(refs[c]["I"], key=ref_key)),
                     "; ".join(ref_pt(r) for r in sorted(refs[c]["S"], key=ref_key))))
    sheet("Categorias", ["Prioridade", "Código", "Título", "Demanda", "Justificativa do agrupamento", "Ênfases", "Eminência explícita",
                         "Versículo representativo (NAA)", "Versículos — dever direto", "Versículos — dever indireto", "Situacionais"],
          data, [8, 8, 30, 45, 60, 50, 40, 50, 45, 45, 20])

    data = [(score[c]["pos_final"], c, CATEGORIAS[c]["titulo"], score[c]["D"], score[c]["I"], score[c]["S"], score[c]["norm"], score[c]["blocos"],
             score[c]["det"], score[c]["enf"], round(score[c]["score"], 1), score[c]["pos_contagem"], score[c]["pos_score"],
             "sim" if c in EMINENCIA else "não", just_ordenacao(c, score[c])) for c in final]
    ws = sheet("Ordenação", ["Posição final", "Código", "Categoria", "Dever direto", "Dever indireto", "Situacionais", "Versículos (D+I)",
                             "Passagens (blocos)", "Com detalhe prático", "Ênfases", "Pontuação", "Posição por contagem", "Posição por pontuação",
                             "Promovida", "Justificativa da ordenação"], data, [8, 8, 30, 8, 8, 8, 9, 9, 9, 8, 9, 9, 9, 9, 90])
    ws.append([])
    ws.append(["Regra:", f"pontuação = versículos com dever direto + {PESO_I} × versículos com dever indireto + {PESO_ENF} × blocos de ênfase. "
               "Promoção por eminência: amar o próximo (segundo maior mandamento) e as três obras nomeadas no juízo das nações (Mt 25:31-46)."])

    data = []
    for c in final:
        for atv, status, evid in ATIVIDADES.get(c, []):
            data.append((score[c]["pos_final"], c, CATEGORIAS[c]["titulo"], atv, status, evid))
    sheet("Atividades da ONG", ["Prioridade", "Código", "Dever", "Atividade", "Status", "Evidência / instrumento"], data, [8, 8, 30, 60, 14, 45])
    out = DOCS / "Deveres_Sociais_Achados.xlsx"
    wb.save(out)
    print("OK ->", out)


# ----------------------------------------------------------------- DOCX helpers
def refs_paragraph(doc, parts, size=8.5):
    p = doc.add_paragraph()
    spacing(p, after=5)
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


# ----------------------------------------------------------------- DOCX 1: documento institucional
def doc_institucional(corpus, versos, st, refs, score, final):
    n_sel = len(versos)
    n_d = sum(1 for v in versos.values() if v["forca"] == "D")
    n_det = sum(v["det"] for v in versos.values())
    doc = new_document(
        header_meta="Documento institucional    •    Base: falas de Jesus nos quatro Evangelhos    •    Tradução: NAA",
        footer_label="Deveres Sociais Ensinados por Jesus — o que a ONG pratica em obediência  •  v1.0",
    )
    title_block(doc, "DEVERES SOCIAIS ENSINADOS POR JESUS",
                "O que a Santidade Integral em Cristo pratica, intencionalmente, em obediência às instruções de Jesus",
                "Em verdade lhes digo que, sempre que vocês fizeram isso a um destes meus pequeninos irmãos, foi a mim que o fizeram.",
                "Mateus 25:40", after=6)

    section_title(doc, "", "Finalidade deste documento")
    body(doc, f"Este documento declara, de forma consolidada, por que a Santidade Integral em Cristo faz o que faz. Foram lidos os {len(corpus)} versículos "
              f"em que Jesus fala nos quatro Evangelhos e selecionados os {n_sel} em que ele descreve um dever do seu ouvinte para com outras pessoas: "
              f"alimentar, visitar, acolher, dar, amar, perdoar, honrar a família, proteger o vulnerável, agir com justiça, servir, cumprir deveres cívicos, "
              f"promover a paz, evangelizar e fazer discípulos. Em {n_d} deles o dever é explícito; em {n_det} Jesus entra em detalhe prático "
              f"('que a mão esquerda não saiba', 'convide quem não pode retribuir', 'um copo de água fria').", size=9.5)
    body(doc, "Os deveres foram organizados em 14 categorias e ordenados por prioridade. Em cada uma: o versículo que melhor a representa (Nova Almeida Atualizada), "
              "a demanda em uma frase, as atividades que a organização pratica ou planeja em obediência a ela, e, entre parênteses, em letra menor, todas as demais "
              "passagens, para que nada do que Jesus ensinou fique de fora.", size=9.5)
    p = doc.add_paragraph(); spacing(p, after=2)
    run(p, "Legenda das atividades:  ", bold=True, size=9)
    run(p, "● praticada    ◐ em implantação    ○ a definir pela diretoria", size=9)
    note(doc, "Abreviaturas: Mt = Mateus, Mc = Marcos, Lc = Lucas, Jo = João. 'Direto' = dever explícito; 'indireto' = implicado por parábola, exemplo de Jesus ou declaração; "
              "'situacional' = ordem presa à ocasião. A prioridade combina a quantidade de passagens com a eminência que o próprio Jesus dá ao tema (quadro final).", size=8.5)

    for c in final:
        m = CATEGORIAS[c]; sc = score[c]
        section_title(doc, f"{sc['pos_final']}.", m["titulo"])
        p = doc.add_paragraph(); spacing(p, after=3); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        run(p, f"“{m['rep_naa']}”  ", size=10.5, bold=True, color=GREEN)
        run(p, f"({m['rep_ref']})", size=9.5, bold=True, color=GREEN)
        body(doc, m["demanda"], size=9.5, after=3)
        p = doc.add_paragraph(); spacing(p, after=1)
        run(p, "Como a Santidade Integral em Cristo pratica:", bold=True, size=9.5)
        for atv, status, evid in ATIVIDADES.get(c, []):
            bullet(doc, atv + (f"  [{evid}]" if evid else ""), lead=STATUS_MARK[status], size=9, after=1)
        parts = [("Direto:", "; ".join(ref_pt(r) for r in sorted(refs[c]["D"], key=ref_key)) or "—")]
        if refs[c]["I"]:
            parts.append(("Indireto:", "; ".join(ref_pt(r) for r in sorted(refs[c]["I"], key=ref_key))))
        if refs[c]["S"]:
            parts.append(("Situacional:", "; ".join(ref_pt(r) for r in sorted(refs[c]["S"], key=ref_key))))
        if m["enfases"]:
            parts.append(("Ênfases:", "; ".join(e.split(" — ")[0] for e in m["enfases"])))
        refs_paragraph(doc, parts)

    doc.add_page_break()
    section_title(doc, "", "Quadro de priorização")
    tbl = [[str(sc["pos_final"]), CATEGORIAS[c]["titulo"], str(sc["D"]), str(sc["I"]), str(sc["blocos"]), str(sc["det"]), str(sc["enf"]),
            f"{sc['score']:.1f}", str(sc["pos_contagem"]), "sim" if c in EMINENCIA else ""] for c in final for sc in [score[c]]]
    table(doc, ["#", "Dever", "Direto", "Indir.", "Passag.", "Detalhe", "Ênfases", "Pontos", "Só cont.", "Eminência"],
          tbl, [0.7, 6.3, 1.1, 1.1, 1.3, 1.3, 1.3, 1.2, 1.2, 1.9], size=8)
    note(doc, f"Pontos = direto + {PESO_I} × indireto + {PESO_ENF} × ênfases. 'Passag.' = blocos de versículos contíguos. 'Só cont.' = posição se apenas o número de versículos "
              "contasse. As quatro categorias com 'eminência' foram postas no topo porque o próprio Jesus as destaca: amar o próximo é o segundo maior mandamento "
              "(Mt 22:39-40) e alimentar, visitar e hospedar são as obras nomeadas no juízo das nações (Mt 25:31-46).", size=8)

    section_title(doc, "", "Compromisso institucional")
    body(doc, "A Santidade Integral em Cristo reconhece estes deveres como instruções do seu Senhor e declara que as suas atividades de assistência e promoção "
              "familiar são praticadas, intencionalmente, em obediência a elas. As atividades marcadas como 'em implantação' ou 'a definir' constituem o plano "
              "de crescimento da organização e serão revisadas anualmente pela diretoria, com o Conselho Fiscal, à luz deste documento.", size=9.5)
    signature_row(doc, ["Presidente", "Diretoria / Coordenação Social", "Conselho Fiscal"], before=18)
    p = doc.add_paragraph(); spacing(p, before=8, after=0)
    run(p, "Aprovado em: ", bold=True, size=9); run(p, "____/____/______", size=9, color=GREY)
    body(doc, "Os textos da NAA foram transcritos para este estudo e devem ser conferidos com a edição oficial da Sociedade Bíblica do Brasil antes de publicação impressa. "
              "A planilha de achados, a metodologia e as observações acompanham este documento no repositório.", size=8.5, italic=True, color=GREY)
    finish(doc, "Deveres_Sociais_Documento_Institucional")


# ----------------------------------------------------------------- DOCX 2: metodologia
def doc_metodologia(corpus, versos, score, final):
    doc = new_document(header_meta="Documento de projeto    •    Pesquisa 2: deveres sociais nas falas de Jesus",
                       footer_label="Deveres Sociais — Projeto e Metodologia  •  v1.0")
    title_block(doc, "PROJETO E METODOLOGIA",
                "Levantamento das falas de Jesus que descrevem deveres do ouvinte para com a sociedade",
                "Vá e faça o mesmo.", "Lucas 10:37")
    section_title(doc, "1", "Definição do projeto")
    body(doc, "Identificar, em todas as falas de Jesus registradas nos quatro Evangelhos, aquelas em que ele descreve uma relação de dever do seu ouvinte "
              "para com outras pessoas e para com a sociedade; organizá-las em categorias, preservando o versículo exato; quantificar, ordenar por prioridade "
              "e justificar cada julgamento; e produzir um documento consolidado em que a Santidade Integral em Cristo declara as atividades que pratica, "
              "intencionalmente, em obediência a essas instruções.")
    section_title(doc, "2", "O que foi entendido do pedido (reformulação em termos do estudo)")
    body(doc, "A primeira pesquisa deste repositório usou um filtro gramatical (modo imperativo). Esta usa um filtro semântico: o conteúdo da fala, não a sua forma. "
              "Em termos de teologia moral, o recorte é a chamada 'segunda tábua' da Lei — os deveres para com o próximo — tal como Jesus os ensina, estende e "
              "radicaliza. Ficam de fora os deveres para com Deus em si (adorar, orar, temer), os deveres para consigo (pureza interior, vigilância, fé pessoal) "
              "e as declarações cristológicas e escatológicas, exceto quando essas falas descrevem explicitamente o que se deve fazer a outra pessoa. "
              "Evangelizar e fazer discípulos foram incluídos, conforme o pedido, por serem deveres do discípulo para com o mundo.")
    body(doc, "Sem o filtro gramatical, o dever pode aparecer como ordem ('deem-lhes vocês de comer'), ensino ('quem recebe uma criança em meu nome…'), parábola "
              "(bom samaritano), critério do juízo ('tive fome e me deram de comer'), bem-aventurança ('os misericordiosos'), advertência ('ai dos que devoram "
              "as casas das viúvas') ou modelo de Jesus ('o Filho do Homem veio para servir'). Cada versículo recebeu um tipo e uma força normativa.")
    section_title(doc, "3", "Fontes e ferramentas")
    bullet(doc, "World English Bible (USFM), marcador \\wj: define o corpus — 1.955 versículos com fala de Jesus. Arquivos comuns em comum/dados.", lead="Falas de Jesus:")
    bullet(doc, "SBLGNT/MorphGNT disponível para consulta do grego; não é critério de seleção nesta pesquisa.", lead="Grego:")
    bullet(doc, "Nova Almeida Atualizada (SBB, 2017) para os versículos representativos do documento final.", lead="Tradução:")
    bullet(doc, "Python (python-docx, openpyxl), LibreOffice; código em pesquisa-2-deveres-sociais/.", lead="Ferramentas:")
    section_title(doc, "4", "Etapas do método")
    for i, e in enumerate([
        "Corpus: extração dos 1.955 versículos com fala de Jesus, em ordem canônica, com o texto marcado.",
        "Leitura integral: cada versículo foi lido e classificado como 'descreve dever do ouvinte para com outros' ou não. A aba 'Triagem' registra o resultado para todos.",
        "Julgamento dos selecionados: categoria(s), tipo (ordem, ensino, parábola, juízo, bem-aventurança, advertência, modelo, citação), força normativa "
        "(direta, indireta, situacional), destinatário, presença de detalhe prático, resumo e nota.",
        "Taxonomia: 14 categorias definidas a partir das ocorrências, cada uma com justificativa do agrupamento, ênfases e versículo representativo.",
        "Quantificação: versículos por força, passagens (blocos contíguos, para mitigar a inflação por paralelos), detalhes práticos e blocos de ênfase.",
        "Ordenação: pontuação = direto + 0,5 × indireto + ênfases; promoção das categorias que Jesus destaca explicitamente (Mt 22:39-40; Mt 25:31-46).",
        "Mapa de obediência: para cada dever, as atividades que a ONG pratica ou planeja, com status e evidência documental (proposta a validar).",
        "Produtos: planilha de achados, documento institucional, este documento e as observações.",
    ], 1):
        bullet(doc, e, lead=f"{i}.")
    section_title(doc, "5", "Critérios de julgamento")
    body(doc, "Critério de seleção: a fala de Jesus descreve algo que o ouvinte deve fazer, deixar de fazer ou ser em relação a outra pessoa ou grupo "
              "(próximo, inimigo, irmão, criança, pais, cônjuge, pobre, enfermo, preso, forasteiro, autoridade, nações). Falas sobre Deus, sobre o próprio Jesus "
              "ou sobre o foro íntimo entram só quando contêm essa relação (ex.: 'misericórdia quero, e não sacrifício').")
    for k, v in FORCA_EXPL.items():
        bullet(doc, v, lead=f"Força {FORCA_PT[k]} ({k}):")
    body(doc, "Exemplos: 'convide os pobres' é ordem direta; 'o samaritano cuidou dele' é parábola com dever direto (Jesus conclui 'vá e faça o mesmo'); "
              "'um amigo chegou de viagem e não tenho o que lhe oferecer' é parábola com dever indireto (pressupõe hospitalidade); 'mostre-se ao sacerdote' é situacional.")
    section_title(doc, "6", "Taxonomia")
    for c in final:
        bullet(doc, CATEGORIAS[c]["agrupamento"], lead=f"{score[c]['pos_final']}. {CATEGORIAS[c]['titulo']} —", size=9)
    section_title(doc, "7", "Regra de priorização")
    body(doc, f"Pontuação = versículos com dever direto + {PESO_I} × versículos com dever indireto + {PESO_ENF} × blocos de ênfase. Sobre essa ordem aplicou-se um "
              "único ajuste: amar o próximo (o segundo maior mandamento, Mt 22:39-40) e as três obras nomeadas no juízo das nações — alimentar, visitar o enfermo "
              "e o preso, hospedar o forasteiro (Mt 25:31-46) — foram promovidas ao topo, porque o próprio Jesus as hierarquiza. A planilha mostra as três ordens.")
    section_title(doc, "8", "Produtos e reprodução")
    bullet(doc, "Deveres_Sociais_Documento_Institucional.docx/.pdf — documento consolidado da ONG.")
    bullet(doc, "Deveres_Sociais_Achados.xlsx — triagem, versículos, categorias, ordenação, atividades.")
    bullet(doc, "Projeto_e_Metodologia e Observacoes_e_Reflexoes (DOCX/PDF).")
    body(doc, "Para reproduzir: `python3 comum/preparar_dados.py` e `python3 pesquisa-2-deveres-sociais/construir.py`. Para alterar um julgamento, edite "
              "dados/rotulos.py; para ajustar o status de uma atividade, edite dados/atividades_ong.py.", size=9.5)
    finish(doc, "Projeto_e_Metodologia")


# ----------------------------------------------------------------- DOCX 3: observações
def doc_observacoes(corpus, versos, score, final):
    doc = new_document(header_meta="Documento de projeto    •    Pontos de atenção sobre a metodologia",
                       footer_label="Deveres Sociais — Observações e Reflexões  •  v1.0")
    title_block(doc, "OBSERVAÇÕES E REFLEXÕES",
                "Pontos de atenção observados durante a seleção, o agrupamento e a priorização",
                "Portanto, tudo o que vocês querem que as pessoas lhes façam, façam também vocês a elas.", "Mateus 7:12")
    top = final[:4]
    obs = [
        ("A fronteira do 'dever social' é um juízo, não um filtro mecânico.",
         "Diferente da pesquisa 1, aqui não há critério gramatical: cada versículo foi lido e julgado. Casos de fronteira foram decididos e documentados: 'orem pelos "
         "que os perseguem' entrou (é dever para com o inimigo); 'amem a Deus' não entrou; 'não sejam chamados Rabi' entrou como dever de servir; 'não acumulem "
         "tesouros' não entrou (dever para consigo), mas 'vendam e deem esmola' entrou. Outro leitor pode traçar a linha em outro lugar; a aba 'Triagem' permite auditar."),
        ("Evangelizar e fazer discípulos como deveres sociais.",
         "Foram incluídos por pedido explícito e porque Jesus os formula como dever para com 'todas as nações' e 'toda criatura'. Mas são de natureza distinta das "
         "obras de misericórdia: não respondem a uma carência material. O documento institucional os mantém em categorias próprias para que a ONG decida com clareza "
         "como os pratica, sem confundi-los com assistência."),
        ("O peso de Mateus 25.",
         "O juízo das nações nomeia seis obras (fome, sede, forasteiro, nudez, enfermidade, prisão) e foi o único trecho tratado como 'eminência explícita' ao lado do "
         "segundo maior mandamento. Isso promove Alimentar, Cuidar dos enfermos e Acolher o forasteiro ao topo, acima de categorias com mais versículos. É uma decisão "
         "teológica, declarada e reversível na planilha."),
        ("Parábolas e exemplo de Jesus contam com peso menor.",
         "O bom samaritano, o rico e Lázaro, o credor incompassivo e a declaração 'o Filho do Homem veio para servir' ensinam deveres com força inegável, mas "
         "não na forma de ordem. Receberam força 'direta' quando Jesus conclui com uma ordem ('vá e faça o mesmo') e 'indireta' nos demais casos (peso 0,5)."),
        ("Paralelos sinóticos inflam a contagem; os 'blocos' mitigam.",
         "'Deem a César' aparece três vezes; 'deem-lhes vocês de comer' também. Além da contagem de versículos, a planilha conta passagens como blocos de versículos "
         "contíguos, o que reduz, mas não elimina, o efeito. Uma contagem por perícope única exigiria harmonização dos Evangelhos, deixada para trabalho futuro."),
        ("Categorias se sobrepõem por desenho.",
         "'Convide os pobres' é hospitalidade, alimentação e generosidade ao mesmo tempo; 'curem os enfermos… de graça deem' é cuidado, missão e generosidade. "
         "Permitiu-se mais de uma categoria por versículo. A soma das categorias excede o número de versículos; isso é intencional."),
        ("As denúncias ('ais') foram lidas como deveres negativos.",
         "'Devoram as casas das viúvas', 'atam fardos pesados', 'fecham o Reino' não são ordens, mas descrevem com precisão o que não se deve fazer aos outros. "
         "Entraram como advertências com força direta. Um leitor mais estrito pode rebaixá-las a 'indireta'."),
        ("Dependência da marcação de letras vermelhas.",
         "O corpus é o da World English Bible. Falas de terceiros aprovadas por Jesus (a resposta do intérprete da Lei em Lc 10:27, a confissão de Zaqueu em Lc 19:8) "
         "não estão no corpus, embora Jesus as endosse; aparecem apenas pelas falas de Jesus que as confirmam (Lc 10:28; 19:9)."),
        ("Texto crítico e passagens disputadas.",
         "Mc 16:15-18, Jo 7:53–8:11, Lc 9:55-56, Mt 23:14 e Mc 11:26 estão ausentes ou entre colchetes nas edições críticas. Foram incluídos com nota, porque "
         "constam das Bíblias de uso corrente, mas a planilha os identifica para quem preferir excluí-los."),
        ("Os textos da NAA foram transcritos de memória.",
         "Não houve acesso a fonte digital licenciada da Nova Almeida Atualizada. Os 14 versículos representativos devem ser conferidos com a edição da SBB antes "
         "de impressão. As demais passagens aparecem só por referência."),
        ("O mapa de atividades é uma proposta.",
         "As atividades listadas por categoria foram inferidas dos documentos institucionais já produzidos (anamnese, prestação de contas, política de boas práticas). "
         "Os status 'praticada', 'em implantação' e 'a definir' precisam ser confirmados pela diretoria. O arquivo dados/atividades_ong.py foi feito para isso."),
        ("Achado que vale registrar: onde Jesus mais detalha.",
         "Os versículos com detalhe prático concentram-se em dar (em secreto, sem retorno, a quem não pode retribuir), em reconciliar (a sós, com testemunhas, "
         "diante da igreja) e nas obras de Mt 25. Para uma organização, isso sugere que o 'como' importa tanto quanto o 'quê': discrição do doador, dignidade do "
         "beneficiário e ausência de contrapartida são parte do mandamento, não acessórios."),
        ("Achado que vale registrar: o inimigo e o estranho.",
         f"Boa parte dos deveres sociais de Jesus é dirigida a quem não pertence ao grupo: inimigos, forasteiros, publicanos, samaritanos, pobres que não podem retribuir. "
         f"As quatro categorias promovidas ({', '.join(CATEGORIAS[c]['titulo'].split(';')[0].split(':')[0] for c in top)}) têm isso em comum."),
        ("Risco pastoral: obediência sem graça.",
         "Um catálogo de deveres pode ser lido como mérito. O próprio material impede essa leitura: 'de graça receberam, de graça deem' (Mt 10:8) coloca a gratuidade "
         "recebida antes da gratuidade praticada. Recomenda-se que o documento institucional seja ensinado a partir daí."),
        ("Reprodutibilidade.",
         "A triagem completa, os julgamentos e as regras estão em arquivos editáveis; qualquer discordância pode ser corrigida em uma linha e os documentos "
         "regenerados em minutos."),
    ]
    for i, (t, txt) in enumerate(obs, 1):
        p = doc.add_paragraph(); spacing(p, before=4, after=1); p.paragraph_format.keep_with_next = True
        run(p, f"{i}. {t}", bold=True, size=10, color=GREEN)
        body(doc, txt, size=9.5, after=4)
    finish(doc, "Observacoes_e_Reflexoes")


if __name__ == "__main__":
    corpus, versos = load()
    st, refs, score, final = stats(versos)
    xlsx(corpus, versos, st, refs, score, final)
    doc_institucional(corpus, versos, st, refs, score, final)
    doc_metodologia(corpus, versos, score, final)
    doc_observacoes(corpus, versos, score, final)
    print("\nOrdem final:", " > ".join(f"{score[c]['pos_final']}.{c}" for c in final))
