from excessoes.TesteNumeroOpcoesException import TesteNumeroOpcoes


class TelaRelatorios(TesteNumeroOpcoes):
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- RELATÓRIOS ----------")
        print()
        print("1 - Rentabilidade por Produto")
        print("2 - Análise de Produtos Mais Vendidos")
        print("3 - Vendas por Vendedor")
        print("0 - Retornar")
        print()
        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0, 1, 2, 3])
        print("\n")
        return opcao

    def mostra_rentabilidade_produto(self, dados_rentabilidade):
        print("PRODUTO:", dados_rentabilidade['nome'])
        print("CÓDIGO:", dados_rentabilidade['codigo_produto'])
        print(f"PREÇO DE VENDA: R${dados_rentabilidade['preco_venda']:.2f}")
        print(f"PREÇO DE COMPRA: R${dados_rentabilidade['preco_compra']:.2f}")
        print(f"LUCRO POR UNIDADE: R${dados_rentabilidade['lucro_unidade']:.2f}")
        print()

    def mostra_analise_produtos_vendidos(self, dados_analise):
        print(f"{dados_analise['lugar']}º LUGAR")
        print("PRODUTO:", dados_analise['nome'])
        print("CÓDIGO:", dados_analise['codigo_produto'])
        print("QUANT TOTAL VENDIDA:", dados_analise['quantidade_total_vendida'])
        print(f"VALOR TOTAL VENDIDO: R${dados_analise['valor_total_vendido']:.2f}")
        print()

    def mostra_vendas_por_vendedor(self, dados_vendedor):
        print(f"{dados_vendedor['lugar']}º lugar")
        print("NOME:", dados_vendedor['nome'])
        print("CPF:", dados_vendedor['cpf'])
        print(f"VALOR TOTAL VENDIDO: R${dados_vendedor['valor_total_vendido']:.2f}")
        print()

    def mostra_mensagem(self, msg):
        print(msg)
        print()