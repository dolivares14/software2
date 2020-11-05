from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sql import newproduct


class agregarprodu(Toplevel):
    def __init__(self,parent,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.title("Nuevo producto")
        self.frameb = Frame(self, bg="white", width = 550, height=380)
        self.frameb.pack()


        self.tit = Label(self.frameb, text="Nuevo producto", font=("Verdana",12),bg="white")
        self.tit.place(x=150, y=40)

        self.lab1 = Label(self.frameb, text="Nombre de producto:",font=("Verdana",12),bg="white")
        self.lab1.place(x=55,y=120)
        self.nom = Entry(self.frameb, width=40)
        self.nom.place(x=280,y=120)

        self.lab2 = Label(self.frameb, text="Clasificación del producto:",font=("Verdana",12),bg="white")
        self.lab2.place(x=55,y=180)
        self.comb = ttk.Combobox(self.frameb,width=25, height=10, state= "readonly")
        self.comb["values"] = ["Limpieza","Enlatados","Bebidas","Refrigerados","Snacks","Panaderia","Salsas y encurtidos","Verduras,legumbres y frutas","Granos","Otros"] 
        self.comb.place(x=280,y=180)

        self.lab3 = Label(self.frameb, text="Precio:",font=("Verdana",12),bg="white")
        self.lab3.place(x=55,y=240)
        self.cost = Entry(self.frameb, width=30)
        self.cost.place(x=280,y=240)

        self.bot1 = Button(self.frameb, text="Regresar", command=self.regre)
        self.bot1.place(x=150,y=320)

        self.bot2 = Button(self.frameb, text="Aceptar", command=self.nuevo)
        self.bot2.place(x=310,y=320)
        


        

    def nuevo(self):
        newproduct(self.nom.get(),float(self.cost.get()),self.comb.get())
        messagebox.showinfo("Operación Exitosa","El producto se ha creado correctamente")
        self.regre()

    def regre(self):
        self.destroy()
        self.parent.refresh()
        self.parent.deiconify()

        

