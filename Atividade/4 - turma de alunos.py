'''
Para uma turma de 45 alunos, construir um algoritmo que determine por meio de
uma função:
a) a idade média dos alunos com menos 1,70m de altura;
b) a altura média dos alunos com mais de 20 anos.
'''
import tkinter as tk
from tkinter.ttk import *
from random import *
from locale import *
a = []
for x in range(1,46):
    z = {}
    z['Nome'] = 'Aluno  '+str(x)+'   '
    z['Altura'] = uniform(1.5, 2.0)
    z['Idade'] = randint(0,70)
    a.append(z)

def idademedia():
    x = 0
    cont = 0
    for ele in range(0,len(a)):
        if a[ele]['Altura'] < 1.7:
            x+= a[ele]['Idade']
            cont+=1
    return x/cont
    
def alturamedia():
    x = 0
    cont = 0
    for ele in range(0,len(a)):
        if a[ele]['Idade'] > 20:
            x+= a[ele]['Altura']
            cont+=1
    return x/cont

JP = tk.Tk()
Label(JP, text='Idade média dos alunos com\n menos de 1,70 de altura'+'%1.2f'%idademedia()).grid()
Label(JP, text='Altura média dos alunos com\n mais de 20 anos'+'%1.2f'%alturamedia()).grid()
for x in a:
    Label(JP, text=x['Nome']+'Altura: '+', %1.2f'%x['Altura']+', Idade: %1.2f'%x['Idade']).grid()
