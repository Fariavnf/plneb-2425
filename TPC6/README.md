<h1>TPC6 - Flask Concept Viewer</h1>

Esta é uma pequena aplicação Web Flask concebida para apresentar uma lista de conceitos e as suas descrições correspondentes, que são carregadas a partir de um ficheiro JSON (conceitos.json).

## 📋 Features

- Mostrar uma lista de conceitos de um ficheiro JSON.
- Mostrar descrições detalhadas de cada conceito.
- Adicionar novos conceitos através de um formulário.
- Pesquisar conceitos com suporte para busca normal e busca por correspondência exata (termo exato).

## ⚙️ Routes 

- `/conceitos`  

Apresenta uma lista de todos os termos do conceito.
  
- `/conceitos/<termo>`

Apresenta a descrição do conceito selecionado.

- `/adicionar>`

Mostra um formulário para adicionar um novo conceito.

- `/api/adicionar>`  (POST)

Processa o formulário e guarda o novo conceito no ficheiro JSON.

## 🧩 Templates

Usa Jinja2 para renderizar HTML dinamicamente.

- `home.html>` – Página principal após adicionar um conceito.
-`conceitos.html>` – Lista de todos os conceitos.
- `descricao.html>` – Descrição detalhada de um conceito.
- `adicionar.html>` – Formulário para adicionar um novo conceito.
- `pesquisa.html>` – Resultados da pesquisa.


