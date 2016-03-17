from tkinter import *
from tkinter import ttk
from math import *

class Teclado():
    def num0(*args):
        N1.set(N1.get() + '0')
        Operacoes.c_off()
    def num1(*args):
        N1.set(N1.get() + '1')
        Operacoes.c_off()
    def num2(*args):
        Visor = str(N1.get()).strip()
        if Visor.find('x') != -1 and Visor.find('²') == -1:
            N1.set(N1.get() + '²')
        else:
            N1.set(N1.get() + '2')   
        Operacoes.c_off()            
    def num3(*args):
        N1.set(N1.get() + '3')
        Operacoes.c_off()
    def num4(*args):
        N1.set(N1.get() + '4')
        Operacoes.c_off()
    def num5(*args):
        N1.set(N1.get() + '5')
        Operacoes.c_off()
    def num6(*args):
        N1.set(N1.get() + '6')
        Operacoes.c_off()
    def num7(*args):
        N1.set(N1.get() + '7')
        Operacoes.c_off()
    def num8(*args):
        N1.set(N1.get() + '8')
        Operacoes.c_off()
    def num9(*args):
        N1.set(N1.get() + '9')
        Operacoes.c_off()
    def back(*args):
        Visor = str(N1.get()).strip()
        N1.set(Visor[:len(Visor)-1])
        Operacoes.c_off()        
    def mai(*args):
        N1.set(N1.get() + '+')
        Operacoes.c_off()
    def men(*args):
        N1.set(N1.get() + '-')
        Operacoes.c_off()
    def igu(*args):
        N1.set(N1.get() + '=')
        Operacoes.c_off()
    def x(*args):
        N1.set(N1.get() + 'x')
        Operacoes.c_off()
    def vir(*args):
        Visor = str(N1.get()).strip()
        if Visor.find('.') != -1:
            pass
        else:
            N1.set(N1.get() + '.')
            Operacoes.c_off()
        
