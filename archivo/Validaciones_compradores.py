#condicional de para validar la cedula
def validarcedula(cedula):
    if (len(cedula) > 8 or len(cedula) == 0) or cedula.isnumeric() == False:
        return False
    return True

#condicional de para validar el rif
def validarRif(rif):
    if (len(rif) > 9 or len(rif) < 9) or rif.isnumeric() == False:
        return False
    return True

#condicional de para validar el carnet
def validarcarnet(carnet):
    if (len(carnet) > 9 or len(carnet) < 9) or carnet.isnumeric() == False:
        return False
    return True

#condicional de para validar el pasaporte
def validarpasaporte(pasaporte):
    if (len(pasaporte) > 9 or len(pasaporte) < 9) or pasaporte.isnumeric() == False:
        return False
    return True

#condicional de para validar el nombre
def validarnombre(nombre_apellido):
    if (len(nombre_apellido) > 50 or len(nombre_apellido) == 0):
        return False
    return True

#condicional de para validar la fecha de nacimiento
def validarfecha(nacimiento):
    if (len(nacimiento) > 8 or len(nacimiento) == 0):
        return False
    return True

#condicional de para validar la direccion
def validardireccion(direccion):
    if (len(direccion) > 50 or len(direccion) == 0):
        return False
    return True

#condicional de para validar el estado
def validarestado(estado):
    if (len(estado) > 15 or len(estado) == 0):
        return False
    return True
