import ast
import os
from tkinter import *
from tkinter import ttk
from archivo.vehiculo_extraccion import carro_mas_vendido

direc_actual = os.path.dirname(__file__)
direc_padre = os.path.dirname(direc_actual)
URL = os.path.join(direc_padre, 'archivo_de_las_ventas.txt')

direc_pecio = os.path.dirname(__file__)
direc_father = os.path.dirname(direc_pecio)
URL_father = os.path.join(direc_father, 'archivo_de_los_vehiculos.txt')


def mas_menos_vendido():
    mas_vendido = Tk()
    mas_vendido.title('ORGANIZACION DE LAS VENTAS')
    mas_vendido.config(bg='light blue')
    data_mas_vendido = carro_mas_vendido()

    columnas = ("MARCA",
                "MODELO",
                "YEAR",
                "KILOMETRAJE ",
                "PRECIO",
                'ESTATUS',
                'CANTIDAD_VENTAS')

    vend_cantidad = ttk.Treeview(mas_vendido, columns=columnas, show='headings')

    for col in columnas:
        vend_cantidad.heading(col, text=col)

    for data in data_mas_vendido:
        vend_cantidad.insert('', 'end', values=list(data.values()))

    # Configurar la altura para mostrar todas las filas
    # Utilizar len(data_vehiculo) + 1 para asegurarse de que se muestren todas las filas
    vend_cantidad['height'] = len(data_mas_vendido) + 1
    vend_cantidad.grid(sticky='nsew')

    # Configurar el peso de las filas y columnas para que se expandan con la ventana
    mas_vendido.grid_rowconfigure(0, weight=1)
    mas_vendido.grid_columnconfigure(0, weight=1)
    mas_vendido.mainloop()


def fecha_vendido(ingreso):
    # Inicializar listas para almacenar datos
    dic_busqueda_fecha = []
    dic_precio = []
    di_fechas = []
    dic_union = []

    keys_a_eliminar_ventas = ['FACTURA', 'CEDULA DEL COMPRADOR', 'CODIGO', 'MODELO']
    keys_a_eliminar_vehiculos = ['ESTATUS', 'KILOMETRAJE']
    # Leer datos del primer archivo (URL)
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
            for j in di_fechas:
                if i['CODIGO'] == j['CODIGO']:
                    for k in keys_a_eliminar_ventas:
                        di_fechas.pop(k)

                    for n in keys_a_eliminar_vehiculos:
                        dic_precio.pop(n)

                    union_diccionarios = {**di_fechas, **dic_precio}
    print(union_diccionarios)
