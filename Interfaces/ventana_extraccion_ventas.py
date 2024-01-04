import tkinter as tk
from tkinter import ttk

from Interfaces.ventana_mas_vendido import fecha_vendido
from archivo.Ventas_extraccion import extracventas
from tkinter import *

Data_ventas = extracventas()


def ventana_extraccion_ventas():
    extraccion_ventas = tk.Tk()
    extraccion_ventas.title("INFORMACION DE LAS VENTAS")
    columna = ("FACTURA",
               "FECHA DE LA COMPRA",
               "CEDULA DEL COMPRADOR",
               "CODIGO ",
               "MODELO")

    infoventas = ttk.Treeview(extraccion_ventas, columns=columna, show='headings')
    infoventas.column('MODELO', width=350)

    for col in columna:
        infoventas.heading(col, text=col)

    for data in Data_ventas:
        infoventas.insert('', 'end', values=list(data.values()))

    # Configurar la altura para mostrar todas las filas
    # Utilizar len(data_vehiculo) + 1 para asegurarse de que se muestren todas las filas
    infoventas['height'] = len(Data_ventas) + 1
    infoventas.grid(sticky='nsew')

    # Configurar el peso de las filas y columnas para que se expandan con la ventana
    extraccion_ventas.grid_rowconfigure(0, weight=1)
    extraccion_ventas.grid_columnconfigure(0, weight=1)

    infoventas.grid()
    extraccion_ventas.mainloop()


def extraccion_por_fecha():
    fecha = Tk()
    fecha.title('BUSQUEDA POR FECHA')
    fecha_Label = Label(fecha, text='VENTAS POR FECHA',
                        font=("times new roman", 12), bg="light blue", justify="center")
    fecha_Label.pack()

    fecha_frame = Frame(fecha)
    fecha_frame.pack()
    fecha_frame.config(width=200, height=200)

    igresar_fecha = Label(fecha_frame, text='InGRESE LA FECHA')
    igresar_fecha.grid(row=0, column=0, padx=10, pady=10)
    ingreso = Entry(fecha_frame, bg='light blue')
    ingreso.grid(row=0, column=1, padx=10, pady=10)

    busqueda_fecha = Button(fecha, text='BUSCAR', command=lambda: fecha_vendido(ingreso.get()))
    busqueda_fecha.pack()
