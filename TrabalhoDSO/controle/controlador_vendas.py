from limite.tela_venda import TelaVenda
from entidade.venda import Venda
from datetime import datetime

class ControladorVendas():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__vendas = []
    self.__tela_venda = TelaVenda()

  def pega_venda_por_codigo(self, codigo: str):
    for venda in self.__vendas:
      if(venda.codigo == int(codigo)):
        return venda
    return None

  def incluir_venda(self):
      self.__controlador_sistema.controlador_pessoas.lista_cliente()
      self.__controlador_sistema.controlador_pessoas.lista_vendedores()
      dados_venda = self.__tela_venda.pega_dados_venda()
      try:
          quantidade = int(dados_venda["quantidade"])
          data = dados_venda["data"]
          codigo_produto = int(dados_venda["codigo_produto"])
          codigo_venda = int(dados_venda["codigo"])
          cliente = self.__controlador_sistema.controlador_pessoas.pega_cliente_por_cpf(dados_venda["cpf_cliente"])
          vendedor = self.__controlador_sistema.controlador_pessoas.pega_vendedor_por_cpf(dados_venda["cpf_vendedor"])
          produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(dados_venda["codigo_produto"])
          if cliente is None or vendedor is None or produto is None:
              self.__tela_venda.mostra_mensagem("Erro: Cliente, vendedor ou produto não encontrado.")
              return
          venda_existe = self.pega_venda_por_codigo(dados_venda["codigo"])
          if venda_existe is not None:
              self.__tela_venda.mostra_mensagem("Erro: Já existe uma venda com este código.")
              return
          if produto.quant_estoque < quantidade:
              self.__tela_venda.mostra_mensagem("Erro: Estoque insuficiente.")
              return
          valor_total = produto.preco_venda * quantidade
          nova_venda = Venda(
              quantidade=quantidade,
              produto=produto,
              data=data,
              valor_total=valor_total,
              codigo=codigo_venda,
              cliente=cliente,
              vendedor=vendedor
          )
          self.__vendas.append(nova_venda)
          produto.quant_estoque -= quantidade
          vendedor.valor_vendido_total += valor_total  
          self.__tela_venda.mostra_mensagem("Venda cadastrada com sucesso!")
      except ValueError:
          self.__tela_venda.mostra_mensagem("Erro: Dados inválidos (certifique-se de que números estão corretos).")
      except Exception as e:
          self.__tela_venda.mostra_mensagem(e)

  def lista_venda(self):
    for venda in self.__vendas:
      self.__tela_venda.mostra_venda({"codigo": venda.codigo,
                                      "vendedor": venda.vendedor.nome,
                                      "cliente": venda.cliente.nome,
                                      "produto": venda.produto.nome,
                                      "quantidade": venda.quantidade,
                                      "data": venda.data.strftime("%d/%m/%Y"),
                                      "valor": venda.valor_total})
    
  def excluir_venda(self):
    self.lista_venda()
    codigo_venda = self.__tela_venda.seleciona_venda()
    venda = self.pega_venda_por_codigo(codigo_venda)

    if (venda is not None):
      venda.vendedor.valor_vendido_total -= venda.valor
      venda.produto.quant_estoque += venda.quantidade
      self.__vendas.remove(venda)
      self.__tela_venda.mostra_mensagem("Venda excluída com sucesso!")
      self.lista_venda()
    else:
      self.__tela_venda.mostra_mensagem("ATENÇÃO: Venda não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_venda,
                    2: self.lista_venda,
                    3: self.excluir_venda,
                    0: self.retornar}

    while True:
        opcao_escolhida = self.__tela_venda.tela_opcoes()
        if opcao_escolhida in lista_opcoes:
            lista_opcoes[opcao_escolhida]()
        else:
            self.__tela_venda.mostra_mensagem("Opção inválida, digite novamente.")