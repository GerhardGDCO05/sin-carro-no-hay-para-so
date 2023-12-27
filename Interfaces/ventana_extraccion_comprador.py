import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from archivo.compradores_extraccion import extractInfo

# Simulando la lista de diccionarios

compradoresData = extractInfo()


def ventana_extraccion_comprador():

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

        # Agregar datos
    for data in compradoresData:
        infocomp.insert('', 'end', values=list(data.values()))

    infocomp.grid()

    info_compradores.mainloop()
