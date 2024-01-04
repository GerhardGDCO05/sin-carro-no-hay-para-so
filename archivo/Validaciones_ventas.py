def validarfactura(factura):
    if len(factura) > 5 or len(factura) == 0 or factura.isnumeric() == False:
        return False
    return True


def validarfechacompra(fecha_compra):
    if len(fecha_compra) > 8 or len(fecha_compra) == 0 or fecha_compra.isnumeric() == False:
        return False
    return True


def validarcedulacomprador(cedula_comprador):
    if len(cedula_comprador) > 8 or len(cedula_comprador) == 0 or cedula_comprador.isnumeric()== False:
        return False
    return True


def validarcodigo(codigo_comprador):
    if len(codigo_comprador) != 3 or codigo_comprador.isnumeric()== False:
        return False
    return True


def validarmodelo(modelo_vehiculo):
    if len(modelo_vehiculo) > 20 or len(modelo_vehiculo) == 0:
        return False
    return True
