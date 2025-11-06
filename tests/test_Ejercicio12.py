import pytest
from ejercicios.Ejercicio12 import analizar_csv


def test_analizar_csv_valores_correctos(tmp_path):
    # Crear un CSV temporal de prueba
    archivo_prueba = tmp_path / "estudiantes.csv"
    archivo_prueba.write_text(
        "nombre,edad,calificacion\n"
        "Ana,20,4.5\n"
        "Luis,22,3.8\n"
        "Marta,19,4.9\n"
        "Carlos,21,2.7\n"
    )

    # Ejecutar la función
    resultados = analizar_csv(str(archivo_prueba), "calificacion")

    # Comprobar resultados
    assert isinstance(resultados, dict)
    assert round(resultados["Promedio"], 2) == 3.98
    assert resultados["Máximo"] == 4.9
    assert resultados["Mínimo"] == 2.7


def test_analizar_csv_columna_invalida(tmp_path):
    archivo_prueba = tmp_path / "estudiantes.csv"
    archivo_prueba.write_text("nombre,edad,calificacion\nAna,20,4.5\nLuis,22,3.8\n")

    # Si la columna no existe, debe lanzar KeyError
    with pytest.raises(KeyError):
        analizar_csv(str(archivo_prueba), "nota")


def test_analizar_csv_columna_vacia(tmp_path):
    archivo_prueba = tmp_path / "estudiantes.csv"
    archivo_prueba.write_text("nombre,edad,nota\nAna,20,\nLuis,22,\n")

    # Si la columna está vacía, debe lanzar ValueError
    with pytest.raises(ValueError):
        analizar_csv(str(archivo_prueba), "nota")
