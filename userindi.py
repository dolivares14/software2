from tkinter import *
from sql import infouser, deluser


class userindi(Toplevel):
    def __init__(self,parent,id,*args, **kwargs):
        super().__init__(parent,*args, **kwargs)
        self.resizable(0,0)
        self.title("Consulta de usuario")
        self.title("Informacion de producto")
        self.parent= parent
        self.protocol("WM_DELETE_WINDOW", self.regre)
        self.parent.withdraw()
        self.frameb = Frame(self, bg="white", width = 450, height=600)
        self.frameb.pack()
        self.id=id
        self.data(infouser(self.id))

        self.titu = Label(self.frameb, text="Información del empleado", font=("Verdana",15),bg="white")
        self.titu.place(x=90,y=50)

        self.lab1 = Label(self.frameb, text="Nombre:",font=("Verdana",12),bg="white")
        self.lab1.place(x=65,y=130)
        

        self.lab2 = Label(self.frameb, text="ID:",font=("Verdana",12),bg="white")
        self.lab2.place(x=65,y=180)
        

        self.lab3 = Label(self.frameb, text="Cedula:",font=("Verdana",12),bg="white")
        self.lab3.place(x=65,y=230)
        

        self.lab4 = Label(self.frameb, text="Privilegios:",font=("Verdana",12),bg="white")
        self.lab4.place(x=65,y=280)
        

        self.lab5 = Label(self.frameb, text="Fecha Registro:",font=("Verdana",12),bg="white")
        self.lab5.place(x=65,y=330)
       

        self.lab6 = Label(self.frameb, text="Fecha ultima sesion:",font=("Verdana",12),bg="white")
        self.lab6.place(x=65,y=380)
        

        self.lab7 = Label(self.frameb, text="Numero de ventas:",font=("Verdana",12),bg="white")
        self.lab7.place(x=65,y=430)
        

        self.lab8 = Label(self.frameb, text="Contraseña:",font=("Verdana",12),bg="white")
        self.lab8.place(x=65,y=480)
        



        self.bot1 = Button(self.frameb, text="Regresar",width=10, command=self.regre)
        self.bot1.place(x=50,y=550) 
        
        self.bot3 = Button(self.frameb, text="Eliminar",width=10, command=self.eli)
        self.bot3.place(x=250,y=550) 


    def data(self,datos):
        self.nom = Label(self.frameb, text=datos.nomb_empleado,font=("Verdana",12),bg="white")
        self.nom.place(x=240,y=130)
        self.id = Label(self.frameb, text=datos.id_empleado,font=("Verdana",12),bg="white")
        self.id.place(x=240,y=180)
        self.ci = Label(self.frameb, text=datos.ci_empleado,font=("Verdana",12),bg="white")
        self.ci.place(x=240,y=230)
        self.privi = Label(self.frameb, text=datos.privilegios,font=("Verdana",12),bg="white")
        self.privi.place(x=240,y=280)
        self.fecharegi = Label(self.frameb, text=datos.Fecha_registro,font=("Verdana",12),bg="white")
        self.fecharegi.place(x=240,y=330)
        self.fechaulti= Label(self.frameb, text=datos.Fecha_ultima_sesion,font=("Verdana",12),bg="white")
        self.fechaulti.place(x=240,y=380)
        self.num = Label(self.frameb, text=datos.numventas,font=("Verdana",12),bg="white")
        self.num.place(x=240,y=430)
        self.con = Label(self.frameb, text=datos.contraseña,font=("Verdana",12),bg="white")
        self.con.place(x=240,y=480)

    def eli(self):
        deluser(self.id)
        self.regre()
        
    def regre(self):
        self.destroy()
        self.parent.refresh()
        self.parent.deiconify()