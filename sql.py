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
    produ.disponibilidad = produ.disponibilidad + cant
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
            lista2=  [item.Codigo_items, produ.Nomb_producto,item.cantidad]
            lista.append(lista2)
    if tipo == "Nombre":
        produ = config.con.query(producto).filter(producto.Nomb_producto.like(search)).first()
        for item in config.con.query(items).filter(items.id_producto.like(produ.id_producto)).all():
            lista2= [item.Codigo_items, produ.Nomb_producto,item.cantidad]
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





# sentencias para la tabla clientes

# busca un cliente en la bdd
def scliente(ci):
    bus = config.con.query(clientes).filter_by(ci_cliente=ci).count()
    if bus <= 0:
        return False
    else:
        return True

            



if __name__== '__main__':
    config.base.metadata.create_all(config.engine)
    run()