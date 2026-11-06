"""Exercício 10.2 - Refatoração de Funcionario.

Code smells no original:
- Data Clumps: rua, numero, bairro, cidade, estado, cep sempre aparecem
  juntos; ddd e telefone_numero também.
- Long Parameter List: __init__ com 12 parâmetros.
- Large Class: Funcionario conhece detalhes de endereço e telefone.

Refatorações aplicadas: Extract Class (Endereco, Telefone) e
Introduce Parameter Object.
"""


class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return (
            f"{self.rua}, {self.numero} - {self.bairro}, "
            f"{self.cidade}/{self.estado} - CEP: {self.cep}"
        )


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f"({self.ddd}) {self.numero}"


class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Funcionario: {self.nome} - {self.cargo}")
        print(f"Contato: {self.telefone}")
        print(f"Endereço: {self.endereco}")
