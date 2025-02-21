
## Exercício 1.1


## Exercício 1.2


## Exercício 1.3


## Exercício 1.4


## Exercício 1.5


## Exercício 2


## Exercício 3


## Exercício 4


## Exercício 5


## Exercício 6


## Exercício 7

```python
import re

def variavel_valida(s):
    return bool(re.match(r'^[a-zA-Z]\w*$',s))


print(variavel_valida("var-n10"))
print(variavel_valida("var_n10"))
print(variavel_valida("var Valida"))
print(variavel_valida("1var_n10"))
```
[//]: <> (False)
[//]: <> (True)
[//]: <> (False)
[//]: <> (False)

## Exercício 8

```python
import re

def inteiros(linha):
  return re.findall(r"(?<![,\w])-?\d+(?=[\s.]|$)", linha)


print(inteiros("Vou comprar 6 maças, 4 bananas e 2 laranjas"))
print(inteiros("42 4,3.-400. 33.-3,2 69"))

```
[//]: <> (['6', '4', '2'])
[//]: <> (['42', '-400', '33', '69'])


## Exercício 9


## Exercício 10
