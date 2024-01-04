from Interfaces.ventana_Insertar_Comprador import *
from Interfaces.ventana_extraccion_comprador import *
from Interfaces.ventana_insertar_vehiculo import *
from Interfaces.ventana_extraccion_vehiculo import *
from Interfaces.ventana_insertar_ventas import *
from Interfaces.ventana_extraccion_ventas import *
from Interfaces.top_ventas import mas_menos_vendido
from archivo.vehiculo_extraccion import cantidad_por_vender, cantidad_vendidos


def ventana_Menu():
    concesionario = Tk()
    concesionario.title("SIN CARRO NO HAY PARAISO")
    concesionario.config(bg="light blue", relief="groove", bd="20")
    concelabel = Label(concesionario, text="CONCESIONARIO SIN CARRO NO HAY PARAISO",
                       font=("times new roman", 12), bg="light blue", justify="center")
    concelabel.pack()

    miframe = Frame(concesionario)
    miframe.pack()
    miframe.config(width=1300, height=600, bg="turquoise")
    miframe.place(x=10, y=50)

    # --------------------------BOTON DE LOS COMPRADORES--------------------
    compraframe = Frame(miframe)
    compraframe.pack()
    compraframe.place(x=100, y=300)

    def botoncomp():
        seleccionCompradores()

    botonComprador = Button(compraframe, text="COMPRADOR", command=botoncomp)
    botonComprador.pack()

    # -----------------------------------------------------------------------------

    def seleccionCompradores():
        Compradores = Tk()
        Compradores.title('COMPRADORES')
        Compradores.config(bg='light blue', )
        Compradores.resizable(height=0, width=0)
        Compradores.geometry('300x200')
        compradores_label = Label(Compradores, text="SECCION DE CLIENTES", font=("times new roman", 12),
                                  bg="light blue", justify="center")
        compradores_label.pack()

        # -------------------boton REGISTRO compradores---------------------------------
        registro_comp_frame = Frame(Compradores)
        registro_comp_frame.pack()
        registro_comp_frame.place(x=120, y=50)

        def boton_registro_comp():
            ventana_insertar_comprador()

        regisComprador = Button(registro_comp_frame, text="REGISTRO", command=boton_registro_comp)
        regisComprador.pack()

        # -------------------boton infocompradores---------------------------------
        informacion_comp_frame = Frame(Compradores)
        informacion_comp_frame.pack()
        informacion_comp_frame.place(x=60, y=100)

        def botoninfcomp():
            ventana_extraccion_comprador()

        boton_inf_comprador = Button(informacion_comp_frame, text="INFORMACION COMPRADORES", command=botoninfcomp)
        boton_inf_comprador.pack()

        Compradores.mainloop()

    # -----------------------BOTON DE LOS VEHICULOS---------------------------
    vehiframe = Frame(miframe)
    vehiframe.pack()
    vehiframe.place(x=650, y=300)

    def botonveh():
        seleccionVehiculos()

    botonvehiculo = Button(vehiframe, text="VEHICULO", command=botonveh)
    botonvehiculo.pack()

    # -----------------------------------------------------------------------------------
    def seleccionVehiculos():
        vehiculo = Tk()
        vehiculo.title('VEHICULOS')
        vehiculo.config(bg='light blue', )
        vehiculo.resizable(height=0, width=0)
        vehiculo.geometry('300x300')
        vehiculo_label = Label(vehiculo, text="SECCION VEHICULOS", font=("times new roman", 12),
                               bg="light blue", justify="center")
        vehiculo_label.pack()

        # -------------------------boton REGISTRO vehiculos-----------------------------
        registro_veh_frame = Frame(vehiculo)
        registro_veh_frame.pack()
        registro_veh_frame.place(x=120, y=60)

        def boton_registro_veh():
            ventana_insertar_vehiculo()

        registroveh = Button(registro_veh_frame, text="REGISTRO", command=boton_registro_veh)
        registroveh.pack()

        # -------------------boton infovehiculo---------------------------------
        infvehiframe = Frame(vehiculo)
        infvehiframe.pack()
        infvehiframe.place(x=60, y=120)

        def botoninfveh():
            ventana_extraccion_vehiculo()

        boton_inf_vehiculo = Button(infvehiframe, text="INFORMACION DE LOS VEHICULOS", command=botoninfveh)
        boton_inf_vehiculo.pack()

        # -------------------boton disponibles--------------------------
        dispovehiculo = Frame(vehiculo)
        dispovehiculo.pack()
        dispovehiculo.place(x=80, y=180)

        def boton_disponibles():
            cantidad_por_vender()

        botonvendidos = Button(dispovehiculo, text='VEHICULOS DISPONIBLES', command=boton_disponibles)
        botonvendidos.pack()

        # ----------------boton vendidos--------------------------------------------
        vehiculos_vendidos = Frame(vehiculo)
        vehiculos_vendidos.pack()
        vehiculos_vendidos.place(x=85, y=240)

        def boton_vendidos():
            cantidad_vendidos()

        botonvendidos = Button(vehiculos_vendidos, text='VEHICULOS VENDIDOS', command=boton_vendidos)
        botonvendidos.pack()
        vehiculo.mainloop()

    # ----------------BOTON DE LAS VENTAS-------------------------------------
    ventasframe = Frame(miframe)
    ventasframe.pack()
    ventasframe.place(x=1175, y=300)

    def botonventas():
        seleccionventas()

    botonventas = Button(ventasframe, text="VENTAS", command=botonventas)
    botonventas.pack()

    # ------------------------------------------------------------------
    def seleccionventas():
        ventas = Tk()
        ventas.title('VENTAS')
        ventas.config(bg='light blue', )
        ventas.resizable(height=0, width=0)
        ventas.geometry('300x300')
        ventas_label = Label(ventas, text="SECCION DE VENTAS", font=("times new roman", 12),
                             bg="light blue", justify="center")
        ventas_label.pack()

        # -------------------boton REGISTRO ventas---------------------------------
        registro_ventas_frame = Frame(ventas)
        registro_ventas_frame.pack()
        registro_ventas_frame.place(x=120, y=60)

        def boton_registo_ventas():
            ventana_insertar_ventas()

        boton_registro_ventas = Button(registro_ventas_frame, text="REGISTRO", command=boton_registo_ventas)
        boton_registro_ventas.pack()
        # --------------------boton infventas---------------------------------
        infventasframe = Frame(ventas)
        infventasframe.pack()
        infventasframe.place(x=60, y=120)

        def boton_info_ventas():
            ventana_extraccion_ventas()

        boton_info_ventas = Button(infventasframe, text="INFORMACION DE LAS VENTAS", command=boton_info_ventas)
        boton_info_ventas.pack()

        # -----------------------boton mas vendidos------------------
        fecha_mas_vendida = Frame(ventas)
        fecha_mas_vendida.pack()
        fecha_mas_vendida.place(x=80, y=180)

        def boton_mas_vendido():
            mas_menos_vendido()

        mas_vendido = Button(fecha_mas_vendida, text='MAYOR Y MENOR VENTA', command=boton_mas_vendido)
        mas_vendido.pack()

        #------------------- fecha especifica-------------
        fecha_mas_vendida = Frame(ventas)
        fecha_mas_vendida.pack()
        fecha_mas_vendida.place(x=95, y=240)

        def fecha_especifica():
            extraccion_por_fecha()

        por_fecha = Button(fecha_mas_vendida, text='VENTAS POR FECHA', command=fecha_especifica)
        por_fecha.pack()

    concesionario.mainloop()
