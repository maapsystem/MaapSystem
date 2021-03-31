from flask import render_template
from flask import Flask
from flask import jsonify
from flask import render_template 
from flask import redirect
from flask import url_for 
from flask import request
from app import app
from modelos import *

@app.route("/")
@app.route("/index", methods=["GET","POST"])
def index():
    print(db.query.all())
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route("/orcamentos", methods=["GET","POST"])
def orcamentos():
    return render_template('orcamentos.html')

@app.route("/pedidos", methods=["GET","POST"])
def pedidos():
    return render_template('pedidos.html')

@app.route("/cancelamentos", methods=["GET","POST"])
def cancelamentos():
    return render_template('cancelamentos.html')

@app.route("/menulogin", methods=["GET","POST"])
def menulogin():
    return render_template('menu.html')

@app.route("/admin")
def admin():
    admin = Log.query.all()
    return render_template("admin.html", admin=admin)


@app.route("/form", methods=["PUT", "POST"])
def form():
    usuarios = Log.query.all()
    print(usuarios)
    login = request.form['usuarioform']
    password = request.form['senhaform']
    for user in usuarios:
        if user.usuario == login and user.senha == password:
            return render_template("menu.html", mensagem = "Login Realizado.")
    return render_template("login.html", mensagem = "Login inválido.")


@app.route("/adicionar", methods=['GET','POST'])
def adicionar():
    if request.method == 'POST':
        user = Log( 
        request.form['usuario'], 
        request.form['senha']) 
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('add.html')


@app.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    user = Log.query.get(id)
    if request.method == 'POST':
        user.usuario = request.form['usuario']
        user.senha = request.form['senha']
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('edit.html', user=user)


@app.route("/deletar/<int:id>")
def deletar(id):
    user = Log.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin'))