-- Tabelas de inserts testes

INSERT INTO tbl_cliente (usuario, senha, endereco, num_endereco, complemento, bairro, cep, cod_cidade, contato, email, observacao)
VALUES('alex', 'alex', 'Av teste', '10', 'ap10', 'bairro teste', '01164030', 1, '', 'alex@teste.com','');
SELECT * FROM tbl_cliente;

INSERT INTO tbl_pessoa_fisica (id_pessoa_fisica, nome, cpf, rg, data_nascimento)
VALUES(3, 'Alexsandro2', '30659439450', '4756123-x', '1989-23-09');
SELECT * FROM tbl_pessoa_fisica;

DELETE FROM tbl_pessoa_fisica
WHERE id_pessoa_fisica = 2;

SELECT * FROM tbl_cidade;

INSERT INTO tbl_cliente (usuario, senha, cod_cidade)
VALUES('teste', 'teste', 1 );
SELECT * FROM tbl_cliente;

UPDATE tbl_pessoa_fisica
SET data_nascimento = '1990017'
WHERE id_pessoa_fisica = 34;
SELECT * FROM tbl_pessoa_fisica;

SELECT * FROM tbl_cliente;
SELECT * FROM tbl_pessoa_fisica;
SELECT * FROM tbl_telefone;


DELETE FROM tbl_pessoa_fisica
WHERE id_pessoa_fisica = 34;

SET FOREIGN_KEY_CHECKS = 0; 
TRUNCATE TABLE tbl_cliente;
TRUNCATE TABLE tbl_pessoa_fisica; 
TRUNCATE TABLE tbl_telefone;  
SET FOREIGN_KEY_CHECKS = 1;

DELETE FROM tbl_cliente
WHERE id_cliente = 34;

SELECT * FROM tbl_telefone;

INSERT INTO tbl_telefone (ddd, telefone, cod_cliente)
VALUES ('11','998548792',54);
INSERT INTO tbl_telefone (ddd, telefone, cod_cliente)
VALUES ('11','998548792',62);

SELECT * FROM tbl_produto;








