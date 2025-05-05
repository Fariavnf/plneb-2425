<h1> TPC 9 - Treino de Modelos com Word2Vec </h1>

Este projeto demonstra a utilização de word embeddings para visualizar as relações semânticas entre palavras com base em dois documentos da saga *Harry Potter* . Os modelos de word embedding tornaram-se ferramentas essenciais para captar estas relações, representando as palavras como vectores de alta dimensão que codificam a semelhança semântica com base na sua utilização em grandes corpus de texto.


## Treino do Modelo

Os word embeddings são treinados utilizando técnicas de aprendizagem não supervisionada como o Word2Vec. Estes modelos aprendem através da análise de grandes quantidades de texto e da otimização das representações vectoriais, de modo a que as palavras que aparecem em contextos semelhantes acabem por ter vectores semelhantes.

In this specific project, a pre-trained embedding model—most likely trained on a Portuguese-language corpus—was used. The model likely has:
  - Vectores de 300 dimensões
  - Treino efectuado com skip-gram
  - Context windows e negative sampling utilizadas para otimizar a precisão da previsão de palavras.



## Testes

São efetuados implicitamente vários testes para avaliar a qualidade da incorporação. Ao inspecionar os vizinhos mais próximos de uma determinada palavra, é possível avaliar até que ponto o modelo capta as relações semânticas. Os padrões visuais - tais como grupos de palavras relacionadas ou agrupamentos significativos - confirmam ainda mais a coerência do espaço vetorial.

Esta visualização não é apenas um elemento técnico, mas também uma ferramenta de exploração linguística. Permite que os utilizadores procurem termos específicos, vejam como os conceitos linguísticos estão agrupados e compreendam melhor como os modelos de aprendizagem automática percepcionam os dados textuais.

## Visualização com Embedding Projector

![](print.png)
