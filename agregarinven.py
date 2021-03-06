from tkinter import *
from tkinter import ttk
from calendario import Calendar
from sql import allproduct, additem,regiope,movinv,checkprodu
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
        prods=allproduct()
        self.comb= ttk.Combobox(self.frameb, width=25, height=10, state= "readonly", values=prods)
        self.comb.set(prods[0])
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

        self.bot2 = Button(self.frameb, text="Aceptar", command=self.val)
        self.bot2.place(x=310,y=520)

        self.mainloop()

    def nuevo(self):
        res=messagebox.askquestion("Confirmación","¿Desea ingresar este item al sistema?")
        if res == "yes":
            additem(int(self.cod.get()),self.comb.get(),self.cal.selection(),int(self.spin.get()))
            ope=regiope(4,"Registro de item")
            movinv(self.cod.get(),ope,"Ingreso",int(self.spin.get()))
            messagebox.showinfo("Operación Exitosa","EL item se ha registrado exitosamente")

    def val(self):
        if self.cod.get() == "" or self.spin.get() =="":
            messagebox.showerror("Error","Uno o más campos estan vacio")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif not len(self.cod.get())==13:
            messagebox.showerror("Error","El codigo debe de tener 13 dígitos")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif not self.cod.get().isdigit():
            messagebox.showerror("Error","Solo se pueden ingresar valores numericos en el código")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif not self.spin.get().isdigit():
            messagebox.showerror("Error","Ingrese una cantidad valida de elementos")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif  checkprodu(self.cod.get()):
            messagebox.showerror("Error","El item ya se encuentra registrado")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif not self.cal.selection():
            messagebox.showerror("Error","Seleccione la fecha de expedición")
        else:
            self.nuevo()  
        


    def produ(self):
        nwin = agregarprodu(self)

    def refresh(self):
        self.comb.config(values=allproduct())
        

        


def main():
    mi_app = agregarinven()
    return 0

if __name__ == '__main__':
    main()