from ejercicios.Ejercicio6 import aplicar_descuento


def test_aplicar_descuento_correcto():
    """
    Verifica que el descuento del 10% se aplique correctamente aun producto.
    """

    productos=[{"nombre":"camisa","precio":100}]
    resultado=aplicar_descuento(productos)
    assert resultado==[90.0]

def test_aplicar_descuento_Lista_vacia():
    """
    Verifica que devuelva una lista vacía si no hay productos
    """

    productos=[]
    resultado=aplicar_descuento(productos)
    assert resultado==[]

def test_aplicar_descuento_multiples_productos():
    """
    Verifica que funcione correctamnete con varios productos
    """

    productos=[
        {"nombre":"Blusa","precio":100},
        {"nombre":"Medias","precio":200},
        {"nombre":"Corbata","precio":300},
    ]

    resultado=aplicar_descuento(productos)
    assert resultado == [90.0,180.0,270.0]
