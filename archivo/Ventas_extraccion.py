#importamos librerias
import os
import ast

#creamos una lista
dic_ventas = []

#ubicamos la direccion
direcventas_actual = os.path.dirname(__file__)
direcventas_padre = os.path.dirname(direcventas_actual)
URLventas = os.path.join(direcventas_padre, 'archivo_de_las_ventas.txt')

#funcion que extrae la informacion
def extracventas():

    #abrimos el archivo
    with open(URLventas, "r") as v:
        line = v.readlines()

        #validamos la longitud del lineas 
        if len(line) != 0:

            #recorremos la informacion del archivo y la guardamos en una lista
            for i in line:
                dic_ventas.append(ast.literal_eval(i))
    
    #retornamos la informacion
    return dic_ventas
