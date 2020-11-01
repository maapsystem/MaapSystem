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

'''

select * from maap_system
delete from maap_system

from app_ac03 import db
db.create_all()
db.drop_all()

http://localhost:5000/

py -m venv venv_xxx       #maquina virtual
venv_xxx\Scripts\activate  #ativando maquina virtual
pip install Flask       
pip install pip ou py -m pip install --upgrade pip
pip install Flask-SQLAlchemy

pip install pipenv
pipenv install requests
pipenv install "dependency"

python -m venv crud_env
crud_env\Scripts\ activate

pip freeze > requirements.txt

heroku
pipenv check
heroku login
cltr c devolve o prompt
heroku create
git push heroku master
git push heroku HEAD:master
heroku ps:scale web=1
heroku open
heroku apps
heroku apps:destroy "nome do app sem aspas"
heroku apps:destroy arcene-40228
heroku buildpacks:clear
heroku buildpacks:add --index heroku/python
heroku logs --tail
heroku logs  > herokulogs
heroku apps:rename NEWNAME
heroku apps:rename crud-cadastro-alunos --app boiling-tundra-56022 
heroku apps:rename maapsystem_sorvetunes --app fathomless-reaches-29620

heroku git:remote -a maapsystem-sorvetunes
git add .


'''