from tkinter import *
from tkinter import ttk
from Calculos import *

def sair():
    Janela.destroy()
 
Janela = Tk()
Janela.title('Calculadora Python 2.0 by Júlio Corp')

Janela.resizable(0,0)
Calculadora = ttk.Frame(Janela, padding='0 0 0 0').grid()# ORDEM: W N E S

N1 =  StringVar()
n1Entrada = ttk.Entry(Calculadora, width=36, textvariable=N1)
n1Entrada.grid(column=0, row=0, columnspan=4, sticky=(W, E))

ttk.Button(Calculadora, text='\nOFF\n', command=sair).grid(column=0, row=1, sticky=(W, E))
ttk.Button(Calculadora, text='\nRAIZ\n').grid(column=1, row=1, sticky=(W, E))
ttk.Button(Calculadora, text='\n%\n').grid(column=2, row=1, sticky=(W, E))

ttk.Button(Calculadora, text='\n7\n').grid(column=0, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n4\n').grid(column=0, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n1\n').grid(column=0, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n0\n').grid(column=0, row=5, sticky=(W, E))

ttk.Button(Calculadora, text='\n8\n').grid(column=1, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n5\n').grid(column=1, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n2\n').grid(column=1, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n,\n').grid(column=1, row=5, sticky=(W, E))

ttk.Button(Calculadora, text='\n9\n').grid(column=2, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n6\n').grid(column=2, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n3\n').grid(column=2, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n=\n').grid(column=2, row=5, sticky=(W, E))

ttk.Button(Calculadora, text='\n/\n').grid(column=3, row=1, sticky=(W, E))
ttk.Button(Calculadora, text='\nX\n').grid(column=3, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n-\n').grid(column=3, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='Enter').grid(column=3, row=4, rowspan=2, sticky=(N, S))

Janela.mainloop()

