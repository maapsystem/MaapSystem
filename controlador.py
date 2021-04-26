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
    usuario = {}
    for user in usuarios:
        check = check_password_hash(user.senha, password)
        usuario[user.nome] = check
    print(usuario)

    for chave in usuario:    
        if usuario[chave] == True:
            return render_template("menu.html", mensagem = "Login Realizado.") 
    return render_template("login.html", mensagem = "Login inválido.")


@app.route("/adicionar", methods=['GET','POST'])
def adicionar():
    if request.method == 'POST':
        senha = request.form['senha']
        senha = generate_password_hash(senha, method='sha256', salt_length=2)
        nome = request.form['usuario']
        session.add(tbl_login(nome=nome, senha=senha, cod_cliente=3))
        session.commit()
        return redirect(url_for('admin'))
    return render_template('add.html')


@app.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    id_user= session.get(tbl_login, id)
    if request.method == 'POST':
        senha = request.form['senha']
        senha = generate_password_hash(senha, method='sha256', salt_length=2)
        print(senha)
        id_user.nome = request.form['usuario']
        id_user.senha = senha
        session.commit()
        return redirect(url_for('admin'))
    return render_template('edit.html', id_user=id_user)


@app.route("/deletar/<int:id>" , methods=['GET','POST'])
def deletar(id):
    id_log = session.get(tbl_login, id)
    session.delete(id_log)
    session.commit()
    msg = "Deletado"
    return redirect(url_for('admin'),msg=msg)




'''
results = session.query(tbl_estado).all()
results2 = session.query(tbl_estado).filter_by(tbl_estado.uf == 'SP').first()

for dados in results2:
    print (dados.id_estado)
'''
