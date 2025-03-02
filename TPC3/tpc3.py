import re

def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub("\n", " ",descricao)
    return descricao

def aula3():

    file = open("dicionario_medico.txt", encoding="utf-8")
    text = file.read()

    # limpar
    text = re.sub(r"\f", "", text)

    # colocar marca
    text = re.sub(r"(\n\n)(.*)\n{1,}", r"\1@\2\n", text)

    #extrait conceitos
    conceitos_raw = re.findall(r"@(.*)\n([^@]*)",text)

    conceitos = [(designacao,limpa_descricao(descricao)) for designacao,descricao in conceitos_raw]


    html_text = gera_html(conceitos)
    html_out = open("dicionario_medico.html", "w")
    html_out.write(html_text)
    html_out.close()

    file.close()


def gera_html(conceitos):


    html_header = f"""
    <!DOCTYPE html>
        <head>
        <h3>DIC MÉDICO</h3>
        </head>
        <body>"""

    html_conceitos = ""
    for designacao, descricao in conceitos:
        html_conceitos += f"""
            <hr>
            <div>
            <p><b>{designacao}</b></p>
            <p>{descricao}</p>
            </div>
            </hr>
        """
    html_footer = """
        </body>
        </html>
    """

    return html_header + html_conceitos + html_footer



if __name__ == "__main__":
    aula3()


