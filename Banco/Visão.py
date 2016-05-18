from Controle import Controle
import tkinter as tk
from tkinter.ttk import *

c = Controle()
def addCliente(nome, telefone):
    c.cli_nome(nome)
    c.cli_telefone(telefone)
    c.Banco.novo_cliente(c.cliente())
    clientes.set(c.Banco.lista_cliente())

def atualizar(key):
    print(c.Banco.busca_cliente(nomec.get()+key.char))
    if c.Banco.busca_cliente(nomec.get()) != False:
        status.set(c.Banco.busca_cliente(nomec.get()))
         
jp = tk.Tk()
#jp.geometry('500x300')
jp.title("Banco do Trapézio Descendente")
jp.grid()
jp.resizable(True,True)

abas = Notebook(jp)
abaCliente = Frame(abas)
abaConta = Frame(abas)
abaBanco = Frame(abas)
abas.add(abaCliente, text='Cliente')
abas.add(abaConta, text='Conta')
abas.add(abaBanco, text='Banco')
abas.grid()

Label(abaCliente, text='Nome: ').grid(row =0, column = 0); nome = tk.StringVar(); Entry(abaCliente, textvariable=nome).grid(row = 0, column = 1)
Label(abaCliente, text='Telefone: ').grid(row =1, column = 0); telefone = tk.StringVar(); Entry(abaCliente, textvariable=telefone).grid(row = 1, column = 1)
    
Button(abaCliente, text='Adicionar Cliente', command=lambda:addCliente(nome.get(), telefone.get())).grid(row = 2, column = 0, columnspan = 2, sticky='we')
clientes = tk.StringVar(); Label(abaCliente, textvariable=clientes).grid(row =3, column = 0, columnspan = 2)

Label(abaConta, text='Nome Cliente: ').grid(row =0, column = 0); nomecliente = tk.StringVar(); nomec = Entry(abaConta, textvariable=nomecliente); nomec.grid(row = 0, column = 1)
Label(abaConta, text='CC: ').grid(row =1, column = 0); cc = tk.StringVar(); Entry(abaConta, textvariable=cc).grid(row = 1, column = 1)
Label(abaConta, text='Número: ').grid(row = 2, column = 0); numero = tk.StringVar(); Entry(abaConta, textvariable = numero).grid(row = 2, column = 1)
Label(abaConta, text='Saldo: ').grid(row = 3, column = 0); saldo = tk.StringVar(); Entry(abaConta, textvariable = saldo).grid(row = 3, column = 1)

Button(abaConta, text='Saque', command=lambda:print('Conta Saque')).grid(row = 3, column = 0, sticky='we'); saque = tk.StringVar(); Entry(abaConta, textvariable=saque).grid(row = 3, column = 1)
Button(abaConta, text='Deposito', command=lambda:print('Conta Depósito')).grid(row = 4, column = 0, sticky='we'); deposito = tk.StringVar(); Entry(abaConta, textvariable=deposito).grid(row = 4, column = 1)
Button(abaConta, text='Extrato', command=lambda:print('Conta Extrato')).grid(row = 5, column = 0, sticky='we'); extrato = tk.StringVar(); Label(abaConta, textvariable=extrato).grid(row = 5, column = 1)
status = tk.StringVar(); Label(abaConta, textvariable=status).grid(row = 6, column = 0, columnspan=2)
nomeBanco = tk.StringVar(); Label(abaConta, textvariable = nomeBanco).grid(row = 0, column = 1); Button(abaBanco, text='Atualizar').grid(row = 0, column = 0)

nomec.bind("<Key>", atualizar)

jp.mainloop()
