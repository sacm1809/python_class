#importar librerias para GUI
from tkinter import *
import tkinter

#####################################

root = tkinter.Tk()
root.geometry ("400x400")#WxH
root.title("Mi calculadora")
root.resizable(FALSE,FALSE)
root.configure(background= "#1D2C81")

#####################################

Display = Entry(root,font = ('Algerian',20,'italic'),width=20,bd=5,insertwidth=4,bg="#31B8D9",justify="center").place(x=30,y=7)
Boton1 = Button(root,text="1",width=3,height=2).place(x=10,y=60)

#Abrir ventana
root.mainloop()
