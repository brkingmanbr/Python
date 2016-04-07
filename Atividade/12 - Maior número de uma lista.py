import tkinter as tk
from tkinter.ttk import *
from random import randint

b = []
for x in range(0,5):
    b.append(randint(-100,100))
    print('X======',x)
a = []
a.extend(b)

JP = tk.Tk()
x = 0
for elemento in a:
    maior = a[0]
    if elemento > maior:
        maior = elemento
Label(JP, text='Dentro desta lista:\n'+str(a)+'\nO maior elemento é: '+str(maior)).grid()
