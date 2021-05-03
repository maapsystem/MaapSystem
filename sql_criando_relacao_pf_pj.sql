SET FOREIGN_KEY_CHECKS = 0; 
TRUNCATE TABLE tbl_login;
SET FOREIGN_KEY_CHECKS = 1;
SELECT * FROM tbl_login;

DROP TABLE tbl_login;

SET FOREIGN_KEY_CHECKS = 0; 
DROP TABLE tbl_cliente;
SET FOREIGN_KEY_CHECKS = 1;

SET FOREIGN_KEY_CHECKS = 0; 
TRUNCATE TABLE  tbl_cliente;
SET FOREIGN_KEY_CHECKS = 1;
SELECT * FROM tbl_cliente;


ALTER TABLE tbl_cliente
DROP COLUMN tipo_pessoa, 
DROP COLUMN  cpf, 
DROP COLUMN cnpj,
DROP COLUMN inscricao_estadual;

ALTER TABLE tbl_cliente
DROP COLUMN nome;

CREATE TABLE `tbl_pessoa_fisica` (
	`id_pessoa_fisica` int NOT NULL,
	`nome` varchar(100) NOT NULL,
	`cpf` char(11) NOT NULL UNIQUE,
	`rg` varchar(11),
    `data_nascimento` DATE NOT NULL , 
	PRIMARY KEY (`id_pessoa_fisica` )
);

CREATE TABLE `tbl_pessoa_juridica` (
	`id_pessoa_juridica` int NOT NULL,
	`nome_fantasia` varchar(100) NOT NULL,
	`razao_social` varchar(100) NOT NULL,
	`cnpj` char(14) NOT NULL UNIQUE,
	`inscricao_estadual` char(9) NULL,
    `data_fundacao` DATE NOT NULL , 
	PRIMARY KEY (`id_pessoa_juridica` )
);

DROP TABLE tbl_pessoa_juridica;

SELECT * FROM tbl_cliente;
SELECT * FROM tbl_login;
SELECT * FROM tbl_estado;
SELECT * FROM tbl_cidade;

SELECT * FROM tbl_pessoa_fisica;
SELECT * FROM tbl_pessoa_juridica;

ALTER TABLE `tbl_pessoa_fisica` ADD CONSTRAINT `tbl_pessoa_fisica_fk0` FOREIGN KEY (`id_pessoa_fisica`) REFERENCES `tbl_cliente`(`id_cliente`);

ALTER TABLE `tbl_pessoa_juridica` ADD CONSTRAINT `tbl_pessoa_juridica_fk0` FOREIGN KEY (`id_pessoa_juridica`) REFERENCES `tbl_cliente`(`id_cliente`);

ALTER TABLE `DB_SORVETUNES`.`tbl_pessoa_fisica` 
DROP FOREIGN KEY `tbl_pessoa_fisica_fk0`;
ALTER TABLE `DB_SORVETUNES`.`tbl_pessoa_fisica` 
ADD CONSTRAINT `tbl_pessoa_fisica_fk0`
  FOREIGN KEY (`id_pessoa_fisica`)
  REFERENCES `DB_SORVETUNES`.`tbl_cliente` (`id_cliente`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  
ALTER TABLE `DB_SORVETUNES`.`tbl_pessoa_juridica` 
DROP FOREIGN KEY `tbl_pessoa_juridica_fk0`;
ALTER TABLE `DB_SORVETUNES`.`tbl_pessoa_juridica` 
ADD CONSTRAINT `tbl_pessoa_juridica_fk0`
  FOREIGN KEY (`id_pessoa_juridica`)
  REFERENCES `DB_SORVETUNES`.`tbl_cliente` (`id_cliente`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
