import tkinter as tk
from tkinter.ttk import *

def login():
    pass

jp = tk.Tk()
jp.title('SGPS - Login')
#jp.geometry('333x325')
logo = tk.PhotoImage(file="aang.png")
jp.configure(bg='#334353')
jp.resizable(False,False)
jp.columnconfigure(0, weight=150)

bg = Frame(jp).grid(row=0)
Label(bg, image=logo).grid(row=0, column=0, columnspan=2)

fp = Frame(jp).grid(row=1)
UsuarioL = Label(fp, text='Username: ', anchor='w').grid(row=1, column=0, sticky='we')
UsuarioE = Entry(fp).grid(row=1, column=1, sticky='we')
SenhaL = Label(fp, text='Password: ', anchor='w').grid(row=2, column=0, sticky='we')
SenhaE = Entry(fp).grid(row=2, column=1, sticky='we')
Login = Button(fp, text='Login', command=login).grid(row=3, columnspan=2, sticky='we')

jp.mainloop()