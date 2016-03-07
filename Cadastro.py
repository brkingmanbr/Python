from tkinter import *
from tkinter import ttk

def nomeCompleto():
    nCompleto.set(pNome,' ',sNome)


Cadastro = Tk()
Cadastro.title('Cadastro')
Cadastro.resizable(0 , 0)
janelaPrincipal = ttk.Frame(Cadastro).grid(padx=50)#, padding=('200 30 2 2'))
#-column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky

ttk.Label(janelaPrincipal, text='Nome: ').grid(column = 0, row = 1, sticky=(W))
ttk.Label(janelaPrincipal, text='Sobrenome: ').grid(column = 0, row = 2, sticky=(W))
ttk.Label(janelaPrincipal, text='Idade: ').grid(column = 0, row = 3, sticky=(W))
ttk.Label(janelaPrincipal, text='RG: ').grid(column = 0, row = 4, sticky=(W))
ttk.Label(janelaPrincipal, text='CPF: ').grid(column = 0, row = 5, sticky=(W))

nome = StringVar()
sobrenome = StringVar()
idade = StringVar()
rg = StringVar()
cpf = StringVar()

ttk.Entry(janelaPrincipal, width='10', textvariable=nome).grid(column = 1, row = 1, sticky=(W, E))
ttk.Entry(janelaPrincipal, width='60', textvariable=sobrenome).grid(column = 1, row = 2)
ttk.Entry(janelaPrincipal, width='60', textvariable=idade).grid(column = 1, row = 3)
ttk.Entry(janelaPrincipal, width='60', textvariable=rg).grid(column = 1, row = 4)
ttk.Entry(janelaPrincipal, width='60', textvariable=cpf).grid(column = 1, row = 5)


def janelaResultado():
    janelaSecundaria = Toplevel()
    #janelaSecundaria = ttk.Frame(Cadastro, padding=('2 30 2 2'))
    #janelaSecundaria.grid(column=0 ,row=0 ,sticky=(N, S, E, W))
    janelaSecundaria.title('È tetra!!!')
    janelaSecundaria.resizable(0, 0)
    ttk.Label(janelaSecundaria, text='Seu nome comleto: ').grid(column = 0, row = 1, sticky=(W, E))
    ttk.Label(janelaSecundaria, text='Sua idade: ').grid(column = 0, row = 2, sticky=(W))
    ttk.Label(janelaSecundaria, text='Seu RG: ').grid(column = 0, row = 3, sticky=(W))
    ttk.Label(janelaSecundaria, text='Seu CPF: ').grid(column = 0, row = 4, sticky=(W))
    
    ttk.Label(janelaSecundaria, textvariable=nome).grid(column = 1, row = 1, sticky=(W, E))
    ttk.Label(janelaSecundaria, textvariable=sobrenome).grid(column = 2, row = 1, sticky=(W, E))
    ttk.Label(janelaSecundaria, textvariable=idade).grid(column = 1, row = 2, sticky=(W))
    ttk.Label(janelaSecundaria, textvariable=rg).grid(column = 1, row = 3, sticky=(W))
    ttk.Label(janelaSecundaria, textvariable=cpf).grid(column = 1, row = 4, sticky=(W))

ttk.Button(janelaPrincipal, text='Cadastrar', command=janelaResultado).grid()




Cadastro.mainloop()
