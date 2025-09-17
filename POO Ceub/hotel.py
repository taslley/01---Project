
from quarto import Quarto
from reserva import Reserva
from hospede import Hospede

class Hotel:
    def __init__(self):
        self._quartos = []
        self._hospedes = []
        self._reservas = []

    def add_quarto(self, quarto):
        self._quartos.append(quarto)

    def remover_quarto(self, quarto):
        if quarto in self._quartos:
            self._quartos.remove(quarto)

    def registrar_hospede(self, hospede):
        self._hospedes.append(hospede)

    def cancelar_reserva(self, reserva):
        if reserva in self._reservas:
            self._reservas.remove(reserva)
            reserva.get_quarto().liberar()