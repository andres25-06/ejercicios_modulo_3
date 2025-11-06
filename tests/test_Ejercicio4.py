from ejercicios.Ejercicio4 import aplicar_validador,es_mayor_a_10,email_valido

def test_email_valido():
    assert email_valido("test@gmail.com") is True
    assert email_valido("Correo_invalido") is False

def test_es_mayor_a_10():
    assert es_mayor_a_10(15) is True
    assert es_mayor_a_10(5) is False

def test_aplicar_validador_emails():
    datos=["tatis@gmail.com","otro.com"]
    resultado =aplicar_validador(datos,email_valido)
    assert resultado == ["tatis@gmail.com"]

def test_aplicar_validador_numeros():
    datos=[3,12,15,7]
    resultado=aplicar_validador(datos,es_mayor_a_10)
    assert resultado == [12,15]


