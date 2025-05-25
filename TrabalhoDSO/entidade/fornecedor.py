from entidade.produto import Produto
from entidade.endereco import Endereco

class Fornecedor:
    def __init__(self, nome: str, cnpj: str, celular: str, produto: Produto, preco: float):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__celular = celular
        self.__produto = produto
        self.__preco = preco
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        self.__cnpj = cnpj

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular: str):
        self.__celular = celular

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto: Produto):
        self.__produto = produto

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        self.__preco = preco

    @property
    def enderecos(self):
        return self.__enderecos

    def incluir_endereco(self, cep: str, rua: str, numero: str):
        self.__enderecos.append(Endereco(cep, rua, numero))
