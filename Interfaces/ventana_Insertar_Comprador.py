import tkinter
from tkinter import *
from tkinter import messagebox

from archivo.Validaciones_compradores import (validarcedula, validarcarnet,
                                              validarpasaporte, validarnombre,
                                              validarfecha, validardireccion, validarestado,
                                              validarRif)
from archivo.compradores_insercion import *


def ventana_insertar_comprador():
    def verificar_contenido(*args):
        address = direccion.get('1.0', 'end-1c')
        name = nombre.get('1.0', 'end-1c')
        cedu = cedula.get()
        numrif = rif.get()
        cardip = CD.get()
        passport = pasaporte.get()
        fechanaci = fecha.get()
        stade = estado.get('1.0', 'end-1c')
        if (address.strip() != '' and address.strip() != ' '
                and name.strip() != '' and name.strip() != ' '
                and cedu.strip() != '' and cedu.strip() != ' '
                and numrif.strip() != '' and numrif.strip() != ' '
                and cardip.strip() != '' and cardip.strip() != ' '
                and passport.strip() != '' and passport.strip() != ' '
                and fechanaci.strip() != '' and fechanaci.strip() != ' '
                and stade.strip() != '' and stade.strip() != ' '):

            botoncomprador.config(state=tkinter.NORMAL)
        else:
            botoncomprador.config(state=tkinter.DISABLED)

    datos_comprador = Tk()
    datos_comprador.title("REGISTRO DE LOS COMPRADORES")
    datos_comprador.config(bg="light blue", relief="groove", bd="20")
    label = Label(datos_comprador, text="DATOS DEL COMPRADOR", font=("times new roman", 12),
                  bg="light blue", justify="center")
    label.pack()

    datosframe = Frame(datos_comprador)
    datosframe.pack()
    datosframe.config(width=200, height=200)

    # ---------------------cedula-----------------------------------------
    cedulalabel = Label(datosframe, text="CEDULA")
    cedulalabel.grid(row=0, column=0, padx=10, pady=10)
    cedula = Entry(datosframe, background="light blue")
    cedula.grid(row=0, column=1, padx=10, pady=10)
    cedula.bind('<<Modified>>', verificar_contenido)
    # -------------------rif---------------------------------------------
    riflabel = Label(datosframe, text="RIF")
    riflabel.grid(row=1, column=0, padx=12, pady=12)
    rif = Entry(datosframe, background="light blue")
    rif.grid(row=1, column=1, padx=12, pady=12)
    rif.bind('<<Modified>>', verificar_contenido)
    # -------------------carnet diplomatico----------------
    CDlabel = Label(datosframe, text="CARNET" "\n""DIPLOMATICO")
    CDlabel.grid(row=2, column=0)
    CD = Entry(datosframe, background="light blue")
    CD.grid(row=2, column=1)
    CD.bind('<<Modified>>', verificar_contenido)
    # ----------------------PASAPORTE--------------------------------------------
    pasaportelabel = Label(datosframe, text="PASAPORTE", )
    pasaportelabel.grid(row=3, column=0, padx=12, pady=12)
    pasaporte = Entry(datosframe, background="light blue")
    pasaporte.grid(row=3, column=1, padx=12, pady=12)
    pasaporte.bind('<<Modified>>', verificar_contenido)
    # -------------------------NOMBRE---------------------------------------------
    nombrelabel = Label(datosframe, text="NOMBRE" "\n""Y""\n" "APELLIDO", )
    nombrelabel.grid(row=4, column=0, padx=12, pady=12)
    nombre = Text(datosframe, background="light blue", width=16, height=3)
    nombre.grid(row=4, column=1, padx=12, pady=12)
    nombre.bind('<<Modified>>', verificar_contenido)

    scroll = Scrollbar(datosframe, command=nombre.yview)
    scroll.grid(row=4, column=2, sticky="nsew")
    nombre.config(yscrollcommand=scroll.set)
    # -------------------------Fecha de nacimiento------------------------------
    fechalabel = Label(datosframe, text="FECHA DE" "\n""NACIMIENTO")
    fechalabel.grid(row=5, column=0, padx=12, pady=12)
    fecha = Entry(datosframe, background="light blue")
    fecha.grid(row=5, column=1, padx=12, pady=12)
    fecha.bind('<<Modified>>', verificar_contenido)
    # -------------------------DIRECCION-----------------------------------
    direccionlabel = Label(datosframe, text="DIRECCION")
    direccionlabel.grid(row=6, column=0, padx=12, pady=12)
    direccion = Text(datosframe, background="light blue", width=16, height=3)
    direccion.bind('<<Modified>>', verificar_contenido)
    direccion.grid(row=6, column=1, padx=12, pady=12)

    scroll = Scrollbar(datosframe, command=direccion.yview)
    scroll.grid(row=6, column=2, sticky="nsew")
    direccion.config(yscrollcommand=scroll.set)
    # -------------------------estado-----------------------------------
    estadolabel = Label(datosframe, text="ESTADO")
    estadolabel.grid(row=7, column=0, padx=12, pady=12)
    estado = Text(datosframe, background="light blue", width=16, height=3)
    estado.grid(row=7, column=1, padx=12, pady=12)
    estado.bind('<<Modified>>', verificar_contenido)

    scroll = Scrollbar(datosframe, command=estado.yview)
    scroll.grid(row=7, column=2, sticky="nsew")
    estado.config(yscrollcommand=scroll.set)

    # ---------------------------------------------------------------------

    def validarData(cedula, rif, carnet, pasaporte, nombre_apellido, nacimiento, direccion, estado):

        if validarcedula(cedula) == False:
            messagebox.showerror('ERROR', 'ERROR EN CEDULA')
            return False
        elif len(cedula) < 8 and len(cedula) != 0:
            while len(cedula) != 8:
                cedula = "0" + cedula

        if (validarRif(rif) == False):
            messagebox.showerror('ERROR', 'ERROR EN RIF')
            return False

        if (validarcarnet(carnet) == False):
            messagebox.showerror('ERROR', 'ERROR EN CARNET DIPLOMATICO')
            return False

        if (validarpasaporte(pasaporte) == False):
            messagebox.showerror('ERROR', 'ERROR EN PASAPORTE')
            return False

        if (validarnombre(nombre_apellido) == False):
            messagebox.showerror('ERROR', 'ERROR EN NOMBRE Y APELLIDO \n MAXIMO 50 CARACTERES')
            return False

        if (validarfecha(nacimiento) == False):
            messagebox.showerror('ERROR', 'ERROR EN FECHA DE NACIMIENTO \n'
                                          'INGRESE LA FECHA DE NACIMIENTO EN ESTE FORMATO DDMMYYYY')
            return False
        elif len(nacimiento) < 8 and len(nacimiento) != 0:
            while len(nacimiento) != 8:
                nacimiento = "0" + nacimiento

        if validardireccion(direccion) == False:
            messagebox.showerror('ERROR', 'ERROR EN DIRECCION \n MAXIMO 50 CARACTERES')
            return False

        if validarestado(estado) == False:
            messagebox.showerror('ERROR', 'ERROR EN ESTADO \n MAXIMO 15 CARACTERES')
            return False

        insertData(cedula, rif, carnet, pasaporte,
                   nombre_apellido, nacimiento, direccion, estado)
        messagebox.showinfo('LOGRADO', 'REGISTRO EXITOSO')
        datos_comprador.destroy()

    botoncomprador = Button(
        datos_comprador,
        text="GUARDAR",
        state=tkinter.DISABLED,
        command=lambda: validarData(cedula.get(),
                                    rif.get(), CD.get(), pasaporte.get(),
                                    nombre.get('1.0', 'end-1c'),
                                    fecha.get(), direccion.get('1.0', 'end-1c'),
                                    estado.get('1.0', 'end-1c')))
    botoncomprador.pack()

    datos_comprador.mainloop()
