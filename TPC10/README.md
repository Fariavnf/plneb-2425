<h1> TPC10 - Web Scraper para a Revista de Medicina Interna </h1>

Este script Python extrai dados de publicação da [Revista da Sociedade Portuguesa de Medicina Interna](https://revista.spmi.pt/index.php/rpmi/issue/archive), extraindo informação sobre o número, metadados da publicação e detalhes completos da publicação, incluindo autores, DOI, palavras-chave e resumos.

## 📋 Features

- Pesquisa e recolhe todas as edições disponíveis no arquivo.
- Extrai todas as publicações de cada edição.
- Recupera metadados pormenorizados para cada publicação:
  - Título e subtítulo
  - Autores, afiliações e IDs ORCID
  - DOI
  - Palavras-chave
  - Resumos (seccionados ou gerais)

 ## 📂 Ficheiros gerados e estrutura do output

- `issues.json`: Contém todos os títulos e URLs das edições.
- `issues_with_pubs.json`: Adiciona títulos de publicações e URLs para cada edição.
- `issues_pubs_content.json`: Metadados completos enriquecidos para cada publicação.

```json
{
    "0": {
        "name": "Janeiro / Março - Vol. 32 No. 1 (2025)",
        "URL": "https://revista.spmi.pt/index.php/rpmi/issue/view/135",
        "publications": [
              {
                "title": "Significado Clínico da Elevação Extrema da Velocidade de Sedimentação: Diagnósticos e Sobrevida em 681 Doentes num Hospital Português",
                "title-pt": "",
                "URL": "https://revista.spmi.pt/index.php/rpmi/article/view/2579",
                "article_id": "article-2579",
                "authors": [
                    {
                        "name": "Tiago  Tribolet de Abreu",
                        "affiliation": "Unit Intensive Care, Unidade Local de Saúde Alentejo Central, Hospital Espírito Santo, Évora, Portugal",
                        "orcid": "https://orcid.org/0000-0001-9013-1095"
                    },
                    {
                        "name": "Bárbara Batista",
                        "affiliation": "Unit Intensive Care, Unidade Local de Saúde Alentejo Central, Hospital Espírito Santo, Évora, Portugal",
                        "orcid": "https://orcid.org/0000-0002-4567-6835"
                    },
                    {
                        "name": "Nuno Lupi Manso",
                        "affiliation": "Radiology Departamente, Hospital CUF Tejo, Lisboa, Portugal",
                        "orcid": "https://orcid.org/0000-0003-2085-5463"
                    }
                ],
                "doi": "https://doi.org/10.24950/rspmi.2579",
                "keywords": "Mortalidade, Velocidade de Sedimentação",
                "abstract": {
                    "Introdução": "O nosso objetivo...",
                    "Métodos": "Estudo retrospetivo....",
                    "Resultados": "Uma VS superior ...",
                    "Conclusão": "Verificámos que quase..."
                }
            },
            ...
        ]
    },
  ...
}
```


