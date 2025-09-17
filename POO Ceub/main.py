
from funcionario import Funcionario
from hospede import Hospede
from quarto import Quarto
from reserva import Reserva
from hotel import Hotel

# Criando instâncias para testes
hotel = Hotel()

# Criando Quartos
quarto1 = Quarto(121, "Simples", True)
quarto2 = Quarto(122, "Duplo", True)

# Adicionando quartos ao hotel
hotel.add_quarto(quarto1)
hotel.add_quarto(quarto2)

# Criando Funcionário e Hospede
funcionario = Funcionario(1, "Carlos", "carlos@funcionario.com")
hospede = Hospede(2, "Tallis", "Tallis@hospede.com")

# Registrando Hospede no hotel
hotel.registrar_hospede(hospede)

# Criando e fazendo uma reserva
reserva1 = Reserva(hospede, quarto1)
hospede.fazer_reserva(reserva1)
hotel._reservas.append(reserva1)

# Exibindo status da reserva
print(f"Reserva feita: Hospede {reserva1.get_hospede().get_nome()} no quarto {reserva1.get_quarto()._numero}")

# Verificando disponibilidade
print(f"Quarto 121 disponível? {quarto1.estaDisponivel()}")

# Cancelando a reserva
hospede.cancelar_reserva(reserva1)
hotel.cancelar_reserva(reserva1)

# Verificando novamente a disponibilidade
print(f"Quarto 121 disponível após cancelamento? {quarto1.estaDisponivel()}")
