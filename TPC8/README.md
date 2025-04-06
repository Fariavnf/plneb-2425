<h1> 🧾 Atlas da Saúde Scraper </h1>

Este projeto é um web scraper Python que recolhe informação médica estruturada do site de saúde português Atlas da Saúde. Vai buscar um dicionário de doenças juntamente com as suas descrições, resumos e detalhes relacionados, e armazena-os num ficheiro JSON.


## 📋 Features

- Pesquisa todas as doenças listadas alfabeticamente no sítio.
- Extrações:
  - Nome da doença
  - Descrição resumida
  - Conteúdo completo do artigo (com secções e subsecções)
  - Notas adicionais, se disponíveis
  - Salva todos os dados coletados em  -`termos.json` no formato UTF-8.


## 📂 Output Format

```json
{
  "Doença Exemplo": {
    "resumo": "Resumo da doença...",
    "URL": "/doenca/exemplo",
    "description": {
      "Text": "Texto introdutório..."
    },
    "Sintomas": {
      "Text": "Texto dos sintomas...",
      "List": ["sintoma1", "sintoma2"]
    },
    "Nota": "Nota adicional se existir"
  },
  ...
}
```
