from tkinter import *
from tkinter import ttk,messagebox
from scroll import ScrollableFrame
from framemod import framemod
from sql import allitem, sitem, allprodu, sprodu
from itemindi import itemindi
from produindi import produindi

class inventario(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.title("Inventario de productos")
        
        
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
        self.comb["values"] = ["Nombre","Código"]
        self.comb.set("Nombre")
        
        
        self.lab2= Label(self.frameb, text="Buscar:",bg="white",font=("Verdana",12))
        self.lab2.place(x=340,y=25)

        self.text= Entry(self.frameb, width=30)
        self.text.place(x=420,y=25)

        
        
        self.bot = Button(self.frameb, width=10,height=1,text= "Aceptar", command=self.vali)
        self.bot.place(x=640,y=25)

        self.bot2 = Button(self.frameb,text="Listado de productos",command=self.lprodu)
        self.bot2.place(x=580,y=500)

        self.bot3 = Button(self.frameb,text="Regresar")
        self.bot3.place(x=25,y=500)

        self.rellenar(allitem())

        

        self.mainloop()

    def rellenar(self,lista):
        self.marco=[]
        i=0
        for item in lista:
            self.marco.append(framemod(self.framet.scrollable_frame, item[0],width=750, height=60, bg="#DB7093"))
            self.marco[i].pack()
            self.marco[i].bind("<Button-1>", self.iteminfo)
            self.id =Label(self.marco[i], text="Codigo de barras: "+str(item[0]), fg="white", bg="#DB7093")
            self.id.place(x=20,y=5)
            self.nom =Label(self.marco[i], text=item[1], fg="white", bg="#DB7093")
            self.nom.place(x=20,y=25)
            self.cant = Label(self.marco[i], text="Cantidad ingresada: "+str(item[2]), fg="white", bg="#DB7093")
            self.cant.place(x=250,y=5)
            self.est = Label(self.marco[i], text="Estado: "+str(item[3]), fg="white", bg="#DB7093")
            self.est.place(x=500,y=5)
            if i % 2 == 0:
                self.marco[i].config(bg="#C40233")
                self.id.config(bg="#C40233")
                self.nom.config(bg="#C40233")
                self.cant.config(bg="#C40233")
                self.est.config(bg="#C40233")
            i+=1

    def rellenarp(self,lista):
        self.marco=[]
        i=0
        for item in lista:
            self.marco.append(framemod(self.framet.scrollable_frame, item[0],width=750, height=60, bg="#DB7093"))
            self.marco[i].pack()
            self.marco[i].bind("<Button-1>", self.prodinfo)
            self.id =Label(self.marco[i], text=str(item[0]), fg="white", bg="#DB7093")
            self.id.place(x=20,y=5)
            self.nom =Label(self.marco[i], text=item[1], fg="white", bg="#DB7093")
            self.nom.place(x=50,y=5)
            self.clas = Label(self.marco[i], text=item[3], fg="white", bg="#DB7093")
            self.clas.place(x=50,y=30)
            self.cant = Label(self.marco[i], text=item[2], fg="white", bg="#DB7093")
            self.cant.place(x=570,y=5)
            if i % 2 == 0:
                self.marco[i].config(bg="#C40233")
                self.id.config(bg="#C40233")
                self.nom.config(bg="#C40233")
                self.cant.config(bg="#C40233")
                self.clas.config(bg="#C40233")
            i+=1

    def vali(self):
        if self.text.get() == "":
            messagebox.showerror("Error","Ingrese un valor para realizar la busqueda")
            self.text.delete(0,END)
        else: 
            self.buscari()
    
    def valp(self):
        if self.text.get() == "":
            messagebox.showerror("Error","Ingrese un valor para realizar la busqueda")
            self.text.delete(0,END)
        else: 
            self.buscarp()


    def buscari(self):
        quer=sitem(self.comb.get(),self.text.get())
        self.text.delete(0,END)
        for i in self.marco:
                i.pack_forget()
                i.destroy()
        if len(quer)<1:
            messagebox.showerror("Error","No se han encontrado relaciones, intente otra vez") 
        else:
            messagebox.showinfo("Busqueda exitosa","Se ha encontrado " +str(len(quer))+" registros")
            self.rellenar(quer)
    
    def buscarp(self):
        quer=sprodu(self.comb.get(),self.text.get())
        self.text.delete(0,END)
        for i in self.marco:
                i.pack_forget()
                i.destroy()
        if len(quer)<1:
            messagebox.showerror("Error","No se han encontrado relaciones, intente otra vez") 
        else:
            messagebox.showinfo("Busqueda exitosa","Se ha encontrado " +str(len(quer))+" registros")
            self.rellenarp(quer)

    def lprodu(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenarp(allprodu())
        self.comb["values"] = ["Nombre","ID","Clasificación"]
        self.comb.set("Nombre")
        self.bot2.config(command=self.litem,text="Listado de items")
        self.bot.config(command=self.valp)

    def litem(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenar(allitem())
        self.comb["values"] = ["Nombre","Código"]
        self.comb.set("Nombre")
        self.bot2.config(command=self.lprodu,text="Listado de productos") 
        self.bot.config(command=self.vali)

    def iteminfo(self,event):
        caller= event.widget
        pos=caller.id
        nwin=itemindi(self,pos)

    def prodinfo(self,event):
        caller= event.widget
        pos=caller.id
        nwin=produindi(self,pos)

    def refreshi(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenar(allitem())

    def refreshp(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenarp(allprodu())





def main():
    mi_app = inventario()
    return 0

if __name__ == '__main__':
    main()