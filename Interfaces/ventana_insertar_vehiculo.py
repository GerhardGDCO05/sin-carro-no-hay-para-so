from tkinter import messagebox
from tkinter import *


def ventana_insertar_vehiculo():
    insert_vehi = Tk()
    insert_vehi.title("REGISTRO VEHICULO")
    insert_vehi.config(bg="light blue")
    insert_vehi_label = Label(insert_vehi, text='REGISTRO DE VEHICULOS',
                              font=("times new roman", 12),bg='light blue', justify='center')
    insert_vehi_label.pack()

    vehiculo = Frame(insert_vehi)
    vehiculo.pack()
    vehiculo.config(width=200, height=200)
    # ---------------marca-----------------------------
    marcalabel = Label(vehiculo, text='MARCA DEL VEHICULO')
    marcalabel.grid(row=0, column=0, padx=10, pady=10)
    marca = Entry(vehiculo, background='light blue')
    marca.grid(row=0, column=1, padx=10, pady=10)
    # --------------------modelo--------------------
    modelo_label = Label(vehiculo, text='MODELO DEL VEHICULO')
    modelo_label.grid(row=1, column=0, padx=10, pady=10)
    modelo = Entry(vehiculo, background='light blue')
    modelo.grid(row=1, column=1, padx=10, pady=10)
    # -----------------YEAR----------------------------
    year_label = Label(vehiculo, text='AÑO DEL VEHICULO')
    year_label.grid(row=2, column=0, padx=10, pady=10)
    year = Entry(vehiculo, background='light blue')
    year.grid(row=2, column=1, padx=10, pady=10)
    # ----------- kilometraje--------------------------
    kilometraje_label = Label(vehiculo, text='KILOMETRAJE')
    kilometraje_label.grid(row=3, column=0, padx=10, pady=10)
    kilometraje = Entry(vehiculo, background='light blue')
    kilometraje.grid(row=3, column=1, padx=10, pady=10)
    # ---------------------precio de venta------------------------
    precio_label = Label(vehiculo, text='PRECIO DEL VEHICULO')
    precio_label.grid(row=4, column=0, padx=10, pady=10)
    precio = Entry(vehiculo, background='light blue')
    precio.grid(row=4, column=1, padx=10, pady=10)

    # -------------------------------------------------------------
    def validar_vehiculo(marca,modelo,year,kilometraje,precio):
        pass

    boton_vehiculo = Button(
        insert_vehi,
        text='GUARDAR',
        command=lambda: validar_vehiculo(marca.get(),modelo.get(),year.get(),kilometraje.get(),precio.get())
    )
    boton_vehiculo.pack()

    insert_vehi.mainloop()
