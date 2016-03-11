from tkinter import *
from tkinter import ttk

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

def som():
    if N2.get() == '':
        N2.set(N1.get())
        N1.set('')
        Operacao.set('som')
    else:
        N1.set(float(N1.get()) + float(N2.get()))
        N2.set('')
        Operacao.set('')
        
def sub(): 
    if N2.get() == '':
        N2.set(N1.get())
        N1.set('')
        Operacao.set('sub')
    else:
        N1.set(float(N2.get()) - float(N1.get()))
        N2.set('')
        Operacao.set('')
        
def mul():
    if N2.get() == '':
        N2.set(N1.get())
        N1.set('')
        Operacao.set('mul')
    else:
        N1.set(float(N1.get()) * float(N2.get()))
        N2.set('')
        Operacao.set('')

def div(): 
    if N2.get() == '':
        N2.set(N1.get())
        N1.set('')
        Operacao.set('div')
    else:
        N1.set(float(N2.get()) / float(N1.get()))
        N2.set('')
        Operacao.set('')
        
def por():
    if N2.get() == '':
        N2.set(N1.get())
        N1.set('')
        Operacao.set('por')
    else:
        N1.set(float(N2.get())/100 * float(N1.get()))
        N2.set('')
        Operacao.set('')
        
def resultado():
    if Operacao.get() == 'som':
        som()
    elif Operacao.get() == 'sub':
        sub()
    elif Operacao.get() == 'mul':
        mul()
    elif Operacao.get() == 'div':
        div()
    else:
        if Operacao.get() == 'por':
            por()

def clear_off():
    if N1.get() != '' or N2.get() != '' or Operacao.get() != '':
        N1.set('')
        N2.set('')
        Operacao.set('')
    else:
        Janela.destroy()      

Janela = Tk()
Janela.title('Calculadora Python 2.0 by Júlio Corp')

Janela.resizable(0,0)
Calculadora = ttk.Frame(Janela, padding='5 5 5 5').grid()# ORDEM(): W N E S

N1 =  StringVar()
N2 =  StringVar()
Operacao = StringVar()
Resultado = StringVar()

n1Entrada = ttk.Entry(Calculadora, width=36, textvariable=N1).grid(column=0, row=0, columnspan=4, rowspan=1, sticky=(N, S, W, E))

ttk.Button(Calculadora, text='\nC/Off\n', command=clear_off).grid(column=0, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n7\n', command=num7).grid(column=0, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n4\n', command=num4).grid(column=0, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n1\n', command=num1).grid(column=0, row=5, sticky=(W, E))
ttk.Button(Calculadora, text='\n0\n', command=num0).grid(column=0, row=6, sticky=(W, E))

ttk.Button(Calculadora, text='\nRAIZ\n').grid(column=1, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n8\n', command=num8).grid(column=1, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n5\n', command=num5).grid(column=1, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n2\n', command=num2).grid(column=1, row=5, sticky=(W, E))
ttk.Button(Calculadora, text='\n,\n', command=virgula).grid(column=1, row=6, sticky=(W, E))

ttk.Button(Calculadora, text='\n%\n', command=por).grid(column=2, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\n9\n', command=num9).grid(column=2, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n6\n', command=num6).grid(column=2, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n3\n', command=num3).grid(column=2, row=5, sticky=(W, E))
ttk.Button(Calculadora, text='\n=\n', command=resultado).grid(column=2, row=6, sticky=(W, E))

ttk.Button(Calculadora, text='\n/\n', command=div).grid(column=3, row=2, sticky=(W, E))
ttk.Button(Calculadora, text='\nX\n', command=mul).grid(column=3, row=3, sticky=(W, E))
ttk.Button(Calculadora, text='\n-\n', command=sub).grid(column=3, row=4, sticky=(W, E))
ttk.Button(Calculadora, text='\n+\n', command=som).grid(column=3, row=5, rowspan=2, sticky=(N, S))
##⤶ é chr(10550) ↲ é chr(8626)
Janela.mainloop()
