from ejercicios.Ejercicio9 import sumar_lista,concatenar_texto
import pytest
def test_sumar_lista_valores_positivos():
    """
    suma de una lista de enteros positivos
    """

    numeros=[1,2,3,4,5]
    resultado=sumar_lista(numeros)
    assert resultado == 15

def test_sumar_lista_incluye_negativos():
    """
    Verifica que la función maneja números negativos correctamente.
    """
    numeros = [10, -5, 3]
    resultado = sumar_lista(numeros)
    assert resultado == 8

def test_sumar_lista_unico_elemento():
    """
    lista con un solo número.
    """
    numeros = [7]
    resultado = sumar_lista(numeros)
    assert resultado == 7


def test_concatenar_texto_basico():
    """
    concatenación de palabras.
    """
    partes = ["Hola", " ", "SENA", "!"]
    resultado = concatenar_texto(partes)
    assert resultado == "Hola SENA!"


