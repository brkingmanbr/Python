from Cliente import Cliente as Cli
from Conta import Conta as Con
from ContaEspecial import ContaEspecial as CE
from Banco import Banco
class Controle():
    def __init__(self):
        self.Cliente = Cli
        self.Conta = Con
        self.ContaEspecial = CE

    def cli_nome(self, nome):
        self.Cliente.nome = nome
    def cli_telefone(self, telefone):
        self.Cliente.telefone = telefone

    def conta(self, numero):
        self.Conta.__init__(
            self.Cliente,
            self.Conta.numero)#,
            #self.Conta.saldo)
    def conta_nome(self, nome_do_cliente):
        self.Conta.cliente.nome = nome_do_cliente
    def conta_numero(self, numero_da_conta):
        self.Conta.numero = numero_da_conta
    def conta_saldo(self, saldo):
        self.Conta.saldo = saldo

    def contaEspecial(self):
        self.ContaEspecial.__init__(
            self.ContaEspecial.cliente,
            self.ContaEspecial.numero,
            self.ContaEspecial.saldo)
    def especial_conta(self, nome_do_cliente):
        self.ContaEspecial.cliente = nome_do_cliente
    def especial_numero(self, numero_da_conta):
        self.ContaEspecial.numero = numero_da_conta
    def especial_saldo(self, saldo):
        self.ContaEspecial.saldo = saldo
    def especial_limite(self, limite):
        self.ContaEspecial.limite = limite
X = Controle()
X.cli_nome("Wesley Safadão")
X.cli_telefone(7112345678)
X.conta_numero(123-4)
X.conta()
