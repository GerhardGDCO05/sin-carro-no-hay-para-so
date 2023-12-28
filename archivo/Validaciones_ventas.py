def validarfactura(factura):
    if len(factura) > 5 and len(factura) == 0:
        return False
    return True


def validarfechacompra(fecha_compra):
    if len(fecha_compra) > 8 and len(fecha_compra) == 0:
        return False
    return True


def validarcedulacomprador(cedula_comprador):
    if len(cedula_comprador) > 8 and len(cedula_comprador) == 0:
        return False
    return True


def validarcodigo(codigo_comprador):
    if len(codigo_comprador) > 3 and len(codigo_comprador) == 0:
        return False
    return True


def validarmodelo(modelo_vehiculo):
    if len(modelo_vehiculo) > 20 and len(modelo_vehiculo) == 0:
        return False
    return True
