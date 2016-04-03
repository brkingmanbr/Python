import tkinter
from tkinter.ttk import *

class Cliente:
    def __init__(self, nome, snome, telefone):
        self.Nome = nome
        self.Snome = snome
        self.Telefone = telefone

class Conta:
    def __init__(self, cliente, numero, saldo = 0):
        self.Cliente = cliente
        self.Numero = numero
        self.Saldo = saldo
    def resumo(self):
        return self.Saldo    
    def saque(Valor):
        self.Saldo = self.Saldo - Valor
    def deposito():
        self.Saldo += Valor

class Banco:
    def __init__(self, nome):
        self.NomeBanco = nome
        self.Clientes = []
        self.Contas = []

    def novoCliente(self, nome, snome, telefone):
        self.Clientes.append( Cliente(nome, snome, telefone) )

    def novaConta(self, cliente, numero):
        self.Contas.append(Conta(cliente, len(self.Clientes)))
        
    def abreConta(self, cliente):
        self.Clientes.append(cliente)

    def listar(self):
        x = 0
        while x < len(self.Clientes):
            print('Lista de Clientes:\n',
                  x,
                  self.Clientes[x].Nome,
                  self.Clientes[x].Snome,
                  self.Clientes[x].Telefone)
            x+=1
        x = 0
        while x < len(self.Contas):
            print('Lista de Contas:\n',
                  x,
                  self.NomeBanco,
                  self.Contas[x].Cliente.Nome,
                  self.Contas[x].Numero,
                  self.Contas[x].Saldo)
            x+=1
##global X
X = Banco('Banco Do Trapézio Descendente')

JanelaCadastro = tkinter.Tk()
JanelaCadastro.title("Sistema Bancário")
Cliente = Frame(JanelaCadastro).grid()

Label(Cliente, text='Nome: ').grid(row=0 , column=0)
Nome = tkinter.StringVar()
Entry(Cliente, textvariable=Nome).grid(row=0 , column=1)

Label(Cliente, text='Sobrenome: ').grid(row=1 , column=0)
Sobrenome = tkinter.StringVar()
Entry(Cliente, textvariable=Sobrenome).grid(row=1 , column=1)

Label(Cliente, text='Telefone: ', anchor='e').grid(row=2 , column=0)
Telefone = tkinter.StringVar()
Entry(Cliente, textvariable=Telefone).grid(row=2 , column=1)

Button(Cliente, text='Cadastrar',
       command= lambda: X.novoCliente(Nome.get(), Sobrenome.get(), Telefone.get())).grid(row=3, column=0, columnspan = 2, sticky='WE')
JanelaCadastro.mainloop()



##X.novoCliente('Jacinto Pinto', 'Aquino Rêgo', '1234-5678')
##X.novaConta(X.Clientes[0], 0)
##
##X.novoCliente('Tamara Navara', 'Jacinto', '9123-4567')
##X.novaConta(X.Clientes[1], 1)
X.listar()
