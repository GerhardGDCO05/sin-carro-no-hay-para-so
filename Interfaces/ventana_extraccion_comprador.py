#importamos librerias y archivos
import tkinter as tk
from tkinter import ttk
from archivo.compradores_extraccion import extractInfo



#funcion que crea la tabla y ordena la informacion en la tabla
def ventana_extraccion_comprador():
    #llamamos a la funcion que extrae la informacion
    compradoresData = extractInfo()

    #creamos la ventana
    info_compradores = tk.Tk()
    info_compradores.title("Información de Clientes")

    # Encabezados
    columns = ('CEDULA',
               'RIF',
               'CARNET DIPLOMATICO',
               'PASAPORTE',
               'NOMBRE',
               'FECHA DE NACIMIENTO',
               'DIRECCION',
               'ESTADO')
    

    #creamos la tabla 
    infocomp = ttk.Treeview(info_compradores, columns=columns, show='headings')
    infocomp.column('CEDULA', width=75)
    infocomp.column('RIF', width=75)
    infocomp.column('CARNET DIPLOMATICO', width=140)
    infocomp.column('PASAPORTE', width=80)
    infocomp.column('NOMBRE', width=300)
    infocomp.column('FECHA DE NACIMIENTO', width=150)
    infocomp.column('DIRECCION', width=350)
    infocomp.column('ESTADO', width=200)

    # Establecer encabezados
    for col in columns:
        infocomp.heading(col, text=col)

    # Agregamos datos
    for data in compradoresData:
        infocomp.insert('', 'end', values=list(data.values()))

    # Configurar la altura para mostrar todas las filas

    infocomp['height'] = len(compradoresData) + 1

    infocomp.grid(sticky='nsew')

    # Configurar el peso de las filas y columnas para que se expandan con la ventana
    info_compradores.grid_rowconfigure(0, weight=1)
    info_compradores.grid_columnconfigure(0, weight=1)

    info_compradores.mainloop()
