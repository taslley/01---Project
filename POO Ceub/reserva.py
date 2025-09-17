
from hospede import Hospede
from quarto import Quarto

class Reserva:
    def __init__(self, hospede: Hospede, quarto: Quarto):
        self._hospede = hospede
        self._quarto = quarto

    def get_hospede(self):
        return self._hospede

    def get_quarto(self):
        return self._quarto
