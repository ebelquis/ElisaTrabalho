from datetime import datetime

class TelaVenda():
    def tela_opcoes(self):
        print("-------- VENDAS ----------")
        print("Escolha a opcao")
        print("1 - Fazer Venda")
        print("2 - Listar Venda")
        print("3 - Excluir Venda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        print()
        return opcao

    def pega_dados_venda(self):
        print("-------- DADOS VENDA ----------")
        vendedor = input("Cpf do vendedor: ")
        cliente = input("Cpf do cliente: ")
        quantidade = input("Quantidade vendida: ")
        data = input("Data da venda(DD/MM/AAAA): ")
        data = datetime.strptime(data, "%d/%m/%Y") 
        codigo_produto = input("Codigo do produto: ")
        codigo = input("Codigo da venda: ")

        return {"vendedor": vendedor, 
                "cliente":cliente,
                "quantidade": quantidade,
                "data": data,
                "codigo_produto": codigo_produto,
                "codigo": codigo}

    def mostra_venda(self, dados_venda):
        print("CODIGO DA VENDA: ", dados_venda["codigo"])
        print("VENDEDOR: ", dados_venda["vendedor"])
        print("CLIENTE: ", dados_venda["cliente"])
        print("NOME DO PRODUTO: ", dados_venda["produto"])
        print("QUANTIDADE: ", dados_venda["quantidade"])
        print("DATA DA VENDA: ", dados_venda["data"])
        print("VALOR DA VENDA: ", dados_venda["valor"])
        print("\n")

    def seleciona_venda(self):
        codigo = input("Código da venda que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)