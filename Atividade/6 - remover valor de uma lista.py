'''
Crie um algoritmo que pode remover um valor, obtido como argumento de uma
função Python, de uma lista.
'''
import tkinter as tk
from tkinter.ttk import *
from random import randint

a = []
for x in range(0,10):
    a.append(randint(-100,100))

JP = tk.Tk()
Label(JP, text='Lista: '+str(a)).grid()
Label(JP, text='Valor a remover:').grid(column = 0)
entrada = tk.StringVar()
Entry(JP, textvariable=entrada).grid(column = 1)
def rmv():
    a.remove(int(entrada.get()))
    Label(JP, text='Resultado: '+str(a)).grid()
Button(JP, text='Remover', command=rmv).grid(column = 0)

