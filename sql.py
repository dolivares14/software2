import config
from models import empleados, clientes, items, producto, ventas, opeinventario, movitems
from datetime import datetime

def run():
    # newuser("lusi",335689,"normal","321")
    login(335689,"321")
    print(scliente(565656))
    # newproduct("Coca-cola 2l",45.5,"Bebidas")
    # additem(123456123,"Coca-cola 2l",datetime.now(),9)





















# Acciones para la tabla de empleados


# envia los datos para la tabla de empleados
def alluser():
    lista=[]
    for emp in config.con.query(empleados).all():
        list2=[emp.id_empleado,emp.ci_empleado,emp.nomb_empleado,emp.privilegios]
        lista.append(list2)
    return lista 

# envia los datos individuales de un empleado
def infouser(idenv):
    data = config.con.query(empleados).filter_by(id_empleado=idenv).first()
    return data

# Modifica los datos de un empleado(sin usar)
def modiuser(id,nom,ci,privi,con):
    emp = config.con.query(empleados).get(id)
    emp.nomb_empleado = nom
    emp.ci_empleado = ci
    emp.privilegios = privi
    emp.contraseña = con
    config.con.commit()

# Elimina a un usuario
def deluser(id):
    config.con.query(empleados).filter_by(id_empleado=id).delete()
    config.con.commit()

# Busca usuarios por un query
def suser(tipo,consu):
    search= "%{}%".format(consu)
    lista=[]
    if tipo =="Cedula":
        for emp in config.con.query(empleados).filter(empleados.ci_empleado.like(search)).all():
           list2=[emp.id_empleado,emp.ci_empleado,emp.nomb_empleado,emp.privilegios]
           lista.append(list2)
    if tipo =="Nombre":
        for emp in config.con.query(empleados).filter(empleados.nomb_empleado.like(search)).all():
           list2=[emp.id_empleado,emp.ci_empleado,emp.nomb_empleado,emp.privilegios]
           lista.append(list2)
    if tipo =="ID":
        for emp in config.con.query(empleados).filter(empleados.id_empleado.like(search)).all():
           list2=[emp.id_empleado,emp.ci_empleado,emp.nomb_empleado,emp.privilegios]
           lista.append(list2)
    return lista 

# Crea un nuevo usuario
def newuser(nombre,cedula,privi,contra):
    now = datetime.now()
    nuevo = empleados(cedula,nombre,privi,0,now,now,contra)
    config.con.add(nuevo)
    config.con.commit()

# Hace login 
def login(user,passw):
    conf = False
    for emp in config.con.query(empleados).all():
        if conf==False:
            if emp.ci_empleado == user and emp.contraseña == passw:
                conf=True
    if conf:
        print("contraseña correcta")
    else:
        print("contraseña incorrecta")







































# Acciones de la tabla productos e items


# Crea un nuevo producto
def newproduct(nomb,precio,clas):
    nuevo = producto(nomb,0,precio,clas)
    config.con.add(nuevo)
    config.con.commit()

# envia la lista de productos para el combobox en agregar inventario
def allproduct():
    lista=[]
    for pro in config.con.query(producto).all():
        lista.append(pro.Nomb_producto)
    return lista

# Añade un item al inventario
def additem(cod,nom,fecha,cant):
    produ = config.con.query(producto).filter_by(Nomb_producto=nom).first() 
    now = datetime.now()
    nuevo = items(cod, produ.id_producto, now, fecha, "disponible", cant)
    config.con.add(nuevo)
    config.con.commit()

# Muestra la tabla de productos
def allprodu():
    lista=[]
    for prod in config.con.query(producto).all():
        lista2=[prod.id_producto,prod.Nomb_producto,prod.disponibilidad, prod.Clasificacion]
        lista.append(lista2)
    return lista

# Muestra la tabla de items
def allitem():
    lista=[]
    for item in config.con.query(items).all():
        produ = config.con.query(producto).filter_by(id_producto=item.id_producto).first()
        lista2= [item.Codigo_items, produ.Nomb_producto,item.cantidad,item.estado]
        lista.append(lista2)
    return lista 

