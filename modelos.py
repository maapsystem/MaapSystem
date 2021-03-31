from app import db

class Log(db.Model):
    __tablename__ = "tbl_login"
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=True, unique=True)
    senha = db.Column(db.String(20), nullable=True)


    def __init__(self, nome, senha):
        self.usuario = nome
        self.senha = senha