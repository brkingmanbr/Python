from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("GUI")
		self.pack(fill=BOTH, expand=1)
		
	#	quitButton = Button(self, text='Quit', command=self.client_exit)
	#	quitButton.place(x=0, y=0)
		menu = Menu(self.master)
		self.master.config(menu=menu)

		file = Menu(menu)
		file.add_command(label='Exit', command=self.client_exit)
		file.add_command(label='Save')

		menu.add_cascade(label='File', menu=file)

		edit = Menu(menu)
		edit.add_command(label='Show Image', command=self.showImg)
		edit.add_command(label='Show Text', command=self.showTxt)
		menu.add_cascade(label='Edit', menu=edit)

	def showImg(self):
		load = Image.open('avatar.png')
		render = ImageTk.PhotoImage(load)

		img = Label(self, image=render)
		img.image = render
		img.place(x=0, y=0)

	def showTxt(self):
		text = Label(self, text='Hey there good lookin')
		text.pack()
		

	def client_exit(self):
		exit()

if __name__ == '__main__':
	root = Tk()
	#root.geometry("333x320")
	Login = Window(root)
	root.mainloop()