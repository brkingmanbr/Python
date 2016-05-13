import tkinter
from tkinter.ttk import *
#from tkinter import *
tudo = tkinter.Tk()

def mes(nome_do_mês, dias, linha_inicial = 0, coluna_inicial = 0):
    diaAtual = 1
    Button(tudo, text=nome_do_mês).grid(row=linha_inicial, column=coluna_inicial, columnspan=7, sticky='WE')
    Label(tudo, text='Segunda').grid(row=linha_inicial+1, column=coluna_inicial+1)
    Label(tudo, text='Terça').grid(row=linha_inicial+1, column=coluna_inicial+2)
    Label(tudo, text='Quarta').grid(row=linha_inicial+1, column=coluna_inicial+3)
    Label(tudo, text='Quinta').grid(row=linha_inicial+1, column=coluna_inicial+4)
    Label(tudo, text='Sexta').grid(row=linha_inicial+1, column=coluna_inicial+5)
    Label(tudo, text='Sábado').grid(row=linha_inicial+1, column=coluna_inicial+6)
    Label(tudo, text='Domingo').grid(row=linha_inicial+1, column=coluna_inicial)
    for linha in range(linha_inicial+2, linha_inicial+7):
        for coluna in range(coluna_inicial, coluna_inicial+7):
            if diaAtual <= dias:
                Button(tudo, text='Dia: %i '%diaAtual).grid(row=linha, column=coluna)
                diaAtual += 1

mes('Janeiro', 30)
mes('Fevereiro', 28, linha_inicial=7)
mes('Março', 31,  linha_inicial=14)
tudo.mainloop()