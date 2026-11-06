"""Exercício 10.1 - Refatoração de GerenciadorDeVendas.

Code smells no original:
- Long Method / Divergent Change: um único método calcula total, aplica
  desconto, cobra, gera relatório e grava em arquivo (viola o SRP).
- Switch Statements: if/elif sobre `metodo_pagamento` (e sem `else`, então
  um método desconhecido passava em silêncio).
- Magic Numbers / Strings: 0.90, 'VIP', 'CARTAO', 'BOLETO', nome do arquivo.

Refatorações aplicadas: Extract Method / Extract Class,
Replace Conditional with Polymorphism (Strategy).
"""

from abc import ABC, abstractmethod

DESCONTO_VIP = 0.10
ARQUIVO_RELATORIO = "relatorio_vendas.txt"


# --- Cálculo -----------------------------------------------------------------
class CalculadoraDeVenda:
    def calcular_subtotal(self, itens):
        return sum(item["preco"] * item["quantidade"] for item in itens)

    def aplicar_desconto(self, total, cliente):
        if cliente["tipo"] == "VIP":
            return total * (1 - DESCONTO_VIP)
        return total


# --- Pagamento (Strategy) ----------------------------------------------------
class MetodoPagamento(ABC):
    @abstractmethod
    def cobrar(self, total):
        ...


class PagamentoCartao(MetodoPagamento):
    def cobrar(self, total):
        print(f"Cobrando R$ {total} no cartão de crédito...")


class PagamentoBoleto(MetodoPagamento):
    def cobrar(self, total):
        print(f"Gerando boleto no valor de R$ {total}...")


METODOS_PAGAMENTO = {
    "CARTAO": PagamentoCartao(),
    "BOLETO": PagamentoBoleto(),
}


# --- Relatório ---------------------------------------------------------------
class RelatorioDeVenda:
    def __init__(self, arquivo=ARQUIVO_RELATORIO):
        self.arquivo = arquivo

    def gerar(self, cliente, total):
        return (
            "--- Relatório de Venda ---\n"
            f"Cliente: {cliente['nome']}\n"
            f"Total: R$ {total}\n"
        )

    def salvar(self, relatorio):
        with open(self.arquivo, "a") as f:
            f.write(relatorio)


# --- Orquestrador ------------------------------------------------------------
class GerenciadorDeVendas:
    def __init__(self, calculadora=None, relatorio=None, metodos=None):
        self.calculadora = calculadora or CalculadoraDeVenda()
        self.relatorio = relatorio or RelatorioDeVenda()
        self.metodos = metodos or METODOS_PAGAMENTO

    def processar_venda(self, itens, cliente, metodo_pagamento):
        subtotal = self.calculadora.calcular_subtotal(itens)
        total = self.calculadora.aplicar_desconto(subtotal, cliente)

        self._cobrar(total, metodo_pagamento)

        self.relatorio.salvar(self.relatorio.gerar(cliente, total))
        print("Venda processada com sucesso.")
        return total

    def _cobrar(self, total, metodo_pagamento):
        metodo = self.metodos.get(metodo_pagamento)
        if metodo is None:
            raise ValueError(f"Método de pagamento desconhecido: {metodo_pagamento}")
        metodo.cobrar(total)
