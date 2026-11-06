"""Exercício 10.3 - Refatoração de criar_reserva.

Code smells no original:
- Long Parameter List: 9 parâmetros.
- Data Clumps: (nome, cpf, email) = hóspede; (numero, tipo, valor_diaria) =
  quarto; (checkin, checkout) = período.
- Magic Number: 50 (valor do café da manhã).
- Mixed Responsibilities: o mesmo método imprime e calcula o total.

Refatorações aplicadas: Introduce Parameter Object (Hospede, Quarto,
Periodo), Extract Class (Reserva), Replace Magic Number with Constant,
Extract Method (cálculo separado da exibição).
"""

from datetime import date

VALOR_CAFE_DA_MANHA_POR_DIA = 50


class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, valor_diaria):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria


class Periodo:
    def __init__(self, checkin, checkout):
        self.checkin = checkin
        self.checkout = checkout

    @property
    def total_dias(self):
        return (self.checkout - self.checkin).days


class Reserva:
    def __init__(self, hospede, quarto, periodo, possui_cafe_da_manha=False):
        self.hospede = hospede
        self.quarto = quarto
        self.periodo = periodo
        self.possui_cafe_da_manha = possui_cafe_da_manha

    def calcular_total(self):
        dias = self.periodo.total_dias
        total = dias * self.quarto.valor_diaria
        if self.possui_cafe_da_manha:
            total += VALOR_CAFE_DA_MANHA_POR_DIA * dias
        return total

    def exibir_resumo(self):
        print(f"Reserva criada para {self.hospede.nome} (CPF: {self.hospede.cpf})")
        print(f"Quarto {self.quarto.numero} ({self.quarto.tipo})")
        print(f"De {self.periodo.checkin} até {self.periodo.checkout}")
        print(f"Total a pagar: R$ {self.calcular_total()}")


def criar_reserva(hospede, quarto, periodo, possui_cafe_da_manha=False):
    reserva = Reserva(hospede, quarto, periodo, possui_cafe_da_manha)
    reserva.exibir_resumo()
    return reserva
