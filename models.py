import config
from sqlalchemy import *


class empleados(config.base):
    __tablename__ = "empleados"
    id_empleado = Column(Integer, primary_key=True, autoincrement=True)
    ci_empleado = Column(Integer, unique=True, nullable=False)
    nomb_empleado = Column(String(50), nullable=False)
    privilegios = Column(String(15), nullable=False)
    numventas = Column(Integer, nullable=False)
    Fecha_registro = Column(DateTime, nullable=False)
    Fecha_ultima_sesion = Column(DateTime, nullable=False)
    contraseña = Column(String(30), unique=True, nullable=False)

    def __init__(self, ci_empleado, nomb_empleado, privilegios, numventas, Fecha_registro, Fecha_ultima_sesion, contraseña):
        self.ci_empleado = ci_empleado
        self.nomb_empleado = nomb_empleado
        self.privilegios = privilegios
        self.numventas = numventas
        self.Fecha_registro = Fecha_registro
        self.Fecha_ultima_sesion = Fecha_ultima_sesion
        self.contraseña = contraseña

    def __repr__(self):
        return f'empleados({self.ci_empleado}, {self.nomb_empleado}, {self.privilegios}, {self.numventas}, {self.Fecha_registro}, {self.Fecha_ultima_sesion}, {self.contraseña})'




class clientes(config.base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    ci_cliente = Column(Integer, unique=True, nullable=False)
    nomb_cliente = Column(String(50), nullable=False)
    numbcompras = Column(Integer, nullable=False)
    direccion = Column(String(80), nullable=False)

    def __init__(self, id_cliente, ci_cliente, nomb_cliente, numbcompras, direccion):
        self.id_cliente = id_cliente
        self.ci_cliente = ci_cliente
        self.nomb_cliente = nomb_cliente
        self.numbcompras = numbcompras
        self.direccion = direccion


    def __repr__(self):
        return f'clientes( {self.ci_cliente}, {self.nomb_cliente}, {self.numbcompras}, {self.direccion} )'





class ventas(config.base):
    __tablename__="ventas"
    nfactura = Column(Integer, primary_key=True, autoincrement=True)
    id_empleado = Column(Integer, nullable=False)
    id_cliente = Column(Integer, nullable=False)
    tipopago = Column(String(20), nullable=False)
    monto = Column(Float, nullable=False)

    def __init__(self, nfactura, id_empleado, id_cliente, tipopago, monto):
        self.nfactura = nfactura
        self.id_empleado = id_empleado
        self.id_cliente = id_cliente
        self.tipopago = tipopago
        self.monto = monto
    
    def __repr__(self):
        return f'ventas({self.nfactura}, {self.id_empleado}, {self.id_cliente}, {self.tipopago}, {self.monto})'






class items(config.base):
    __tablename__="items"
    Codigo_items = Column(Integer, primary_key=True, autoincrement=False)
    id_producto = Column(Integer, nullable=False)
    fecha_registro = Column(DateTime, nullable=False)
    fecha_expedicion = Column(DateTime, nullable=False)
    estado = Column(String(30), nullable=False)
    cantidad = Column(Integer,nullable=False)

    def __init__(self, Codigo_items, id_producto, fecha_registro, fecha_expedicion, estado,cantidad):
        self.Codigo_items= Codigo_items
        self.id_producto = id_producto
        self.fecha_registro = fecha_registro
        self.fecha_expedicion = fecha_expedicion
        self.estado = estado
        self.cantidad = cantidad
    
    def __repr__(self):
        return f'items({self.Codigo_items}, {self.id_producto}, {self.fecha_registro}, {self.fecha_expedicion}, {self.estado})'







class producto(config.base):
    __tablename__="producto"
    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    Nomb_producto = Column(String(50), nullable=False)
    disponibilidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)
    Clasificacion = Column(String(20), nullable=False)

    def __init__(self, Nomb_producto, disponibilidad, precio, Clasificacion ):
        self.Nomb_producto = Nomb_producto
        self.disponibilidad = disponibilidad
        self.precio = precio
        self.Clasificacion  = Clasificacion 


    def __repr__(self):
        return f'producto( {self.Nomb_producto}, {self.disponibilidad}, {self.precio}, {self.Clasificacion } )'






class opeinventario(config.base):
    __tablename__="opeinventario"
    id_ope = Column(Integer, primary_key=True, autoincrement=True)
    id_empleado = Column(Integer, nullable=False)
    descripcion = Column(String(100), nullable=False)
    hora_ope = Column(DateTime, nullable=False)

    def __init__(self, id_ope, id_empleado, descripcion, hora_ope, numventas, Fecha_registro, Fecha_ultima_sesion, contraseña):
        self.id_ope = id_ope
        self.id_empleado = id_empleado
        self.descripcion = descripcion
        self.hora_ope = hora_ope
  

    def __repr__(self):
        return f'opeinventario( {self.id_empleado}, {self.descripcion}, {self.hora_ope})'





class movitems(config.base):
    __tablename__="movitems"
    idmov = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, nullable=False)
    n_factura = Column(Integer)
    id_ope = Column(Integer)
    accion = Column(String(20), nullable=False)
    cantidad = Column(Integer, nullable=False)

    def __init__(self, idmov, id_producto, n_factura, privilegios, id_ope, accion, cantidad):
        self.idmov = idmov
        self.id_producto = id_producto
        self.n_factura = n_factura
        self.id_ope = id_ope
        self.accion  = accion 
        self.cantidad = cantidad


    def __repr__(self):
        return f'movitems( {self.id_producto}, {self.n_factura}, {self.id_ope}, {self.accion}, {self.cantidad})'

    