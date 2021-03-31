SELECT * FROM tbl_cidade;
SELECT * FROM tbl_cliente;
SELECT * FROM tbl_estado ;
SELECT * FROM tbl_item;
SELECT * FROM tbl_ligacao_codigo;
SELECT * FROM tbl_login;
SELECT * FROM tbl_pedido;
SELECT * FROM tbl_pedido;
SELECT * FROM tbl_produto;
SELECT * FROM tbl_status_pedido;

INSERT INTO tbl_cidade
(cidade,cod_estado)
VALUES
('São paulo', 2);

INSERT INTO tbl_cliente (nome, cod_cidade)
VALUES ('alex', 2);

INSERT INTO tbl_login (cod_cliente, nome, senha)
VALUES(9, 'alex', 'admin@1')
