#importamos librerias y archivos 
import os
from tkinter import *
from tkinter import ttk
from Interfaces.busquedas_por_fecha import busqueda
from archivo.vehiculo_extraccion import carro_mas_vendido

#ubicamos la direccion de los archivos que vamos a revisar
direc_actual = os.path.dirname(__file__)
direc_padre = os.path.dirname(direc_actual)
URL = os.path.join(direc_padre, 'archivo_de_las_ventas.txt')

direc_precio = os.path.dirname(__file__)
direc_father = os.path.dirname(direc_precio)
URL_father = os.path.join(direc_father, 'archivo_de_los_vehiculos.txt')

#funcion que busca los mas vendidos
def mas_menos_vendido():

    #creamos la ventana
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

    #creamos la tabla
    vend_cantidad = ttk.Treeview(mas_vendido, columns=columnas, show='headings')

    #ordenamos encabezados
    for col in columnas:
        vend_cantidad.heading(col, text=col)

    #ingresamos la informacion
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

#funcion que busca por fechas
def fecha_vendido(ingreso):

    global valores_mostrados
    
    #llamamos a la funcion que busca los vehiculos vendidos en esa fecha
    data_busqueda = busqueda(ingreso)

    #creamos la ventana
    fechas_especificas = Tk()
    fechas_especificas.title('BUSQUEDAS POR FECHAS')
    fechas_especificas.config(bg='light blue')

    columnas = ('CODIGO',
                'MARCA',
                'MODELO',
                'YEAR',
                'KILOMETRAJE',
                'PRECIO',
                'ESTATUS')

    #creamos la tabla
    fechas_ordenado = ttk.Treeview(fechas_especificas, columns=columnas, show='headings')
    fechas_ordenado.column('CODIGO', width=75)
    fechas_ordenado.column('MARCA', width=75)
    fechas_ordenado.column('MODELO', width=80)
    fechas_ordenado.column('YEAR', width=70)
    fechas_ordenado.column('KILOMETRAJE', width=100)
    fechas_ordenado.column('PRECIO', width=100)

    #ordenamos encabezados
    for col in columnas:
        fechas_ordenado.heading(col, text=col)

    #ingresamos los datos
    for data in data_busqueda:
        fechas_ordenado.insert('', 'end', values=list(data.values()))

    #buscamos los precios de los carros de la fecha pedida y los sumamos
    total_ventas = sum(float(data_busqueda['PRECIO'].replace(',', '')) for data_busqueda in data_busqueda)

    #ordenamos los vehiculos de la fecha 
    fechas_ordenado.insert("", "end", values=["" for _ in columnas])  # Fila en blanco como separador
    
    #ubicamos el total de la venta a nivel de la casilla de precios y le colocamos el formato 999,999.99
    fechas_ordenado.insert("", "end", values=["TOTAL DE VENTAS", "", "", "", "", f"${total_ventas:.2f}",""])

    # Configurar la altura para mostrar todas las filas
    # Utilizar len(data_vehiculo) + 1 para asegurarse de que se muestren todas las filas
    fechas_ordenado['height'] = len(data_busqueda) + 1

    fechas_ordenado.grid(sticky='nsew')

    # Configurar el peso de las filas y columnas para que se expandan con la ventana
    fechas_especificas.grid_rowconfigure(0, weight=1)
    fechas_especificas.grid_columnconfigure(0, weight=1)

    fechas_especificas.mainloop()
