
from flask import Flask, render_template, request, redirect, url_for
import re
import json

app = Flask(__name__)

with open(r'conceitos.json', encoding='utf-8') as file:
    data = json.load(file)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/conceitos')
def conceitos():
    termos = list(data.keys())
    return render_template("termos.html", termos=termos, title="Lista de conceitos")


@app.route('/conceitos/<termo>')
def conceito_termo(termo):
    descricao = data.get(termo)

    return render_template("termo_descricao.html", termo=termo, descricao=descricao,
                           title="Designação - Descrição")


@app.route('/adicionar')
def adicionar_form():
    return render_template("adicionar.html")

@app.post('/adicionar')
def adicionar_conceito_api():
    termo = request.form.get('termo')
    desc = request.form.get('descricao')

    if data.get(termo) is None: #ADICIONAR CHECK BOX PARA DAR REPLACE
        data[termo] = desc

    f_out = open("conceitos.json", "w", encoding="utf-8")
    json.dump(data, f_out, indent=4 ,ensure_ascii=False)
    f_out.close()

    return render_template("home.html")



@app.route('/pesquisar')
def pesquisar():
    query = request.args.get('query', '').lower().strip()
    exact_match = request.args.get('exact') is not None

    if not query:
        return redirect(url_for('conceitos'))

    termo_match = []
    desc_match = []

    for termo in data.keys():

        if exact_match:
            term_pattern = r'\b' + re.escape(query) + r'\b'

            if re.search(term_pattern, termo.lower()):
                termo_match.append(termo)
            elif re.search(term_pattern, data[termo].lower()):
                desc_match.append(termo)

        else:
            if query in termo.lower():
                termo_match.append(termo)
            elif query in data[termo].lower():
                desc_match.append(termo)

    termo_match.sort()
    desc_match.sort()

    return render_template("pesquisa.html", termo_match=termo_match,
                           desc_match=desc_match, query=query)




@app.delete('/conceitos/<termo>')
def delete_conceito(termo):

    if termo in data:
        f_out = open("conceitos.json", "w", encoding="utf-8")
        del data[termo]
        json.dump(data, f_out, indent=4, ensure_ascii=False)
        f_out.close()

        return {"success": True ,"message": "Conceito apagado com sucesso!",
                "redirect_url": "/conceitos", "data": termo}

    return {"success": False, "message": "Conceito não existe!", "data": termo}


@app.get("/conceitos/tabela")
def tabela():
    conceitos = list(data.items())
    return render_template("table.html", conceitos=conceitos)

app.run(host="localhost", port=10000, debug=True)
























'''

import json

from flask import Flask, request, render_template

app = Flask(__name__)

#db_file = open("../aula4/conceitos.json", encoding="utf-8")
db_file = open("conceitos_.json", encoding="utf-8")
db_data = json.load(db_file)

@app.route("/api/conceitos")
def api_conceitos():
    return db_data

@app.route("/conceitos")
def conceitos():
    termos = list(db_data.keys())
    return render_template("termos.html", termos=termos, title="Lista de termos")

@app.route("/api/conceitos/<designacao>")
def api_conceito(designacao):
    return {"designação": designacao, "descrição": db_data[designacao]}


@app.post("/conceitos")
def adicionar_conceito():
    data = request.get_json()
    db_data[data["descricao"]] = data["designacao"]
    f_out = open("conceitos_.json", "w", encoding="utf-8")
    json.dump(db_data, f_out, ensure_ascii=False)
    f_out.close()
    return data

app.run(host="localhost", port=9000, debug=True)

'''
