#importaciones de librerias necesarias
import os
from io import open
import numpy as np

#ubicamos la direccion del archivo
direcActual = os.path.dirname(__file__)
direcPadre = os.path.dirname(direcActual)
#ubicamos el archivo donde vamos a guardar el registro
URLFile = os.path.join(direcPadre, 'archivo_de_los_compradores.txt')

#funcion que guarda el registro
def insertData(cedula, rif, carnet, pasaporte, nombre_apellido, nacimiento, direccion, estado):
    
    #creamos una lista
    listcompradores = []
    
    #pasamos los datos ya verificados y los guardamos en un diccionario
    comprador = {
        'CEDULA': cedula,
        'RIF': rif,
        'CARNET DIPLOMATICO': carnet,
        'PASAPORTE': pasaporte,
        'NOMBRE': nombre_apellido,
        'FECHA DE NACIMIENTO': nacimiento,
        'DIRECCION': direccion,
        'ESTADO': estado}

    #ingresamos el diccionario a la lista creando una lista de diccionarios
    listcompradores.append(str(comprador) + '\n')

    #ingresamos la lista a un arreglo
    arreglocompradores = np.array(listcompradores)

    #abrimos el archivo donde vamos a guardar el registro
    archivocompradores = open(URLFile, "a")
    
    #guardamos la informacion
    archivocompradores.writelines(arreglocompradores)

    #cerramos el archivo
    archivocompradores.close()
