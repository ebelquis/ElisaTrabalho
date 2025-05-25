from limite.tela_produto import TelaProduto
from entidade.produto import Produto


class ControladorPedidos():
    def __init__(self, controlador_sistema):
        self.__produtos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_produto = TelaProduto()

    def pega_produto_por_codigo_produto(self, codigo_produto: int):
        for i in self.__produtos:
            if i.codigo_produto == codigo_produto:
                return i
        return None

    def incluir_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        codigo_produto = self.pega_produto_por_codigo_produto(dados_produto["codigo_produto"])
        if codigo_produto is None:
            produto = Produto(dados_produto["nome"], 
                              dados_produto["codigo_produto"],
                              dados_produto["preco_venda"],
                              dados_produto["quant_estoque"])
            self.__produtos.append(produto)
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto já existente")

    def alterar_preco_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo_produto(codigo_produto)
        if produto is not None:
            valor = self.__tela_produto.pega_dados_produto_alterar()
            produto.preco_venda = int(produto.preco_venda) + int(valor)
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

    def alterar_estoque(self):
        self.lista_produtos()
        codigo_produto_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo_produto(codigo_produto_produto)
        if produto is not None:
            valor = self.__tela_produto.pega_dados_produto_alterar()
            produto.quant_estoque = int(produto.quant_estoque) + int(valor) 
            self.lista_produtos()

    def lista_produtos(self):
        for produto in self.__produtos:
            self.__tela_produto.mostra_produto({"nome": produto.nome,
                                              "codigo_produto": produto.codigo_produto,
                                              "preco_venda": produto.preco_venda,
                                              "quant_estoque": produto.quant_estoque})

    def excluir_produto(self):
        self.lista_produtos()
        codigo_produto_produto = self.__tela_produto.seleciona_produto()
        produto = self.pega_produto_por_codigo_produto(codigo_produto_produto)
        if produto is not None:
            self.__produtos.remove(produto)
        else:
            self.__tela_produto.mostra_mensagem("ATENCAO: Produto não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_produto,
                        2: self.alterar_preco_produto,
                        3: self.alterar_estoque,
                        4: self.lista_produtos,
                        5: self.excluir_produto,
                        0: self.retornar}

        continua = True
        while continua:
            opcao = self.__tela_produto.tela_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()