"""Exercício 10.6 - Refatoração de ProcessadorFinanceiro.

Code smells no original:
- Duplicated Code: crédito e débito têm exatamente a mesma estrutura
  (validar valor, aplicar taxa, imprimir); só mudam a taxa e o rótulo.
- Magic Numbers: 0.05 e 0.02.
- Comments: comentários que só repetem o que o código já diz
  ("Imprime o valor na tela"); o código deve se explicar por nomes.

Refatorações aplicadas: Extract Method (_processar), Replace Magic Number
with Constant, Remove Redundant Comments, Guard Clause.
"""

TAXA_CREDITO = 0.05
TAXA_DEBITO = 0.02


class ProcessadorFinanceiro:
    def processar_pagamento_credito(self, valor):
        self._processar("crédito", valor, TAXA_CREDITO)

    def processar_pagamento_debito(self, valor):
        self._processar("débito", valor, TAXA_DEBITO)

    def _processar(self, tipo, valor, taxa):
        if valor <= 0:
            print("Valor inválido")
            return
        valor_com_taxa = valor + valor * taxa
        print(f"Processando {tipo}: R$ {valor_com_taxa}")
