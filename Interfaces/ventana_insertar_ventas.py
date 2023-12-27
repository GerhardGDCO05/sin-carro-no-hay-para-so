import tkinter
from tkinter import *
from tkinter import messagebox

def ventana_insertar_ventas():
    insertventas = Tk()
    insertventas.title("REGISTRO DE LAS VENTAS")
    insertventas.config(bg="light blue")
    insertventas_label=Label(insertventas, text="DATOS DE LA VENTA", font=("times new roman", 12),
                  bg="light blue", justify="center")
    insertventas_label.pack()

    ventasframe=Frame(insertventas)
    ventasframe.pack()
    ventasframe.config(width=200,height=200)
#------------factura-----------------------------
    facturalabel = Label(ventasframe, text="FACTURA")
    facturalabel.grid(row=0, column=0, padx=10, pady=10)
    factura = Entry(ventasframe, background="light blue")
    factura.grid(row=0, column=1, padx=10, pady=10)
# -------------------------Fecha de LA COMPRA------------------------------
    fecha_compra_label = Label(ventasframe, text="FECHA DE" "\n""LA COMPRA")
    fecha_compra_label.grid(row=1, column=0, padx=12, pady=12)
    fecha_de_la_compra = Entry(ventasframe, background="light blue")
    fecha_de_la_compra.grid(row=1, column=1, padx=12, pady=12)
# ---------------------cedula del comprador-----------------------------------------
    cedula_del_comprador_label = Label(ventasframe, text="CEDULA DEL \n COMPRADOR")
    cedula_del_comprador_label.grid(row=2, column=0, padx=10, pady=10)
    cedula_del_comprador = Entry(ventasframe, background="light blue")
    cedula_del_comprador.grid(row=2, column=1, padx=10, pady=10)
#---------------------------cedula_del_comprador---------------------------
    codigo_del_vehiculo_label = Label(ventasframe, text="CODIGO DEL \n VEHICULO")
    codigo_del_vehiculo_label.grid(row=3, column=0, padx=10, pady=10)
    codigo_del_vehiculo = Entry(ventasframe, background="light blue")
    codigo_del_vehiculo.grid(row=3, column=1, padx=10, pady=10)
# ---------------------------MODELO DEL vehiculo---------------------------
    modelo_del_vehiculo_label=Label(ventasframe,text='MODELO DEL \n VEHICULO')
    modelo_del_vehiculo_label.grid(row=4,column=0,padx=10,pady=10)
    modelo_del_vehiculo=Entry(ventasframe,background='light blue')
    modelo_del_vehiculo.grid(row=4,column=1,padx=10,pady=10)
#---------------------------------------------------------------------------
    def validarData_ventas(factura,fecha_compra,cedula_comprador,codigo_comprador,modelo_vehiculo):
        pass

    botonsaveventas=Button(
        insertventas,
        text='GUARDAR',
        state=tkinter.DISABLED,
        command=lambda :validarData_ventas(factura.get(),
                                           fecha_de_la_compra.get(),
                                           cedula_del_comprador.get(),
                                           codigo_del_vehiculo.get(),
                                           modelo_del_vehiculo.get()
                                           )
    )
    botonsaveventas.pack()