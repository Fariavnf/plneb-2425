
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
