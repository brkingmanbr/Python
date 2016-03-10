from tkinter import *
from tkinter import ttk
#from Calculos import Logica

def num1():
    N1.set(N1.get() + '1')
       
def num2():
    N1.set(N1.get() + '2')

def num3():
    N1.set(N1.get() + '3')

def num4():
    N1.set(N1.get() + '4')

def num5():
    N1.set(N1.get() + '5')

def num6():
    N1.set(N1.get() + '6')

def num7():
    N1.set(N1.get() + '7')

def num8():
    N1.set(N1.get() + '8')

def num9():
    N1.set(N1.get() + '9')

def num0():
    N1.set(N1.get() + '0')

def virgula():
    N1.set(N1.get() + '.')

'''
123 >>> 123 == N1
+ >>>  N2 == 123 e N1 == 0

245 >>> N1 == 245 e N2 == 123
+ >>> N1 == (N1 + N2) e N2 == 0
'''

def som():

    if N2.get() == '':
        N2.set(N1.get())
        N1.set('')
        Operacao.set('som')

    elif N2.get() != '' and N1.get() != '':
        N1.set(float(N1.get()) + float(N2.get()))
        N2.set('')
        Operacao.set('')
    else:
        print('nada')

def sub():
    Resultado.set(float(N1.get()) - float(N2.get())) 
    print('Resultado: '+Resultado.get())
def mul():
    Resultado.set(float(N1.get()) * float(N2.get()))
    print('Resultado: '+Resultado.get())
def div():
    Resultado.set(float(N1.get()) / float(N2.get()))
    print('Resultado: '+Resultado.get())
def resultado():
    if Operacao.get() == 'som':
        som()
    elif Operacao.get() == 'sub':
        sub()
    elif Operacao.get() == 'mul':
        mul()
    elif Operacao.get() == 'div':
        div()
    else
        
def sair():
    Janela.destroy()

Janela = Tk()
Janela.title('Calculadora Python 2.0 by Júlio Corp')

Janela.resizable(0,0)
Calculadora = ttk.Frame(Janela, padding='5 5 5 5').grid()# ORDEM(): W N E S

N1 =  StringVar()
n1Entrada = ttk.Entry(Calculadora, width=36, textvariable=N1)
n1Entrada.grid(column=0, row=0, columnspan=4, rowspan=1, sticky=(N, S, W, E))

N2 =  StringVar()
n2Entrada = ttk.Entry(Calculadora, width=36, textvariable=N2)
n2Entrada.grid(column=0, row=7, columnspan=4, rowspan=6, sticky=(N, S, W, E))

Operacao = StringVar()

Resultado = StringVar()

ttk.Button(Calculadora, text='\nOFF\n', command=sair).grid(column=0, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n7\n', command=num7).grid(column=0, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n4\n', command=num4).grid(column=0, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n1\n', command=num1).grid(column=0, row=5, sticky=(W, E))
ttk.Button(Calculadora, text='\n0\n', command=num0).grid(column=0, row=6, sticky=(W, E))

ttk.Button(Calculadora, text='\nRAIZ\n').grid(column=1, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n8\n', command=num8).grid(column=1, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n5\n', command=num5).grid(column=1, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n2\n', command=num2).grid(column=1, row=5, sticky=(W, E))
ttk.Button(Calculadora, text='\n,\n', command=virgula).grid(column=1, row=6, sticky=(W, E))

ttk.Button(Calculadora, text='\n%\n').grid(column=2, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n9\n', command=num9).grid(column=2, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n6\n', command=num6).grid(column=2, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n3\n', command=num3).grid(column=2, row=5, sticky=(W, E))
ttk.Button(Calculadora, text='\n=\n', command=resultado).grid(column=2, row=6, sticky=(W, E))

ttk.Button(Calculadora, text='\n/\n', command=div).grid(column=3, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\nX\n', command=mul).grid(column=3, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n-\n', command=sub).grid(column=3, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n+\n', command=som).grid(column=3, row=5, rowspan=2, sticky=(N, S))
##⤶ é 10550##↲ é 8626
##print(N1)
##↲ é 8626
Janela.mainloop()

