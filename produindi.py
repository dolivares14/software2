from tkinter import *
from entryplaceholder import entryplaceholder
from sql import infoprodu
from tkinter import ttk, messagebox
from sql import modprodu,checkproduct

class produindi(Toplevel):
    def __init__(self,parent,id,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Informacion de producto")
        self.parent= parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.frameb = Frame(self, bg="white", width = 500, height=480)
        self.frameb.pack()
        self.id=id
        self.data(infoprodu(self.id))
        

        self.titu = Label(self.frameb, text="Información del producto", font=("Verdana",15),bg="white")
        self.titu.place(x=130,y=50)

        self.lab1 = Label(self.frameb, text="Nombre de producto:",font=("Verdana",12),bg="white")
        self.lab1.place(x=50,y=130)
        

        self.lab2 = Label(self.frameb, text="ID:",font=("Verdana",12),bg="white")
        self.lab2.place(x=50,y=180)
        

        self.lab3 = Label(self.frameb, text="Clasificación:",font=("Verdana",12),bg="white")
        self.lab3.place(x=50,y=230)
        

        self.lab4 = Label(self.frameb, text="Precio:",font=("Verdana",12),bg="white")
        self.lab4.place(x=50,y=280)
        

        self.lab5 = Label(self.frameb, text="Disponibilidad:",font=("Verdana",12),bg="white")
        self.lab5.place(x=50,y=330)

        self.bot1 = Button(self.frameb, text="Regresar",width=10, command=self.regre)
        self.bot1.place(x=100,y=400) 
        
        self.bot2 = Button(self.frameb, text="Modificar producto", command=self.mod)
        self.bot2.place(x=300,y=400) 


    def val(self):
        if self.nom.get() == "" or self.cost.get() =="":
            messagebox.showerror("Error","Uno o más campos estan vacio")
            self.nom.delete(0, END)
            self.cost.delete(0, END)
        elif len(self.nom.get()) < 5:
            messagebox.showerror("Error","El nombre es demasiado corto")
            self.nom.delete(0, END)
            self.cost.delete(0, END)
        elif not self.es_flotante(self.cost.get()):
            messagebox.showerror("Error","Solo se pueden ingresar valores numericos en el precio")
            self.nom.delete(0, END)
            self.cost.delete(0, END)
        elif float(self.cost.get()) <= 0:
            messagebox.showerror("Error","El precio no puede ser igual o menor a cero")
            self.nom.delete(0, END)
            self.cost.delete(0, END)
        elif checkproduct(self.nom.get()):
            messagebox.showerror("Error","El nombre del producto ya se encuentra registrado")
            self.nom.delete(0, END)
            self.cost.delete(0, END)
        else:
            self.conf()

    def es_flotante(self,variable):
        try:
            float(variable)
            return True
        except:
            return False


    def data(self,datos):
        self.nom = entryplaceholder(self.frameb, placeholder=datos.Nomb_producto)
        self.nom.config(state="disabled",width=38)
        self.nom.place(x=240,y=130)
        self.ide = Label(self.frameb, text=datos.id_producto,font=("Verdana",12),bg="white")
        self.ide.place(x=240,y=180)
        self.clas = ttk.Combobox(self.frameb, state="disabled" ,width=35)
        self.clas["values"] = ["Limpieza","Enlatados","Bebidas","Refrigerados","Snacks","Panaderia","Salsas y encurtidos","Verduras,legumbres y frutas","Granos","Otros"]
        self.clas.set(datos.Clasificacion)
        self.clas.place(x=240,y=230)
        self.cost = entryplaceholder(self.frameb, placeholder="Bs.S "+str(datos.precio))
        self.cost.config(state="disabled",width=38)
        self.cost.place(x=240,y=280)
        self.disp = Label(self.frameb, text=datos.disponibilidad,font=("Verdana",12),bg="white")
        self.disp.place(x=240,y=330)


    def mod(self):
        self.bot1.config(text="Cancelar", command=self.cancelar)
        self.bot2.config(text="Aceptar", command=self.conf)
        self.nom.config(state="normal")
        self.clas.config(state="readonly")
        self.cost.config(state="normal")

    def conf(self):
        res=messagebox.askquestion("Confirmación","¿Desea modificar este producto?")
        if res == "yes":
            modprodu(self.id,self.nom.get(),self.clas.get(),self.cost.get())
            messagebox.showinfo("Operación Exitosa","El producto se ha modificado correctamente")
            self.regre()

    def cancelar(self):
        self.nom.config(state="disabled")
        self.clas.config(state="disabled")
        self.cost.config(state="disabled")
        self.bot1.config(text="Regresar",command=self.regre)
        self.bot2.config(text="Modificar", command=self.mod)

    def regre(self):
        self.destroy()
        self.parent.refreshp()
        self.parent.deiconify()
        
