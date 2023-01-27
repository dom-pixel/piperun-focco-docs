# this script is aimed to people who want to generate a POST json body just by you passing your params into the params array

params = ["nome", "codigoSegmentoMercado", "codigoTipoCliente", "nomeEstabelecimento", 'nomeFantasia', "cnpj", "cpf", "inscricaoEstadual", "cep", "logradouro", "numero",
          "bairro", "codigoMicrorregiao", "codigoCidade", "codigotabelaVenda", "ddd", "numeroTeledone", "TipoDeTelefone", "email", "codigoRepresentante", "codigoTransportadora"]

n = 0
print("{")
while n < len(params):
    print('"' + params[n] + '": ""')
    n += 1
print("}")
