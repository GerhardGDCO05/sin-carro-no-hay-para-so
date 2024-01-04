import os
import ast
from tkinter import *
from tkinter import ttk

directorio1 = os.path.dirname(__file__)
directorio2 = os.path.dirname(directorio1)
pag = os.path.join(directorio2, 'archivo_de_los_vehiculos.txt')


def extrac_vehiculo():
    dic_vehiculo = []
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


def cantidad_por_vender():
    por_vender = Tk()
    por_vender.title("VEHICULOS DISPONIBLES")
    por_vender.config(bg="light blue")
    dic_por_vender = []
    dic_disponibles = []
    with open(pag, 'r') as d:
        no_vendidos = d.readlines()

        for i in no_vendidos:
            dic_disponibles.append(ast.literal_eval(i))

        for i in dic_disponibles:
            if i['ESTATUS'] == 0:
                dic_por_vender.append(i)

    columna = ('CODIGO',
               "MARCA",
               "MODELO",
               "YEAR",
               "KILOMETRAJE ",
               "PRECIO",
               'ESTATUS')

    info_disp = ttk.Treeview(por_vender, columns=columna, show='headings')
    info_disp.column('CODIGO', width=75)
    info_disp.column('YEAR', width=75)
    info_disp.column('MARCA', width=300)
    info_disp.column('MODELO', width=300)
    info_disp.column('ESTATUS', width=75)
    info_disp.column('PRECIO', width=100)

    for col in columna:
        info_disp.heading(col, text=col)

    for data in dic_por_vender:
        info_disp.insert('', 'end', values=list(data.values()))

    # Configurar la altura para mostrar todas las filas
    # Utilizar len(data_vehiculo) + 1 para asegurarse de que se muestren todas las filas
    info_disp['height'] = len(no_vendidos) + 1
    info_disp.grid(sticky='nsew')

    # Configurar el peso de las filas y columnas para que se expandan con la ventana
    por_vender.grid_rowconfigure(0, weight=1)
    por_vender.grid_columnconfigure(0, weight=1)

    por_vender.mainloop()


def cantidad_vendidos():
    vendidos = Tk()
    vendidos.title("VEHICULOS VENDIDOS")
    vendidos.config(bg="light blue")
    dic_vendidos = []
    dic_no_vendidos = []
    with open(pag, 'r') as d:
        no_disponibles = d.readlines()

        for i in no_disponibles:
            dic_vendidos.append(ast.literal_eval(i))

        for i in dic_vendidos:
            if i['ESTATUS'] == 1:
                dic_no_vendidos.append(i)

    columnas_vendidos = ('CODIGO',
                         "MARCA",
                         "MODELO",
                         "YEAR",
                         "KILOMETRAJE ",
                         "PRECIO",
                         'ESTATUS')

    info_vend = ttk.Treeview(vendidos, columns=columnas_vendidos, show='headings')
    info_vend.column('CODIGO', width=75)
    info_vend.column('YEAR', width=75)
    info_vend.column('MARCA', width=300)
    info_vend.column('MODELO', width=300)
    info_vend.column('ESTATUS', width=75)
    info_vend.column('PRECIO', width=100)

    for col in columnas_vendidos:
        info_vend.heading(col, text=col)

    for data in dic_no_vendidos:
        info_vend.insert('', 'end', values=list(data.values()))

    # Configurar la altura para mostrar todas las filas
    # Utilizar len(data_vehiculo) + 1 para asegurarse de que se muestren todas las filas
    info_vend['height'] = len(dic_no_vendidos) + 1
    info_vend.grid(sticky='nsew')

    # Configurar el peso de las filas y columnas para que se expandan con la ventana
    vendidos.grid_rowconfigure(0, weight=1)
    vendidos.grid_columnconfigure(0, weight=1)
    vendidos.mainloop()


def carro_mas_vendido():
    lista_estatus = []
    dic_vendidos = []
    with open(pag, 'r') as m:
        vendidos = m.readlines()

        for i in vendidos:
            dic_vendidos.append(ast.literal_eval(i))

        for i in dic_vendidos:
            if i['ESTATUS'] == 1:
                lista_estatus.append(i)

        contCars = []
        cars = []
        for i in lista_estatus:
            i_copy = i.copy()
            i_copy.pop('CODIGO')
            if i_copy in cars:

                car_index = cars.index(i_copy)
                contCars[car_index]['CANTIDAD_VENTAS'] += 1
            else:
                cars.append(i_copy.copy())
                i_copy['CANTIDAD_VENTAS'] = 1
                contCars.append(i_copy)

        contCars = sorted(contCars, key=lambda x: x['CANTIDAD_VENTAS'], reverse=True)
    return contCars
