from limite.tela_relatorios import TelaRelatorios
from excessoes.NaoEncontradoNaListaException import NaoEncontradoNaListaException


class ControladorRelatorios():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorios = TelaRelatorios()

    def gerar_relatorio_rentabilidade(self):
        produtos = self.__controlador_sistema.controlador_produtos.produtos
        if not produtos:
            self.__tela_relatorios.mostra_mensagem("Não há produtos para gerar o relatório de rentabilidade.")
            return None
        
        self.__tela_relatorios.mostra_mensagem("------ RENTABILIDADE POR PRODUTO ----")
        for produto in produtos:
            preco_compra = 0
            for fornecedor in self.__controlador_sistema.controlador_fornecedores.fornecedores:
                if fornecedor.produto.codigo_produto == produto.codigo_produto:
                    preco_compra = fornecedor.preco
                    break
            #preço de compra nunca vai ser 0 porque n trabalhamos com doações
            if not preco_compra != 0:
                self.__tela_relatorios.mostra_mensagem(f"ATENÇÃO: Não foi encontrado preço de compra para o produto {produto.nome}.")
                lucro_unidade = "Não é possível calcular o lucro"
                preco_compra = "Sem preço de compra"
            else:
                lucro_unidade = produto.preco_venda - preco_compra

            dados_rentabilidade = { 
                "nome": produto.nome,
                "codigo_produto": produto.codigo_produto,
                "preco_venda": produto.preco_venda,
                "preco_compra": preco_compra,
                "lucro_unidade": lucro_unidade
            }
            self.__tela_relatorios.mostra_rentabilidade_produto(dados_rentabilidade)

    def analisar_produtos_mais_vendidos(self):
        vendas = self.__controlador_sistema.controlador_vendas.vendas
        if not vendas:
            self.__tela_relatorios.mostra_mensagem("Não há vendas registradas para análise.")
            return None

        todos_produtos_vendidos = {} #dicionário de dicionários => codigo: dicionário do produto
        for venda in vendas:
            codigo_produto = int(venda.produto.codigo_produto)
            if codigo_produto not in todos_produtos_vendidos:
                todos_produtos_vendidos[codigo_produto] = {
                    "nome": venda.produto.nome,
                    "codigo_produto": codigo_produto,
                    "quantidade_total_vendida": 0,
                    "valor_total_vendido": 0
                }
            todos_produtos_vendidos[codigo_produto]["quantidade_total_vendida"] += venda.quantidade
            todos_produtos_vendidos[codigo_produto]["valor_total_vendido"] += venda.valor

        #isso daqui foi 100% pesquisado
        lista_ordenada = sorted(todos_produtos_vendidos.values(), key=lambda x: x["quantidade_total_vendida"], reverse=True)

        if not lista_ordenada:
            self.__tela_relatorios.mostra_mensagem("Nenhum produto foi vendido.")
            return None
        self.__tela_relatorios.mostra_mensagem("------ ANÁLISE DE PRODUTOS MAIS VENDIDOS ------")
        for produto_dados in lista_ordenada:
            self.__tela_relatorios.mostra_mensagem(f"{lista_ordenada.index(produto_dados)+1}º lugar", end = "")
            self.__tela_relatorios.mostra_analise_produtos_vendidos(produto_dados)

    def relatorio_vendas_por_vendedor(self):
        vendedores = self.__controlador_sistema.controlador_pessoas.vendedores # Acessa a lista de vendedores
        if not vendedores:
            self.__tela_relatorios.mostra_mensagem("Não há vendedores cadastrados para gerar o relatório.")
            return None
        self.__tela_relatorios.mostra_mensagem("----- RELATÓRIO DE VENDAS POR VENDEDOR -----")
        
        lista_ordenada = sorted(vendedores, key=lambda x: x.valor_vendido_total, reverse=True)
        if not lista_ordenada:
            self.__tela_relatorios.mostra_mensagem("Nenhum vendedor possui vendas registradas.")
            return None
        lugar = 0
        for vendedor in lista_ordenada:
            lugar += 1
            dados_vendedor = {
                "lugar": lugar,
                "nome": vendedor.nome,
                "cpf": vendedor.cpf,
                "valor_total_vendido": vendedor.valor_vendido_total
            }
            self.__tela_relatorios.mostra_vendas_por_vendedor(dados_vendedor)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.gerar_relatorio_rentabilidade,
                        2: self.analisar_produtos_mais_vendidos,
                        3: self.relatorio_vendas_por_vendedor,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_relatorios.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_relatorios.mostra_mensagem("Opção inválida, digite novamente.")
