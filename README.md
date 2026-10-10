# Os Mandamentos de Jesus — Santidade Integral em Cristo

Pesquisas bíblicas da ONG sobre o que Jesus ordenou e ensinou nos quatro Evangelhos,
com documentos timbrados (DOCX/PDF), planilhas de achados (XLSX) e código reprodutível.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `comum/` | Fontes e dados comuns: `preparar_dados.py` (baixa MorphGNT, WEB e Strong's; gera `dados/web_redletter.json`) e `biblia.py` (acesso aos dados) |
| `pesquisa-1-imperativos/` | **Pesquisa 1** — todas as ordens de Jesus no **modo imperativo** do grego, em 17 categorias priorizadas (à maneira de John Piper) |
| `pesquisa-2-deveres-sociais/` | **Pesquisa 2** — todas as falas de Jesus que descrevem um **dever do ouvinte para com a sociedade** (sem filtro gramatical), em 14 categorias priorizadas, com o mapa das atividades da ONG |
| `timbrado.py`, `assets/` | Papel timbrado da ONG (mesmo do repositório `santidade-integral-documentos`) |

Cada pesquisa tem `construir.py`, `dados/` (rótulos editáveis com os julgamentos) e `docs/`
(documento final, planilha de achados, Projeto e Metodologia, Observações e Reflexões).

## Pesquisa 1 — Imperativos (`pesquisa-1-imperativos/docs/`)

- `Mandamentos_de_Jesus.docx/.pdf` — documento final: 17 categorias, versículo representativo (NAA) e demais passagens entre parênteses
- `Mandamentos_de_Jesus_Achados.xlsx` — 843 imperativos, 482 versículos julgados, categorias, ordenação, complemento (†), excluídos, glossário
- `Projeto_e_Metodologia.*`, `Observacoes_e_Reflexoes.*`

Método: MorphGNT → modo imperativo em Mt/Mc/Lc/Jo → cruzamento com as falas de Jesus (WEB `\wj`) → julgamento de destinatário e alcance → categorias → pontuação + eminência explícita.

## Pesquisa 2 — Deveres sociais (`pesquisa-2-deveres-sociais/docs/`)

- `Deveres_Sociais_Documento_Institucional.docx/.pdf` — documento consolidado da ONG: 14 deveres priorizados, versículo representativo (NAA), atividades praticadas/planejadas com status, demais passagens entre parênteses, compromisso institucional
- `Deveres_Sociais_Achados.xlsx` — triagem dos 1.955 versículos com fala de Jesus, versículos selecionados com julgamento, categorias, ordenação, atividades da ONG
- `Projeto_e_Metodologia.*`, `Observacoes_e_Reflexoes.*`

Método: leitura integral das 1.955 falas de Jesus → seleção pelo critério "descreve dever do ouvinte para com outras pessoas" → tipo (ordem, ensino, parábola, juízo, bem-aventurança, advertência, modelo, citação), força (direta, indireta, situacional), detalhe prático → categorias → pontuação + eminência (Mt 22:39-40; Mt 25:31-46) → mapa de obediência da ONG (`dados/atividades_ong.py`, a validar pela diretoria).

## Reproduzir

```bash
python3 comum/preparar_dados.py                       # fontes comuns
python3 pesquisa-1-imperativos/extrair_imperativos.py # imperativos (pesquisa 1)
python3 pesquisa-1-imperativos/construir.py           # docs da pesquisa 1
python3 pesquisa-2-deveres-sociais/construir.py       # docs da pesquisa 2
```

Para alterar um julgamento, edite a linha correspondente em `dados/rotulos.py` da pesquisa e rode o `construir.py`.

## Fontes

- SBLGNT + MorphGNT (CC BY-SA 3.0); World English Bible, USFM (domínio público); Dicionário de Strong, Open Scriptures (CC BY-SA)
- Nova Almeida Atualizada (SBB, 2017) — versículos representativos. **Transcritos de memória; conferir com a edição oficial antes de imprimir.**
