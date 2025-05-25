from excessoes.TesteNumeroOpcoesException import TesteNumeroOpcoes

class TelaProduto(TesteNumeroOpcoes):

    def __init__(self):
        pass

    def teste_do_float(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = float(valor_recebido)
                    return valor_recebido_tipo
                except ValueError:
                    print("Por favor, escreva somente com numeros. (erro na digitação)")


    def teste_do_inteiro(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = int(valor_recebido)
                    return valor_recebido_tipo
                except ValueError:
                    print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def tela_opcoes(self):
        print("-------- PRODUTO ----------")
        print("Escolha a opcao")
        print("1 - Incluir Produto")
        print("2 - Alterar Valor Do Produto")
        print("3 - Alterar Quantidade De Estoque Do Produto")
        print("4 - Listar Produto")
        print("5- Excluir Produto")
        print("0 - Retornar")

        opcao = self.teste_numero_opcoes("Escolha a opcao: ", [0, 1, 2, 3, 4, 5])
        print("\n")
        return opcao

    def pega_dados_produto(self):
        print("-------- DADOS PRODUTO ----------")
        nome = input("Nome: ")
        codigo_produto = self.teste_do_inteiro("codigo_produto: ")
        preco_venda = self.teste_do_float("Preco de Venda: ")
        quant_estoque = self.teste_do_inteiro("Quantidade comprada: ")
        print("\n")
        
        return {"nome": nome, "codigo_produto": codigo_produto, "preco_venda": preco_venda, "quant_estoque": quant_estoque}  
    
    def pega_dados_produto_alterar(self):
        print("-------- VALOR PARA ALTERAR ----------")
        valor = self.teste_do_float("Preco venda / Quantidade a mais no estoque : ")
        print("\n")
        return valor

    def mostra_produto(self, dados_produto):
        print("NOME DO PRODUTO ", dados_produto["nome"])
        print("CODIGO DO PRODUTO: ", dados_produto["codigo_produto"])
        print("PRECO DO PRODUTO: ", dados_produto["preco_venda"])
        print("QUANTIDADE NO ESTOQUE DO PRODUTO: ", dados_produto["quant_estoque"])
        print("\n")

    def seleciona_produto(self):
        print("-------- SELECIONADOR DE PRODUTO ----------")
        codigo = self.teste_do_inteiro("Código do produto que deseja selecionar: ")
        print("\n")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
        print("\n")