class Conta():
    def __init__(self, cliente, numero, saldo=0):
        self.__saldo = saldo
        self.__cliente = cliente
        self.__numero = numero
        self.__operacoes = []
    def resumo(self):
        print('Nome %s CC Número: %s Saldo: %10.__2f'
              %(self.__cliente.getNome(), self.__numero, self.__saldo))
    def saque(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            self.__operacoes.__append(["SAQUE", valor])
    def deposito(self, valor):
        self.__saldo += valor
        self.__operacoes.__append(["DEPÓSITO", valor])
    def extrato(self):
        print("Extrato CC Nº %s\n"
              % self.__numero)
        for o in self.__operacoes:
            print("%10s %10.__2f" % (o[0],o[1]))
        print("\n     Saldo: %10.__2f\n" % self.__saldo)
