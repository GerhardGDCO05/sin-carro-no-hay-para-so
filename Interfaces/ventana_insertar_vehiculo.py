from tkinter import messagebox
from tkinter import *

from archivo.Validaciones_vehiculo import validar_marca, validar_year, validar_modelo, validar_kilometraje, \
    validar_precio
from archivo.vehiculo_extraccion import generar_codigo_vehiculo
from archivo.vehiculo_insercion import insertvehiculos


def ventana_insertar_vehiculo():
    insert_vehi = Tk()
    insert_vehi.title("REGISTRO VEHICULO")
    insert_vehi.config(bg="light blue")
    insert_vehi_label = Label(insert_vehi, text='REGISTRO DE VEHICULOS',
                              font=("times new roman", 12), bg='light blue', justify='center')
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
    def validar_vehiculo(marca, modelo, year, kilometraje, precio):
        global estatus,codigo
        if validar_marca(marca) == False:
            messagebox.showerror('ERROR', 'ERROR EN MARCA \n MAXIMO EN 20 CARACTERES ')
            return False

        if validar_modelo(modelo) == False:
            messagebox.showerror('ERROR', 'ERROR EN EL MODELO \n MAXIMO EN 20 CARACTERES ')
            return False

        if validar_year(year) == False:
            messagebox.showerror('ERROR', 'ERROR EN EL AÑO DEL VEHICULO \n MAXIMO 4 DIGITOS')
            return False

        if validar_kilometraje(kilometraje) == False:
            messagebox.showerror('ERROR', 'ERROR EN EL KILOMETRAJE \n MAXIMO 6 DIGITOS')
            return False

        if validar_precio(precio) == False:
            messagebox.showerror('ERROR', 'ERROR EN EL PRECIO  ')
            return False
        else:
            formato_precio = '{:,.2f}'.format(float(precio))

        if (validar_marca(marca) == True and validar_modelo(modelo) == True
                and validar_year(year) == True
                and validar_kilometraje(kilometraje) == True
                and validar_precio(precio) == True):

            codigo=generar_codigo_vehiculo()

            estatus = 0


        insertvehiculos(codigo, marca, modelo, year, kilometraje, formato_precio, estatus)
        messagebox.showinfo('LOGRADO', 'INGRESO EXITOSO')
        insert_vehi.destroy()

    boton_vehiculo = Button(
        insert_vehi,
        text='GUARDAR',
        command=lambda: validar_vehiculo(marca.get(),
                                         modelo.get(),
                                         year.get(),
                                         kilometraje.get(), precio.get()
                                         ))
    boton_vehiculo.pack()

    insert_vehi.mainloop()
