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


def estatus_vendidos(codigo_comprador):
    dic_vendidos = []
    str_vendidos = []
    with open(pag, 'r') as vendido:
        linea = vendido.readlines()
    with open(pag, 'w') as vendido:
        for i in linea:
            dic_vendidos.append(ast.literal_eval(i))

        for i in dic_vendidos:
            if i['CODIGO']==codigo_comprador:
                i['ESTATUS']=1

        for i in dic_vendidos:
            str_vendidos.append(str(i)+'\n')

        vendido.writelines(str_vendidos)

