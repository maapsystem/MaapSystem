from flask import render_template
from flask import Flask
from flask import jsonify
from flask import render_template 
from flask import redirect
from flask import url_for 
from flask import request
from app import app, session, tbl_pessoa_fisica, tbl_pessoa_juridica, tbl_cidade, tbl_estado, tbl_cliente, tbl_item, tbl_ligacao_codigo, tbl_pedido,tbl_produto, tbl_status_pedido, tbl_telefone
from modelos import *
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Environment, FileSystemLoader
import time

# def formatar_data(alguma_data):
#     return alguma_data.strftime("%d/%m/%Y")

# env = Environment(loader=FileSystemLoader('C://MaapSystem//templates'))
# env.globals['formatar_data'] = formatar_data



@app.route("/")
@app.route("/index", methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route("/pedido", methods=["GET","POST"])
def pedidos():
    return render_template('pedidos.html')

@app.route("/produto", methods=["GET","POST"])
def cancelamentos():
    return render_template('cancelamentos.html')

@app.route("/menulogin", methods=["GET","POST"])
def menulogin():
    return render_template('menu.html')

@app.route("/adminpj", methods=["GET","POST"])
def orcamentos():
    return render_template('orcamentos.html')

@app.route("/adminpf")
def adminpf():
    cliente = session.query(tbl_cliente, tbl_pessoa_fisica, tbl_cidade, tbl_estado, tbl_telefone).join(tbl_pessoa_fisica, tbl_cidade, tbl_estado, tbl_telefone).all()
    return render_template("admin.html", cliente=cliente)


@app.route("/form", methods=["PUT", "POST"])
def form():
    usuarios = session.query(tbl_cliente).all()
    print(usuarios)
    login = request.form['usuarioform']
    password = request.form['senhaform']
    usuario = {}
    for user in usuarios:
        check = check_password_hash(user.senha, password)
        usuario[user.usuario] = check
    print(usuario)

    for chave in usuario:    
        if usuario[chave] == True:
            return render_template("menu.html", mensagem = "Login Realizado.") 
    return render_template("login.html", mensagem = "Login inválido.")


@app.route("/adicionar", methods=['GET','POST'])
def adicionar():
    cidades = session.query(tbl_cidade).all()
    
    if request.method == 'POST':

        # tbl_cliente
        usuario = request.form['usuario']
        senha = request.form['senha']
        senha = generate_password_hash(senha, method='sha256', salt_length=2)
        endereco = request.form['endereco']
        num_endereco = request.form['num_endereco']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cep = request.form['cep']
        cod_cidade = request.form['cod_cidade']
        contato = request.form['contato']
        email = request.form['email']
        observacao = request.form['observacao']
        cliente = tbl_cliente(usuario=usuario, senha=senha, endereco=endereco, num_endereco=num_endereco, complemento=complemento, bairro=bairro, cep=cep, cod_cidade=cod_cidade, contato=contato, email=email, observacao=observacao)
        session.add(cliente)
        session.commit()
        
        # tbl_pessoa_fisica
        nome = request.form['nome']
        cpf = request.form['cpf']
        rg = request.form['rg']
        data_nascimento = request.form['data_nascimento']
        pessoa_fisica = tbl_pessoa_fisica(id_pessoa_fisica = cliente.id_cliente, nome=nome, cpf=cpf, rg=rg, data_nascimento=data_nascimento)
        session.add(pessoa_fisica)
        session.commit()

        # tbl_telefone
        ddd = request.form['ddd']
        telefone  = request.form['telefone']
        tb_telefone = tbl_telefone(ddd=ddd, telefone=telefone, cod_cliente = cliente.id_cliente)
        session.add(tb_telefone)
        session.commit()

        return redirect(url_for('adminpf'))
    return render_template('add.html', cidades=cidades)


@app.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    id_tbl_cliente= session.get(tbl_cliente, id)
    id_tbl_pessoa_fisica = session.get(tbl_pessoa_fisica, id)
    id_tbl_telefone = session.get(tbl_telefone, id)
    cidades = session.query(tbl_cidade).all()
    if request.method == 'POST':

        # tbl_cliente
        id_tbl_cliente.usuario = request.form['usuario']
        senha = request.form['senha']
        id_tbl_cliente.senha = generate_password_hash(senha, method='sha256', salt_length=2)
        id_tbl_cliente.endereco = request.form['endereco']
        id_tbl_cliente.num_endereco = request.form['num_endereco']
        id_tbl_cliente.complemento = request.form['complemento']
        id_tbl_cliente.bairro = request.form['bairro']
        id_tbl_cliente.cep = request.form['cep']
        id_tbl_cliente.cod_cidade = request.form['cod_cidade']
        id_tbl_cliente.contato = request.form['contato']
        id_tbl_cliente.email = request.form['email']
        id_tbl_cliente.observacao = request.form['observacao']

        # tbl_pessoa_fisica
        id_tbl_pessoa_fisica.nome = request.form['nome']
        id_tbl_pessoa_fisica.cpf = request.form['cpf']
        id_tbl_pessoa_fisica.rg = request.form['rg']
        id_tbl_pessoa_fisica.data_nascimento = request.form['data_nascimento']
        session.commit()

        # tbl_telefone
        id_tbl_telefone.ddd = request.form['ddd']
        id_tbl_telefone.telefone  = request.form['telefone']
        session.commit()

        return redirect(url_for('adminpf'))
    return render_template('edit.html', id_tbl_cliente=id_tbl_cliente, cidades=cidades)


@app.route("/deletar/<int:id>" , methods=['GET','POST'])
def deletar(id):
    id_log = session.get(tbl_cliente, id)
    session.delete(id_log)
    session.commit()
    return redirect(url_for('adminpf'))




'''
results = session.query(tbl_estado).all()
results2 = session.query(tbl_estado).filter_by(tbl_estado.uf == 'SP').first()

for dados in results2:
    print (dados.id_estado)
'''
