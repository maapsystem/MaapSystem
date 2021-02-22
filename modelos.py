from app import db

class Log(db.Model):
    __tablename__ = "tb_cadastro_login"
    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(10), nullable=True, unique=True)
    senha = db.Column(db.String(8), nullable=True)

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha