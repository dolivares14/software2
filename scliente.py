from tkinter import *
from sql import scliente,infocliente
from tkinter import messagebox
from agrecliente import agrecliente


class bcliente(Toplevel):
    def __init__(self,parent,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Consulta de cliente")
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.frameb= Frame(self)
        self.frameb.pack()
        self.frameb.config(width=300,height=200)
        self.frameb.config(bg="white")
        

        self.lab= Label(self.frameb,text="Ingrese la \n cedula del cliente",font=("Verdana",15),bg="white")
        self.lab.place(x=50,y=5)

        self.ced= Entry(self.frameb)
        self.ced.place(x=90,y=100)

        self.but= Button(self.frameb,text="Buscar",command=self.search)
        self.but.place(x=130,y=150)

    def prose(self,nom,ci):
        self.destroy()
        self.parent.infoclient(ci,nom)
        self.parent.deiconify()
        

    def search(self):
        if scliente(self.ced.get()):
            data = infocliente(self.ced.get())
            self.prose(data.nomb_cliente,data.ci_cliente)
        else:
            resultado = messagebox.askquestion("Fallo en la busqueda", "¿Deseas agregar un nuevo cliente?")
            if resultado == "yes":
                nwin= agrecliente(self)




