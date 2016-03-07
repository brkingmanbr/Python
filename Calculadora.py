from tkinter import *
from tkinter import ttk

def som(*args):
    Resultado.set(int(N1.get()) + int(N2.get()))

def sub(*args):
    Resultado.set(int(N1.get()) - int(N2.get()))

def mul(*args):
    Resultado.set(int(N1.get()) * int(N2.get()))

def div(*args):
     Resultado.set(int(N1.get()) / int(N2.get()))

def sair():
    Calculadora.destroy()
    
Calculadora = Tk()
Calculadora.title('Calculadora Python by Júlio Corp')

Calculadora.resizable(0,0)
janela = ttk.Frame(Calculadora, padding='10 20 10 10')# ORDEM: W N E S
janela.grid(column=0 ,row=0)# ,sticky=(N, S, E, W))      

ttk.Label(janela, text='Numero 1:').grid(column = 1, row = 1, sticky=(W))
ttk.Label(janela, text='Numero 2:').grid(column = 1, row = 2, sticky=(W))

N1 =  StringVar()
n1Entrada = ttk.Entry(janela, width=36, textvariable=N1).grid(column=2, row=1, columnspan=3, sticky=(W, E))

N2 =  StringVar()
n2Entrada = ttk.Entry(janela, width=36, textvariable=N2).grid(column=2, row=2, columnspan=3, sticky=(W, E))

ttk.Button(janela, text='  +  ', command=som).grid(column=1, row=3, sticky=(W, E))
ttk.Button(janela, text='  -  ', command=sub).grid(column=2, row=3, sticky=(W, E))
ttk.Button(janela, text='  *  ', command=mul).grid(column=3, row=3, sticky=(W, E))
ttk.Button(janela, text='  /  ', command=div).grid(column=4, row=3, sticky=(W, E))

Resultado = IntVar()
ttk.Label(janela, text='Resultado = ').grid(column = 1, row = 4)
ttk.Label(janela, textvariable=Resultado).grid(column=2, row=4, columnspan=3, sticky=(W, E))

ttk.Button(janela, text='Sair', command=sair).grid(column=1, row=5, columnspan = 4, sticky=(W, E))

Calculadora.mainloop()

