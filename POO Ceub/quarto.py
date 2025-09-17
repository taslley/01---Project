
class Quarto:
    def __init__(self, numero, tipo, disponivel=True):
        self._numero = numero
        self._tipo = tipo
        self._disponivel = disponivel

    def reservar(self):
        if self._disponivel:
            self._disponivel = False
        else:
            print(f"Quarto {self._numero} já está ocupado.")

    def liberar(self):
        self._disponivel = True

    def estaDisponivel(self):
        return self._disponivel
