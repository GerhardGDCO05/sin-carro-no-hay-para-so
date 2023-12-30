def validar_marca(marca):
    if len(marca) > 20 or len(marca) == 0:
        return False
    return True


def validar_modelo(modelo):
    if len(modelo) > 20 or len(modelo) == 0:
        return False
    return True


def validar_year(year):
    if len(year) > 4 or len(year) == 0 or year.isnumeric == False:
        return False
    return True


def validar_kilometraje(kilometraje):
    if len(kilometraje) > 6 or len(kilometraje) == 0 or kilometraje.isnumeric == False:
        return False
    return True


def validar_precio(precio):
    if len(precio) == 0 or precio.isnumeric == False:
        return False
    return True
