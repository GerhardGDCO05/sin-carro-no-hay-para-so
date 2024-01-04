import ast
import os

direc_actual = os.path.dirname(__file__)
direc_padre = os.path.dirname(direc_actual)
URL = os.path.join(direc_padre, 'archivo_de_las_ventas.txt')

direc_pecio = os.path.dirname(__file__)
direc_father = os.path.dirname(direc_pecio)
URL_father = os.path.join(direc_father, 'archivo_de_los_vehiculos.txt')

def busqueda(ingreso):
    # Inicializar listas para almacenar datos
    dic_busqueda_fecha = []
    dic_precio = []
    di_fechas = []
    dic_union = []

    keys_a_eliminar_ventas = ['FACTURA', 'CEDULA DEL COMPRADOR', 'CODIGO', 'MODELO']
    keys_a_eliminar_vehiculos = ['ESTATUS', 'KILOMETRAJE']
    # Leer datos del primer archivo (URL)
    diccionarios_unidos=[]
    with open(URL, 'r') as f:
        for linea in f.readlines():
            dic_busqueda_fecha.append(ast.literal_eval(linea))

        for i in dic_busqueda_fecha:
            if i['FECHA DE LA COMPRA'] == ingreso:
                di_fechas.append(i)
    # Leer datos del segundo archivo (URL_father)
    with open(URL_father, 'r') as pre:
        for linea in pre.readlines():
            dic_precio.append(ast.literal_eval(linea))

        for i in dic_precio:
            i_copy = i.copy()
            for j in di_fechas:
                j_copy = j.copy()

                if i_copy['CODIGO'] == j_copy['CODIGO']:
                    union_diccionarios = {**i_copy, **j_copy}
                    diccionarios_unidos.append(union_diccionarios)

    return diccionarios_unidos