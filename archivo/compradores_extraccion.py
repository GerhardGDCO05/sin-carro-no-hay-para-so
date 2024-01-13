#importamos librerias
import ast
import os

#creamos una lista
dictcompradores = []

#ubicamos la direccion del archivo 
direcActual=os.path.dirname(__file__)
direcPadre=os.path.dirname(direcActual)

URLFile = os.path.join(direcPadre,  'archivo_de_los_compradores.txt')

#funcion de extraccion
def extractInfo():

    #abrimos el archivo
    with open(URLFile,'r') as f:
        #metemos la informacion del archivo en lineas
        lineas = f.readlines()

        #verificamos si el archivo esta vacio
        if len(lineas) != 0:

            #iteramos lineas y convertimos cada linea en un diccionario
            #guardamos cada diccionario en una casilla de la lista
            for i in lineas:
                dictcompradores.append(ast.literal_eval(i))

    #retornamos la informacion completa
    return dictcompradores
