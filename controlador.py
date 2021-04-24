from flask import render_template
from flask import Flask
from flask import jsonify
from flask import render_template 
from flask import redirect
from flask import url_for 
from flask import request
from app import app, session, tbl_pessoa_fisica, tbl_pessoa_juridica, tbl_cidade, tbl_estado, tbl_cliente, tbl_item, tbl_ligacao_codigo, tbl_login,tbl_pedido,tbl_produto, tbl_status_pedido, tbl_telefone
from modelos import *
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
@app.route("/index", methods=["GET","POST"])
def index():
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
    admin = session.query(tbl_login).all()
    return render_template("admin.html", admin=admin)


@app.route("/form", methods=["PUT", "POST"])
def form():
    usuarios = session.query(tbl_login).all()
    print(usuarios)
    login = request.form['usuarioform']
    password = request.form['senhaform']
    for user in usuarios:
        #print(user)
        if user.nome == login and user.senha == password:
            return render_template("menu.html", mensagem = "Login Realizado.")
    return render_template("login.html", mensagem = "Login inválido.")


@app.route("/adicionar", methods=['GET','POST'])
def adicionar():
    if request.method == 'POST':
        senha = request.form['senha']
        session.add(tbl_login(nome=request.form['usuario'], senha=senha, cod_cliente=2))
        session.commit()
        return redirect(url_for('admin'))
    return render_template('add.html')


@app.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    user = session.query(tbl_login).get(id)
    if request.method == 'POST':
        user.usuario = request.form['usuario']
        user.senha = request.form['senha']
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('edit.html', user=user)


@app.route("/deletar/<int:id>" , methods=['GET','POST'])
def deletar(id):
    
    id_log = session.get(tbl_login, id)
    session.delete(id_log)
    session.commit()
    return redirect(url_for('admin'))



'''
results = session.query(tbl_estado).all()
results2 = session.query(tbl_estado).filter_by(tbl_estado.uf == 'SP').first()

for dados in results2:
    print (dados.id_estado)
'''
