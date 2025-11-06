import pytest

from ejercicios.Ejercicio10 import explorar_estructura


def test_explorar_lista_simple(capsys: pytest.CaptureFixture) -> None:
    """
    Prueba una lista simple con elementos anidados.
    Args:
        capsys (pytest.CaptureFixture): Captura la salida impresa en consola.
    """
    estructura = [1, [2, 3]]
    explorar_estructura(estructura)
    salida = capsys.readouterr().out

    # Verifica que se imprimen los valores esperados
    assert "1" in salida
    assert "2" in salida
    assert "3" in salida
    assert "Profundidad" in salida


def test_explorar_valor_simple(capsys: pytest.CaptureFixture) -> None:
    """
    cuando el valor no es una estructura iterable.
    """
    estructura = 42
    explorar_estructura(estructura)
    salida = capsys.readouterr().out

    assert "Valor" in salida
    assert "42" in salida
    assert "Profundidad" in salida
