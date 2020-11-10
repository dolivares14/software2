from tkinter import *
from sql import regiope,movinv, retiitem
from tkinter import messagebox
from tkinter import ttk
from agrecliente import agrecliente



class bcliente(Toplevel):
    def __init__(self,parent,id,cant,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Consulta de cliente")
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.frameb= Frame(self)
        self.frameb.pack()
        self.frameb.config(width=400,height=400)
        self.frameb.config(bg="white")
        self.id=id
        self.cant=cant
        

        self.lab= Label(self.frameb,text="N° de elementos a retirar",font=("Verdana",12),bg="white")
        self.lab.place(x=50,y=15)

        self.spin= Spinbox(self.frameb,from_=0,to=cant,width=7)
        self.spin.place(x=150,y=15)

        self.lab2= Label(self.frameb,text="Causa",font=("Verdana",12),bg="white")
        self.lab2.place(x=50,y=140)

        self.comb= ttk.Combobox(self.frameb, width=25, height=10, state= "readonly")
        self.comb["values"]=["Desecho por expiración","Cambio por defecto","Otro"]
        self.comb.set("Desecho por expiración")
        self.comb.place(x=150, y=140)

        self.but= Button(self.frameb,text="Regresar",command=self.regre)
        self.but.place(x=130,y=250)

        self.but2= Button(self.frameb,text="Retirar",command=self.reti)
        self.but2.place(x=130,y=250)


    def val(self):
        if not self.spin.get().isdigit():
            messagebox.showerror("Error","Ingrese una cantidad valida de elementos")
            self.spin.delete(0,END)
        else: 
            self.reti()

    def regre(self):
        self.destroy()
        self.parent.refreshi()
        self.parent.deiconify()

    def reti(self):
        res=messagebox.askquestion("Confirmación","¿Desea ingresar este item al sistema?")
        if res == "yes":
            ope=regiope(4,self.comb.get())
            movinv(self.id,ope,self.comb.get(),self.cant)
            retiitem(self.id,self.cant)
            messagebox.showinfo("Operación Exitosa","Se han retirado exitosamente los elementos")
            self.regre()
