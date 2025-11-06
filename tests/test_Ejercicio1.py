import pytest

from ejercicios.Ejercicio1 import calcular_imc, interpretar_imc


def test_calcular_imc_correcto():
    """
    Verifica que el IMC se calcule correctamente
    """
    resultado = calcular_imc(70,1.75)
    assert round (resultado,2) == 22.86

def test_calcular_imc_estatura_invalida():
    """
    Verifica que se lance un error su la estatura es cero o negativa
    """
    with pytest.raises(ValueError):
        calcular_imc(70,0)
def test_interpretar_imc_bajo():

    assert interpretar_imc(17.0) == "Bajo peso"
def test_interpretar_imc_normal():
    assert interpretar_imc(22.0) == "Normal"

def test_interpretar_imc_sobrepeso():
    assert interpretar_imc(27.5) == "Sobrepeso"

def test_interpretar_imc_obesidad():
    assert interpretar_imc(31.5) == "Obesidad"
