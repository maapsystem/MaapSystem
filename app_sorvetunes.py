from flask import Flask, request, jsonify, render_template , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app_sorvetunes = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cliente.db"
#app_ac03.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbimpacta:impacta#2020@dbimpacta.postgresql.dbaas.com.br/dbimpacta'
#db = SQLAlchemy(app_ac03)

@app_sorvetunes.route("/")
@app_sorvetunes.route("/login")
def index():
    return render_template("login.html")

if __name__ == '__main__':
    #db.create_all()
    #db.drop_all()
    port = int(os.environ.get("PORT",5000))
    app_sorvetunes.run(debug=True, host='0.0.0.0', port=port)
    #app_sorvetunes.run(debug=True, host='0.0.0.0', port=port)
