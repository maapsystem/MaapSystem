from flask import Flask, request, jsonify, render_template , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app_sorvetunes = Flask(__name__)
app_sorvetunes.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xwaztxslppnkyn:3cce96499e9b5b4f88c1885e26ddf903eeddf98654b7ffebdfe263024a0c9620@ec2-52-44-235-121.compute-1.amazonaws.com/d91oaqltutn28e'
db = SQLAlchemy(app_sorvetunes)

class Log(db.Model):
    __tablename__ = "tb_cadastro_login"
    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(10), nullable=True, unique=True)
    senha = db.Column(db.String(8), nullable=True)

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha


@app_sorvetunes.route("/")
@app_sorvetunes.route("/login", methods=["GET","POST"])
def login():
    return render_template('login.html')


@app_sorvetunes.route("/form", methods=["PUT", "POST"])
def form():
    usuarios = Log.query.all()
    login = request.form['usuarioform']
    password = request.form['senhaform']
    for user in usuarios:
        if user.usuario == login and user.senha == password:
            return render_template("index.html", mensagem = "Login Realizado.")
    return render_template("login.html", mensagem = "Login inválido.")


if __name__ == '__main__':
    db.create_all()
    #db.drop_all()
    port = int(os.environ.get("PORT",5000))
    app_sorvetunes.run(debug=True, host='0.0.0.0', port=port)