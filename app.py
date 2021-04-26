from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'esse_e_um_segredo'
app.config['SECURITY_PASSWORD_SALT'] = 'esse_e_um_segredo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://adminSovertunes:Sorvetunes2021@database-sorvetunes.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com/DB_SORVETUNES'


db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)

tbl_login = Base.classes.tbl_login
tbl_cliente = Base.classes.tbl_cliente
tbl_pessoa_fisica = Base.classes.tbl_pessoa_fisica
tbl_pessoa_juridica = Base.classes.tbl_pessoa_juridica
tbl_estado = Base.classes.tbl_estado
tbl_cidade = Base.classes.tbl_cidade
tbl_telefone = Base.classes.tbl_telefone
tbl_item = Base.classes.tbl_item
tbl_ligacao_codigo = Base.classes.tbl_ligacao_codigo
tbl_pedido = Base.classes.tbl_pedido
tbl_status_pedido = Base.classes.tbl_status_pedido
tbl_produto = Base.classes.tbl_produto

session = Session(db.engine)

from controlador import * 

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)