'''
Construa um algoritmo que para um grupo de 50 valores inteiros, determine por

meio de uma função uma lista para:

a) determinar a soma dos 25 números positivos;

b) determinar a quantidade de valores negativos. (usar filtro)
'''
import tkinter as tk
from tkinter.ttk import *
from random import *
a = []
for x in range(0,50):
    a.append(randint(-100,100))

def positivos():
    x = 0
    cont = 0
    for ele in a:
        if ele > 0:
            x+= ele
    return x

def quantnegativos():
    x = 0
    for ele in a:
        if ele < 0:
            x+= 1
    return x
