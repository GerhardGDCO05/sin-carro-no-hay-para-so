import tkinter as tk
from tkinter import ttk
from archivo.vehiculo_extraccion import extrac_vehiculo

data_vehiculo = extrac_vehiculo()


def ventana_extraccion_vehiculo():
    extraccion_vehiculo = tk.Tk()
    extraccion_vehiculo.title("INFORMACION DE LOS VEHICULOS")
    columna = ('CODIGO',"MARCA",
               "MODELO",
               "YEAR",
               "KILOMETRAJE ",
               "PRECIO",'ESTATUS')

    info_vehiculo = ttk.Treeview(extraccion_vehiculo, columns=columna, show='headings')

    for col in columna:
        info_vehiculo.heading(col, text=col)

    info_vehiculo.grid()
    extraccion_vehiculo.mainloop()
