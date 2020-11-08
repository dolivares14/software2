from tkinter import *
from tkinter import ttk
from calendario import Calendar
from sql import allproduct, additem,regiope,movinv
from agregarprodu import agregarprodu
from tkinter import messagebox

class agregarinven(Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.title("ingreso de items")
        self.frameb = Frame(self, bg="white", width = 550, height=600)
        self.frameb.pack()

        self.tit = Label(self.frameb, text="Agregar elemento(s) al inventario", font=("Verdana",12),bg="white")
        self.tit.place(x=150, y=40) 

        self.lab1 = Label(self.frameb, text="Código de barras:",font=("Verdana",12),bg="white")
        self.lab1.place(x=55,y=120)
        self.cod = Entry(self.frameb, width=30)
        self.cod.place(x=250,y=120)

        self.lab2 = Label(self.frameb, text="Tipo de producto:",font=("Verdana",12),bg="white")
        self.lab2.place(x=55,y=180)
        self.comb= ttk.Combobox(self.frameb, width=25, height=10, state= "readonly", values=allproduct())
        self.comb.place(x=250, y=180)
        self.but = Button(self.frameb, text="+ Nuevo", command=self.produ)
        self.but.place(x=430,y=180)

        self.lab3 = Label(self.frameb, text="Cantidad:",font=("Verdana",12),bg="white")
        self.lab3.place(x=55,y=240)
        self.spin = Spinbox(self.frameb, from_=0,to=10000, width=7)
        self.spin.place(x=250,y=240)

        self.lab4 = Label(self.frameb, text="Fecha de expedición:",font=("Verdana",12),bg="white")
        self.lab4.place(x=55,y=300)
        self.cal= Calendar(self.frameb)
        self.cal.place(x=250,y=300)

        self.bot1 = Button(self.frameb, text="Regresar")
        self.bot1.place(x=150,y=520)

        self.bot2 = Button(self.frameb, text="Aceptar", command=self.nuevo)
        self.bot2.place(x=310,y=520)

        self.mainloop()

    def nuevo(self):
        additem(int(self.cod.get()),self.comb.get(),self.cal.selection(),int(self.spin.get()))
        ope=regiope(4,"Registro de item")
        movinv(self.cod.get(),ope,"Ingreso",int(self.spin.get()))
        messagebox.showinfo("Operación Exitosa","EL item se ha registrado exitosamente")

        
        


    def produ(self):
        nwin = agregarprodu(self)

    def refresh(self):
        self.comb.config(values=allproduct())
        

        


def main():
    mi_app = agregarinven()
    return 0

if __name__ == '__main__':
    main()