import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
local = filedialog.askdirectory()#mode='w')

par = open(local+'/par.txt','w')
impar = open(local+'/impar.txt','w')

for número in range(1,100):
    if número%2 == 0:
        par.write('%d William é viado\n'%número)
    else:
        impar.write('%d William é viado\n'%número)

par.close()
impar.close()

##for linha in arquivo.readlines():
##    print(linha)
##arquivo.close()

