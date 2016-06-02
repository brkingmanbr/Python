from tkinter import *
#import tkinter as tk
from tkinter.ttk import *


def mes(frame, nome_do_mês = 'sem nome', dias = 30, dia_inicial = 0, linha_inicial = 0, coluna_inicial = 0):
    diaAtual = 1
    Button(frame, text='♪┏ ( ･o･) ┛♪┗ (･o･ ) ┓♪').grid(row=linha_inicial, column=coluna_inicial, columnspan=8, sticky='WE')
    Label(frame, text='Segunda').grid(row=linha_inicial+1, column=coluna_inicial+2)
    Label(frame, text='Terça').grid(row=linha_inicial+1, column=coluna_inicial+3)
    Label(frame, text='Quarta').grid(row=linha_inicial+1, column=coluna_inicial+4)
    Label(frame, text='Quinta').grid(row=linha_inicial+1, column=coluna_inicial+5)
    Label(frame, text='Sexta').grid(row=linha_inicial+1, column=coluna_inicial+6)
    Label(frame, text='Sábado').grid(row=linha_inicial+1, column=coluna_inicial+7)
    Label(frame, text='Domingo').grid(row=linha_inicial+1, column=coluna_inicial+1)

    for linha in range(linha_inicial+2, linha_inicial+23, 5):#18, 5):
        if diaAtual <= dias:
            Label(frame, text='7:30 - 8:30').grid(row=linha+1, column=coluna_inicial)
            Label(frame, text='8:30 - 9:30').grid(row=linha+2, column=coluna_inicial)
            Label(frame, text='9:30 - 10:30').grid(row=linha+3, column=coluna_inicial)
            Label(frame, text='10:30 - 11:30').grid(row=linha+4, column=coluna_inicial)
            for coluna in range(coluna_inicial+1+dia_inicial, coluna_inicial+8):
                if diaAtual <= dias:
                    Button(frame, text='Dia: %i'%diaAtual).grid(row=linha, column=coluna)
                    Button(frame, text='7:30 - 8:30').grid(row=linha+1, column=coluna)
                    Button(frame, text='8:30 - 9:30').grid(row=linha+2, column=coluna)
                    Button(frame, text='9:30 - 10:30').grid(row=linha+3, column=coluna)
                    Button(frame, text='10:30 - 11:30').grid(row=linha+4, column=coluna)
                    diaAtual += 1

if __name__ == '__main__':
    JP = Tk()
    JP.resizable(False, False)
    tudo = Frame(JP).grid()
    meses = Notebook(JP)

    Janeiro = Frame(meses)
    Fevereiro = Frame(meses)
    Março = Frame(meses)
    Abril = Frame(meses)
    Maio = Frame(meses)
    Junho = Frame(meses)
    Julho = Frame(meses)
    Agosto = Frame(meses)
    Setembro = Frame(meses)
    Outubro = Frame(meses)
    Novembro = Frame(meses)
    Dezembro = Frame(meses)

    meses.add(Janeiro, text='Janeiro')
    meses.add(Fevereiro, text='Fevereiro')
    meses.add(Março, text='Março')
    meses.add(Abril, text='Abril')
    meses.add(Maio, text='Maio')
    meses.add(Junho, text='Junho')
    meses.add(Julho, text='Julho')
    meses.add(Agosto, text='Agosto')
    meses.add(Setembro, text='Setembro')
    meses.add(Outubro, text='Outubro')
    meses.add(Novembro, text='Novembro')
    meses.add(Dezembro, text='Dezembro')
    meses.grid()
    #26 Linhas por mês normal de 30 dias
    #meses = 'Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'
    mes(frame=Janeiro, dias=30)
    mes(frame=Fevereiro, dias=31)
    mes(frame=Março, dias=30)
    mes(frame=Abril, dias=31)
    mes(frame=Maio, dias=30)
    mes(frame=Junho, dias=31)
    mes(frame=Julho, dias=30)
    mes(frame=Agosto, dias=31)
    mes(frame=Setembro, dias=30)
    mes(frame=Outubro, dias=31)
    mes(frame=Novembro, dias=31)
    mes(frame=Dezembro, dias=30)
    JP.mainloop()