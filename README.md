# Gurudev Programação Comparada

> Schema Alexandria v3.1 — O primeiro protocolo formal de catalogação para **Programação Comparada**

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
| **Modelo de Negócio** | [COMMERCIAL/README.md](COMMERCIAL/README.md) |

---

## O que é Programação Comparada?

Inspirada em Literatura Comparada, Direito Comparado e Gramática Comparada, a **Programação Comparada (ProCP)** é uma nova disciplina que estuda linguagens de programação como objetos de estudo científico — através de análise sistemática, semiótica e hermenêutica comparativa, visando compreender princípios universais e facilitar interoperabilidade.

O **Schema Alexandria v3.1** é o protocolo formal que operacionaliza essa disciplina: cada linguagem é catalogada em **14 blocos analíticos validáveis automaticamente** via JSON Schema, fundamentados em TATS (Teoria da Analogia), GILP (Gramática de Interfaces de Linguagens de Programação, 5 camadas) e Análise Savigny (4 dimensões hermenêuticas).

**Working Paper**: Machado, G. G. (2026). [DOI: 10.5281/zenodo.20028887](https://doi.org/10.5281/zenodo.20028887)

---

## Estrutura do Repositório

```
gurudev-programacao-comparada/
├── corpus/                              # FONTE DA VERDADE (Schema Alexandria)
│   ├── schema/alexandria-v3.1.json      # JSON Schema formal (381 linhas)
│   ├── entries/python.yaml               # Entry-exemplo validada 14/14 blocos
│   └── README.md                         # Documentação do corpus
├── data/                                # Banco de dados legado (pré-schema)
│   ├── comparative_programming.json      # Protótipo anterior ao schema
│   └── README.md                         # Nota: separação de camadas
├── scripts/
│   └── validate_corpus.py                # POC: validação automática
├── gurudev/                              # Pacote Python (Apache 2.0)
├── COMMERCIAL/
│   ├── README.md                         # Visão geral do modelo de negócio
│   ├── modelo-freemium.md                # Arquitetura freemium detalhada
│   └── spinoffs.md                       # Mapa de spinoffs com fases
├── PITCH/
│   └── Pitch_Deck_Alexandria.pdf         # Pitch deck para investidores
├── docs/
│   ├── strategic/                        # Documentação estratégica
│   └── working-paper/                    # Working Paper publicado
├── ROADMAP.md                            # Roteiro estratégico público
├── LICENSE                               # Apache 2.0 (código)
├── LICENSE-DATA                          # CC BY 4.0 (conteúdo)
└── README.md                             # Você está aqui
```

> **Nota**: `corpus/` é a fonte da verdade científica do Schema Alexandria. `data/` é um banco de dados legado com estrutura independente, mantido para a biblioteca de interoperabilidade. As duas camadas têm propósitos distintos.

---

## Schema Alexandria v3.1 — 14 Blocos

| Bloco | Descrição | Fundamento Teórico |
|-------|-----------|-------------------|
| 1. Metadados | Identificação e rastreabilidade | Fase gramatical (WP Seção 8.4) |
| 2. Classificação ProCP | 7 eixos + era histórica | Estrutura ProCP, GILP |
| 3. Status de Mercado | Rankings, tendências | Camada ecossistêmica |
| 4. Metáfora Fundante | Núcleo semiótico — imagem central | TATS (3 modos de analogia) |
| 5. Interface Grammar (GILP) | 5 camadas: cognitiva, infraestrutural, sistêmica, ecossistêmica, cultural | GILP (Seção 5.4) |
| 6. Análise Savigny | 4 dimensões: gramatical, semântica, histórica, sistemática | Savigny (Seção 6.2) |
| 7. Sintático | Inventário de constructos sintáticos | Estrutura superficial vs. profunda |
| 8. Léxico | Inventário lexical completo | Lexicologia comparada |
| 9. Sistema de Tipos | Primitivos, genéricos, algébricos | Camada infraestrutural |
| 10. Comparativo | Analogias e contrastes entre linguagens | TATS, espiral comparativa |
| 11. Ecossistema | Licenças, frameworks, comunidades | Camada ecossistêmica |
| 12. Ordenação | Metadados de navegação | Funcional |
| 13. Acesso | Modelo de disponibilização (Free/Freemium/Paid) | Seções 2.5 e 3.4 |
| 14. Semiótico (Peirce) | Relação icônica/indicial/simbólica, estrutura triádica | Peirce — bloco opcional v3.1 |

---

## Validação Automática (POC)

O corpus é validado automaticamente contra o JSON Schema:

```bash
pip install jsonschema pyyaml
python scripts/validate_corpus.py
```

Resultado esperado: **14/14 blocos validados** (Python como entry-exemplo).

---

## Modelo de Negócio Freemium

| Camada | Preço | Conteúdo |
|--------|-------|----------|
| **Free** | Aberto | Metadados, ProCP, metáfora fundante parcial |
| **Freemium** | Registro | GILP completa, Savigny, busca avançada, API básica |
| **Explorer** | USD 9/mês | API ilimitada, comparação multi-linguagem |
| **Professional** | USD 39/mês | Alexandria LLM, dashboards, certificações |
| **Enterprise** | USD 200-500/mês | On-premise, consulting, SLA |

Princípio: o conteúdo analítico de alta densidade teórica é **sempre acessível**. Camadas de conveniência e ferramenta são monetizáveis. A integridade epistemológica não é negociável.

Detalhes completos: [COMMERCIAL/modelo-freemium.md](COMMERCIAL/modelo-freemium.md)

---

## Spinoffs

| Fase | Spinoff | Risco | Retorno |
|------|---------|-------|---------|
| 0-6m | Alexandria Insights | Baixo | Médio |
| 0-6m | Alexandria LLM Alpha (wrapper) | Baixo | Médio |
| 6-12m | Alexandria Academy | Médio | Alto |
| 6-12m | Alexandria for Teams | Médio | Alto |
| 12-18m | Alexandria Consulting | Baixo | Médio |
| 12-18m | Alexandria Journal | Baixo | Baixo |
| 12-18m | Alexandria LLM (fine-tuning) | Médio | Alto |
| 18-24m | Alexandria Games | Alto | Médio |

> **Alexandria LLM** foi dividida em duas fases. O Alpha (wrapper de prompt) é viável nos primeiros 6 meses. O fine-tuning, que requer corpus maduro (50+ entries), foi realocado para a Fase 3.

Detalhes completos: [COMMERCIAL/spinoffs.md](COMMERCIAL/spinoffs.md) | [ROADMAP.md](ROADMAP.md)

---

## Dodecálogo Gurudev

1. Simplicidade Elegante sobre complexidade desnecessária
2. Expressividade Clara sobre otimização prematura
3. Interoperabilidade Universal sobre isolamento linguístico
4. Segurança por Design sobre correção posterior
5. Composabilidade sobre monolitismo
6. Imutabilidade Padrão sobre mutabilidade irrestrita
7. Tipagem Gradual sobre extremos absolutos
8. Concorrência Cooperativa sobre competição destrutiva
9. Metaprogramação Responsável sobre magia excessiva
10. Evolução Incremental sobre revoluções disruptivas
11. Documentação Viva sobre comentários mortos
12. Comunidade Inclusiva sobre elitismo técnico

---

## Casos de Uso

**Educação**: Ensino comparativo de linguagens, currículos multi-paradigmáticos, avaliação de proficiência cross-linguagem.

**Indústria**: Migração de sistemas legados, integração de equipes multi-linguagem, decisões de stack tecnológico fundamentadas em análise semiótica.

**Pesquisa**: Análise de evolução de linguagens, desenvolvimento de DSLs, estudos de usabilidade linguística.

---

## Instalação

```bash
pip install gurudev-comparative-programming
```

---

## Licença

Este repositório utiliza duas licenças distintas para separar código de conteúdo:

| Camada | Arquivos | Licença |
|--------|----------|---------|
| **Código** | `gurudev/`, `scripts/`, `setup.py`, `pyproject.toml` | Apache 2.0 ([LICENSE](LICENSE)) |
| **Conteúdo** | `corpus/`, `data/`, `docs/`, `COMMERCIAL/`, `ROADMAP.md` | CC BY 4.0 ([LICENSE-DATA](LICENSE-DATA)) |

> Ver [data/README.md](data/README.md) para a documentação da separação entre `corpus/` e `data/`.

---

## Autor

**Guilherme Gonçalves Machado** — Hubstry DeepTech

- **Working Paper**: [DOI: 10.5281/zenodo.20028887](https://doi.org/10.5281/zenodo.20028887)
- **Repositório**: [github.com/Hubstry-DeepTech/gurudev-programacao-comparada](https://github.com/Hubstry-DeepTech/gurudev-programacao-comparada)