# Busca un producto 
def sprodu(tipo,consu):
    search= "%{}%".format(consu)
    lista=[]
    if tipo =="ID":
        for prod in config.con.query(producto).filter(producto.id_producto.like(search)).all():
            lista2=  [prod.id_producto, prod.Nomb_producto,prod.disponibilidad,prod.Clasificacion]
            lista.append(lista2)
    if tipo == "Nombre":
        for prod in config.con.query(producto).filter(producto.Nomb_producto.like(search)).all():
            lista2=  [prod.id_producto, prod.Nomb_producto,prod.disponibilidad,prod.Clasificacion]
            lista.append(lista2)
    if tipo == "Clasificación":
        for prod in config.con.query(producto).filter(producto.Clasificacion.like(search)).all():
            lista2=  [prod.id_producto, prod.Nomb_producto,prod.disponibilidad,prod.Clasificacion]
            lista.append(lista2)
    return lista

# Busca un item
def sitem(tipo,consu):
    search= "%{}%".format(consu)
    lista=[]
    if tipo =="Código":
        for item in config.con.query(items).filter(items.Codigo_items.like(search)).all():
            produ = config.con.query(producto).filter_by(id_producto=item.id_producto).first()
            lista2=  [item.Codigo_items, produ.Nomb_producto,item.cantidad,item.estado]
            lista.append(lista2)
    if tipo == "Nombre":
        for produ in config.con.query(producto).filter(producto.Nomb_producto.like(search)).all():
            for item in config.con.query(items).filter_by(id_producto=produ.id_producto).all():
                lista2= [item.Codigo_items, produ.Nomb_producto,item.cantidad,item.estado]
                lista.append(lista2)
    return lista

# Muestra la informacion completa de un item
def infoitem(codenv):
    data = config.con.query(items).filter_by(Codigo_items=codenv).first()
    produ = config.con.query(producto).filter_by(id_producto=data.id_producto).first()
    lista = [produ.Nomb_producto,data.Codigo_items,data.fecha_registro,data.fecha_expedicion,data.cantidad,data.estado]
    return lista

 #Muestra la informacion completa de un producto  
def infoprodu(idenv):
    data = config.con.query(producto).filter_by(id_producto=idenv).first()
    return data

# Modifica un producto
def modprodu(id,nomb,clas,precio):
    prod = config.con.query(producto).get(id)
    prod.Nomb_producto= nomb
    prod.Clasificacion = clas
    prod.precio = precio
    config.con.commit()

# Envia la informacion del producto para su venta
def produforventa(codenv):
    data = config.con.query(items).filter_by(Codigo_items=codenv).first()
    produ = config.con.query(producto).filter_by(id_producto=data.id_producto).first()
    lista = [produ.Nomb_producto,produ.precio,data.cantidad]
    return lista 
    
# Se retira una cantidad de productos de la bdd
def retiitem(id,cant):
    it = config.con.query(items).filter_by(Codigo_items=id)
    produ=config.con.query(producto).filter_by(id_producto=it.id_producto)
    produ.cantidad-= cant
    config.con.commit()

# Chequea si el producto ya existe
def checkproduct(nom):
    bus = config.con.query(producto).filter_by(Nomb_producto=nom).count()
    if bus <= 0:
        return False
    else:
        return True































# sentencias para la tabla clientes

# busca un cliente en la bdd
def scliente(ci):
    bus = config.con.query(clientes).filter_by(ci_cliente=ci).count()
    if bus <= 0:
        return False
    else:
        return True

# agrega un cliente a la bdd
def ncliente(nom,ci,dir):
    nuevo= clientes(ci,nom,0,dir)
    config.con.add(nuevo)
    config.con.commit()

# envia la info de un cliente por su cedula
def infocliente(ci):
    data = config.con.query(clientes).filter_by(ci_cliente=ci).first()
    return data

# Obtiene la id de un cliente
def getidcliet(ci):
    data = config.con.query(clientes).filter_by(ci_cliente=ci).first()
    return data.id_cliente 

# Envia la informacion de todos los clientes para la tabla
def allclient():
    lista = []
    data = config.con.query(clientes).all()
    for cli in data:
        lista2=[cli.id_cliente,cli.nomb_cliente,cli.ci_cliente,cli.numbcompras]
        lista.append(lista2)
    return lista

