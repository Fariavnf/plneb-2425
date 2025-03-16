<h1>TPC5 - Flask Concept Viewer</h1>

Esta é uma pequena aplicação Web Flask concebida para apresentar uma lista de conceitos e as suas descrições correspondentes, que são carregadas a partir de um ficheiro JSON (conceitos.json).

## 📋 Features

- Mostrar uma lista de conceitos de um ficheiro JSON.
- Mostrar descrições detalhadas de cada conceito.

## ⚙️ Routes 

- `/conceitos`  
  Apresenta uma lista de todos os termos do conceito.
- `/conceitos/<termo>`
   Apresenta a descrição do conceito selecionado.

  ## 🧩 Templates

  Usa Jinja2 para renderizar HTML dinamicamente.
