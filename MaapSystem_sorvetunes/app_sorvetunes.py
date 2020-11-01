from flask import Flask, request, jsonify, render_template , redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app_ac03 = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cliente.db"
app_ac03.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbimpacta:impacta#2020@dbimpacta.postgresql.dbaas.com.br/dbimpacta'
db = SQLAlchemy(app_ac03)

if __name__ == '__main__':
    #db.create_all()
    #db.drop_all()
    port = int(os.environ.get("PORT",5000))
    app_ac03.run(debug=True, host='0.0.0.0', port=port)