# Busca clientes por un query
def qcliente(tipo,consu):
    search= "%{}%".format(consu)
    lista=[]
    if tipo =="Cedula":
        for cli in config.con.query(clientes).filter(clientes.ci_cliente.like(search)).all():
           lista2=[cli.id_cliente,cli.nomb_cliente,cli.ci_cliente,cli.numbcompras]
           lista.append(lista2)
    if tipo =="Nombre":
        for cli in config.con.query(clientes).filter(clientes.nomb_cliente.like(search)).all():
           lista2=[cli.id_cliente,cli.nomb_cliente,cli.ci_cliente,cli.numbcompras]
           lista.append(lista2)
    return lista


# Envia la informacion completa de un cliente
def infoclient(idc):
    data = config.con.query(clientes).filter_by(id_cliente=idc).first()
    return data

# Modifica la info de un cliente
def modclient(id,nomb,ci,dire):
    cli = config.con.query(clientes).get(id)
    cli.nomb_cliente= nomb
    cli.ci_cliente = ci
    cli.direccion = dire
    config.con.commit()
































# Termina de procesar una venta
def proceventa(ide,idc,met,mont):
    nuevo = ventas(ide,idc,met,mont)
    config.con.add(nuevo)
    emp=config.con.query(empleados).filter_by(id_empleado=ide).first()
    emp.numventas += 1
    cli=config.con.query(clientes).filter_by(id_cliente=idc).first()
    cli.numbcompras += 1
    config.con.commit()
    return nuevo.nfactura

# Registra una operacion en la bdd
def regiope(ide,accion):
    nuevo = opeinventario(ide,accion,datetime.now())
    config.con.add(nuevo)
    config.con.commit()
    return nuevo.id_ope

# Registra un movimiento de items en el inventario
def movinv(cod,idop,accion,cant):
    it=config.con.query(items).filter_by(Codigo_items=cod).first()
    nuevo = movitems(it.id_producto,0,idop,accion,cant)
    config.con.add(nuevo)
    config.con.commit()

# Guarda el registro de movimientos de items durante una venta
def movventa(cod,factu,cant):
        it=config.con.query(items).filter_by(Codigo_items=cod).first()
        nuevo = movitems(it.id_producto,factu,0,"Venta",cant)
        config.con.add(nuevo)
        config.con.commit()

# Chequea que el item exista
def checkprodu(cod):
    bus = config.con.query(items).filter_by(Codigo_items=cod).count()
    if bus <= 0:
        return False
    else:
        return True

# Chequea la disponibilidad de un producto  
def checkcant(cod):
    it= config.con.query(items).filter_by(Codigo_items=cod).first()
    produ = config.con.query(producto).filter_by(id_producto=it.id_producto).first()
    return produ.disponibilidad

# Muestra todas las ventas para la tabla
def allventa():
    lista = []
    data = config.con.query(ventas).all()
    for ven in data:
        cli = config.con.query(clientes).filter_by(id_cliente=ven.id_cliente).first()
        emp = config.con.query(empleados).filter_by(id_empleado=ven.id_empleado).first()
        lista2=[ven.nfactura,emp.ci_empleado,cli.ci_cliente,ven.tipopago,ven.monto]
        lista.append(lista2)
    return lista

# Realiza la busqueda de ventas
def sventa(tipo,consu):
    search= "%{}%".format(consu)
    lista=[]
    if tipo =="CI Cliente":
        for cli in config.con.query(clientes).filter(clientes.ci_cliente.like(search)).all():
            for ven in config.con.query(ventas).filter_by(id_cliente=cli.id_cliente).all():
                emp = config.con.query(empleados).filter_by(id_empleado=ven.id_empleado).first()
                lista2= [ven.nfactura,emp.ci_empleado,cli.ci_cliente,ven.tipopago,ven.monto]
                lista.append(lista2)
    if tipo =="CI Empleado":
        for emp in config.con.query(empleados).filter(empleados.ci_empleado.like(search)).all():
            for ven in config.con.query(ventas).filter_by(id_empleado=emp.id_empleado).all():
                cli = config.con.query(clientes).filter_by(id_cliente=ven.id_cliente).first()
                lista2= [ven.nfactura,emp.ci_empleado,cli.ci_cliente,ven.tipopago,ven.monto]
                lista.append(lista2)
    if tipo =="N° de Factura":
        for ven in config.con.query(ventas).filter(ventas.nfactura.like(search)).all():
           cli = config.con.query(clientes).filter_by(id_cliente=ven.id_cliente).first()
           emp = config.con.query(empleados).filter_by(id_empleado=ven.id_empleado).first()
           lista2=[ven.nfactura,emp.ci_empleado,cli.ci_cliente,ven.tipopago,ven.monto]
           lista.append(lista2)
    if tipo =="Metodo":
        for ven in config.con.query(ventas).filter(ventas.tipopago.like(search)).all():
           cli = config.con.query(clientes).filter_by(id_cliente=ven.id_cliente).first()
           emp = config.con.query(empleados).filter_by(id_empleado=ven.id_empleado).first()
           lista2=[ven.nfactura,emp.ci_empleado,cli.ci_cliente,ven.tipopago,ven.monto]
           lista.append(lista2)
    return lista

