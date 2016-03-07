from tkinter import *
from tkinter import ttk
def calculo(*args):
    try:
        valor = float(pes.get())
        metros.set((0.3048 * valor * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
root = Tk()
root.title('Conversor de pés para metros')
meuframe= ttk.Frame(root, padding='3 3 12 12')
meuframe.grid(column=0 ,row=0 ,sticky=(N, W, E, S))
meuframe.columnconfigure(0,weight=1)
meuframe.rowconfigure(0, weight=1)

pes = StringVar()
metros = StringVar()

pesEntrada = ttk.Entry(meuframe, width=20, textvariable=pes)
pesEntrada.grid(column=2, row=1, sticky=(W,E))
ttk.Label(meuframe, textvariable=metros).grid(column=2, row=2, sticky=(W,E))

ttk.Label(meuframe, text='Essa quantidade de Pés: ').grid(column=1, row=1, sticky=(E))
ttk.Button(meuframe, text='Converter', command=calculo).grid(column=3, row=3, sticky=(W))
ttk.Label(meuframe, text='É equivalente a').grid(column=1, row=2, sticky=(N))
ttk.Label(meuframe, text='metros.').grid(column=3, row=2, sticky=(E))


for crianca in meuframe.winfo_children():
    crianca.grid_configure(padx=0, pady=0)

pesEntrada.focus()
root.bind('<Return>', calculo)
root.mainloop()
