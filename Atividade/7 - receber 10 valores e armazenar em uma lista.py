'''
Crie uma função Python que permita obter, por meio do teclado, 10 valor que
serão guardados em uma lista vazia.
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
X = tkinter.StringVar()
Y = tkinter.StringVar()
Entry(JP, textvariable=X).grid(columnspan = 2, column = 1, row = 0)
Button(JP, text='Guardar', command=gua).grid(columnspan = 2, column = 1, row = 1)
Label(JP, textvariable=Y).grid(columnspan = 2, column = 0, row = 2)

JP.mainloop()

res = tkinter.Tk()
Label(res, text=L).grid(columnspan = 2, column = 0, row = 2)
res.mainloop()
