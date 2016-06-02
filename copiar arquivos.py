from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import shutil

p = Tk()
p.title("Copia de arquivos")
p.resizable(False,False)
p.grid()
origem = fd.askdirectory()
destino = fd.asksaveasfilename(title='')

#Label = (p, text = "Diretorio para copiar os arquivos:").grid()
#Label = (p, text = 'Diretorio para salvar os arquivos:').grid()
print(destino)
shutil.copytree(origem, destino)
p.mainloop()
