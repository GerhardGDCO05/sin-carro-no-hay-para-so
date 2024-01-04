import os
from io import open
import numpy as np

direcActual = os.path.dirname(__file__)
direcPadre = os.path.dirname(direcActual)

URLFile = os.path.join(direcPadre, 'archivo_de_los_compradores.txt')


def insertData(cedula, rif, carnet, pasaporte, nombre_apellido, nacimiento, direccion, estado):
    listcompradores = []
    comprador = {
        'CEDULA': cedula,
        'RIF': rif,
        'CARNET DIPLOMATICO': carnet,
        'PASAPORTE': pasaporte,
        'NOMBRE': nombre_apellido,
        'FECHA DE NACIMIENTO': nacimiento,
        'DIRECCION': direccion,
        'ESTADO': estado}

    listcompradores.append(str(comprador) + '\n')

    arreglocompradores = np.array(listcompradores)

    archivocompradores = open(URLFile, "a")
    archivocompradores.writelines(arreglocompradores)

    archivocompradores.close()
