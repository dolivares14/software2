from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from scroll import ScrollableFrame
from framemod import framemod
from sql import produforventa, proceventa,getidcliet, movventa, checkprodu, checkcant,retiitem
from scliente import bcliente
from procepago import metodop
from tkinter import Widget



class venta(Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.title("Procesar venta")
        
        self.frameb= Frame(self)
        self.frameb.pack()
        self.frameb.config(width=950,height=550)
        self.frameb.config(bg="white")


        self.framet= ScrollableFrame(self.frameb)
        self.framet.canvas.config(height=180)
        self.framet.place(x=25,y=330)

        self.frmcl = Frame(self.frameb,width=270,height=120,relief="sunken",bd=5,bg="white")
        self.frmcl.place(x=660,y=20)

        self.titu = Label(self.frameb, text="Agregar item a \n la compra", font=("Verdana",15),bg="white")
        self.titu.place(x=100,y=30)
        
        self.lab1 = Label(self.frameb, text="Código:",font=("Verdana",12),bg="white")
        self.lab1.place(x=70,y=130)

        self.lab2 = Label(self.frameb, text="Cantidad:",font=("Verdana",12),bg="white")
        self.lab2.place(x=50,y=205)

        self.cod = Entry(self.frameb,width=30)
        self.cod.place(x=150,y=130)

        self.spin = Spinbox(self.frameb, from_=0,to=10000, width=7)
        self.spin.place(x=150,y=205)

        self.agre = Button(self.frameb,text="Agregar",command=self.val)
        self.agre.place(x=150,y=255)

        self.regr = Button(self.frameb,text="Regresar al\n menu anterior", width=25,height=3, command=self.regre)
        self.regr.place(x=730,y=332)
        self.rein = Button(self.frameb,text="Reiniciar \nCompra", width=25,height=3,command=self.reiniciar)
        self.rein.place(x=730,y=402)  
        self.fin = Button(self.frameb,text="Proseguir \nCompra", width=25,height=3,command=self.sig)
        self.fin.place(x=730,y=472)

        self.lab3 = Label(self.frameb, text="TOTAL",font=("Verdana",20),bg="white")
        self.lab3.place(x= 500,y=30)

        self.total = Label(self.frameb,text="0.00", font=("Verdana",40),bg="white")
        self.sum = 0.00
        self.total.place(x=480,y=150)

        nwin = bcliente(self)

        self.item=[]
        self.i=0
        self.tota=[]
        self.cantidad=[]
        

        self.mainloop()

        
    def val(self):
        if self.cod.get()=="":
            messagebox.showerror("Error","Ingrese un código de barras")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif len(self.cod.get()) < 7:
            messagebox.showerror("Error","El codigo debe tener un total de 13 dígitos")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif not self.cod.get().isdigit():
            messagebox.showerror("Error","El codigo solo puede tener números")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif not self.spin.get().isdigit():
            messagebox.showerror("Error","Ingrese una cantidad valida de elementos")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif not checkprodu(self.cod.get()):
            messagebox.showerror("Error","El item no se ha encontrado")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        elif checkcant(self.cod.get())<int(self.spin.get()):
            messagebox.showerror("Error","El item no posee suficientes elementos")
            self.cod.delete(0,END)
            self.spin.delete(0,END)
        else:
            self.fill()
            
            
        

    def fill(self):
        self.item.append(framemod(self.framet.scrollable_frame, self.cod.get(),width=750, height=80, bg="white"))
        self.item[self.i].pack()
        info = produforventa(self.cod.get())
        self.nompro = Label(self.item[self.i], text=info[0],bg="white")
        self.nompro.place(x=20,y=5)
        self.costi = Label(self.item[self.i], text=str(self.spin.get()) + " x Bs.S "+ str(info[1]),bg="white")
        self.costi.place(x=20,y=25)
        self.toti = Label(self.item[self.i], text=str(float(self.spin.get())*info[1]),font=("Verdana",17),bg="white")
        self.toti.place(x=250,y=5)
        self.tota.append(float(self.spin.get())*info[1])
        self.cantidad.append(self.spin.get())
        self.canc = Button(self.item[self.i], text="Cancelar",bg="white",command=partial(self.eli,self.item[self.i],self.tota[self.i],self.cantidad[self.i]))
        self.canc.place(x=600,y=15)
        self.sum = self.sum + (float(self.spin.get())*info[1])
        self.total.config(text=self.sum)
        self.cod.delete("0","end")
        self.spin.delete("0","end")
        self.i+=1

    def eli(self,fram,tota,cant):
        rest=float(tota)
        self.sum-= rest
        self.total.config(text=self.sum)
        fram.pack_forget()
        fram.destroy()
        self.item.remove(fram)
        self.tota.remove(tota)
        self.cantidad.remove(cant)
        self.i-=1
        
    def infoclient(self,ci,nom):
        self.titu2 = Label(self.frmcl, text="Inf. cliente", font=("Verdana",15),bg="white")
        self.titu2.place(x=40,y=5)
        self.nom = Label(self.frmcl, text="Nombre: "+str(nom),font=("Verdana",12),bg="white")
        self.nom.place(x=5,y=45)
        self.cic = Label(self.frmcl, text="CI: "+str(ci),font=("Verdana",12),bg="white")
        self.cic.place(x=5,y=85)
        self.ciclient= ci

    def regre(self):
        ans=messagebox.askquestion("Confirmación","¿Estas seguro que deseas abandonar la ventana?")
        if ans== "yes":
            self.destroy()

    def reiniciar(self):
        ans=messagebox.askquestion("Confirmación","¿Estas seguro que deseas reiniciar el proceso?")
        if ans== "yes":
            self.ini()
    
    def ini(self):
        for i in self.item:
            i.pack_forget()
            i.destroy()
        self.total.config(text=0)
        self.sum=0.00
        self.i=0
        self.item=[]
        self.tota=[]
        self.cantidad=[]
        nwin = bcliente(self)
    
    def sig(self):
        nwind=metodop(self)

    def final(self,met):
        # NOTA: CAMBIAR EL ID DEL EMPLEADO CUANDO ESTE COMPLETO LOS MENUS
        idemp=4
        factura=proceventa(idemp,getidcliet(self.ciclient),met,self.sum)
        j=0
        for i in self.item:
            movventa(i.id,factura,self.cantidad[j])
            retiitem(i.id,self.cantidad[j])
            j+=1
        
        messagebox.showinfo("Compra exitosa","La compra se ha procesado correctamente")    
        self.ini()








        

def main():
    app = venta()
    return 0

if __name__ == '__main__':
    main()