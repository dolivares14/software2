from tkinter import *
from tkinter import ttk,messagebox
from sql import allclient,qcliente
from scroll import ScrollableFrame
from framemod import framemod
from clientindi import clientindi
from reporte1 import export_to_pdf
from datetime import datetime,date

class bcliente(Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.title("Consulta de clientes")
        
        
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
        self.comb["values"] = ["Cedula","Nombre"]
        
        
        self.lab2= Label(self.frameb, text="Buscar:",bg="white",font=("Verdana",12))
        self.lab2.place(x=340,y=25)

        self.text= Entry(self.frameb, width=30)
        self.text.place(x=420,y=25)

        self.rellenar(allclient())
        
        
        self.bot = Button(self.frameb, width=10,height=1,text= "Aceptar", command= self.val)
        self.bot.place(x=640,y=25)

        self.bot3 = Button(self.frameb,text="Realizar reporte", command=self.reportc)
        self.bot3.place(x=150,y=500)

        

        

        self.mainloop()

    def rellenar(self,lista):
        self.marco=[]
        self.reportdata=lista
        i=0
        for cli in lista:
            self.marco.append(framemod(self.framet.scrollable_frame, cli[0],width=750, height=60, bg="#DB7093"))
            self.marco[i].pack()
            self.marco[i].bind("<Button-1>", self.allinfo)
            self.id =Label(self.marco[i], text=cli[0], fg="white")
            self.id.place(x=20,y=5)
            self.nom =Label(self.marco[i], text=cli[1], fg="white")
            self.nom.place(x=50,y=5)
            self.ci = Label(self.marco[i], text="Cedula: "+str(cli[2]), fg="white")
            self.ci.place(x=50,y=30)
            self.num = Label(self.marco[i], text="N° Compras: "+str(cli[3]), fg="white")
            self.num.place(x=500,y=5)
            self.id.config(bg="#DB7093")
            self.nom.config(bg="#DB7093")
            self.ci.config(bg="#DB7093")
            self.num.config(bg="#DB7093")
            if i % 2 == 0:
                self.marco[i].config(bg="#C40233")
                self.id.config(bg="#C40233")
                self.nom.config(bg="#C40233")
                self.ci.config(bg="#C40233")
                self.num.config(bg="#C40233")
            i+=1

    def val(self):
        if self.text.get() == "":
            messagebox.showerror("Error","Ingrese un valor para realizar la busqueda")
            self.text.delete(0,END)
        else: 
            self.buscar()

    def buscar(self):
        quer=qcliente(self.comb.get(),self.text.get())
        self.text.delete(0,END)
        for i in self.marco:
                i.pack_forget()
                i.destroy()
        if len(quer)<1:
            messagebox.showerror("Error","No se han encontrado relaciones, intente otra vez") 
        else:
            messagebox.showinfo("Busqueda exitosa","Se ha encontrado " +str(len(quer))+" registros")
            self.rellenar(quer)

    def allinfo(self,event):
        caller= event.widget
        pos=caller.id
        nwin = clientindi(self,pos)

    def refresh(self):
        for i in self.marco:
            i.pack_forget()
            i.destroy()
        self.rellenar(allclient())

    def reportc(self):
        res=messagebox.askquestion("Confirmación","¿Estas seguro que deseas guardar un reporte de los elementos seleccionados?")
        if res == "yes":
            self.clireport=[["ID","Nombre","CI Cliente","N°compras","Dirección"]]
            for c in self.reportdata:
                self.clireport.append(c)
            now=datetime.now()

            titulo="Reporte de clientes "+str(date.today()) +"  "+ str(now.hour) + "-" + str(now.minute) + "-" + str(now.second) + ".pdf"
            export_to_pdf(4,titulo,"Clientes",self.clireport)
            messagebox.showinfo("Operación Exitosa","El reporte se ha generado exitosamente")
        



def main():
    mi_app = bcliente()
    return 0

if __name__ == '__main__':
    main()