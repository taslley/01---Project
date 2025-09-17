
from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)
        self._reservas = []

    def fazer_reserva(self, reserva):
        self._reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        self._reservas.remove(reserva)

    def consultar_reservas(self):
        return self._reservas
