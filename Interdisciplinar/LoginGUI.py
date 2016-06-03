from tkinter import *
from tkinter.ttk import *
from time import strftime
from PIL import Image, ImageTk

class Visao(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.start_menu()
		self.start_login()

	def start_menu(self):
		self.menu = Menu(self.master)
		self.master.config(menu=self.menu)
		self.file = Menu(self.menu)    
		self.menu.add_cascade(label="Editar", menu=self.file)
		self.file.add_command(label="Editar Professores") #deve abrir o CRUD de professor
		self.file.add_command(label="Editar Turmas") #deve abrir o CRUD de turmas
		self.login = Menu(self.menu)
		self.menu.add_cascade(label="Login", menu=self.login)
		#self.aang = PhotoImage(file='aang.png')
		#self.login.add_command(label="Alterar senha", image=self.aang, command=lambda: print('XX'))
		self.menu.add_cascade(label="Cronograma", command=lambda: print('XX'))

	def start_login(self):
		self.master.title("Tela de Login")
		self.master.resizable(False,False)
		self.grid()
		load = Image.open('aang.png')
		render = ImageTk.PhotoImage(load)
		img = Label(self, image=render)
		img.image = render
		img.grid(row=0, column=0, columnspan=2)

		UsuarioL = Label(self, text='Username: ', anchor='w').grid(row=1, column=0, sticky='we')
		UsuarioE = Entry(self).grid(row=1, column=1, sticky='we')
		SenhaL = Label(self, text='Password: ', anchor='w').grid(row=2, column=0, sticky='we')
		SenhaE = Entry(self).grid(row=2, column=1, sticky='we')
		Login = Button(self, text='Login', command=self.verifica_login).grid(row=3, columnspan=2, sticky='we')
		self.master.title("Tela de Login")
	
	

	def tictac(self):
		self.agora = strftime('%H:%M:%S')
		if self.agora != relogio['text']:
			relogio['text'] = agora
		relogio.after(100, tictac)
		
		tictac()
		self.relogio = tkinter.Label()
		relogio['font'] = 'Helvetica 20 bold'
		relogio['text'] = strftime('%H:%M:%S')


	def verifica_login(self, login, senha):
		print('isso tem que estar no controle')

if __name__ == '__main__':
	JP = Tk()
	#root.geometry("333x320")
	Visao(JP)
	print(JP.title)
	JP.mainloop()
	exit()