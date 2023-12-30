import tkinter as tk
from tkinter import ttk
from archivo.vehiculo_extraccion import extrac_vehiculo

data_vehiculo = extrac_vehiculo()


def ventana_extraccion_vehiculo():
    extraccion_vehiculo = tk.Tk()
    extraccion_vehiculo.title("INFORMACION DE LOS VEHICULOS")
    extraccion_vehiculo.resizable(0,0)
    columna = ('CODIGO',
               "MARCA",
               "MODELO",
               "YEAR",
               "KILOMETRAJE ",
               "PRECIO",
               'ESTATUS')

    info_vehiculo = ttk.Treeview(extraccion_vehiculo, columns=columna, show='headings')
    info_vehiculo.column('CODIGO',width=75)
    info_vehiculo.column('YEAR',width=75)
    info_vehiculo.column('MARCA', width=300)
    info_vehiculo.column('MODELO', width=300)
    info_vehiculo.column('ESTATUS', width=75)
    info_vehiculo.column('PRECIO', width=100)


    for col in columna:
        info_vehiculo.heading(col, text=col)

    for data in data_vehiculo:
        info_vehiculo.insert('', 'end', values=list(data.values()))

    info_vehiculo.grid()
    extraccion_vehiculo.mainloop()
