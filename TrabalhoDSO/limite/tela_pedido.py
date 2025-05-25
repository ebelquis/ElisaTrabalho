from datetime import datetime


class TelaPedido():
    def tela_opcoes(self):
        print("-------- PEDIDOS ----------")
        print("Escolha a opcao")
        print("1 - Fazer Pedido")
        print("2 - Listar Pedido")
        print("3 - Excluir Pedido")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        print()
        return opcao

    def pega_dados_pedido(self):
        print("-------- DADOS PEDIDOS ----------")
        cnpj = input("CNPJ do fornecedor: ")
        codigo = input("Codigo do pedido: ")
        codigo_produto = input("Codigo do Produto: ")
        quantidade = input("Quantidade do pedido: ")
        data = input("Data do pedido feito (DD/MM/AAAA): ")
        data = datetime.strptime(data, "%d/%m/%Y") #fazer tratamento de erro aqui AAAAA
        valor_frete = input("Valor do frete do pedido: ")
        prazo_entrega = input("Prazo do pedido (dias): ")

        return {"cnpj": cnpj, "codigo": codigo,
                "codigo_produto": codigo_produto,
                "quantidade": quantidade,
                "data": data,
                "valor_frete": valor_frete,
                "prazo_entrega": prazo_entrega}
    

    def mostra_pedidos(self, dados_pedidos):
        print("CODIGO DO PEDIDO: ", dados_pedidos["codigo"])
        print("QUANTIDADE DO PEDIDO: ", dados_pedidos["quantidade"])
        print("NOME DO PRODUTO: ", dados_pedidos["nome_produto"])
        print("DATA DO PEDIDO: ", dados_pedidos["data"])
        print("VALOR DO PRODUTO: ", dados_pedidos["valor"])
        print("NOME DO FORNECEDOR: ", dados_pedidos["nome_fornecedor"])
        print("VALOR DO FRETE: ", dados_pedidos["frete"])
        print("PRAZO DE ENTREGA: ", dados_pedidos["prazo_entrega"])
        print("\n")

    def seleciona_pedido(self):
        codigo = input("Código do pedido que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)