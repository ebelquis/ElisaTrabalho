from datetime import datetime

class TelaVenda():
    def tela_opcoes(self):
        print("-------- VENDAS ----------")
        print()
        print("1 - Fazer Venda")
        print("2 - Listar Venda")
        print("3 - Excluir Venda")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        print()
        return opcao

    def pega_dados_venda(self):
        print("-------- DADOS VENDA ----------")
        print()
        vendedor = input("CPF do vendedor: ")
        cliente = input("CPF do cliente: ")
        data = input("Data da venda(DD/MM/AAAA): ")
        data = datetime.strptime(data, "%d/%m/%Y") 
        codigo_produto = input("Código do produto: ")
        quantidade = input("Quantidade vendida: ")
        codigo = input("Código da venda: ")
        print()

        return {"vendedor": vendedor, 
                "cliente":cliente,
                "quantidade": quantidade,
                "data": data,
                "codigo_produto": codigo_produto,
                "codigo": codigo}

    def mostra_venda(self, dados_venda):
        print("CÓDIGO DA VENDA: ", dados_venda["codigo"])
        print("DATA DA VENDA: ", dados_venda["data"])
        print("VENDEDOR: ", dados_venda["vendedor"])
        print("CLIENTE: ", dados_venda["cliente"])
        print("NOME DO PRODUTO: ", dados_venda["produto"])
        print("QUANTIDADE: ", dados_venda["quantidade"])
        print("VALOR DA VENDA: ", dados_venda["valor"])
        print()

    def seleciona_venda(self):
        codigo = input("Código da venda que deseja selecionar: ")
        print()
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
        print()