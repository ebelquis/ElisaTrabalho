from excessoes.TesteNumeroOpcoesException import TesteNumeroOpcoes

class TelaPessoa(TesteNumeroOpcoes):
    
    def __init__(self):
        pass
    
    def teste_do_inteiro(self, mensagem=" "):
            while True:
                valor_recebido = input(mensagem)
                try:
                    valor_recebido_tipo = int(valor_recebido)
                    return valor_recebido_tipo
                except ValueError:
                    print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def teste_do_cpf(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if len(valor_recebido) == 11:
                    return valor_recebido_tipo
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros e 9 digitos. Exemplo 1234 (erro na digitação)")

    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Cliente")
        print("2 - Incluir Vendedor")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("5 - Listar Vendedores")
        print("6 - Excluir Vendedor")
        print("0 - Retornar")

        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0,1,2,3,4,5,6])
        print("\n")
        return opcao

    def pega_dados_pessoa(self):
        print("-------- DADOS PESSOA ---------")
        nome = input("Nome: ")
        cpf = self.teste_do_cpf("CPF: ")
        celular = self.teste_do_inteiro("Celular (deve ser escrito na forma: 984847837): ")

        return {"nome": nome, "cpf": cpf, "celular": celular}

    def mostra_cliente(self, dados_cliente):
        print("------CLIENTE------")
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("CPF DO CLIENTE: ", dados_cliente["cpf"])
        print("CELULAR DO CLEINTE: ", dados_cliente["celular"])
        print("\n")

    def mostra_vendedor(self, dados_vendedor):
        print("------VENDEDOR------")
        print("NOME DO VENDEDOR: ", dados_vendedor["nome"])
        print("CPF DO VENDEDOR: ", dados_vendedor["cpf"])
        print("CELULAR DO VENDEDOR: ", dados_vendedor["celular"])
        print("VALOR VENDIDO TOTAL DO VENDEDOR: R$", dados_vendedor["valor_vendido_total"])
        print("\n")
    
    def seleciona_pessoa(self):
        cpf = self.teste_do_inteiro("CPF da pessoa que deseja selecionar (deve conter somente numeros - sem caracteres especiais): ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)