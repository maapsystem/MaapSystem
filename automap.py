from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine



Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine('mysql://adminSovertunes:Sorvetunes2021@database-sorvetunes.c0ymnqcdkbj5.us-east-2.rds.amazonaws.com/DB_SORVETUNES')

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.

tbl_cidade = Base.classes.tbl_cidade
tbl_cliente = Base.classes.tbl_cliente
tbl_estado = Base.classes.tbl_estado
tbl_item = Base.classes.tbl_item
tbl_ligacao_codigo = Base.classes.tbl_ligacao_codigo
tbl_login = Base.classes.tbl_login
tbl_pedido = Base.classes.tbl_pedido
tbl_produto = Base.classes.tbl_produto
tbl_status_pedido = Base.classes.tbl_status_pedido
tbl_telefone = Base.classes.tbl_telefone


session = Session(engine)

# rudimentary relationships are produced
results = session.query(tbl_estado).all()

results2 = session.query(tbl_estado).filter_by(tbl_estado.uf == 'SP').first()

#print(results2)
# collection-based relationships are by default named
# "<classname>_collection"

for dados in results2:
    print (dados.id_estado)