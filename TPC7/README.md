
<h1>Meter as novas features</h1>


<h1>TPC6 - Flask Concept Viewer</h1>

Esta é uma pequena aplicação Web Flask concebida para apresentar uma lista de conceitos e as suas descrições correspondentes, que são carregadas a partir de um ficheiro JSON (conceitos.json).

## 📋 Features

- Mostrar uma lista de conceitos de um ficheiro JSON.
- Mostrar descrições detalhadas de cada conceito.
- Pesquisar conceitos com suporte para busca normal e busca por correspondência exata (termo exato).
- Mostrar conceitos em formato de tabela interativa com pesquisa e ordenação.
- Pesquisa avançada com suporte para expressões regulares (regex).
- Adicionar novos conceitos através de um formulário.
- Eliminar conceitos de forma dinâmica via AJAX.


## ⚙️ Routes 

- `/conceitos`  

Apresenta uma lista de todos os termos do conceito.
  
- `/conceitos/<termo>`

Apresenta a descrição do conceito selecionado.

- `/conceitos/tabela`

Apresenta a lista de conceitos em formato de tabela interativa.

- `/adicionar>`

Mostra um formulário para adicionar um novo conceito.

- `adicionar>` (POST)

Processa o formulário e guarda o novo conceito no ficheiro JSON.

- `/conceitos/<termo>` (DELETE)

Permite apagar um conceito via AJAX.

## 🧩 Templates

Usa Jinja2 para renderizar HTML dinamicamente.

- `home.html>` – Página principal após adicionar um conceito.
-`conceitos.html>` – Lista de todos os conceitos.
-`table.html` - Tabela interativa com conceitos.
- `descricao.html>` – Descrição detalhada de um conceito.
- `adicionar.html>` – Formulário para adicionar um novo conceito.
- `pesquisa.html>` – Resultados da pesquisa.

## 🎨 Tecnologias Utilizadas

A aplicação usa várias bibliotecas para um design responsivo e interatividade:

*Flask* – Framework backend para servir as páginas e gerenciar conceitos.

*Bootstrap* – Para um layout responsivo e estilizado.

*jQuery* – Para manipulação dinâmica do DOM e requisições AJAX.

*DataTables.js* – Para criar tabelas interativas com pesquisa instantânea com suporte para regex, ordenação dinâmica e paginação automática.


