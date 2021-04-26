SELECT * FROM tbl_login;
SELECT * FROM tbl_cliente;
SELECT * FROM tbl_pessoa_fisica;
SELECT * FROM tbl_pessoa_juridica;
SELECT * FROM tbl_estado;
SELECT * FROM tbl_cidade;
SELECT * FROM tbl_telefone;
SELECT * FROM tbl_item;
SELECT * FROM tbl_ligacao_codigo;
SELECT * FROM tbl_pedido;
SELECT * FROM tbl_status_pedido;
SELECT * FROM tbl_produto;


INSERT INTO tbl_login (cod_cliente, nome, senha)
VALUES(1, 'alex', 'admin@1');

INSERT INTO tbl_cliente (endereco, cod_cidade)
VALUES('av teste', 1);

INSERT INTO tbl_pessoa_fisica (id_pessoa_fisica, nome, cpf, rg, data_nascimento)
VALUES(2, 'Adriel','30059129900', '445552503','01-01-1990');

UPDATE tbl_pessoa_fisica
SET data_nascimento = '1990-01-01'
WHERE id_pessoa_fisica = 2;


UPDATE tbl_cliente
SET cod_cidade = 1
WHERE id_cliente = 1;

SELECT *
FROM tbl_login
JOIN tbl_pessoa_fisica ON tbl_login.cod_cliente = tbl_pessoa_fisica.id_pessoa_fisica
JOIN tbl_cliente ON tbl_login.cod_cliente = tbl_pessoa_fisica.id_pessoa_fisica
JOIN tbl_cidade ON tbl_cidade.id_cidade = tbl_cliente.cod_cidade
JOIN tbl_estado ON tbl_estado.id_estado = tbl_cidade.cod_estado;

ALTER TABLE tbl_login 
MODIFY senha CHAR(200) NOT NULL ;

