<h1>TPC3</h1>

Este trabalho explica o processo para processar um dicionário médico extraído a partir de um ficheiro de texto, formatá-lo corretamente e gerar um HTML estruturado. O principal desafio será o tratamento das descrições para garantir uma estrutura organizada e limpa.

Comparando com a resolução efetuada na aula, houve apenas uma alteração no código para o melhor funcionamento do script. A seguinte linha e código:

```python

text = re.sub(r"\n\n", "\n\n@", text)

```

foi substituída por:

```python

text = re.sub(r"(\n\n)(.*)\n{1,}", r"\1@\2\n", text)

```

Esta alteração impede que haja conceitos que tenha mais que um \n a separar a sua descrição
