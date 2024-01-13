#importamos librerias y archivos
import os
from io import open
import numpy as np
from .Validaciones_ventas import *
from .vehiculo_extraccion import cambio_estatus

#ubicamos la direccion del archivo
direc_ventas_actual=os.path.dirname(__file__)
direc_ventas_padre=os.path.dirname(direc_ventas_actual)

URLventas=os.path.join(direc_ventas_padre,'archivo_de_las_ventas.txt')

#funcion que guarda la informacion
def Data_ventas(factura, fecha_compra, cedula_comprador, codigo_comprador, modelo_vehiculo):

    #funcion que cambia el estatus de 0 a 1 
    cambio_estatus(codigo_comprador)


    #creamos una lista
    listaventas=[]
    #guardamos la informacion en un dicionario
    vendidos={
        "FACTURA":factura,
        "FECHA DE LA COMPRA":fecha_compra,
        "CEDULA DEL COMPRADOR":cedula_comprador,
        "CODIGO":codigo_comprador,
        "MODELO": modelo_vehiculo}
    
    #creamos una lista de diccionarios
    listaventas.append(str(vendidos)+'\n')

    #guardamos la lista en un arreglo
    arregloventas=np.array(listaventas)

    #abrimos el archivo
    archivo_ventas=open(URLventas,"a")

    #guardamos la informacion
    archivo_ventas.writelines(arregloventas)

    #cerramos el archivo
    archivo_ventas.close()

