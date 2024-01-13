#hacemos las importaciones
import os
from io import open
import numpy as np

#ubicamos la direccion
directorio1 = os.path.dirname(__file__)
directorio2 = os.path.dirname(directorio1)
pag = os.path.join(directorio2, 'archivo_de_los_vehiculos.txt')

#funcion que guardad la informacion
def insertvehiculos(codigo, marca, modelo, year, kilometraje, precio, estatus):
    #creamos una lista
    listadeval = []
    
    #diccionario con los valores registrados
    veh = {
        'CODIGO': codigo,
        'MARCA': marca,
        'MODELO': modelo,
        'YEAR': year,
        'KILOMETRAJE': kilometraje,
        'PRECIO': precio,
        'ESTATUS': estatus, }

    #hacemos una lista de diccionarios
    listadeval.append(str(veh) + '\n')

    #guardamos la lista en un arreglo
    arregloveh = np.array(listadeval)

    #abrimos el archivo
    archivovehiculo = open(pag, 'a')
    
    #guardamos la informacion el el archivo
    archivovehiculo.writelines(arregloveh)

    #cerramos el archivo
    archivovehiculo.close()
