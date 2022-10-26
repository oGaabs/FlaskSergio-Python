from flask import Flask, render_template

app = Flask(__name__)

# criar primeira página
# route => paginainicial.com/index
# função => o que voce quer exibir naquela pagina


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/on', methods=["POST"])
def on():
    msg = "Ligado"
    return render_template('on.html', msg=msg)


@app.route('/off', methods=["POST"])
def off():
    msg = "Desligado"
    return render_template('off.html', msg=msg)


@app.route('/<string:nome>')
def NotFound(nome):
    resposta = f"Página ({nome}) não existe"
    return render_template("notFound.html", resposta=resposta)


# colocar o site no ar
if (__name__ == "__main__"):
    app.run(debug=True)