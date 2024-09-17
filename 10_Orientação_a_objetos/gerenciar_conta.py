from dominio.cliente import Cliente
from dominio.conta import Conta

lucas = Cliente("Lucas", '96545-8451')
jose = Cliente("Jose", '96111-8451')

conta1 = Conta(lucas, 2530, 4000)
conta2 = Conta(jose, 2650, 4000)

conta1.resumo()

conta1.deposito(2000)
conta1.resumo()

conta1.saque(5500)
conta1.resumo()