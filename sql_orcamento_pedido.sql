SELECT * FROM tbl_cidade
ORDER BY cidade;

SELECT *
FROM tbl_pedido
JOIN tbl_pessoa_fisica ON tbl_pedido.cod_cliente = tbl_pessoa_fisica.id_pessoa_fisica
JOIN tbl_item ON tbl_pedido.id_pedido = tbl_item.cod_pedido
JOIN tbl_produto ON  tbl_item.cod_produto = tbl_produto.id_produto
JOIN tbl_ligacao_codigo ON tbl_pedido.id_pedido = tbl_ligacao_codigo.cod_pedido
JOIN tbl_status_pedido ON tbl_status_pedido.id_status = tbl_ligacao_codigo.cod_status;

SELECT * FROM tbl_pedido;
SELECT * FROM tbl_item;

SELECT * FROM tbl_status_pedido;
SELECT * FROM tbl_ligacao_codigo;

INSERT INTO tbl_pedido (data_pedido, cod_cliente, desconto)
VALUES(now(), 2, 0);

INSERT INTO tbl_item (quantidade_venda, valor_unitario, cod_produto, cod_pedido)
VALUES(30,40.30, 5, 2);

INSERT INTO tbl_ligacao_codigo (data_status, cod_pedido, cod_status)
VALUES(now(), 1, 1);
