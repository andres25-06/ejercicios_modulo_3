from ejercicios.Ejercicio8 import contar_longitud_palabras, filtrar_palabras_largas


def test_filtrar_palabras_largas():
    texto="Hola me llamo Tatiana y estoy programando en Python"
    resultado=filtrar_palabras_largas(texto)
    assert "TATIANA" in resultado
    assert all(len(palabra) > 5 for palabra in resultado)

def test_contar_longitud_palabras():
    palabras=["PYTHON","PROGRAMACION"]
    resultado=contar_longitud_palabras(palabras)
    assert resultado ["PYTHON"] == 6
    assert resultado ["PROGRAMACION"] == 12
