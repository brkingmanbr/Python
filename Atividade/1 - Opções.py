import tkinter as tk
from tkinter.ttk import *

JP = tk.Tk()
resp = tk.BooleanVar()
Label(JP, text='''Você quer ir na praia mas descobre que a \ngasolina acabou, o que voce faz?''').grid()
Radiobutton(JP, text="Vai comprar mais gasolina no caminho", variable=resp, value='Comprar mais gasolina').grid()
Radiobutton(JP, text="É melhor ficar em casa mesmo.", variable=resp, value='Ficar em casa').grid()
