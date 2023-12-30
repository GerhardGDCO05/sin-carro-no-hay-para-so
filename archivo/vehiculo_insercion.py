import os
from io import open
import numpy as np

directorio1 = os.path.dirname(__file__)
directorio2 = os.path.dirname(directorio1)
pag = os.path.join(directorio2, 'archivo_de_los_vehiculos.txt')


def insertvehiculos(codigo, marca, modelo, year, kilometraje, precio, estatus):
    listadeval = []
    veh = {
        'CODIGO': codigo,
        'MARCA': marca,
        'MODELO': modelo,
        'YEAR': year,
        'KILOMETRAJE': kilometraje,
        'PRECIO': precio,
        'ESTATUS': estatus, }

    listadeval.append(str(veh) + '\n')

    arregloveh = np.array(listadeval)
    archivovehiculo = open(pag, 'a')
    archivovehiculo.writelines(arregloveh)
    archivovehiculo.close()
