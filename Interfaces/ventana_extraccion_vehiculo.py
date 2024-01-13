#importaciones de librerias y archivos
import tkinter as tk
from tkinter import ttk
from archivo.vehiculo_extraccion import extrac_vehiculo



#funcion que extrae la informacion
def ventana_extraccion_vehiculo():
    #creamos la ventana con la tabla de informacion
    data_vehiculo = extrac_vehiculo()
    extraccion_vehiculo = tk.Tk()
    extraccion_vehiculo.title("INFORMACION DE LOS VEHICULOS")
    columna = ('CODIGO',
               "MARCA",
               "MODELO",
               "YEAR",
               "KILOMETRAJE ",
               "PRECIO",
               'ESTATUS')

    #creamos la tabla
    info_vehiculo = ttk.Treeview(extraccion_vehiculo, columns=columna, show='headings')
    info_vehiculo.column('CODIGO',width=75)
    info_vehiculo.column('YEAR',width=75)
    info_vehiculo.column('MARCA', width=300)
    info_vehiculo.column('MODELO', width=300)
    info_vehiculo.column('ESTATUS', width=75)
    info_vehiculo.column('PRECIO', width=100)

    #ordenamos los encabezados
    for col in columna:
        info_vehiculo.heading(col, text=col)

    #ingresamos la informacion
    for data in data_vehiculo:
        info_vehiculo.insert('', 'end', values=list(data.values()))

    # Configurar la altura para mostrar todas las filas
    # Utilizar len(data_vehiculo) + 1 para asegurarse de que se muestren todas las filas
    info_vehiculo['height']=len(data_vehiculo)+1

    info_vehiculo.grid(sticky="nsew")

    # Configurar el peso de las filas y columnas para que se expandan con la ventana
    extraccion_vehiculo.grid_rowconfigure(0, weight=1)
    extraccion_vehiculo.grid_columnconfigure(0, weight=1)

    info_vehiculo.grid()
    extraccion_vehiculo.mainloop()
