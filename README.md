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

Duas etapas, preservadas em subpastas:

**`01-levantamento-inicial/`** — a busca inicial e o documento institucional
- `Deveres_Sociais_Documento_Institucional.docx/.pdf` — 14 deveres priorizados, versículo representativo (NAA), atividades da ONG com status, demais passagens entre parênteses
- `Deveres_Sociais_Achados.xlsx` — triagem dos 1.955 versículos, 384 julgados, categorias, ordenação, atividades
- `Projeto_e_Metodologia.*`, `Observacoes_e_Reflexoes.*`

**`02-lista-de-praticas/`** — o produto principal: a lista de afazeres do voluntário, à maneira das obras de misericórdia metodistas
- `Lista_de_Praticas_do_Voluntario.docx/.pdf` — 52 ações concretas em 7 grupos (corpo, alma, reconciliação, dar, família, serviço, paz/justiça), cada uma com "como fazer agora", versículo-base, demais versículos e caixas hoje/semana/mês; exame semanal
- `Cartao_de_Bolso.docx/.pdf` — uma página com as 52 práticas e caixas de marcação
- `Lista_de_Praticas_Rastreabilidade.xlsx` — cada prática ligada aos versículos julgados na etapa 1, justificativa, paralelo metodista, versículos não usados e motivo

Método: leitura integral das 1.955 falas de Jesus → seleção pelo critério "descreve dever do ouvinte para com outras pessoas" → tipo (ordem, ensino, parábola, juízo, bem-aventurança, advertência, modelo, citação), força (direta, indireta, situacional), detalhe prático → categorias → pontuação + eminência (Mt 22:39-40; Mt 25:31-46) → mapa de obediência da ONG (`dados/atividades_ong.py`, a validar pela diretoria) → etapa 2: 52 práticas imediatas (`dados/praticas.py`).

## Reproduzir

```bash
python3 comum/preparar_dados.py                       # fontes comuns
python3 pesquisa-1-imperativos/extrair_imperativos.py # imperativos (pesquisa 1)
python3 pesquisa-1-imperativos/construir.py           # docs da pesquisa 1
python3 pesquisa-2-deveres-sociais/construir.py           # etapa 1 (levantamento)
python3 pesquisa-2-deveres-sociais/construir_praticas.py  # etapa 2 (lista de práticas)
```

Para alterar um julgamento, edite a linha correspondente em `dados/rotulos.py` da pesquisa e rode o `construir.py`.

## Fontes

- SBLGNT + MorphGNT (CC BY-SA 3.0); World English Bible, USFM (domínio público); Dicionário de Strong, Open Scriptures (CC BY-SA)
- Nova Almeida Atualizada (SBB, 2017) — versículos representativos. **Transcritos de memória; conferir com a edição oficial antes de imprimir.**
