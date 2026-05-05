# data/ — Banco de Dados Legado

Este diretório contém o banco de dados comparativo original (`comparative_programming.json`), criado antes da formalização do **Schema Alexandria v3.1**.

## Relação com o corpus formal

- **corpus/** — Fonte da verdade para o protocolo Alexandria. Todas as entries seguem o JSON Schema formal (`corpus/schema/alexandria-v3.1.json`) e são validáveis automaticamente.
- **data/** — Protótipo legado com estrutura independente. Mantido para referência histórica e como base de dados para a biblioteca de interoperabilidade (`gurudev/core/`).

As duas camadas têm propósitos distintos e não devem ser confundidas. O corpus Alexandria é o artefato científico; o data/ é a camada de engenharia anterior ao schema.

## Licença

Conteúdo sob CC BY 4.0 (ver `LICENSE-DATA` na raiz do repositório).
