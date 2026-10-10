# Os Mandamentos de Jesus — Santidade Integral em Cristo

Levantamento de **todas as ordens de Jesus nos quatro Evangelhos expressas no modo
imperativo do grego**, agrupadas em categorias (à maneira de John Piper, *What Jesus
Demands from the World*) e ordenadas por prioridade, com o fim de promover a
obediência a Cristo: "ensinando-os a guardar todas as coisas que tenho ordenado a
vocês" (Mt 28:20).

## Produtos (pasta `docs/`)

| Arquivo | O que é |
|---|---|
| `Mandamentos_de_Jesus.docx` / `.pdf` | **Documento final** para a prática: 17 categorias priorizadas, versículo representativo (NAA) e todas as demais passagens entre parênteses |
| `Mandamentos_de_Jesus_Achados.xlsx` | Todos os achados: cada imperativo, cada versículo com seus julgamentos, categorias, ordenação, complemento, excluídos e glossário |
| `Projeto_e_Metodologia.docx` / `.pdf` | Definição do projeto, reformulação em termos de estudo teológico, fontes, conceitos, etapas, critérios e regra de priorização |
| `Observacoes_e_Reflexoes.docx` / `.pdf` | Pontos de atenção metodológicos observados durante o trabalho |

## Método em uma frase

MorphGNT (SBLGNT com morfologia) → filtrar modo imperativo em Mt/Mc/Lc/Jo → cruzar com
as falas de Jesus marcadas na World English Bible (`\wj`) via números de Strong → revisar
casos ambíguos → julgar destinatário e alcance de cada versículo → categorizar → somar
passagens, complemento e ênfases → promover as categorias que o próprio Jesus hierarquiza.

## Números

- 843 verbos no imperativo nos quatro Evangelhos; 678 em versículos com fala de Jesus
- 482 versículos classificados um a um (`dados/rotulos.py`)
- 267 passagens normativas (universais ou generalizáveis) em 17 categorias
- 54 ordens em formas não imperativas no complemento (marcadas †)

## Reproduzir

```bash
python3 preparar_dados.py   # baixa MorphGNT, WEB e Strong's; gera dados/*.json
python3 construir.py        # aplica rótulos, glossário, complemento e taxonomia; gera docs/
```

Para alterar um julgamento, edite a linha correspondente em `dados/rotulos.py`
(destinatário, alcance, categoria, resumo, nota) e rode `construir.py` de novo.

## Fontes

- SBLGNT + MorphGNT (CC BY-SA 3.0) — texto grego e morfologia
- World English Bible, USFM (domínio público) — marcação das palavras de Jesus
- Dicionário de Strong, Open Scriptures (CC BY-SA) — ponte grego–inglês
- Nova Almeida Atualizada (SBB, 2017) — versículos representativos. **Os textos foram
  transcritos de memória e devem ser conferidos com a edição oficial antes de impressão.**

O papel timbrado (`timbrado.py`, `assets/logo.png`) é o mesmo do repositório
`santidade-integral-documentos`.
