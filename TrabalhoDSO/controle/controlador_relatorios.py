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
            return
        self.__tela_relatorios.mostra_mensagem("...GERANDO RELATÓRIO DE RENTABILIDADE...")

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
            self.__tela_relatorios.mostra_mensagem("------ RENTABILIDADE POR PRODUTO ----")
            self.__tela_relatorios.mostra_rentabilidade_produto(dados_rentabilidade)
        self.__tela_relatorios.mostra_mensagem("-----------------------")

    def analisar_produtos_mais_vendidos(self):
        vendas = self.__controlador_sistema.controlador_vendas.vendas
        if not vendas:
            self.__tela_relatorios.mostra_mensagem("Não há vendas registradas para análise.")
            return

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

        