class Operacoes():

    def som(*args):
        Operacoes.c_off()
        Visor = str(N1.get()).strip()
        if Visor.find('x') != -1:
            Teclado.mai()
        else:
            if N2.get() == '':
                N2.set(N1.get())
                N1.set('')
                Operacao.set(' + ')
            else:
                Historico.set(Historico.get() + N2.get() +  Operacao.get() + N1.get())
                N1.set(float(N1.get()) + float(N2.get()))
                Historico.set(Historico.get() + ' = ' + N1.get() + '\n')
                N2.set('')
                Operacao.set('')
        
    def sub(*args):
        Operacoes.c_off()
        Visor = str(N1.get()).strip()
        if Visor.find('x') != -1:
            Teclado.men()
        else:
            if N2.get() == '':
                N2.set(N1.get())
                N1.set('')
                Operacao.set(' - ')
            else:
                Historico.set(Historico.get() + N2.get() +  Operacao.get() + N1.get())
                N1.set(float(N2.get()) - float(N1.get()))
                Historico.set(Historico.get() + ' = ' + N1.get() + '\n')
                N2.set('')
                Operacao.set('')
            
    def mul(*args):
        Operacoes.c_off()
        Visor = str(N1.get()).strip()
        if Visor.find('x') != -1:
            pass
        else:
            if N2.get() == '':
                N2.set(N1.get())
                N1.set('')
                Operacao.set(' * ')
            else:
                Historico.set(Historico.get() + N2.get() +  Operacao.get() + N1.get())
                N1.set(float(N1.get()) * float(N2.get()))
                Historico.set(Historico.get() + ' = ' + N1.get() + '\n')
                N2.set('')
                Operacao.set('')

    def div(*args):
        Operacoes.c_off()
        Visor = str(N1.get()).strip()
        if Visor.find('x') != -1:
            pass
        else:
            if N2.get() == '':
                N2.set(N1.get())
                N1.set('')
                Operacao.set(' / ')
            else:
                Historico.set(Historico.get() + N2.get() +  Operacao.get() + N1.get())
                N1.set(float(N2.get()) / float(N1.get()))
                Historico.set(Historico.get() + ' = ' + N1.get() + '\n')
                N2.set('')
                Operacao.set('')
            
    def por(*args):
        Operacoes.c_off()
        Visor = str(N1.get()).strip()
        if Visor.find('x') != -1:
            pass
        else:
            if N2.get() == '':
                N2.set(N1.get())
                N1.set('')
                Operacao.set(' % ')
            else:
                Historico.set(Historico.get() + N2.get() +  Operacao.get() + 'de ' + N1.get())
                N1.set(float(N2.get())/100 * float(N1.get()))
                Historico.set(Historico.get() + ' = ' + N1.get() + '\n')
                N2.set('')
                Operacao.set('')

    def rad(*args):
        Operacoes.c_off()
        Visor = str(N1.get()).strip()
        if Visor.find('x') != -1:
            pass
        else:
            if N2.get() == '':
                N2.set(N1.get())
                N1.set('')
                Operacao.set(' '+chr(8730)+' ')
            else:
                Historico.set(Historico.get() + Operacao.get() + N1.get() + ' de ' + N2.get())
                N1.set(float(N2.get()) ** (1/float(N1.get())))
                Historico.set(Historico.get() + ' = ' + N1.get() + '\n')
                N2.set('')
                Operacao.set('')

    def equ(*args):
        Visor = str(N1.get()).strip()
        A = 0
        try:
            A = int(Visor[:Visor.find('x²')])
        except ValueError:
            A = 1
        
        aux = 0
        while Visor[Visor.find('²')+aux] != '+' and Visor[Visor.find('²')+aux] != '-':
            aux += 1
        B1 = Visor[Visor.find('²')+aux]
        aux += 1
        while Visor[Visor.find('²')+aux] == ' ':
            aux += 1
        B = int(B1+Visor[Visor.find('²')+aux : Visor.find('x', Visor.find('²'))])
        aux = Visor.find('x', Visor.find('²'))
        while Visor[aux] != '+' and Visor[aux] != '-':
            aux += 1    
        C1 = Visor[aux]
        aux+=1
        while Visor[aux] == ' ':
            aux += 1    
        C = int(C1+Visor[aux : Visor.find('=')])

        try:
            aux = Visor.find('=')+1
            while Visor[aux] != '+' and Visor[aux] != '-':
                aux += 1
            C1 = Visor[aux]
            aux += 1
            while Visor[aux] == ' ':
                aux += 1   
            C+= int(C1+Visor[aux:])
        except IndexError:
            pass
       
        D = B**2 - 4 * A * C
        #D = B**2 – 4 * A * C parece igual a linha de cima mas não é
        if D > 0:
            X1 = ((-1*B)+sqrt(D))/2*A
            X2 = ((-1*B)-sqrt(D))/2*A
            Resultado = 'X\' = '+str(X1)+' X\" = '+str(X2)
            N1.set(Resultado)
        elif D == 0:
            X = ((-1*B)+sqrt(D))/2*A
            Resultado = 'X\' = '+str(X)+' X\" = '+str(X)
            print('X\' = '+str(X)+'X\" = '+str(X))
            print(type(Resultado))
            N1.set(Resultado)
        else:
            N1.set('Não há raízes reais')
        Historico.set(Historico.get() + '\n' + Visor + ' = ' + Resultado + '\n')                 
            
    def res(*args):
        Operacoes.c_off()
        Visor = str(N1.get()).strip()
        if Operacao.get() == ' + ':
            Operacoes.som()
        elif Operacao.get() == ' - ':
            Operacoes.sub()
        elif Operacao.get() == ' * ':
            Operacoes.mul()
        elif Operacao.get() == ' / ':
            Operacoes.div()
        elif Operacao.get() == ' % ':
            Operacoes.por()
        elif Operacao.get() == ' '+chr(8730)+' ':
            Operacoes.rad()
        elif Visor.find('x²') != -1:
            if Visor.find('=') == -1:
                Teclado.igu()
            else:
                Operacoes.equ()
        else:
            pass
                
    def clear_off(*args):
        if N1.get() != '' or N2.get() != '' or Operacao.get() != '':
            N1.set('')
            N2.set('')
            Operacao.set('')
        else:
            Janela.destroy()
        Operacoes.c_off()

    def c_off(*args):
        if N1.get() != '' or N2.get() != '' or Operacao.get() != '':
            COFF.set('\nC\n')
        else:
            COFF.set('\nOFF\n')

    def apa_his(*args):
        Historico.set('')

Janela = Tk()
Janela.title('Calculadora Python 2.0 by Júlio Corp')
Janela.grid()
Janela.resizable(0,0)
Calculadora = ttk.Frame(Janela, padding='50 50 50 50').grid()# ORDEM(): W N E S
ttk.Style().configure("TButton", padding=10, relief="flat", background='black')
ttk.Style().configure("TLabel", padding=6, relief="flat", background='silver', foreground='black')

