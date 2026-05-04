# Gurudev — Programação Comparada

> **Schema Alexandria v3.1** — Protocolo formal de catalogação para a Ciência de Interface das Linguagens de Programação.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Schema](https://img.shields.io/badge/schema-v3.1-green.svg)](corpus/schema/alexandria-v3.1.json)

## O que é?

Este repositório implementa o **Schema Alexandria** — um protocolo formal de catalogação para **Programação Comparada** (ProCP), um campo emergente que estuda linguagens de programação como objetos de estudo científico, aplicando métodos da semiótica (Peirce), hermenêutica (Savigny) e gramática comparada às interfaces humano-máquina.

Cada linguagem é catalogada em **14 blocos analíticos** que capturam desde metadados básicos até a metáfora fundante, a gramática de interface em 5 camadas (GILP), a análise hermenêutica em 4 dimensões (Savigny), e o nível semiótico stricto sensu.

## Fundamentação Teórica

| Pilar | Descrição |
|-------|-----------|
| **TATS** | Teoria Analógica do Tipo Semiótico — 3 modos de analogia (heurística, funcional, homológica) |
| **GILP** | Gramática de Interface de Linguagem de Programação — 5 camadas (cognitiva, infraestrutural, sistêmica, ecossistêmica, cultural) |
| **Savigny** | Hermenêutica comparada — 4 dimensões (gramatical, semântica, histórica, sistemática) |

Consulte o [Working Paper completo](https://doi.org/10.5281/zenodo.20028887 ) para a fundamentação teórica detalhada (Machado, 2026).

## Estrutura do Repositório

```
gurudev-programacao-comparada/
├── corpus/                          # Corpus Alexandria
│   ├── schema/
│   │   └── alexandria-v3.1.json     # JSON Schema formal (validação automática)
│   ├── entries/
│   │   └── python.yaml              # Entry-exemplo completa (14 blocos)
│   └── README.md                    # Documentação do corpus
├── COMMERCIAL/                      # Modelo de negócio e spinoffs
│   ├── README.md                    # Visão geral
│   ├── modelo-freemium.md           # Arquitetura freemium detalhada
│   └── spinoffs.md                  # Mapa de 7 spinoffs priorizados
├── docs/
│   ├── framework_teorico.md         # Framework teórico (Dodecálogo Gurudev)
│   ├── working-paper/               # Working Paper (fundamentação teórica)
│   └── strategic/                   # Plano estratégico completo
│       └── Plano_Estrategico_Schema_Alexandria_v3.pdf
├── gurudev/                         # Módulo Python (biblioteca core)
│   └── core/                        # Biblioteca de Interoperabilidade
├── data/                            # Dados legados (comparative_programming.json)
├── examples/                        # Exemplos de uso
│   └── basic_usage.py
├── scripts/                         # Scripts utilitários
│   └── validate_corpus.py           # Validação do corpus contra o schema
├── LICENSE                          # Apache 2.0
├── README.md                        # Este arquivo
├── pyproject.toml
└── requirements.txt
```

## Visão Geral dos 14 Blocos do Schema

| Bloco | Nome | Fundamento | Obrigatório |
|-------|------|-----------|-------------|
| Meta | Metadados da versão | Versionamento semântico | Sim |
| B1 | Metadados | Identificação e rastreabilidade | Sim |
| B2 | Classificação ProCP | 7 eixos + era histórica | Sim |
| B3 | Status de Mercado | Rankings e tendências | Não |
| B4 | Metáfora Fundante | TATS — 3 modos de analogia | Sim |
| B5 | Interface Grammar (GILP) | 5 camadas analíticas | Sim |
| B6 | Análise Savigny | 4 dimensões hermenêuticas | Sim |
| B7 | Sintático | Formas sintáticas da linguagem | Sim |
| B8 | Léxico | Inventário lexical completo | Sim |
| B9 | Sistema de Tipos | Tipos primitivos, genéricos, algébricos | Sim |
| B10 | Comparativo Relacional | Similaridades, diferenças, genealogia | Sim |
| B11 | Ecossistema | Licença, comunidades, frameworks | Sim |
| B12 | Ordenação | Metadados de navegação | Não |
| B13 | Acesso | Modelo de disponibilização + confiança | Sim |
| B14 | Semiótico | Peirce — nível semiótico (proposto) | Não |

## Quick Start — Validar o Corpus

```bash
pip install jsonschema pyyaml
python scripts/validate_corpus.py
```

Ou diretamente:

```bash
python -c "
import json, yaml, jsonschema
schema = json.load(open('corpus/schema/alexandria-v3.1.json'))
entry = yaml.safe_load(open('corpus/entries/python.yaml'))
jsonschema.validate(entry, schema)
print('Validação OK — entry Python conforme ao Schema Alexandria v3.1')
"
```

## Quick Start — Biblioteca Gurudev

```bash
pip install -r requirements.txt
python examples/basic_usage.py
```

## Dodecálogo Gurudev

O Dodecálogo é o framework pedagógico que orienta o projeto:

1. **Simplicidade Elegante** sobre complexidade desnecessária
2. **Expressividade Clara** sobre otimização prematura
3. **Interoperabilidade Universal** sobre isolamento linguístico
4. **Segurança por Design** sobre correção posterior
5. **Composabilidade** sobre monolitismo
6. **Imutabilidade Padrão** sobre mutabilidade irrestrita
7. **Tipagem Gradual** sobre extremos absolutos
8. **Concorrência Cooperativa** sobre competição destrutiva
9. **Metaprogramação Responsável** sobre magia excessiva
10. **Evolução Incremental** sobre revoluções disruptivas
11. **Documentação Viva** sobre comentários mortos
12. **Comunidade Inclusiva** sobre elitismo técnico

## Modelo Freemium

O conteúdo analítico de alta densidade teórica é **sempre acessível**. Camadas de conveniência e ferramenta são monetizáveis.

| Camada | Acesso | Conteúdo |
|--------|--------|----------|
| Free | Aberto | Metadados, ProCP, metáfora fundante parcial |
| Freemium | Registro | GILP completa, Savigny, busca avançada, API |
| Explorer | USD 9/mês | API ilimitada, comparação multi-linguagem |
| Professional | USD 39/mês | Alexandria LLM, dashboards, certificações |
| Enterprise | USD 200-500/mês | On-premise, consulting, SLA |

Consulte [COMMERCIAL/modelo-freemium.md](COMMERCIAL/modelo-freemium.md) para detalhes.

## Spinoffs

| Spinoff | Descrição | Fase |
|---------|-----------|------|
| Alexandria LLM | Fine-tuning de LLM no corpus | 0-6m |
| Alexandria Insights | Relatórios analíticos periódicos | 0-6m |
| Alexandria Academy | Plataforma de ensino | 6-12m |
| Alexandria for Teams | Decisão tecnológica para equipes | 6-12m |
| Alexandria Consulting | Auditoria de stack | 12-18m |
| Alexandria Journal | Periódico acadêmico | 12-18m |
| Alexandria Games | Jogos sérios e gamificação | 18-24m |

Consulte [COMMERCIAL/spinoffs.md](COMMERCIAL/spinoffs.md) para detalhes.

## Como Contribuir

1. Copie `corpus/entries/python.yaml` como template
2. Preencha todos os campos obrigatórios do schema
3. Valide contra o JSON Schema
4. Marque `nivel_confianca: "Preliminar"` para primeira versão
5. Abra Pull Request

## Licença

- **Conteúdo** (corpus, documentação): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Código** (módulo gurudev): [Apache 2.0](LICENSE)

---

**Autor**: Guilherme Gonçalves Machado — [Hubstry DeepTech](https://github.com/Hubstry-DeepTech)

**Working Paper**: Machado, G. G. (2026). *Programação Comparada: Fundamentos para uma Ciência de Interface das Linguagens de Programação.*
