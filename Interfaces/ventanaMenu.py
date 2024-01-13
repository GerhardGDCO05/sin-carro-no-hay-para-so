#importamos los archivos que vamos a nesecitar
from Interfaces.ventana_Insertar_Comprador import *
from Interfaces.ventana_extraccion_comprador import *
from Interfaces.ventana_insertar_vehiculo import *
from Interfaces.ventana_extraccion_vehiculo import *
from Interfaces.ventana_insertar_ventas import *
from Interfaces.ventana_extraccion_ventas import *
from Interfaces.top_ventas import mas_menos_vendido
from archivo.vehiculo_extraccion import cantidad_por_vender, cantidad_vendidos

#funcion del menu principal
def ventana_Menu():
    #interfaz principal
    concesionario = Tk()
    concesionario.title("SIN CARRO NO HAY PARAISO")
    concesionario.config(bg="light blue", relief="groove", bd="20")
    concelabel = Label(concesionario, text="CONCESIONARIO SIN CARRO NO HAY PARAISO",
                       font=("times new roman", 12), bg="light blue", justify="center")
    concelabel.pack()
    

    #frame principal
    miframe = Frame(concesionario)
    miframe.pack(fill=BOTH, expand=True)
    miframe.config(bg="turquoise")
    

    # --------------------------BOTON DE LOS COMPRADORES--------------------
    #frame del boton
    compraframe = Frame(miframe)
    compraframe.pack()
    compraframe.place(x=260, y=350)

    #llamda a la funcion del boton
    def botoncomp():
        #llamamos a la funcion del submenu de los compradores
        seleccionCompradores()
        
    #creamos el boton
    botonComprador = Button(compraframe, text="COMPRADOR", command=botoncomp)
    botonComprador.pack()

    # -----------------------------------------------------------------------------
    #funcion del submenu compradores
    def seleccionCompradores():
        #submenu compradores
        Compradores = Tk()
        Compradores.title('COMPRADORES')
        Compradores.config(bg='light blue', )
        Compradores.resizable(height=0, width=0)
        Compradores.geometry('300x200')
        compradores_label = Label(Compradores, text="SECCION DE CLIENTES", font=("times new roman", 12),
                                  bg="light blue", justify="center")
        compradores_label.pack()

    # -------------------boton REGISTRO compradores---------------------------------
        # frame del boton del registro de los compradores
        registro_comp_frame = Frame(Compradores)
        registro_comp_frame.pack()
        registro_comp_frame.place(x=120, y=50)

        # funcion que llama a lapestaña de registro
        def boton_registro_comp(): 
            
            ventana_insertar_comprador() 
     
        #  creamos el boton de registro        
        regisComprador = Button(registro_comp_frame, text="REGISTRO", command=boton_registro_comp)
        regisComprador.pack()

    # -------------------boton infocompradores---------------------------------
        #frame del boton de informacion de los compradores
        informacion_comp_frame = Frame(Compradores)
        informacion_comp_frame.pack()
        informacion_comp_frame.place(x=60, y=100)

        #funcion que llama a la funcion de extraccion de informacion
        def botoninfcomp():
            ventana_extraccion_comprador()

        #boton de la informacion
        boton_inf_comprador = Button(informacion_comp_frame, text="INFORMACION COMPRADORES", command=botoninfcomp)
        boton_inf_comprador.pack()

        Compradores.mainloop()

    # -----------------------BOTON DE LOS VEHICULOS---------------------------
    #frame del boton de vehiculos
    vehiframe = Frame(miframe)
    vehiframe.pack()
    vehiframe.place(x=700, y=350)

    #funcion que llama a la funcion que crea el submenu de vehiculos
    def botonveh():

        #funcion que crea el submenu
        seleccionVehiculos()

    #boton de vehiculos
    botonvehiculo = Button(vehiframe, text="VEHICULO", command=botonveh)
    botonvehiculo.pack()

    # -----------------------------------------------------------------------------------
    
    #funcion del submenu de vehiculos
    def seleccionVehiculos():
        #creamos la ventana del submenu de vehiculos
        vehiculo = Tk()
        vehiculo.title('VEHICULOS')
        vehiculo.config(bg='light blue', )
        vehiculo.resizable(height=0, width=0)
        vehiculo.geometry('300x300')
        vehiculo_label = Label(vehiculo, text="SECCION VEHICULOS", font=("times new roman", 12),
                               bg="light blue", justify="center")
        vehiculo_label.pack()

    # -------------------------boton REGISTRO vehiculos-----------------------------
        #frame del boton de registro
        registro_veh_frame = Frame(vehiculo)
        registro_veh_frame.pack()
        registro_veh_frame.place(x=120, y=60)
        
        #funcion que llama al registro
        def boton_registro_veh():

            #funcion que crea la ventana de registro
            ventana_insertar_vehiculo()

        #creamos el boton de registro
        registroveh = Button(registro_veh_frame, text="REGISTRO", command=boton_registro_veh)
        registroveh.pack()

    # -------------------boton infovehiculo---------------------------------
        #frame del boton de informacion
        infvehiframe = Frame(vehiculo)
        infvehiframe.pack()
        infvehiframe.place(x=60, y=120)
       
        #funcion que llama a la tabla de informacion
        def botoninfveh():

            #funcion que crea la tabla
            ventana_extraccion_vehiculo()
        
        #creamos el boton de informacion
        boton_inf_vehiculo = Button(infvehiframe, text="INFORMACION DE LOS VEHICULOS", command=botoninfveh)
        boton_inf_vehiculo.pack()

    # -------------------boton disponibles--------------------------
        
        #frame del boton de vehiculos disponibles 
        dispovehiculo = Frame(vehiculo)
        dispovehiculo.pack()
        dispovehiculo.place(x=80, y=180)
        
        #llamada a la funcion que crea la tabla de vehiculos disponibles
        def boton_disponibles():

            #funcion que crea la tabla de disponibles
            cantidad_por_vender()

        #creamos el boton
        botonvendidos = Button(dispovehiculo, text='VEHICULOS DISPONIBLES', command=boton_disponibles)
        botonvendidos.pack()

    # ----------------boton vendidos--------------------------------------------
        #frame del boton de los vendidos
        vehiculos_vendidos = Frame(vehiculo)
        vehiculos_vendidos.pack()
        vehiculos_vendidos.place(x=85, y=240)

        #llamada a la funcion que crea la tabla de vendidos
        def boton_vendidos():

            #funcion que crea la tabla de vendidos
            cantidad_vendidos()

        #boton de vendidos
        botonvendidos = Button(vehiculos_vendidos, text='VEHICULOS VENDIDOS', command=boton_vendidos)
        botonvendidos.pack()
        vehiculo.mainloop()

    # ----------------BOTON DE LAS VENTAS-------------------------------------
    #frame del boton de ventas
    ventasframe = Frame(miframe)
    ventasframe.pack()
    ventasframe.place(x=1175, y=350)

    #llamada a la funcion que crea al submenu
    def botonventas():
        #funcion que crea el submenu de ventas
        seleccionventas()

    #boton de ventas
    botonventas = Button(ventasframe, text="VENTAS", command=botonventas)
    botonventas.pack()

    # ------------------------------------------------------------------
    #submenu de ventas
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
        #frame del boton de registro
        registro_ventas_frame = Frame(ventas)
        registro_ventas_frame.pack()
        registro_ventas_frame.place(x=120, y=60)

        #llamada a la funcion que crea la ventana de registro
        def boton_registo_ventas():
            
            #ventana de registro
            ventana_insertar_ventas()

        #boton de registro
        boton_registro_ventas = Button(registro_ventas_frame, text="REGISTRO", command=boton_registo_ventas)
        boton_registro_ventas.pack()
    # --------------------boton infventas---------------------------------
        #frame de el boton de informacion de ventas
        infventasframe = Frame(ventas)
        infventasframe.pack()
        infventasframe.place(x=60, y=120)

        #llamada a la tabla de informacion
        def boton_info_ventas():

            #creamos la tabla
            ventana_extraccion_ventas()

        #boton de informacion
        boton_info_ventas = Button(infventasframe, text="INFORMACION DE LAS VENTAS", command=boton_info_ventas)
        boton_info_ventas.pack()

    # -----------------------boton mas vendidos------------------
        #frame del boton de mayor venta
        fecha_mas_vendida = Frame(ventas)
        fecha_mas_vendida.pack()
        fecha_mas_vendida.place(x=80, y=180)

        #llamada a la tabla
        def boton_mas_vendido():

            #creamos la tabla
            mas_menos_vendido()

        #boton de mayor venta
        mas_vendido = Button(fecha_mas_vendida, text='MAYOR Y MENOR VENTA', command=boton_mas_vendido)
        mas_vendido.pack()

    #------------------- fecha especifica-------------
        #frame del boton ventas por fecha 
        fecha_mas_vendida = Frame(ventas)
        fecha_mas_vendida.pack()
        fecha_mas_vendida.place(x=95, y=240)

        #llamada a la tabla
        def fecha_especifica():
            #creamos la tabla
            extraccion_por_fecha()

        #boton de ventas por fecha
        por_fecha = Button(fecha_mas_vendida, text='VENTAS POR FECHA', command=fecha_especifica)
        por_fecha.pack()

    concesionario.mainloop()
