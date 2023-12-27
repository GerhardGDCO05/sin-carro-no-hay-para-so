import ast
import numpy as np
import os

dictcompradores = []
direcActual=os.path.dirname(__file__)
direcPadre=os.path.dirname(direcActual)

URLFile = os.path.join(direcPadre,  'archivo_de_los_compradores.txt')


def extractInfo():
    print(URLFile)
    with open(URLFile, "r") as f:
        lineas=f.readlines()
        if len(lineas) != 0:
            for i in lineas:
                dictcompradores.append(ast.literal_eval(i))
    return dictcompradores
