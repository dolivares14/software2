import config
from models import empleados, clientes, items, producto, ventas, opeinventario, movitems
from datetime import datetime

def run():
    # newuser("lusi",335689,"normal","321")
    login(335689,"321")
    # newproduct("Coca-cola 2l",45.5,"Bebidas")
    # additem(123456123,"Coca-cola 2l",datetime.now(),9)


# Acciones para la tabla de empleados

def alluser():
    lista=[]
    for emp in config.con.query(empleados).all():
        list2=[emp.id_empleado,emp.ci_empleado,emp.nomb_empleado,emp.privilegios]
        lista.append(list2)
    return lista 

def infouser(idenv):
    data = config.con.query(empleados).filter_by(id_empleado=idenv).first()
    return data

def modiuser(id,nom,ci,privi,con):
    emp = config.con.query(empleados).get(id)
    emp.nomb_empleado = nom
    emp.ci_empleado = ci
    emp.privilegios = privi
    emp.contraseña = con
    config.con.commit()

def deluser(id):
    config.con.query(empleados).filter_by(id_empleado=id).delete()
    config.con.commit()

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

def newuser(nombre,cedula,privi,contra):
    now = datetime.now()
    nuevo = empleados(cedula,nombre,privi,0,now,now,contra)
    config.con.add(nuevo)
    config.con.commit()


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
def newproduct(nomb,precio,clas):
    nuevo = producto(nomb,0,precio,clas)
    config.con.add(nuevo)
    config.con.commit()

def allproduct():
    lista=[]
    for pro in config.con.query(producto).all():
        lista.append(pro.Nomb_producto)
    return lista

def additem(cod,nom,fecha,cant):
    produ = config.con.query(producto).filter_by(Nomb_producto=nom).first() 
    now = datetime.now()
    nuevo = items(cod, produ.id_producto, now, fecha, "disponible", cant)
    config.con.add(nuevo)
    produ.disponibilidad = produ.disponibilidad + cant
    config.con.commit()


    

            



if __name__== '__main__':
    config.base.metadata.create_all(config.engine)
    run()