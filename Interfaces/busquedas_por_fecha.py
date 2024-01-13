#importamos librerias
import ast
import os

#ubicamos la direccion de los archivos que necesitamos
direc_actual = os.path.dirname(__file__)
direc_padre = os.path.dirname(direc_actual)
URL = os.path.join(direc_padre, 'archivo_de_las_ventas.txt')

direc_pecio = os.path.dirname(__file__)
direc_father = os.path.dirname(direc_pecio)
URL_father = os.path.join(direc_father, 'archivo_de_los_vehiculos.txt')

#funcion que extrae la informacion de los archivo y compara los codigo para conseguir lo vehiculos de la fecha pedida
def busqueda(ingreso):
    # Inicializar listas para almacenar datos
    dic_busqueda_fecha = []
    dic_precio = []
    di_fechas = []
    
    
    # Leer datos del primer archivo (URL)
    diccionarios_unidos=[]
    with open(URL, 'r') as f:
        #recorremos la informacion del primer archivo
        for linea in f.readlines():

            #guardamos la informacion
            dic_busqueda_fecha.append(ast.literal_eval(linea))

        #recorremos la lista
        for i in dic_busqueda_fecha:
            #validamos la fecha y guardamos las que cumplan
            if i['FECHA DE LA COMPRA'] == ingreso:
                di_fechas.append(i)
    
    # Leer datos del segundo archivo (URL_father)
    with open(URL_father, 'r') as pre:
        #recorremos el segundo archivo
        for linea in pre.readlines():
            #guardamos la informacion
            dic_precio.append(ast.literal_eval(linea))

        #recorremos la lista
        for i in dic_precio:
            #creamos copias
            i_copy = i.copy()
            #recorremos la lista con las fechas correctas
            for j in di_fechas:
                #creamos copias
                j_copy = j.copy()
                 #validamos los codigos de las copias
                if i_copy['CODIGO'] == j_copy['CODIGO']:
                    #unimos la informacion de las copias
                    union_diccionarios = {**i_copy, **j_copy}
                    #guardamos la informacion en una lista
                    diccionarios_unidos.append(union_diccionarios)

    #retornamos la lista
    return diccionarios_unidos