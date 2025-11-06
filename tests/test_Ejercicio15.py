import json
import pytest
from ejercicios.Ejercicio15 import (
    cargar_biblioteca,
    guardar_biblioteca,
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
)


@pytest.fixture
def biblioteca_temp(tmp_path):
    ruta = tmp_path / "biblioteca.json"
    libros = [
        {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
        {"libro_id": "002", "titulo": "El Principito", "prestado_a": "Ana"},
        {"libro_id": "003", "titulo": "Don Quijote", "prestado_a": None},
    ]
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4)
    return ruta


def test_cargar_y_guardar_biblioteca(biblioteca_temp):
    biblioteca = cargar_biblioteca(biblioteca_temp)
    assert len(biblioteca) == 3
    biblioteca[0]["titulo"] = "Nuevo Título"
    guardar_biblioteca(biblioteca_temp, biblioteca)
    nueva = cargar_biblioteca(biblioteca_temp)
    assert nueva[0]["titulo"] == "Nuevo Título"


def test_prestar_libro_disponible(biblioteca_temp):
    biblioteca = cargar_biblioteca(biblioteca_temp)
    assert prestar_libro(biblioteca, "003", "Carlos") is True
    assert biblioteca[2]["prestado_a"] == "Carlos"


def test_prestar_libro_no_disponible(biblioteca_temp):
    biblioteca = cargar_biblioteca(biblioteca_temp)
    assert prestar_libro(biblioteca, "002", "Pedro") is False


def test_devolver_libro(biblioteca_temp):
    biblioteca = cargar_biblioteca(biblioteca_temp)
    assert devolver_libro(biblioteca, "002") is True
    assert biblioteca[1]["prestado_a"] is None


def test_buscar_libro(capsys, biblioteca_temp):
    biblioteca = cargar_biblioteca(biblioteca_temp)
    resultados = buscar_libro(biblioteca, "Cien")
    salida = capsys.readouterr().out
    assert len(resultados) == 1
    assert "Cien Años de Soledad" in salida


def test_ver_libros_prestados(capsys, biblioteca_temp):
    biblioteca = cargar_biblioteca(biblioteca_temp)
    prestados = ver_libros_prestados(biblioteca)
    salida = capsys.readouterr().out
    assert len(prestados) == 1
    assert "El Principito" in salida
