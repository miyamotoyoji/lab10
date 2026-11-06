"""Exercício 10.7 - Refatoração da cadeia de mensagens.

Code smell no original:
- Message Chains: o cliente do código navega
  pedido.cliente.endereco.estado.pais.nome, acoplando
  `verificar_frete_internacional` à estrutura interna de cinco classes
  (viola a Lei de Demeter: "fale apenas com seus amigos próximos").

Refatoração aplicada: Hide Delegate. Cada classe expõe o que a anterior
precisa, e quem consome só fala com Pedido.
"""

PAIS_ORIGEM = "Brasil"


class Pais:
    def __init__(self, nome):
        self.nome = nome


class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    @property
    def nome_pais(self):
        return self.pais.nome


class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

    @property
    def nome_pais(self):
        return self.estado.nome_pais


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    @property
    def nome_pais(self):
        return self.endereco.nome_pais


class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    @property
    def pais_destino(self):
        return self.cliente.nome_pais

    def eh_internacional(self):
        return self.pais_destino != PAIS_ORIGEM


def verificar_frete_internacional(pedido):
    if pedido.eh_internacional():
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão.")
