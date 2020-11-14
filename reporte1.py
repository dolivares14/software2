import itertools
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A6,A4
from datetime import datetime
from sql import infouser,infoclient

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


def gen_factura(data,total,num,idc):
    cli = infoclient(idc)
    titulo="Factura "+str(num)+str(cli.id_cliente)+str(cli.numbcompras)+".pdf"
    c = canvas.Canvas(titulo,pagesize=A6)
    w, h = A6
    enca = c.beginText(20, h - 20)
    enca.setFont("Times-Roman", 10)
    enca.textLine("R.I.F: Nº J-00006275-7")
    enca.textLine("Contribuyente formal")
    enca.textLine("Supermercados central Madeirense")
    c.drawText(enca)

    c.line(20, h - 55, 270.2, h - 55)

    c.drawString(126, h - 75, "FACTURA")

    enca2 = c.beginText(20, h - 85)
    enca2.setFont("Times-Roman", 10)
    enca2.textLine("Número:   "+str(num))
    now=datetime.now()
    enca2.textLine("Fecha: "+str(now.date())+"    Hora:  "+str(now.time()))
    c.drawText(enca2)

    c.line(20, h - 110, 270.2, h - 110)

    cli = infoclient(idc)

    enca3 = c.beginText(20, h - 130)
    enca3.setFont("Times-Roman", 10)
    enca3.textLine("Razón social")
    enca3.textLine(str(cli.nomb_cliente))
    enca3.textLine("RIF/CI:  "+str(cli.ci_cliente))
    c.drawText(enca3)

    c.line(20, h - 165, 270.2, h - 165)

    distancia=185
    contl = c.beginText(20,h - 185)
    contr = c.beginText(240,h-185)
    contl.setFont("Times-Roman", 9)
    contr.setFont("Times-Roman", 9)
    for d in data:
        contl.textLine(str(d[0])+"X"+str(d[1]))
        contr.textLine("")
        contl.textLine(str(d[2]))
        contr.textLine(str(d[3]))
        distancia+=23

    c.drawText(contl)
    c.drawText(contr)

    
    c.line(20, h - distancia, 270.2, h - distancia)

    distancia += 20

    fin = c.beginText(20,h - distancia)
    fin.setFont("Times-Roman", 12)
    fin.textLine("I.V.A  .................................................."+str(round(total*0.1,2)))
    fin.textLine("TOTAL  .................................................."+ str(total))
    c.drawText(fin)

    distancia += 25

    c.line(20, h - distancia, 270.2, h - distancia)











    c.save()
    



#  Una hoja A4 está constituida por 595.2 puntos de ancho (width) y 841.8 puntos de alto (height).
def export_to_pdf(ide,titulo,tabla,data):
    c = canvas.Canvas(titulo, pagesize=A4)
    w, h = A4
    inf=infouser(ide)
    c.rect(30, h - 180, 535.2, 150)
    c.line(50, h - 90, 525.2, h - 90)
    c.line(30, h - 220, 565.2, h - 220)
    enca = c.beginText(50, h - 50)
    enca.setFont("Times-Roman", 16)
    enca.textLine("Supermercados central Madeirense")
    enca.textLine("Hoja de reportes")
    c.drawText(enca)
    
    enca2= c.beginText(300,h - 120)
    enca2.setFont("Times-Roman", 12)
    enca2.textLine(str(datetime.now()))
    enca2.textLine(inf.nomb_empleado)
    enca2.textLine(str(inf.ci_empleado))
    enca2.textLine(tabla)
    c.drawText(enca2)

    enca3= c.beginText(50,h - 120)
    enca3.setFont("Times-Roman", 12)
    enca3.textLine("Fecha: ")
    enca3.textLine("Realizado por el empleado: ")
    enca3.textLine("Cédula: ")
    enca3.textLine("Elementos referenciados: ")
    c.drawText(enca3)

    max_rows_per_page = 25
    # Margin.
    x_offset = 50
    y_offset = 280
    # Space between rows.
    padding = 15


    if tabla == "Ventas":
        xlist = [x + x_offset for x in [0, 100, 200, 300, 400, 500]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    elif tabla == "Movimientos de items":
        xlist = [x + x_offset for x in [0, 30, 250, 320, 400, 450,500]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    elif tabla == "Operaciones de inventario":
        xlist = [x + x_offset for x in [0, 50, 150, 270, 450]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    elif tabla == "Productos":
        xlist = [x + x_offset for x in [0, 50, 250, 320, 430, 500]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    elif tabla == "Inventario de items":
        x_offset = 20
        xlist = [x + x_offset for x in [0, 90, 290, 370, 430, 500,570]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    elif tabla == "Empleados":
        xlist = [x + x_offset for x in [0, 50, 150, 300, 370, 440,510]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    elif tabla == "Clientes":
        x_offset = 20
        xlist = [x + x_offset for x in [0, 50, 210, 280, 350, 570]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

        
    
    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()
    
    c.save()