N1 = StringVar()
N2 = StringVar()
Operacao = StringVar()
Virgula = BooleanVar()
Historico = StringVar()
COFF = StringVar()
COFF.set('\nOFF\n')

ttk.Label(Calculadora, textvariable=N1, anchor=NE).grid(column=0, row=1, columnspan=4, rowspan=1, sticky='N, S, W, E')#tinha no label  anchor=NW

ttk.Button(Calculadora, textvariable=COFF, command=Operacoes.clear_off).grid(column=0, row=2, sticky='W, E')
ttk.Button(Calculadora, text='\n7\n', command=Teclado.num7).grid(column=0, row=3, sticky='W, E')
ttk.Button(Calculadora, text='\n4\n', command=Teclado.num4).grid(column=0, row=4, sticky='W, E')
ttk.Button(Calculadora, text='\n1\n', command=Teclado.num1).grid(column=0, row=5, sticky='W, E')
ttk.Button(Calculadora, text='\n0\n', command=Teclado.num0).grid(column=0, row=6, sticky='W, E')
##√ é chr(8730)
ttk.Button(Calculadora, text='\n'+chr(8730)+'\n', command=Operacoes.rad).grid(column=1, row=2, sticky='W, E')
ttk.Button(Calculadora, text='\n8\n', command=Teclado.num8).grid(column=1, row=3, sticky='W, E')
ttk.Button(Calculadora, text='\n5\n', command=Teclado.num5).grid(column=1, row=4, sticky='W, E')
ttk.Button(Calculadora, text='\n2\n', command=Teclado.num2).grid(column=1, row=5, sticky='W, E')
ttk.Button(Calculadora, text='\n,\n', command=Teclado.vir).grid(column=1, row=6, sticky='W, E')

ttk.Button(Calculadora, text='\n%\n', command=Operacoes.por).grid(column=2, row=2, sticky='W, E')
ttk.Button(Calculadora, text='\n9\n', command=Teclado.num9).grid(column=2, row=3, sticky='W, E')
ttk.Button(Calculadora, text='\n6\n', command=Teclado.num6).grid(column=2, row=4, sticky='W, E')
ttk.Button(Calculadora, text='\n3\n', command=Teclado.num3).grid(column=2, row=5, sticky='W, E')
ttk.Button(Calculadora, text='\n=\n', command=Operacoes.res).grid(column=2, row=6, sticky='W, E')

ttk.Button(Calculadora, text='\n/\n', command=Operacoes.div).grid(column=3, row=2, sticky='W, E')
ttk.Button(Calculadora, text='\nX\n', command=Operacoes.mul).grid(column=3, row=3, sticky='W, E')
ttk.Button(Calculadora, text='\n-\n', command=Operacoes.sub).grid(column=3, row=4, sticky='W, E')
ttk.Button(Calculadora, text='\n+\n', command=Operacoes.som).grid(column=3, row=5, rowspan=2, sticky='N, S')

ttk.Label(Calculadora, text='Histórico de operações: ', anchor=W).grid(column=4, row=1, sticky='W, E')
ttk.Label(Calculadora, textvariable=Historico, anchor=NW).grid(column=4, row=2, rowspan=4, sticky='N, S, W, E')
ttk.Button(Calculadora, text='Apagar Histórico', command=Operacoes.apa_his).grid(column=4, row=6, rowspan=1, sticky='NSWE')

Janela.bind('0', Teclado.num0),Janela.bind('1', Teclado.num1),Janela.bind('2', Teclado.num2)
Janela.bind('3', Teclado.num3),Janela.bind('4', Teclado.num4),Janela.bind('5', Teclado.num5)
Janela.bind('6', Teclado.num6),Janela.bind('7', Teclado.num7),Janela.bind('8', Teclado.num8)
Janela.bind('9', Teclado.num9),Janela.bind(',', Teclado.vir),Janela.bind('x', Teclado.x)
Janela.bind('X', Teclado.x),Janela.bind('+', Operacoes.som),Janela.bind('-', Operacoes.sub)
Janela.bind('*', Operacoes.mul),Janela.bind('/', Operacoes.div),Janela.bind('<Return>', Operacoes.res)
Janela.bind('<Delete>', Operacoes.clear_off),Janela.bind('<BackSpace>', Teclado.back)

Janela.mainloop()
