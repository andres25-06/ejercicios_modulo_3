from ejercicios.Ejercicio5 import actualizar_tasa_iva, calcular_iva


def test_caculo_inicial():
    """
    Verifica que el cálculo de IVA inical (19%) sea correcto
    """

    precio=100.0
    resultado =calcular_iva(precio)
    assert round(resultado,2) == 19.0

def test_actualizar_tasa():
    actualizar_tasa_iva(0.25)
    precio=100.0
    resultado=calcular_iva(precio)
    assert round (resultado,2) ==25.0
