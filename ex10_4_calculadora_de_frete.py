"""Exercício 10.4 - Refatoração de CalculadoraDeFrete.

Code smells no original:
- Switch Statements: cadeia if/elif sobre o tipo de transporte; cada novo
  transporte obriga a editar o método (viola o Open/Closed).
- Magic Numbers: 2.0, 3.5, 10.0, 8.0, 50.0, 1.0.

Refatoração aplicada: Replace Conditional with Polymorphism (Strategy).
Para adicionar um transporte, basta criar uma classe e registrá-la.
"""

from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def calcular(self, distancia):
        ...


class _TransportePorKm(Transporte):
    valor_por_km = 0.0
    taxa_base = 0.0

    def calcular(self, distancia):
        return distancia * self.valor_por_km + self.taxa_base


class Moto(_TransportePorKm):
    valor_por_km = 2.0


class Carro(_TransportePorKm):
    valor_por_km = 3.5
    taxa_base = 10.0


class Caminhao(_TransportePorKm):
    valor_por_km = 8.0
    taxa_base = 50.0


class Bicicleta(_TransportePorKm):
    valor_por_km = 1.0


class CalculadoraDeFrete:
    TRANSPORTES = {
        "MOTO": Moto(),
        "CARRO": Carro(),
        "CAMINHAO": Caminhao(),
        "BICICLETA": Bicicleta(),
    }

    def calcular_frete(self, tipo_transporte, distancia):
        transporte = self.TRANSPORTES.get(tipo_transporte)
        if transporte is None:
            raise ValueError("Tipo de transporte desconhecido")
        return transporte.calcular(distancia)
