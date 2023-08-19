from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'lol'

# Configuração da extensão Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    # session.clear()

    if 'carrinho' not in session:
        session["carrinho"] = {}

    if request.method == 'POST':

        if (not request.form["produto"]) or (not float(request.form["quantidade"])) or (float(request.form["quantidade"]) <= 0):
            return redirect(url_for("index"))
        
        produto = request.form["produto"].lower()
        quantidade = float(request.form["quantidade"])

        if produto in session["carrinho"]:
            session["carrinho"][produto] += quantidade
        else:
            session["carrinho"][produto] = quantidade

        # print(session["carrinho"])
        return render_template("index.html")

    else:
        return render_template("index.html")

@app.route("/remover/<produto>")
def remover(produto):

    del session["carrinho"][produto]

    return redirect(url_for("index"))

@app.route("/checkout")
def checkout():
    session.clear()

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
