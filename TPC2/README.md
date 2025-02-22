## Exercício 8

```python
import re

def inteiros(linha):
  return re.findall(r"(?<![,\w])-?\d+(?=[\s.]|$)", linha)


print(inteiros("Vou comprar 6 maças, 4 bananas e 2 laranjas"))   #Output: ['6', '4', '2']
print(inteiros("42 4,3.-400. 33.-3,2 69"))                       #Output: ['42', '-400', '33', '69']
```
