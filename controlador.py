from typing import BinaryIO
from flask import render_template
from flask import Flask
from flask import jsonify
from flask import render_template 
from flask import redirect
from flask import url_for 
from flask import request
from flask import make_response
from flask.helpers import send_file
from pdfkit.api import configuration
from app import app, mail, session, tbl_pessoa_fisica, tbl_pessoa_juridica, tbl_cidade, tbl_estado, tbl_cliente, tbl_item, tbl_pedido, tbl_produto, tbl_telefone, tbl_status_pedido
from modelos import *
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Environment, FileSystemLoader
from contextlib import closing
from datetime import date, datetime
from flask_mail import Mail, Message
import time
import pdfkit
import os


# Rotas Principais.
@app.route("/")
@app.route("/index", methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route("/menulogin", methods=["GET","POST"])
def menulogin():
    return render_template('menu.html')

# Rotas para Login e Logout
@app.route("/login", methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return redirect(url_for('login'))


@app.route("/form", methods=["PUT", "POST"])
def form():
    usuarios = session.query(tbl_cliente).all()
    
    print(usuarios)
    login = request.form['usuarioform']
    secret = request.form['senhaform']
    secret = str(secret)
    logins = {}
    for user in usuarios: 
        senha=str(user.senha) 
        check = check_password_hash(senha, secret)
        print(check)
        logins[user.usuario] = check
    
    print(logins)
    for chave in logins:    
        if logins[chave] == True and chave == login:
            session.close()
            return render_template("menu.html", mensagem = "Login Realizado.")
    session.close() 
    return  render_template("login.html", mensagem = "Login inválido.")

# Rotas para impressão
@app.route('/download_pdf/<url>', methods=['GET','POST'])
def download_pdf(url):
    
    # cliente = session.query(tbl_cliente, tbl_pessoa_fisica, tbl_cidade, tbl_estado, tbl_telefone).join(tbl_pessoa_fisica, tbl_cidade, tbl_estado, tbl_telefone).all()
    # session.close() 
    # html = render_template(url, cliente=cliente)
    # pdf = pdfkit.from_string(html, False)
    # response = make_response(pdf)
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = "inline; filename=output.pdf" # download inline ou attachment 

    return render_template("devops.html")

# Enviar E-mail
@app.route('/sendemail/<url>', methods=['GET','POST'])
def sendemail(url):
    if request.method == 'POST':
        email = request.form['aprovacao']
        id_aprovacao = 1 #request.form['id_aprovacao']
        sub_msg = "Olá, pedido aprovado."
        msg = Message(subject=sub_msg,
                      recipients=[email],
                      body='Teste',
                      html = "<b>Olá seu pedido 1 foi aprovado</b>")
        msgemail = "Mensagem enviada."
        mail.send(msg)
        return render_template(f"{url}", msgemail=msgemail )
    else:
        msgemail = "Mensagem não enviada."
        return render_template(f"{url}", msgemail=msgemail )

#Filtros
@app.template_filter('datetimeformat')
def datetimeformat(value, format="%d/%m/%Y"):
    if value == None or value == 0:
        data = '00-00-0000'
        return data
    return value.strftime(format)

@app.template_filter('cpfformat')
def cpfformat(value):
    if len(value) <= 11:
        value = value.zfill(11)
        cpf_fort = f'{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}'
    return cpf_fort

@app.template_filter('rgdocformat')
def rgdocformat(value):
    if len(value) <= 9:
        value = value.zfill(9)
        doc_rg_fort = f'{value[:2]}.{value[2:5]}.{value[5:8]}-{value[8:9]}'
    return doc_rg_fort

@app.template_filter('cnpjformat')
def cnpjformat(value):
    if len(value) <= 14:
        value = value.zfill(14)
        cnpj_fort = f'{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:14]}'
    return cnpj_fort

@app.template_filter('ieformat')
def ieformat(value):
    if len(value) <= 9:
        value = value.zfill(9)
        ie_fort = f'{value[:3]}.{value[3:6]}.{value[6:9]}'
    return ie_fort

@app.template_filter('cepformat')
def cepformat(value):
    if len(value) <= 8:
        value = value.zfill(8)
        cep_fort = f'{value[:5]}-{value[5:8]}'
    return cep_fort

@app.template_filter('dddformat')
def dddformat(value):
    value = str(value)
    if len(value) <= 2:
        value = value.zfill(2)
        ddd_fort = f'({value})'
    return ddd_fort

@app.template_filter('celularformat')
def celularformat(value):
    value = str(value)
    if len(value) <= 9:
        value = value.zfill(9)
        celular_fort = f'{value[:5]}-{value[5:9]}'
    return celular_fort

    



#errorhandler.
@app.errorhandler(400)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('400.html'), 400

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

###############################################################
# Rotas para Adicionar cliente pessoa fisica.
@app.route("/adminpf")
def adminpf():
    cliente = session.query(tbl_cliente, tbl_pessoa_fisica, tbl_cidade, tbl_estado, tbl_telefone).join(tbl_pessoa_fisica, tbl_cidade, tbl_estado, tbl_telefone).all()
    session.close()
    return render_template("admin_pessoafisica.html", cliente=cliente)

@app.route("/adicionar", methods=['GET','POST'])
def adicionar():
    cidades = session.query(tbl_cidade).order_by(tbl_cidade.cidade).all()
    
    
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
        session.close()

        return redirect(url_for('adminpf'))
    return render_template('adicionar_pessoafisica.html', cidades=cidades)


@app.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    tb_cliente = session.get(tbl_cliente, id)
    tb_pessoa_fisica = session.get(tbl_pessoa_fisica, id) 
    tb_telefone = session.get(tbl_telefone, id)
    query_cidade = session.query(tbl_cidade).order_by(tbl_cidade.cidade).all()
    
    
    if request.method == 'POST':

        # tbl_cliente
        tb_cliente.usuario = request.form['usuario']
        senha = request.form['senha']
        tb_cliente.senha = generate_password_hash(senha, method='sha256', salt_length=2)
        tb_cliente.endereco = request.form['endereco']
        tb_cliente.num_endereco = request.form['num_endereco']
        tb_cliente.complemento = request.form['complemento']
        tb_cliente.bairro = request.form['bairro']
        tb_cliente.cep = request.form['cep']
        tb_cliente.cod_cidade = request.form['cod_cidade']
        tb_cliente.contato = request.form['contato']
        tb_cliente.email = request.form['email']
        tb_cliente.observacao = request.form['observacao']

        # tbl_pessoa_fisica
        tb_pessoa_fisica.nome = request.form['nome']
        tb_pessoa_fisica.cpf = request.form['cpf']
        tb_pessoa_fisica.rg = request.form['rg']
        tb_pessoa_fisica.data_nascimento = request.form['data_nascimento']
        session.commit()

        # tbl_telefone
        tb_telefone.ddd = request.form['ddd']
        tb_telefone.telefone  = request.form['telefone']
        session.commit()
        session.close()

        return redirect(url_for('adminpf'))
    session.close()
    return render_template('editar_pessoafisica.html', tb_cliente = tb_cliente,tb_pessoa_fisica = tb_pessoa_fisica, tb_telefone = tb_telefone, query_cidade=query_cidade)


@app.route("/deletar/<int:id>" , methods=['GET','POST'])
def deletar(id):
    id_log = session.get(tbl_cliente, id)
    session.delete(id_log)
    session.commit()
    session.close()
    return redirect(url_for('adminpf'))

###############################################################
# Rotas para Adicionar cliente pessoa juridica.
@app.route("/adminpj", methods=["GET","POST"])
def adminpj():
    cliente = session.query(tbl_cliente, tbl_pessoa_juridica, tbl_cidade, tbl_estado, tbl_telefone).join(tbl_pessoa_juridica, tbl_cidade, tbl_estado, tbl_telefone).all()
    session.close()
    return render_template("admin_pessoajuridica.html", cliente=cliente)



@app.route("/adicionar_pessoajuridica", methods=['GET','POST'])
def adicionar_pessoajuridica():
    cidades = session.query(tbl_cidade).order_by(tbl_cidade.cidade).all()

    
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

        # tbl_pessoa_juridica
        nome_fantasia = request.form['nome_fantasia']
        razao_social = request.form['razao_social']
        cnpj = request.form['cnpj']
        inscricao_estadual = request.form['inscricao_estadual']
        data_fundacao = request.form['data_fundacao']
        pessoa_juridica = tbl_pessoa_juridica(id_pessoa_juridica = cliente.id_cliente, nome_fantasia=nome_fantasia, razao_social=razao_social, cnpj=cnpj, inscricao_estadual=inscricao_estadual, data_fundacao=data_fundacao)
        session.add(pessoa_juridica)
        session.commit()

        # tbl_telefone
        ddd = request.form['ddd']
        telefone  = request.form['telefone']
        tb_telefone = tbl_telefone(ddd=ddd, telefone=telefone, cod_cliente = cliente.id_cliente)
        session.add(tb_telefone)
        session.commit()
        session.close()

        return redirect(url_for('adminpj'))
    session.close()
    return render_template('adicionar_pessoajuridica.html', cidades=cidades)


@app.route("/editar_pessoajuridica/<int:id>", methods=['GET','POST'])
def editar_pessoajuridica(id):
    tb_cliente = session.get(tbl_cliente, id)
    tb_pessoa_juridica = session.get(tbl_pessoa_juridica, id)    
    tb_telefone = session.get(tbl_telefone, id)
    query_cidade = session.query(tbl_cidade).order_by(tbl_cidade.cidade).all()

    
    if request.method == 'POST':

        # tbl_cliente
        tb_cliente.usuario = request.form['usuario']
        senha = request.form['senha']
        tb_cliente.senha = generate_password_hash(senha, method='sha256', salt_length=2)
        tb_cliente.endereco = request.form['endereco']
        tb_cliente.num_endereco = request.form['num_endereco']
        tb_cliente.complemento = request.form['complemento']
        tb_cliente.bairro = request.form['bairro']
        tb_cliente.cep = request.form['cep']
        tb_cliente.cod_cidade = request.form['cod_cidade']
        tb_cliente.contato = request.form['contato']
        tb_cliente.email = request.form['email']
        tb_cliente.observacao = request.form['observacao']
        

        # tbl_pessoa_juridica
        tb_pessoa_juridica.nome_fantasia = request.form['nome_fantasia']
        tb_pessoa_juridica.razao_social = request.form['razao_social']
        tb_pessoa_juridica.cnpj = request.form['cnpj']
        tb_pessoa_juridica.inscricao_estadual = request.form['inscricao_estadual']
        tb_pessoa_juridica.data_fundacao = request.form['data_fundacao']
        session.commit()


        # tbl_telefone
        tb_telefone.ddd = request.form['ddd']
        tb_telefone.telefone  = request.form['telefone']
        session.commit()
        session.close()

        return redirect(url_for('adminpj'))
    session.close()
    return render_template('editar_pessoajuridica.html', tb_cliente = tb_cliente, tb_pessoa_juridica = tb_pessoa_juridica, tb_telefone = tb_telefone, query_cidade=query_cidade)


@app.route("/deletar_pessoajuridica/<int:id>" , methods=['GET','POST'])
def deletar_pessoajuridica(id):
    id_log = session.get(tbl_cliente, id)
    session.delete(id_log)
    session.commit()
    session.close()
    return redirect(url_for('adminpj'))

###############################################################
# Rotas para Produto.
@app.route("/admin_produto", methods=["GET","POST"])
def admin_produto():
    tb_produto = session.query(tbl_produto).all()
    session.close()
    return render_template('admin_produto.html', tb_produto=tb_produto)

@app.route("/adicionar_produto", methods=['GET','POST'])
def adicionar_produto():
    
    if request.method == 'POST':
        
        nome_produto = request.form['nome_produto']  
        descricao = request.form['descricao']
        qtd_produto = 0
        valor_unitario = request.form['valor_unitario'] 
        print(valor_unitario)
        valor_unitario = valor_unitario.replace(",",".")
        print(valor_unitario)
        valor_unitario = float(valor_unitario)

        add_produto = tbl_produto(nome_produto=nome_produto, descricao=descricao, qtd_produto=qtd_produto, valor_unitario=valor_unitario)
        session.add(add_produto)
        session.commit()
        session.close()

        return redirect(url_for('admin_produto'))
    session.close()
    return render_template('adicionar_produto.html')

@app.route("/editar_produto/<int:id>", methods=['GET','POST'])
def editar_produto(id):
    tb_produto = session.get(tbl_produto, id)

    if request.method == 'POST':
        
        tb_produto.nome_produto = request.form['nome_produto']  
        tb_produto.descricao = request.form['descricao']
        tb_produto.qtd_produto = 0
        valor_unitario = request.form['valor_unitario']
        print(valor_unitario)
        valor_unitario = valor_unitario.replace(",",".")
        print(valor_unitario) 
        tb_produto.valor_unitario = float(valor_unitario)

        session.commit()
        session.close()

        return redirect(url_for('admin_produto'))
    session.close()
    return render_template('editar_produto.html', tb_produto=tb_produto)



@app.route("/deletar_produto/<int:id>" , methods=['GET','POST'])
def deletar_produto(id):
    id_produto = session.get(tbl_produto, id)
    session.delete(id_produto)
    session.commit()
    session.close()
    return redirect(url_for('admin_produto'))


###############################################################
# Rotas e lógicas para pedido.
# Converte uma linha em um dicionário.
def row_to_dict(description, row):
    if row is None: return None
    d = {}
    for i in range(0, len(row)):
        d[description[i][0]] = row[i]
    return d

# Converte uma lista de linhas em um lista de dicionários.
def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result


def conectar():
    import mysql.connector
    return mysql.connector.connect(
        user = "adminSovertunes",
        password = "Sorvetunes2021",
        host = "database-sorvetunes.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com",
        database = "DB_SORVETUNES"
    )

def db_consultar_itens(id=None):
    sql = f"""
        SELECT
            i.id_item, i.quantidade_venda, i.valor_unitario, i.cod_produto, i.cod_pedido, round(i.valor_unitario * i.quantidade_venda, 2) as valor_total,
            pd.nome_produto, pd.descricao, pd.qtd_produto, 
            pp.data_pedido, pp.mod_pgto,
            coalesce(pf.nome, pj.nome_fantasia) as nome,
            sp.descricao as status_pedido
        FROM tbl_item i
        INNER JOIN tbl_produto pd ON i.cod_produto = pd.id_produto
        INNER JOIN tbl_pedido pp ON i.cod_pedido = pp.id_pedido
        LEFT OUTER JOIN tbl_pessoa_fisica pf ON pp.cod_cliente = pf.id_pessoa_fisica
        LEFT OUTER JOIN tbl_pessoa_juridica pj ON pp.cod_cliente = pj.id_pessoa_juridica
        INNER JOIN tbl_status_pedido sp ON sp.id_status = pp.cod_status
        WHERE i.cod_pedido  = {id}
        
    """
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute(sql)
        r = rows_to_dict(cur.description, cur.fetchall()) 
        cur.close()
        return r
    
  

@app.route("/admin_pedido", methods=["GET","POST"])
def admin_pedido():
    tb_ped = session.query(tbl_pedido).all()

      
    # orcamento = session.query(tbl_pedido, tbl_pessoa_fisica, tbl_item, tbl_produto, tbl_ligacao_codigo, tbl_status_pedido).join(tbl_pessoa_fisica, tbl_pedido.cod_cliente == tbl_pessoa_fisica.id_pessoa_fisica).join(tbl_item, tbl_produto, tbl_ligacao_codigo, tbl_status_pedido).all()
    # orcamento_opt = session.query(tbl_pedido, tbl_pessoa_fisica, tbl_item, tbl_produto, tbl_ligacao_codigo, tbl_status_pedido).join(tbl_pessoa_fisica, tbl_pedido.cod_cliente == tbl_pessoa_fisica.id_pessoa_fisica).join(tbl_item, tbl_produto, tbl_ligacao_codigo, tbl_status_pedido).all()
    # # items = session.query(tbl_item)
    # # orcamento2 = session.query(tbl_item).join(tbl_pedido, tbl_item.cod_pedido == tbl_pedido.id_pedido).join(tbl_cliente).join(tbl_produto).all()
    # # totais = {}  

    # # for item, pedido, cliente, produto in orcamento2:
    # #     if pedido.id_pedido not in  totais:
    # #         totais [pedido.id_pedido] = 0
    # #     totais [pedido.id_pedido] += item.quantidade_venda * item.valor_unitario
    # # for k in totais:
    # #     totais[k] = round(totais[k], 2)
    # session.close()
    session.close()
    return render_template("admin_pedido.html", tb_ped=tb_ped)

@app.route("/admin_pedido_get", methods=["GET","POST"])
def admin_pedido_get():
    tb_ped = session.query(tbl_pedido).order_by(tbl_pedido.id_pedido).all()

    id = request.form['id_pedido']
    if request.method == 'POST': 
        pedido = db_consultar_itens(id)
        total = 0
        for valor in pedido:
            total += valor['valor_total']  
            # print(valor)
        session.close()
        return render_template("admin_pedido.html", pedido=pedido, tb_ped=tb_ped, id=id, total=total)
    # elif request.method == 'POST' and request.method == None:
    #     return render_template("admin_pedido.html")
    session.close()
    return render_template("admin_pedido.html")

#Adicionar Item ao Pedido
@app.route("/adicionar_item_pedido", methods=['GET','POST'])
def adicionar_item_pedido():

    produto_list = session.query(tbl_produto).order_by(tbl_produto.nome_produto).all()
    tb_ped = session.query(tbl_pedido).order_by(tbl_pedido.id_pedido).all()
    id = request.form.get('cod_produto')
    tb_prod = session.get(tbl_produto, id) 
    print(id)
    
    if request.method == 'POST':        

        # tbl_item
        quantidade_venda = request.form['quantidade_venda']
        quantidade_venda = int(quantidade_venda)
        valor_unitario = request.form['id_valor_unitario']
        valor_unitario = float(valor_unitario)
        cod_produto = request.form['id_cod_produto']
        cod_pedido = request.form['id_pedido']
        itens = tbl_item(quantidade_venda=quantidade_venda, valor_unitario=valor_unitario, cod_produto=cod_produto, cod_pedido=cod_pedido)
        session.add(itens)
        session.commit()

        session.close()
        return redirect(url_for('admin_pedido'))
    session.close()
    return render_template('adicionar_item_pedido.html', tb_ped=tb_ped, tb_prod=tb_prod,  produto_list=produto_list )



#Pedido ADD PF
@app.route("/adicionar_pedido_pf", methods=['GET','POST'])
def adicionar_pedido_pf():

    cliente_pf = session.query(tbl_pessoa_fisica).order_by(tbl_pessoa_fisica.nome).all()
    status_list = session.query(tbl_status_pedido).order_by(tbl_status_pedido.id_status).all()
    
    if request.method == 'POST':        
        # tbl_pedido
        cod_cliente = request.form['cod_cliente']
        mod_pgto = request.form['mod_pgto']
        cod_status = request.form['cod_status']
        desconto = 0
        pedido = tbl_pedido(data_pedido= datetime.now(), cod_cliente=cod_cliente, desconto=desconto, cod_status=cod_status, mod_pgto=mod_pgto)
        session.add(pedido)
        session.commit()

        session.close()
        return redirect(url_for('admin_pedido'))
    session.close()
    return render_template('adicionar_pedido_pf.html', cliente_pf = cliente_pf, status_list=status_list)

#Pedido ADD PJ
@app.route("/adicionar_pedido_pj", methods=['GET','POST'])
def adicionar_pedido_pj():
    cliente_pj = session.query(tbl_pessoa_juridica).order_by(tbl_pessoa_juridica.razao_social).all()
    status_list = session.query(tbl_status_pedido).order_by(tbl_status_pedido.id_status).all()
    
    if request.method == 'POST':        
        # tbl_pedido
        cod_cliente = request.form['cod_cliente']
        mod_pgto = request.form['mod_pgto']
        cod_status = request.form['cod_status']
        desconto = 0
        pedido = tbl_pedido(data_pedido= datetime.now(), cod_cliente=cod_cliente, desconto=desconto, cod_status=cod_status, mod_pgto=mod_pgto)
        session.add(pedido)
        session.commit()

        session.close()
        return redirect(url_for('admin_pedido'))
    session.close()
    return render_template('adicionar_pedido_pj.html', cliente_pj=cliente_pj, status_list=status_list)


#Pedido Editar 
@app.route("/editar_pedido/<int:id_item>/<int:id_cod_pdt>/<int:id_cod_ped>", methods=['GET','POST'])
def editar_pedido(id_item, id_cod_pdt, id_cod_ped):
    
    tb_pp =  session.get(tbl_pedido, id_cod_ped)
    tb_it =  session.query(tbl_item).get((id_item, id_cod_pdt, id_cod_ped)) 
    tb_pto = session.get(tbl_produto, id_cod_pdt)  
    status_list = session.query(tbl_status_pedido).order_by(tbl_status_pedido.id_status).all() 
    produto_list = session.query(tbl_produto).order_by(tbl_produto.nome_produto).all()
    
    if request.method == 'POST':

        # tbl_pedido
        tb_pp.mod_pgto = request.form['mod_pgto']
        tb_pp.cod_status = request.form['cod_status']
        session.commit()

        # tbl_item
        # tb_pessoa_juridica.nome_fantasia = request.form['nome_fantasia']
        quantidade_venda = request.form['quantidade_venda']
        valor_unitario = request.form['id_valor_unitario']

        tb_it.quantidade_venda = int(quantidade_venda)
        tb_it.valor_unitario = float(valor_unitario)
        tb_it.cod_produto = request.form['id_cod_produto']
        session.commit()
      
        session.close()
        return redirect(url_for('admin_pedido'))
    session.close()
    return render_template('editar_pedido.html', produto_list=produto_list, status_list=status_list, tb_pp=tb_pp, tb_it=tb_it, tb_pto=tb_pto)


#Pedido Deletar item
@app.route("/deletar_item_pedido/<int:id>/<int:id_cod_pt>/<int:id_cod_pd>/<int:id_pp>" , methods=['GET','POST'])
def deletar_item_pedido(id, id_cod_pt, id_cod_pd, id_pp):
    # del_pedido = session.get(tbl_pedido, id_pp)
    # session.delete(del_pedido)

    del_item = session.query(tbl_item).get((id, id_cod_pt, id_cod_pd))
    session.delete(del_item)
    session.commit()
    session.close()
    return redirect(url_for('admin_pedido'))

#Pedido Deletar pedido
@app.route("/deletar_pedido/<int:id>" , methods=['GET','POST'])
def deletar_pedido(id):
    del_pedido = session.get(tbl_pedido, id)
    session.delete(del_pedido)
    session.commit()
    session.close()
    return redirect(url_for('admin_pedido'))

# Gerar Pedido

@app.route("/gerar_pedido/<int:id>", methods=['GET','POST'])
def gerar_pedido(id):
    
    if request.method == 'POST':
        tb_ped = session.query(tbl_pedido).order_by(tbl_pedido.id_pedido).all()
        query_pd = session.get(tbl_pedido, id)
        query_cl = session.get(tbl_cliente, query_pd.cod_cliente)
        query_tl = session.get(tbl_telefone, query_cl.id_cliente)
        query_cd = session.get(tbl_cidade, query_cl.cod_cidade)
        query_uf = session.get(tbl_estado, query_cd.cod_estado)
        query_st = session.get(tbl_status_pedido, query_pd.cod_status)
        query_pj = session.get(tbl_pessoa_juridica, query_pd.cod_cliente ) 
        query_pf = session.get(tbl_pessoa_fisica, query_pd.cod_cliente ) 

        # id = request.form['id_pedido']
        if request.method == 'POST': 
            pedido = db_consultar_itens(id)
            total = 0
            for valor in pedido:
                total += valor['valor_total']  
                # print(valor)
                session.close()
            return render_template("report_pedido.html", pedido=pedido, tb_ped=tb_ped, id=id, query_cl=query_cl, query_cd=query_cd, query_uf=query_uf, query_tl=query_tl, query_pf=query_pf, query_pj=query_pj, query_st=query_st, query_pd=query_pd,  total=total)
    session.close()
    return render_template("admin_pedido.html")