# Busca todos los mov de items para la tabla
def allmov():
    lista = []
    data= config.con.query(movitems).all()
    for mov in data:
        produ= config.con.query(producto).filter_by(id_producto=mov.id_producto).first()
        lista2=[mov.idmov,produ.Nomb_producto,mov.n_factura,mov.id_ope,mov.accion,mov.cantidad]
        lista.append(lista2)
    return lista

# Busca un movimiento
def smov(tipo,consu):
    search= "%{}%".format(consu)
    lista=[]
    if tipo =="ID":
        for mov in config.con.query(movitems).filter(movitems.idmov.like(search)).all():
            produ= config.con.query(producto).filter_by(id_producto=mov.id_producto).first()
            lista2=[mov.idmov,produ.Nomb_producto,mov.n_factura,mov.id_ope,mov.accion,mov.cantidad]
            lista.append(lista2)
    if tipo =="Nombre de producto":
        for produ in config.con.query(producto).filter(producto.Nomb_producto.like(search)).all():
            for mov in config.con.query(movitems).filter_by(id_producto=produ.id_producto).all():
                lista2=[mov.idmov,produ.Nomb_producto,mov.n_factura,mov.id_ope,mov.accion,mov.cantidad]
                lista.append(lista2)
    if tipo =="Acción":
        for mov in config.con.query(movitems).filter(movitems.accion.like(search)).all():
            produ= config.con.query(producto).filter_by(id_producto=mov.id_producto).first()
            lista2=[mov.idmov,produ.Nomb_producto,mov.n_factura,mov.id_ope,mov.accion,mov.cantidad]
            lista.append(lista2)
    return lista

# muestra todas las operaciones del inventario para la tabla
def allope():
    lista = []
    data = config.con.query(opeinventario).all()
    for ope in data:
        emp = config.con.query(empleados).filter_by(id_empleado=ope.id_empleado).first()
        lista2=[ope.id_ope,emp.ci_empleado,ope.descripcion,ope.hora_ope]
        lista.append(lista2)
    return lista

# Busca una operacion
def sope(tipo,consu):
    search= "%{}%".format(consu)
    lista=[]
    if tipo =="ID":
       for ope in config.con.query(opeinventario).filter(opeinventario.id_ope.like(search)).all():
           emp = config.con.query(empleados).filter_by(id_empleado=ope.id_empleado).first()
           lista2=[ope.id_ope,emp.ci_empleado,ope.descripcion,ope.hora_ope]
           lista.append(lista2)
    if tipo =="CI Empleado":
        for emp in config.con.query(empleados).filter(empleados.ci_empleado.like(search)).all():
            for ope in config.con.query(opeinventario).filter_by(id_empleado=emp.id_empleado).all():
                lista2=[ope.id_ope,emp.ci_empleado,ope.descripcion,ope.hora_ope]
                lista.append(lista2)
    if tipo=="Descripción":
        for ope in config.con.query(opeinventario).filter(opeinventario.descripcion.like(search)).all():
           emp = config.con.query(empleados).filter_by(id_empleado=ope.id_empleado).first()
           lista2=[ope.id_ope,emp.ci_empleado,ope.descripcion,ope.hora_ope]
           lista.append(lista2)
    return lista

    

        




            



if __name__== '__main__':
    config.base.metadata.create_all(config.engine)
    run()