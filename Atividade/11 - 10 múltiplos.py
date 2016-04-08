
##Por meio de uma função crie uma estrutura com
##while para imprimir os 10 múltiplos de um número
import tkinter
from tkinter.ttk import *

L = []
def cal():
    n = int(X.get())
    for x in range(0, 10):
        L.append(n* (x+1))
    Y.set(L)

JP = tkinter.Tk()
Label(JP, text='Digite um número').grid(column = 0, row = 0)
X = tkinter.StringVar()
Y = tkinter.StringVar()
Entry(JP, textvariable=X).grid(columnspan = 2, column = 1, row = 0)
Button(JP, text='Multiplos', command=cal).grid(columnspan = 2, column = 1, row = 1)
Label(JP, textvariable=Y).grid(columnspan = 2, column = 0, row = 2)
JP.mainloop()
