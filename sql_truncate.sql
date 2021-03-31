
TRUNCATE TABLE tbl_login;

SET FOREIGN_KEY_CHECKS = 0; 
TRUNCATE TABLE tbl_cliente;
SET FOREIGN_KEY_CHECKS = 1;

SET FOREIGN_KEY_CHECKS = 0; 
TRUNCATE TABLE tbl_cidade;
SET FOREIGN_KEY_CHECKS = 1;

DELETE FROM tbl_cidade WHERE (`id_cidade` = '2');
DELETE FROM tbl_cidade WHERE (`id_cidade` = '3');
DELETE FROM tbl_cliente WHERE (`id_cliente` = '9');

SELECT * FROM tbl_cidade;
SELECT * FROM tbl_login;
SELECT * FROM tbl_cliente;
SELECT * FROM tbl_estado;

ALTER TABLE tbl_cliente
DROP COLUMN cidade, 
DROP COLUMN  uf, 
DROP COLUMN estado;


-- LOAD DATA LOCAL INFILE 'c:/Users/Fred/Desktop/municipios.csv'  //Aqui vc especifica o local do arquivo
-- INTO TABLE municipios          //Aqui você especifica o nome da tabela
-- FIELDS TERMINATED BY ';'    //Aqui será o tipo de separador 
--  LINES TERMINATED BY '\r\n'   //Aqui é a quebra de cada linha por inserts
-- (uf, codigo, nome)   // Aqui você coloca os campos na mesma sequencia das células do arquivo.csv

LOAD DATA LOCAL INFILE 'C:/git/wca_py/exercicio_tbl_estados_cidades/cidades_newload.csv' 
INTO TABLE tbl_cidade
CHARACTER SET UTF8
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(cidade, cod_estado);
SELECT * FROM tbl_cidade;
SELECT * FROM tbl_cidade LIMIT 10444;

INSERT INTO tbl_cliente (tipo_pessoa, nome, cpf, cnpj, inscricao_estadual, endereco, num_endereco,complemento, bairro, cep, cod_cidade, contato, email, observacao)
VALUES ('pessoa física', 'Alexsandro Augusto Ignácio', '36159729800', '', '', 'Av Teste', '10', 'ap 10', 'centro', '01154020',  1, 'noiva','alex@contato.com.br', 'programador');
SELECT * FROM tbl_cliente;

INSERT INTO tbl_login (cod_cliente, nome, senha)
VALUES (1, 'alex', 'admin@1');
SELECT * FROM tbl_login;
 
ALTER TABLE tbl_cliente MODIFY tipo_pessoa VARCHAR(20) ;
 
UPDATE tbl_cliente
SET tipo_pessoa = 'Pessoa Física'
WHERE id_cliente = 1;
SELECT * FROM tbl_cliente;
