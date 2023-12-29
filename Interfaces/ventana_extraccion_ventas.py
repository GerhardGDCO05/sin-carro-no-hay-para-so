import tkinter as tk
from tkinter import ttk
from archivo.Ventas_extraccion import extracventas

Data_ventas = extracventas()


def ventana_extraccion_ventas():
    extraccion_ventas = tk.Tk()
    extraccion_ventas.title("INFORMACION DE LAS VENTAS")
    extraccion_ventas.resizable(0,0)
    columna = ("FACTURA",
               "FECHA DE LA COMPRA",
               "CEDULA DEL COMPRADOR",
               "CODIGO ",
               "MODELO")

    infoventas = ttk.Treeview(extraccion_ventas, columns=columna, show='headings')
    infoventas.column('MODELO',width=350)

    for col in columna:
        infoventas.heading(col, text=col)

    for data in Data_ventas:
        infoventas.insert('', 'end', values=list(data.values()))

    infoventas.grid()
    extraccion_ventas.mainloop()
