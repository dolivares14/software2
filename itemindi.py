from tkinter import *
from sql import infoitem

class itemindi(Toplevel):
    def __init__(self,parent,id,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Información del item")
        self.parent= parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.frameb = Frame(self, bg="white", width = 500, height=500)
        self.frameb.pack()
        self.id=id
        self.data(infoitem(self.id))

        self.titu = Label(self.frameb, text="Información del item", font=("Verdana",15),bg="white")
        self.titu.place(x=100,y=50)

        self.lab1 = Label(self.frameb, text="Nombre de producto:",font=("Verdana",12),bg="white")
        self.lab1.place(x=50,y=130)
        

        self.lab2 = Label(self.frameb, text="Código:",font=("Verdana",12),bg="white")
        self.lab2.place(x=50,y=180)
        

        self.lab3 = Label(self.frameb, text="Fecha de registro:",font=("Verdana",12),bg="white")
        self.lab3.place(x=50,y=230)
        

        self.lab4 = Label(self.frameb, text="Fecha de expiración:",font=("Verdana",12),bg="white")
        self.lab4.place(x=50,y=280)
        

        self.lab5 = Label(self.frameb, text="Cantidad ingresada:",font=("Verdana",12),bg="white")
        self.lab5.place(x=50,y=330)

        self.lab6 = Label(self.frameb, text="Estado:",font=("Verdana",12),bg="white")
        self.lab6.place(x=50,y=380)


        self.bot1 = Button(self.frameb, text="Regresar",command=self.regre)
        self.bot1.place(x=50,y=450) 
        
        self.bot3 = Button(self.frameb, text="Retirar elementos")
        self.bot3.place(x=250,y=450)



    def data(self,datos):
        self.nom = Label(self.frameb, text=datos[0],font=("Verdana",12),bg="white")
        self.nom.place(x=225,y=130)
        self.cod = Label(self.frameb, text=datos[1],font=("Verdana",12),bg="white")
        self.cod.place(x=225,y=180)
        self.fing = Label(self.frameb, text=datos[2],font=("Verdana",12),bg="white")
        self.fing.place(x=225,y=230)
        self.fexp = Label(self.frameb, text=datos[3],font=("Verdana",12),bg="white")
        self.fexp.place(x=225,y=280)
        self.cant = Label(self.frameb, text=datos[4],font=("Verdana",12),bg="white")
        self.cant.place(x=225,y=330)
        self.est = Label(self.frameb, text=datos[5],font=("Verdana",12),bg="white")
        self.est.place(x=225,y=380)

    def regre(self):
        self.destroy()
        self.parent.refreshi()
        self.parent.deiconify()
        



