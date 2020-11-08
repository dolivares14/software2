from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class metodop(Toplevel):
    def __init__(self,parent,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Tipo de pago")
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.frameb= Frame(self)
        self.frameb.pack()
        self.frameb.config(width=400,height=200)
        self.frameb.config(bg="white")

        self.lab= Label(self.frameb,text="Seleccione el  \n metodo de pago",font=("Verdana",15),bg="white")
        self.lab.place(x=100,y=5)

        self.comb = ttk.Combobox(self.frameb,width=25, height=10, state= "readonly")
        self.comb["values"] = ["Debito","Credito","Efectivo","Cheque"]
        self.comb.set("Debito")
        self.comb.place(x=30,y=100)

        self.but= Button(self.frameb,text="Aceptar",command=self.avan)
        self.but.place(x=220,y=100)

        self.but2= Button(self.frameb,text="Regresar",command=self.regre)
        self.but2.place(x=300,y=100)

    def regre(self):
        self.destroy()
        self.parent.deiconify()

    def avan(self):
        nwin= finventa(self)
    
    def avan2(self):
        met=self.comb.get()
        self.destroy()
        self.parent.deiconify()
        self.parent.final(met)
        


class finventa(Toplevel):
    def __init__(self,parent,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Finalizar")
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.parent.deiconify)
        self.parent.withdraw()
        self.frameb= Frame(self)
        self.frameb.pack()
        self.frameb.config(width=300,height=200)
        self.frameb.config(bg="white")
        self.lab= Label(self.frameb,text="Presione aceptar cuando \n se confirme la transacción",font=("Verdana",15),bg="white")
        self.lab.place(x=10,y=5)

        self.but= Button(self.frameb,text="Aceptar",command=self.acept)
        self.but.place(x=50,y=150)
        self.but2= Button(self.frameb,text="Regresar",command=self.regre)
        self.but2.place(x=200,y=150)

    def regre(self):
        resp=messagebox.askquestion("Regresar","¿Deseas volver a la ventana de venta?")
        if resp== "yes":
            self.destroy()
            self.parent.regre()

    def acept(self):
        resp=messagebox.askquestion("Confirmación","¿Estas seguro que deseas completar la transacción?")
        if resp== "yes":
            self.parent.avan2()
            self.destroy()

