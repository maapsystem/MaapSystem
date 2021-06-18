function SetValor(valor) {

    var strArray;
    var strDescProd;
    if (valor == ""){
      alert("Valor não encontrado");
    } else {
      strArray = valor.split("-");
  
      document.getElementById('id_cod_produto').value = strArray[0];
      document.getElementById('id_valor_unitario').value = strArray[1];
  
      strDescProd = strArray[1].replace(".", ",");
      document.getElementById('id_desc_valor_unitario').value = 'R$ ' + strDescProd;
    }
  
  }