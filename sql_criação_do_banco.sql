-- CREATE DATABASE DB_SORVETUNES;

CREATE TABLE `tbl_login` (
	`id_usuario` int NOT NULL AUTO_INCREMENT,
	`cod_cliente` int NOT NULL UNIQUE,
	`nome` varchar(200) NOT NULL,
	`senha` char(20) NOT NULL,
	`data_login` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id_usuario`)
);

CREATE TABLE `tbl_cliente` (
	`id_cliente` int NOT NULL AUTO_INCREMENT,
	`endereco` varchar(100) NOT NULL,
	`num_endereco` varchar(6) NOT NULL,
	`complemento` varchar(40) NOT NULL,
	`bairro` varchar(50) NOT NULL,
	`cep` char(8) NOT NULL,
	`cod_cidade` int NOT NULL,
	`contato` varchar(40) NOT NULL,
	`email` varchar(150) NOT NULL,
	`observacao` TEXT(300) NOT NULL,
	`data_cliente` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id_cliente`)
);

CREATE TABLE `tbl_item` (
	`id_item` int NOT NULL AUTO_INCREMENT,
	`quantidade_venda` int NOT NULL,
	`valor_unitario` FLOAT NOT NULL,
	`cod_produto` int NOT NULL,
	`cod_pedido` int NOT NULL,
	PRIMARY KEY (`id_item`,`cod_produto`,`cod_pedido`)
);

CREATE TABLE `tbl_pedido` (
	`id_pedido` int NOT NULL AUTO_INCREMENT,
	`data_pedido` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`cod_cliente` int NOT NULL,
	`desconto` FLOAT NOT NULL,
	PRIMARY KEY (`id_pedido`)
);

CREATE TABLE `tbl_produto` (
	`id_produto` int NOT NULL,
	`nome_produto` varchar(200) NOT NULL,
	`descricao` varchar(200) NOT NULL,
	`qtd_produto` int NOT NULL,
	`valor_unitario` FLOAT NOT NULL,
	`data_produto` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id_produto`)
);

CREATE TABLE `tbl_status_pedido` (
	`id_status` int NOT NULL AUTO_INCREMENT,
	`descricao` varchar(150) NOT NULL,
	PRIMARY KEY (`id_status`)
);

CREATE TABLE `tbl_telefone` (
	`id_telefone` int NOT NULL AUTO_INCREMENT,
	`ddd` int(2) NOT NULL,
	`telefone` varchar(9) NOT NULL,
	`cod_cliente` int NOT NULL,
	PRIMARY KEY (`id_telefone`)
);

CREATE TABLE `tbl_estado` (
	`id_estado` int NOT NULL AUTO_INCREMENT,
	`estado` varchar(50) NOT NULL,
	PRIMARY KEY (`id_estado`)
);

CREATE TABLE `tbl_cidade` (
	`id_cidade` int NOT NULL AUTO_INCREMENT,
	`cidade` varchar(50) NOT NULL,
	`cod_estado` int NOT NULL,
	PRIMARY KEY (`id_cidade`)
);

CREATE TABLE `tbl_ligacao_codigo` (
	`id_ligacao_codigo` int NOT NULL AUTO_INCREMENT,
	`data_status` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`cod_pedido` int NOT NULL,
	`cod_status` int NOT NULL,
	PRIMARY KEY (`id_ligacao_codigo`,`cod_pedido`,`cod_status`)
);

ALTER TABLE `tbl_login` ADD CONSTRAINT `tbl_login_fk0` FOREIGN KEY (`cod_cliente`) REFERENCES `tbl_cliente`(`id_cliente`);

ALTER TABLE `tbl_cliente` ADD CONSTRAINT `tbl_cliente_fk0` FOREIGN KEY (`cod_cidade`) REFERENCES `tbl_cidade`(`id_cidade`);

ALTER TABLE `tbl_item` ADD CONSTRAINT `tbl_item_fk0` FOREIGN KEY (`cod_produto`) REFERENCES `tbl_produto`(`id_produto`);

ALTER TABLE `tbl_item` ADD CONSTRAINT `tbl_item_fk1` FOREIGN KEY (`cod_pedido`) REFERENCES `tbl_pedido`(`id_pedido`);

ALTER TABLE `tbl_pedido` ADD CONSTRAINT `tbl_pedido_fk0` FOREIGN KEY (`cod_cliente`) REFERENCES `tbl_cliente`(`id_cliente`);

ALTER TABLE `tbl_telefone` ADD CONSTRAINT `tbl_telefone_fk0` FOREIGN KEY (`cod_cliente`) REFERENCES `tbl_cliente`(`id_cliente`);

ALTER TABLE `tbl_cidade` ADD CONSTRAINT `tbl_cidade_fk0` FOREIGN KEY (`cod_estado`) REFERENCES `tbl_estado`(`id_estado`);

ALTER TABLE `tbl_ligacao_codigo` ADD CONSTRAINT `tbl_ligacao_codigo_fk0` FOREIGN KEY (`cod_pedido`) REFERENCES `tbl_pedido`(`id_pedido`);

ALTER TABLE `tbl_ligacao_codigo` ADD CONSTRAINT `tbl_ligacao_codigo_fk1` FOREIGN KEY (`cod_status`) REFERENCES `tbl_status_pedido`(`id_status`);

ALTER TABLE tbl_estado add `uf` char(2) NOT NULL; 

ALTER TABLE tbl_cliente add `cidade` VARCHAR(50) NOT NULL; 
ALTER TABLE tbl_cliente add `uf` CHAR(2) NOT NULL; 
ALTER TABLE tbl_cliente add `estado` VARCHAR(50) NOT NULL; 