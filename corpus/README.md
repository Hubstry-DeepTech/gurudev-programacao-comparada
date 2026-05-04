# Corpus Alexandria

Banco de dados estruturado de linguagens de programação catalogadas segundo o protocolo da **Programação Comparada**.

## Fundamentação Teórica

Cada entrada do corpus é materialização computacional dos fundamentos teóricos do campo:

| Bloco | Fundamento | Working Paper |
|-------|-----------|---------------|
| B2 - ProCP | Estrutura de classificação multi-eixos | Seção 2.3 |
| B4 - Metáfora Fundante | TATS - 3 modos de analogia | Seção 5.2 |
| B5 - GILP | Gramática das Interfaces - 5 camadas | Seção 5.4 |
| B6 - Savigny | Hermenêutica comparada - 4 dimensões | Seção 6.2 |
| B7-B9 | Análise lexical, sintática e semântica | Seção 4.2 |
| B10 - Comparativo | TATS + espiral comparativa | Seções 5.2, 6.4 |
| B14 - Semiótico | Semiótica de Peirce (nível semiótico) | Seção 4.2 |

## Estrutura

```
corpus/
├── schema/
│   └── alexandria-v3.1.json   # JSON Schema formal (validação automática)
├── entries/
│   ├── python.yaml            # Entrada-exemplo (preliminar)
│   ├── rust.yaml              # (a preencher)
│   └── ...                    # Uma entry por linguagem
└── README.md                  # Este arquivo
```

## Validação

Para validar uma entrada contra o schema:

```bash
# Com Python (recomendado)
pip install jsonschema pyyaml
python -c "
import json, yaml, jsonschema
schema = json.load(open('corpus/schema/alexandria-v3.1.json'))
entry = yaml.safe_load(open('corpus/entries/python.yaml'))
jsonschema.validate(entry, schema)
print('Validação OK')
"
```

## Níveis de Confiança

- **Alto**: Fontes primárias verificadas + revisão por segundo analista
- **Médio**: Fontes secundárias confiáveis (documentação oficial, livros, artigos)
- **Preliminar**: Inferência analítica — revisão pendente

## Contribuição

1. Copie `corpus/entries/python.yaml` como template
2. Preencha todos os campos obrigatórios
3. Valide contra o JSON Schema
4. Marque `nivel_confianca: "Preliminar"` se for primeira versão
5. Abra Pull Request

Consulte o [Working Paper](../docs/working-paper/) para a fundamentação teórica completa.
