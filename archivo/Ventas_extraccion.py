import os
import ast

dic_ventas = []
direcventas_actual = os.path.dirname(__file__)
direcventas_padre = os.path.dirname(direcventas_actual)
URLventas = os.path.join(direcventas_padre, 'archivo_de_las_ventas.txt')


def extracventas():
    with open(URLventas, "r") as v:
        line = v.readlines()
        if len(line) != 0:
            for i in line:
                dic_ventas.append(ast.literal_eval(i))
    return dic_ventas
