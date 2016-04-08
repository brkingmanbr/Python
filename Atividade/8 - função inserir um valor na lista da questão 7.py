'''
Crie uma função Python que insira um
valor na lista da questão 7 na posição 2.
'''
import tkinter
from tkinter.ttk import *

global L
L = []
def gua():
    L.append(X.get())
    X.set('')

JP = tkinter.Tk()
Label(JP, text='Digite quantos números desejar').grid(column = 0, row = 0)
X = tkinter.StringVar(JP)
Y = tkinter.StringVar()
Entry(JP, textvariable=X).grid(columnspan = 2, column = 1, row = 0)
Button(JP, text='Guardar', command=gua).grid(columnspan = 2, column = 1, row = 1)
Label(JP, textvariable=Y).grid(columnspan = 2, column = 0, row = 2)

JP.mainloop()

res = tkinter.Tk()
def ins():
    L.insert(2, X.get())

Label(res, text='O valor para alterar o 2º elemento da lista anterior').grid(columnspan = 2, column = 0, row = 0)
X = tkinter.StringVar(res)
Entry(res, textvariable=X).grid(columnspan = 2, column = 1, row = 0)
Button(res, text='Trocar', command=ins).grid(columnspan = 2, column = 1, row = 1)
Label(res, text=L).grid(columnspan = 2, column = 0, row = 2)

res.mainloop()

Final = tkinter.Tk()
Label(Final, text=L).grid(columnspan = 2, column = 0, row = 2)
Final.mainloop()
