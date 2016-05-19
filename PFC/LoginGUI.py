from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class TelaLogin(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		
		self.master = master

		self.init_window()

	def init_window(self):
		self.master.title("SGPS - Login")
		self.master.resizable(False,False)
		selfpack(fill=BOTH, expand=1)

		load = Image.open('aang.png')
		render = ImageTk.PhotoImage(load)
		img = Label(self, image=render)
		img.image = render
		img#.grid(row=0, column=0, columnspan=2)

	
		UsuarioL = Label(self, text='Username: ', anchor='w')#.grid(row=1, column=0, sticky='we')
		UsuarioL.pack()
		UsuarioL.place(x)
		UsuarioE = Entry(self)#.grid(row=1, column=1, sticky='we')
		SenhaL = Label(self, text='Password: ', anchor='w')#.grid(row=2, column=0, sticky='we')
		SenhaE = Entry(self)#.grid(row=2, column=1, sticky='we')
		Login = Button(self, text='Login', command=self.verifica_login)#.grid(row=3, columnspan=2, sticky='we')
	
	def verifica_login(self, login, senha):
		
		print('s')


if __name__ == '__main__':
	root = Tk()
	#root.geometry("333x320")
	Login = TelaLogin(root)
	root.mainloop()
