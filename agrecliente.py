from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sql import ncliente


class agrecliente(Toplevel):
    def __init__(self,parent,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.prose)
        self.parent.withdraw()
        self.title("Nuevo cliente")
        self.frameb = Frame(self, bg="white", width = 550, height=380)
        self.frameb.pack()


        self.tit = Label(self.frameb, text="Nuevo cliente", font=("Verdana",12),bg="white")
        self.tit.place(x=150, y=40)

        self.lab1 = Label(self.frameb, text="Nombre del cliente:",font=("Verdana",12),bg="white")
        self.lab1.place(x=55,y=120)
        self.nom = Entry(self.frameb, width=40)
        self.nom.place(x=280,y=120)

        self.lab2 = Label(self.frameb, text="Cedula del cliente:",font=("Verdana",12),bg="white")
        self.lab2.place(x=55,y=180)
        self.ci = Entry(self.frameb, width=40)
        self.ci.place(x=280,y=180)

        self.lab3 = Label(self.frameb, text="Dirección:",font=("Verdana",12),bg="white")
        self.lab3.place(x=55,y=240)
        self.dir = Text(self.frameb, width=30,height=5)
        self.dir.place(x=280,y=240)

        self.bot1 = Button(self.frameb, text="Regresar", command=self.regre)
        self.bot1.place(x=150,y=320)

        self.bot2 = Button(self.frameb, text="Aceptar", command=self.nuevo)
        self.bot2.place(x=310,y=320)


    def nuevo(self):
        ncliente(self.nom.get(),self.ci.get(),self.dir.get("1.0",END))
        self.prose()

    def regre(self):
        self.destroy()
        self.parent.deiconify()

    def prose(self):
        messagebox.showinfo("Operación exitosa","Se ha creado el registro exitosamente")
        nom=self.nom.get()
        ci=self.ci.get()
        self.destroy()
        self.parent.prose(nom,ci)
        self.parent.destroy()
        