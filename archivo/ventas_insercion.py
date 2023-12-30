import os
from io import open
import numpy as np
from .Validaciones_ventas import *

direc_ventas_actual=os.path.dirname(__file__)
direc_ventas_padre=os.path.dirname(direc_ventas_actual)

URLventas=os.path.join(direc_ventas_padre,'archivo_de_las_ventas.txt')
def Data_ventas(factura, fecha_compra, cedula_comprador, codigo_comprador, modelo_vehiculo):
    listaventas=[]
    vendidos={
        "FACTURA":factura,
        "FECHA DE LA COMPRA":fecha_compra,
        "CEDULA DEL COMPRADOR":cedula_comprador,
        "CODIGO ":codigo_comprador,
        "MODELO": modelo_vehiculo}
    listaventas.append(str(vendidos)+'\n')
    arregloventas=np.array(listaventas)

    archivo_ventas=open(URLventas,"a")
    archivo_ventas.writelines(arregloventas)
    archivo_ventas.close()

    numero = 123456.78
    formato_numero = "{:,.2f}".format(numero)

    print(formato_numero)