import config
from models import empleados, clientes, items, producto, ventas, opeinventario, movitems
from datetime import datetime

def run():
    # newuser("lusi",335689,"normal","321")
    login(335689,"321")
    print(alluser())

def alluser():
    lista=[]
    for emp in config.con.query(empleados).all():
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

            



if __name__== '__main__':
    config.base.metadata.create_all(config.engine)
    run()