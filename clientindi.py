from tkinter import *
from sql import infoclient,modclient
from entryplaceholder import entryplaceholder


class clientindi(Toplevel):
    def __init__(self,parent,idc,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Informacion de cliente")
        self.parent= parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.frameb = Frame(self, bg="white", width = 450, height=600)
        self.frameb.pack()
        self.idc=idc
        self.data(infoclient(idc))

        self.titu = Label(self.frameb, text="Información del cliente", font=("Verdana",15),bg="white")
        self.titu.place(x=90,y=50)

        self.lab1 = Label(self.frameb, text="Nombre:",font=("Verdana",12),bg="white")
        self.lab1.place(x=65,y=130)
        

        self.lab2 = Label(self.frameb, text="ID:",font=("Verdana",12),bg="white")
        self.lab2.place(x=65,y=180)
        

        self.lab3 = Label(self.frameb, text="Cedula:",font=("Verdana",12),bg="white")
        self.lab3.place(x=65,y=230)
        

        self.lab4 = Label(self.frameb, text="Número de compras:",font=("Verdana",12),bg="white")
        self.lab4.place(x=65,y=280)
        

        self.lab5 = Label(self.frameb, text="Fecha Registro:",font=("Verdana",12),bg="white")
        self.lab5.place(x=65,y=330)



        self.bot1 = Button(self.frameb, text="Regresar",width=10, command=self.regre)
        self.bot1.place(x=100,y=550) 
        
        self.bot2 = Button(self.frameb, text="Modificar producto", command=self.mod)
        self.bot2.place(x=300,y=550) 



    def data(self,datos):
        self.nom = entryplaceholder(self.frameb, placeholder=datos.nomb_cliente)
        self.nom.config(state="disabled",width=38)
        self.nom.place(x=240,y=130)
        self.id = Label(self.frameb, text=datos.id_cliente,font=("Verdana",12),bg="white")
        self.id.place(x=240,y=180)
        self.ci = entryplaceholder(self.frameb, placeholder=datos.ci_cliente)
        self.ci.config(state="disabled",width=38)
        self.ci.place(x=240,y=230)
        self.num = Label(self.frameb, text=datos.numbcompras,font=("Verdana",12),bg="white")
        self.num.place(x=240,y=280)
        self.dire= Text(self.frameb, width=20,height=12)
        self.dire.insert(INSERT,datos.direccion)
        self.dire.place(x=240,y=330)

    def mod(self):
        self.bot1.config(text="Cancelar", command=self.cancelar)
        self.bot2.config(text="Aceptar", command=self.conf)
        self.nom.config(state="normal")
        self.ci.config(state="normal")

    def conf(self):
        modclient(self.idc,self.nom.get(),self.ci.get(),self.dire.get("1.0",END))
        self.regre()
 
    def cancelar(self):
        self.nom.config(state="disabled")
        self.ci.config(state="disabled")
        self.bot1.config(text="Regresar",command=self.regre)
        self.bot2.config(text="Modificar", command=self.mod)
        

        
    def regre(self):
        self.destroy()
        self.parent.refresh()
        self.parent.deiconify()