from tkinter import Tk, Frame, Button

from Interfaces.ventana_Insertar_Comprador import ventana_insertar_comprador


def registroCompradores():
    registroCompradores = Tk()
    registroCompradores.title('COMPRADORES')
    registroCompradores.config(background='red')
    registroCompradores.pack()

    registro_comp_frame = Frame(registroCompradores)
    registro_comp_frame.pack()
    registro_comp_frame.place(x=100, y=100)

    def boton_registro_comp():
        ventana_insertar_comprador()

    registroComprador = Button(registroCompradores, text="REGISTRO", command=boton_registro_comp)
    registroComprador.pack()

    registroCompradores.mainloop()
