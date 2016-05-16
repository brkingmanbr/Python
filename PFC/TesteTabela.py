import tkinter as tk
from tkinter.ttk import *
#from tkinter import *
JP = tk.Tk()
tudo = Frame(JP).grid()
scrollbar = Scrollbar(JP)
scrollbar.grid(column=9, row=0, rowspan=2600, sticky='ns')

def mes(nome_do_mês, dias, linha_inicial = 0, coluna_inicial = 0):
    diaAtual = 1
    Button(tudo, text=nome_do_mês).grid(row=linha_inicial, column=coluna_inicial, columnspan=8, sticky='WE')
    Label(tudo, text='Segunda').grid(row=linha_inicial+1, column=coluna_inicial+2)
    Label(tudo, text='Terça').grid(row=linha_inicial+1, column=coluna_inicial+3)
    Label(tudo, text='Quarta').grid(row=linha_inicial+1, column=coluna_inicial+4)
    Label(tudo, text='Quinta').grid(row=linha_inicial+1, column=coluna_inicial+5)
    Label(tudo, text='Sexta').grid(row=linha_inicial+1, column=coluna_inicial+6)
    Label(tudo, text='Sábado').grid(row=linha_inicial+1, column=coluna_inicial+7)
    Label(tudo, text='Domingo').grid(row=linha_inicial+1, column=coluna_inicial+1)



    for linha in range(linha_inicial+1, linha_inicial+22, 5):#18, 5):
        Label(tudo, text='7:30 - 8:30').grid(row=linha+1, column=coluna_inicial)
        Label(tudo, text='8:30 - 9:30').grid(row=linha+2, column=coluna_inicial)
        Label(tudo, text='9:30 - 10:30').grid(row=linha+3, column=coluna_inicial)
        Label(tudo, text='10:30 - 11:30').grid(row=linha+4, column=coluna_inicial)
        for coluna in range(coluna_inicial+1, coluna_inicial+8):
            if diaAtual <= dias:
                Button(tudo, text='Dia: %i '%diaAtual).grid(row=linha, column=coluna)
                Button(tudo, text='7:30 - 8:30').grid(row=linha+1, column=coluna)
                Button(tudo, text='8:30 - 9:30').grid(row=linha+2, column=coluna)
                Button(tudo, text='9:30 - 10:30').grid(row=linha+3, column=coluna)
                Button(tudo, text='10:30 - 11:30').grid(row=linha+4, column=coluna)
                diaAtual += 1

if __name__ == '__main__':



    #26 Linhas por mês normal de 30 dias
    mes('Janeiro', 30)
    #mes('Fevereiro', 28, linha_inicial=0, coluna_inicial=8)
    #mes('Março', 31,  linha_inicial=14)
    JP.mainloop()