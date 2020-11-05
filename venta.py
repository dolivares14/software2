from tkinter import *
from tkinter import ttk
from scroll import ScrollableFrame
from framemod import framemod
from sql import produforventa
from scliente import scliente


class venta(Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(0,0)
        self.title("Inventario de productos")
        
        self.frameb= Frame(self)
        self.frameb.pack()
        self.frameb.config(width=950,height=550)
        self.frameb.config(bg="white")


        self.framet= ScrollableFrame(self.frameb)
        self.framet.canvas.config(height=180)
        self.framet.place(x=25,y=350)

        self.titu = Label(self.frameb, text="Agregar item a \n la compra", font=("Verdana",15),bg="white")
        self.titu.place(x=100,y=50)
        
        self.lab1 = Label(self.frameb, text="Código:",font=("Verdana",12),bg="white")
        self.lab1.place(x=70,y=150)

        self.lab2 = Label(self.frameb, text="Cantidad:",font=("Verdana",12),bg="white")
        self.lab2.place(x=50,y=225)

        self.cod = Entry(self.frameb,width=30)
        self.cod.place(x=150,y=150)

        self.spin = Spinbox(self.frameb, from_=0,to=10000, width=7)
        self.spin.place(x=150,y=225)

        self.agre = Button(self.frameb,text="Agregar",command=self.fill)
        self.agre.place(x=150,y=275)
        self.fin = Button(self.frameb,text="Finalizar \nCompra", width=25,height=3)
        self.fin.place(x=730,y=472)

        self.lab3 = Label(self.frameb, text="TOTAL",font=("Verdana",20),bg="white")
        self.lab3.place(x= 500,y=50)

        self.total = Label(self.frameb,text="0.00", font=("Verdana",40),bg="white")
        self.sum = 0.00
        self.total.place(x=480,y=180)

        self.mainloop()

        

    def fill(self):
        self.item= framemod(self.framet.scrollable_frame, self.cod.get(),width=750, height=60, bg="white")
        self.item.pack()
        info = produforventa(self.cod.get())
        self.nompro = Label(self.item, text=info[0],bg="white")
        self.nompro.place(x=20,y=5)
        self.costi = Label(self.item, text=str(self.spin.get()) + " x Bs.S "+ str(info[1]),bg="white")
        self.costi.place(x=20,y=25)
        self.toti = Label(self.item, text=str(float(self.spin.get())*info[1]),font=("Verdana",17),bg="white")
        self.toti.place(x=250,y=5)
        self.canc = Button(self.item, text="Cancelar",bg="white")
        self.canc.place(x=600,y=15)
        self.sum = self.sum + (float(self.spin.get())*info[1])
        self.total.config(text=self.sum)
        self.cod.delete("0","end")
        self.spin.delete("0","end")
        

def main():
    app = venta()
    return 0

if __name__ == '__main__':
    main()