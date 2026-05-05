# Gurudev Programacao Comparada

> Schema Alexandria v3.1 — O primeiro protocolo formal de catalogacao para **Programacao Comparada**

[![Working Paper](https://img.shields.io/badge/Working_Paper-DOI_10.5281%2Fzenodo.20028887-blue)](https://doi.org/10.5281/zenodo.20028887)
[![Schema v3.1](https://img.shields.io/badge/Schema-v3.1-green)](corpus/schema/alexandria-v3.1.json)
[![License: Code](https://img.shields.io/badge/License-Code-Apache_2.0-orange.svg)](LICENSE)
[![License: Data](https://img.shields.io/badge/License-Data-CC_BY_4.0-lightgrey.svg)](LICENSE-DATA)

---

## Para Investidores e Parceiros

| | |
|---|---|
| **Pitch Deck** | [PITCH/Pitch_Deck_Alexandria.pdf](PITCH/Pitch_Deck_Alexandria.pdf) |
| **Roadmap 24 meses** | [ROADMAP.md](ROADMAP.md) |
| **Modelo de Negocio** | [COMMERCIAL/README.md](COMMERCIAL/README.md) |

---

## O que e Programacao Comparada?

Inspirada em Literatura Comparada, Direito Comparado e Gramatica Comparada, a **Programacao Comparada (ProCP)** e uma nova disciplina que estuda linguagens de programacao como objetos de estudo cientifico — atraves de analise sistematica, semiotica e hermeneutica comparativa, visando compreender principios universais e facilitar interoperabilidade.

O **Schema Alexandria v3.1** e o protocolo formal que operacionaliza essa disciplina: cada linguagem e catalogada em **14 blocos analiticos validaveis automaticamente** via JSON Schema, fundamentados em TATS (Teoria da Analogia), GILP (Gramatica de Interfaces de Linguagens de Programacao, 5 camadas) e Analise Savigny (4 dimensoes hermeneuticas).

**Working Paper**: Machado, G. G. (2026). [DOI: 10.5281/zenodo.20028887](https://doi.org/10.5281/zenodo.20028887)

---

## Estrutura do Repositorio

```
gurudev-programacao-comparada/
├── corpus/                              # FONTE DA VERDADE (Schema Alexandria)
│   ├── schema/alexandria-v3.1.json      # JSON Schema formal (381 linhas)
│   ├── entries/python.yaml               # Entry-exemplo validada 14/14 blocos
│   └── README.md                         # Documentacao do corpus
├── data/                                # Banco de dados legado (pre-schema)
│   ├── comparative_programming.json      # Prototipo anterior ao schema
│   └── README.md                         # Nota: separacao de camadas
├── scripts/
│   └── validate_corpus.py                # POC: validacao automatica
├── gurudev/                              # Pacote Python (Apache 2.0)
├── COMMERCIAL/
│   ├── README.md                         # Visao geral do modelo de negocio
│   ├── modelo-freemium.md                # Arquitetura freemium detalhada
│   └── spinoffs.md                       # Mapa de spinoffs com fases
├── PITCH/
│   └── Pitch_Deck_Alexandria.pdf         # Pitch deck para investidores
├── docs/
│   ├── strategic/                        # Documentacao estrategica
│   └── working-paper/                    # Working Paper publicado
├── ROADMAP.md                            # Roteiro estrategico publico
├── LICENSE                               # Apache 2.0 (codigo)
├── LICENSE-DATA                          # CC BY 4.0 (conteudo)
└── README.md                             # Voce esta aqui
```

> **Nota**: `corpus/` e a fonte da verdade cientifica do Schema Alexandria. `data/` e um banco de dados legado com estrutura independente, mantido para a biblioteca de interoperabilidade. As duas camadas tem propositos distintos.

---

## Schema Alexandria v3.1 — 14 Blocos

| Bloco | Descricao | Fundamento Teorico |
|-------|-----------|-------------------|
| 1. Metadados | Identificacao e rastreabilidade | Fase gramatical (WP Secao 8.4) |
| 2. Classificacao ProCP | 7 eixos + era historica | Estrutura ProCP, GILP |
| 3. Status de Mercado | Rankings, tendencias | Camada ecossistemica |
| 4. Metafora Fundante | Nucleo semiotico — imagem central | TATS (3 modos de analogia) |
| 5. Interface Grammar (GILP) | 5 camadas: cognitiva, infraestrutural, sistemica, ecossistemica, cultural | GILP (Secao 5.4) |
| 6. Analise Savigny | 4 dimensoes: gramatical, semantica, historica, sistematica | Savigny (Secao 6.2) |
| 7. Sintatico | Inventario de constructos sintaticos | Estrutura superficial vs. profunda |
| 8. Lexico | Inventario lexical completo | Lexicologia comparada |
| 9. Sistema de Tipos | Primitivos, genericos, algebricos | Camada infraestrutural |
| 10. Comparativo | Analogias e contrastes entre linguagens | TATS, espiral comparativa |
| 11. Ecossistema | Licencas, frameworks, comunidades | Camada ecossistemica |
| 12. Ordenacao | Metadados de navegacao | Funcional |
| 13. Acesso | Modelo de disponibilizacao (Free/Freemium/Paid) | Secoes 2.5 e 3.4 |
| 14. Semiotico (Peirce) | Relacao iconica/indicial/simbolica, estrutura triadica | Peirce — bloco opcional v3.1 |

---

## Validacao Automatica (POC)

O corpus e validado automaticamente contra o JSON Schema:

```bash
pip install jsonschema pyyaml
python scripts/validate_corpus.py
```

Resultado esperado: **14/14 blocos validados** (Python como entry-exemplo).

---

## Modelo de Negocio Freemium

| Camada | Preco | Conteudo |
|--------|-------|----------|
| **Free** | Aberto | Metadados, ProCP, metafora fundante parcial |
| **Freemium** | Registro | GILP completa, Savigny, busca avancada, API basica |
| **Explorer** | USD 9/mes | API ilimitada, comparacao multi-linguagem |
| **Professional** | USD 39/mes | Alexandria LLM, dashboards, certificacoes |
| **Enterprise** | USD 200-500/mes | On-premise, consulting, SLA |

Principio: o conteudo analitico de alta densidade teorica e **sempre acessivel**. Camadas de conveniencia e ferramenta sao monetizaveis. A integridade epistemologica nao e negociavel.

Detalhes completos: [COMMERCIAL/modelo-freemium.md](COMMERCIAL/modelo-freemium.md)

---

## Spinoffs

| Fase | Spinoff | Risco | Retorno |
|------|---------|-------|---------|
| 0-6m | Alexandria Insights | Baixo | Medio |
| 0-6m | Alexandria LLM Alpha (wrapper) | Baixo | Medio |
| 6-12m | Alexandria Academy | Medio | Alto |
| 6-12m | Alexandria for Teams | Medio | Alto |
| 12-18m | Alexandria Consulting | Baixo | Medio |
| 12-18m | Alexandria Journal | Baixo | Baixo |
| 12-18m | Alexandria LLM (fine-tuning) | Medio | Alto |
| 18-24m | Alexandria Games | Alto | Medio |

> **Alexandria LLM** foi dividida em duas fases. O Alpha (wrapper de prompt) e viável nos primeiros 6 meses. O fine-tuning, que requer corpus maduro (50+ entries), foi realocado para a Fase 3.

Detalhes completos: [COMMERCIAL/spinoffs.md](COMMERCIAL/spinoffs.md) | [ROADMAP.md](ROADMAP.md)

---

## Dodecagogo Gurudev

1. Simplicidade Elegante sobre complexidade desnecessaria
2. Expressividade Clara sobre otimizacao prematura
3. Interoperabilidade Universal sobre isolamento linguistico
4. Seguranca por Design sobre correcao posterior
5. Composabilidade sobre monolitismo
6. Imutabilidade Padrao sobre mutabilidade irrestrita
7. Tipagem Gradual sobre extremos absolutos
8. Concorrencia Cooperativa sobre competicao destrutiva
9. Metaprogramacao Responsavel sobre magia excessiva
10. Evolucao Incremental sobre revolucoes disruptivas
11. Documentacao Viva sobre comentarios mortos
12. Comunidade Inclusiva sobre elitismo tecnico

---

## Casos de Uso

**Educacao**: Ensino comparativo de linguagens, curriculos multi-paradigmaticos, avaliacao de proficiencia cross-linguagem.

**Industria**: Migracao de sistemas legados, integracao de equipes multi-linguagem, decisoes de stack tecnologico fundamentadas em analise semiotica.

**Pesquisa**: Analise de evolucao de linguagens, desenvolvimento de DSLs, estudos de usabilidade linguistica.

---

## Instalacao

```bash
pip install gurudev-comparative-programming
```

---

## Licenca

Este repositorio utiliza duas licencas distintas para separar codigo de conteudo:

| Camada | Arquivos | Licenca |
|--------|----------|---------|
| **Codigo** | `gurudev/`, `scripts/`, `setup.py`, `pyproject.toml` | Apache 2.0 ([LICENSE](LICENSE)) |
| **Conteudo** | `corpus/`, `data/`, `docs/`, `COMMERCIAL/`, `ROADMAP.md` | CC BY 4.0 ([LICENSE-DATA](LICENSE-DATA)) |

> Ver [data/README.md](data/README.md) para a documentacao da separacao entre `corpus/` e `data/`.

---

## Autor

**Guilherme Goncalves Machado** — Hubstry DeepTech

- **Working Paper**: [DOI: 10.5281/zenodo.20028887](https://doi.org/10.5281/zenodo.20028887)
- **Repositorio**: [github.com/Hubstry-DeepTech/gurudev-programacao-comparada](https://github.com/Hubstry-DeepTech/gurudev-programacao-comparada)
