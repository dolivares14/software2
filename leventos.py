from tkinter import *
from tkinter import ttk,messagebox
from scroll import ScrollableFrame
from framemod import framemod
from sql import allventa, sventa, allmov, smov, allope, sope
from itemindi import itemindi
from produindi import produindi

class leventos(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.title("Listado de eventos")
        
        
        self.frameb= Frame(self)
        self.frameb.pack()
        self.frameb.config(width=750,height=550)
        self.frameb.config(bg="white")


        self.framet= ScrollableFrame(self.frameb,width=100)
        self.framet.place(x=25,y=75)

        
        self.lab1= Label(self.frameb, text="Buscar por...",bg="white",font=("Verdana",12))
        self.lab1.place(x=25,y=25)

        self.comb= ttk.Combobox(self.frameb, width=25,height=10,state="readonly")
        self.comb.place(x=150,y=25)
        self.comb["values"] = ["CI Cliente","CI Empleado","N° de Factura","Metodo"]
        self.comb.set("CI Cliente")
        
        
        self.lab2= Label(self.frameb, text="Buscar:",bg="white",font=("Verdana",12))
        self.lab2.place(x=340,y=25)

        self.text= Entry(self.frameb, width=30)
        self.text.place(x=420,y=25)

        
        
        self.bot = Button(self.frameb, width=10,height=1,text= "Aceptar", command=self.valv)
        self.bot.place(x=640,y=25)

        self.bot2 = Button(self.frameb,text="Movimiento de items",command=self.lmov)
        self.bot2.place(x=580,y=500)

        self.bot3 = Button(self.frameb,text="Operaciones de inventario",command=self.lope)
        self.bot3.place(x=400,y=500)

        self.bot4 = Button(self.frameb,text="Ventas realizadas",command=self.lventa,state="disabled")
        self.bot4.place(x=265,y=500)

        self.bot5 = Button(self.frameb,text="Regresar")
        self.bot5.place(x=25,y=500)

        self.rellenar(allventa())

        

        self.mainloop()

    def rellenar(self,lista):
        self.marco=[]
        i=0
        for vent in lista:
            self.marco.append(framemod(self.framet.scrollable_frame, vent[0],width=750, height=60, bg="#DB7093"))
            self.marco[i].pack()
            self.id = Label(self.marco[i], text="N° Factura: "+str(vent[0]), fg="white", bg="#DB7093")
            self.id.place(x=20,y=5)
            self.cie = Label(self.marco[i], text="CI empleado: "+str(vent[1]), fg="white", bg="#DB7093")
            self.cie.place(x=20,y=25)
            self.cic = Label(self.marco[i], text="CI cliente: "+str(vent[2]), fg="white", bg="#DB7093")
            self.cic.place(x=250,y=25)
            self.met = Label(self.marco[i], text="Pago en: "+str(vent[3]), fg="white", bg="#DB7093")
            self.met.place(x=250,y=5)
            self.mon = Label(self.marco[i], text="Monto: Bs.S"+str(vent[4]), fg="white", bg="#DB7093")
            self.mon.place(x=500,y=5)
            if i % 2 == 0:
                self.marco[i].config(bg="#C40233")
                self.id.config(bg="#C40233")
                self.cie.config(bg="#C40233")
                self.cic.config(bg="#C40233")
                self.met.config(bg="#C40233")
                self.mon.config(bg="#C40233")
            i+=1

    def rellenarm(self,lista):
        self.marco=[]
        i=0
        for mov in lista:
            self.marco.append(framemod(self.framet.scrollable_frame, mov[0],width=750, height=60, bg="#DB7093"))
            self.marco[i].pack()
            self.id =Label(self.marco[i], text="ID: " + str(mov[0]), fg="white", bg="#DB7093")
            self.id.place(x=20,y=5)
            self.prod =Label(self.marco[i], text="Producto: "+ str(mov[1]), fg="white", bg="#DB7093")
            self.prod.place(x=20,y=25)
            if mov[2]==0:
                self.iden= Label(self.marco[i], text="ID operación: "+str(mov[3]), fg="white", bg="#DB7093")
            else:
                self.iden= Label(self.marco[i], text="N° factura: "+str(mov[2]), fg="white", bg="#DB7093")  
            self.iden.place(x=250,y=5)
            self.acc =Label(self.marco[i], text="Acción: "+ str(mov[4]), fg="white", bg="#DB7093")
            self.acc.place(x=250,y=25)
            self.cant = Label(self.marco[i], text="Cantidad: "+str(mov[5]), fg="white", bg="#DB7093")
            self.cant.place(x=500,y=5)
            if i % 2 == 0:
                self.marco[i].config(bg="#C40233")
                self.id.config(bg="#C40233")
                self.prod.config(bg="#C40233")
                self.iden.config(bg="#C40233")
                self.acc.config(bg="#C40233")
                self.cant.config(bg="#C40233")
            i+=1

    def rellenaro(self,lista):
        self.marco=[]
        i=0
        for ope in lista:
            self.marco.append(framemod(self.framet.scrollable_frame, ope[0],width=750, height=60, bg="#DB7093"))
            self.marco[i].pack()
            self.id = Label(self.marco[i], text="ID Operación: "+str(ope[0]), fg="white", bg="#DB7093")
            self.id.place(x=20,y=5)
            self.cie = Label(self.marco[i], text="CI empleado: "+str(ope[1]), fg="white", bg="#DB7093")
            self.cie.place(x=20,y=25)
            self.des = Label(self.marco[i], text="Acción: "+str(ope[2]), fg="white", bg="#DB7093")
            self.des.place(x=250,y=25)
            self.hora = Label(self.marco[i], text="Fecha: "+str(ope[3]), fg="white", bg="#DB7093")
            self.hora.place(x=250,y=5)
            if i % 2 == 0:
                self.marco[i].config(bg="#C40233")
                self.id.config(bg="#C40233")
                self.cie.config(bg="#C40233")
                self.des.config(bg="#C40233")
                self.hora.config(bg="#C40233")
            i+=1

    def valv(self):
        if self.text.get() == "":
            messagebox.showerror("Error","Ingrese un valor para realizar la busqueda")
            self.text.delete(0,END)
        else: 
            self.buscarv()

    def valm(self):
        if self.text.get() == "":
            messagebox.showerror("Error","Ingrese un valor para realizar la busqueda")
            self.text.delete(0,END)
        else: 
            self.buscarm()

    def valo(self):
        if self.text.get() == "":
            messagebox.showerror("Error","Ingrese un valor para realizar la busqueda")
            self.text.delete(0,END)
        else: 
            self.buscaro()


    def buscarv(self):
        quer=sventa(self.comb.get(),self.text.get())
        self.text.delete(0,END)
        for i in self.marco:
                i.pack_forget()
                i.destroy()
        if len(quer)<1:
            messagebox.showerror("Error","No se han encontrado relaciones, intente otra vez") 
        else:
            messagebox.showinfo("Busqueda exitosa","Se ha encontrado " +str(len(quer))+" registros")
            self.rellenar(quer)
    
    def buscarm(self):
        quer=smov(self.comb.get(),self.text.get())
        self.text.delete(0,END)
        for i in self.marco:
                i.pack_forget()
                i.destroy()
        if len(quer)<1:
            messagebox.showerror("Error","No se han encontrado relaciones, intente otra vez") 
        else:
            messagebox.showinfo("Busqueda exitosa","Se ha encontrado " +str(len(quer))+" registros")
            self.rellenarm(quer)

    def buscaro(self):
        quer=sope(self.comb.get(),self.text.get())
        self.text.delete(0,END)
        for i in self.marco:
                i.pack_forget()
                i.destroy()
        if len(quer)<1:
            messagebox.showerror("Error","No se han encontrado relaciones, intente otra vez") 
        else:
            messagebox.showinfo("Busqueda exitosa","Se ha encontrado " +str(len(quer))+" registros")
            self.rellenaro(quer)

    def lmov(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenarm(allmov())
        self.comb["values"] = ["ID","Nombre de producto","Acción"]
        self.comb.set("ID")
        self.bot2.config(state="disabled")
        self.bot3.config(state="normal")
        self.bot4.config(state="normal")
        self.bot.config(command=self.valm)

    def lventa(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenar(allventa())
        self.comb["values"] = ["CI Cliente","CI Empleado","N° de Factura","Metodo"]
        self.comb.set("CI Cliente")
        self.bot4.config(state="disabled")
        self.bot2.config(state="normal")
        self.bot3.config(state="normal")
        self.bot.config(command=self.valv)

    def lope(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenaro(allope())
        self.comb["values"] = ["ID","CI Empleado","Descripción"]
        self.comb.set("ID")
        self.bot4.config(state="normal")
        self.bot2.config(state="normal")
        self.bot3.config(state="disabled")
        self.bot.config(command=self.valo)





def main():
    mi_app = leventos()
    return 0

if __name__ == '__main__':
    main()