from Cliente import *
from Conta import *
from ContaEspecial import *
from Banco import *
class Controle():
    def __init__(self):
        self.Cliente = Cliente
        self.Conta = Conta
        self.ContaEspecial = ContaEspecial
        self.Banco = Banco('Trapézio Descendente')
        
    def cliente(self):
        self.Cliente = Cliente(
            self.Cliente.nome,
            self.Cliente.telefone)
        return self.Cliente
    def cli_nome(self, nome):
        self.Cliente.nome = nome
    def cli_telefone(self, telefone):
        self.Cliente.telefone = telefone

    def conta(self, numero):
        self.Conta = Conta(
            self.Cliente,
            self.Conta.numero)
    def conta_nome(self, nome_do_cliente):
        self.Conta.cliente.nome = nome_do_cliente
    def conta_numero(self, numero_da_conta):
        self.Conta.numero = numero_da_conta
    def conta_saldo(self, saldo):
        self.Conta.saldo = saldo

    def contaEspecial(self):
        self.ContaEspecial = ContaEspecial(
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
    def lista_cliente(self):
            lista = ''
            for c in self.clientes:
                print("c: ",c)
                lista = lista+'\n'+str(
                        c.getNome()
                        ) 
            self.LISTA = lista
            return lista

if __name__ == '__main__':
    c = Controle()
    c.cli_nome('Jailson Mendes')
    c.cli_telefone(123456)
    c.cliente()
    c.Banco.novo_cliente(c.Cliente)
    c.cli_nome('Italo Regulado')
    c.cli_telefone(123456)
    c.cliente()
    c.Banco.novo_cliente(c.Cliente)
    c.cli_nome('Kléber Bam Bam')
    c.cli_telefone(123456)
    c.cliente()
    c.Banco.novo_cliente(c.Cliente)
    from tkinter import *
    root = Tk()
    x = StringVar()
    Label(root, textvariable=x).grid()
    print("antes")
    x.set(c.Banco.lista_cliente())
    print("depois")
    print("lista:",c.Banco.LISTA)
    print("stringvar:",x.get())
    x.get()
    root.mainloop()
