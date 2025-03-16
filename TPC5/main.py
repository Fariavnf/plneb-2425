
from flask import  Flask, render_template
import json

app = Flask(__name__)

with open(r'conceitos.json', encoding='utf-8') as file:
    data = json.load(file)


@app.route('/conceitos')
def conceitos():
    termos = list(data.keys())
    return render_template("termos.html", termos=termos, title="Lista de conceitos")


@app.route('/conceitos/<termo>')
def conceito_termo(termo):
    descricao = data.get(termo)

    return render_template("termo_descricao.html", termo=termo, descricao=descricao,
                           title="Designação - Descrição")



app.run(host="localhost", port=5000, debug=True)
























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
