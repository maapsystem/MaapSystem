from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from conexao import Conexao

import os

conexao = Conexao()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'esse e um segredo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://adminSovertunes:Sorvetunes2021@database-sorvetunes.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com/DB_SORVETUNES'

db = SQLAlchemy(app)


from controlador import * 

if __name__ == '__main__':
    #db.create_all()
    #db.drop_all()
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)