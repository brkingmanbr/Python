import tkinter as tk
from tkinter.ttk import *

'''
Por meio de uma função Python retorne o valor dos argumentos na ordem
sobrenome, nome de alguém.
'''
global X
def gerar():
    NSN.set('Sobrenome: '+SN.get()+' Nome: '+N.get())
JP = tk.Tk()
Label(JP, text='Nome: ').grid(column=0, row=0)
Label(JP, text='Sobrenome: ').grid(column=0, row=1)
N = tk.StringVar()
SN = tk.StringVar()
NSN = tk.StringVar(JP, 'Sobrenome Nome')
Entry(JP, textvariable=N).grid(column=1, row=0)
Entry(JP, textvariable=SN).grid(column=1, row=1)
Button(JP, text='Gerar nome completo', command=gerar).grid(column=0, columnspan=2, row=2)
Label(JP, textvariable=NSN).grid(column=0, row=3)
JP.mainloop()
