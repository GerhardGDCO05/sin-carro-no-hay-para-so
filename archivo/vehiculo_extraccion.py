import os
import ast

dic_vehiculo = []
directorio1 = os.path.dirname(__file__)
directorio2 = os.path.dirname(directorio1)
pag = os.path.join(directorio2, 'archivo_de_los_vehiculos.txt')


def extrac_vehiculo():
    with open(pag, 'r') as v:
        lineas = v.readlines()
        if len(lineas) != 0:
            for i in lineas:
                dic_vehiculo.append(ast.literal_eval(i))
    return dic_vehiculo


def generar_codigo_vehiculo():
    with open(pag, 'r') as c:
        lineas = c.readlines()

    diferencia = 3 - len(str(len(lineas) + 1))
    codigo = str(len(lineas) + 1)
    for i in range(diferencia):
        codigo = '0' + codigo

    return codigo


def cambio_estatus(codigo_comprador):
    dic_vendidos = []
    str_vendidos = []
    with open(pag, 'r') as cambio:
        linea = cambio.readlines()
    with open(pag, 'w') as cambio:
        for i in linea:
            dic_vendidos.append(ast.literal_eval(i))

        for i in dic_vendidos:
            if i['CODIGO'] == codigo_comprador:
                i['ESTATUS'] = 1

        for i in dic_vendidos:
            str_vendidos.append(str(i) + '\n')

        cambio.writelines(str_vendidos)


def estatus_disponibles():
    diccionario=[]
    with open(pag, 'r') as archivo:
        # Inicializa el contador
        lineas_con_estatus_1 = 0

        # Lee cada línea del archivo
        for linea in archivo:
            # Convierte la línea en un diccionario utilizando
            diccionario.append(ast.literal_eval(linea))

        for i in diccionario:
            # Verifica si el diccionario tiene 'ESTATUS' igual a 0
            if i['ESTATUS'] == 0:
                lineas_con_estatus_1 += 1
    return lineas_con_estatus_1
