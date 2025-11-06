import json
import pytest
import os
from ejercicios.Ejercicio13 import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
)


# === FIXTURE GENERAL ===
@pytest.fixture
def archivo_temp(tmp_path, monkeypatch):
    """Crea un archivo JSON temporal para pruebas."""
    ruta = tmp_path / "inventario.json"
    monkeypatch.setattr(
        "Ejercicio13_GestorInventarioPersistente.RUTA_ARCHIVO", str(ruta)
    )
    return ruta


# === TESTS DE CARGA Y GUARDADO ===
def test_cargar_inventario_vacio(archivo_temp):
    """Debe retornar lista vacía si el archivo no existe."""
    assert cargar_inventario() == []


def test_cargar_inventario_datos(archivo_temp):
    """Debe leer correctamente los datos guardados en JSON."""
    datos = [{"nombre": "Martillo", "cantidad": 5, "precio": 12000}]
    with open(archivo_temp, "w", encoding="utf-8") as f:
        json.dump(datos, f)
    assert cargar_inventario() == datos


def test_guardar_inventario(archivo_temp):
    """Debe guardar los datos correctamente en el archivo JSON."""
    inventario = [{"nombre": "Taladro", "cantidad": 3, "precio": 85000}]
    guardar_inventario(inventario)

    with open(archivo_temp, "r", encoding="utf-8") as f:
        datos = json.load(f)

    assert datos == inventario


# === TESTS DE AGREGAR PRODUCTO ===
def test_agregar_producto_nuevo(archivo_temp):
    """Debe agregar un producto nuevo al inventario."""
    inventario = []
    agregar_producto(inventario, "Cemento", 10, 25000)

    with open(archivo_temp, "r", encoding="utf-8") as f:
        datos = json.load(f)

    assert len(datos) == 1
    assert datos[0]["nombre"] == "Cemento"
    assert datos[0]["cantidad"] == 10
    assert datos[0]["precio"] == 25000


def test_agregar_producto_existente_actualiza(archivo_temp):
    """Debe actualizar cantidad y precio si el producto ya existe."""
    inventario = [{"nombre": "Clavos", "cantidad": 5, "precio": 1000}]
    guardar_inventario(inventario)

    agregar_producto(inventario, "Clavos", 3, 1200)

    with open(archivo_temp, "r", encoding="utf-8") as f:
        datos = json.load(f)

    assert datos[0]["cantidad"] == 8
    assert datos[0]["precio"] == 1200


# === TESTS DE VENTA DE PRODUCTO ===
def test_vender_producto_valido(archivo_temp):
    """Debe descontar cantidad cuando hay suficiente stock."""
    inventario = [{"nombre": "Tubo PVC", "cantidad": 10, "precio": 5000}]
    guardar_inventario(inventario)

    vender_producto(inventario, "Tubo PVC", 3)

    with open(archivo_temp, "r", encoding="utf-8") as f:
        datos = json.load(f)

    assert datos[0]["cantidad"] == 7


def test_vender_producto_insuficiente(archivo_temp, capsys):
    """Debe mostrar mensaje si no hay suficiente stock."""
    inventario = [{"nombre": "Arena", "cantidad": 2, "precio": 15000}]
    guardar_inventario(inventario)

    vender_producto(inventario, "Arena", 5)
    capturado = capsys.readouterr().out

    assert "No hay suficiente stock" in capturado
    with open(archivo_temp, "r", encoding="utf-8") as f:
        datos = json.load(f)
    assert datos[0]["cantidad"] == 2  # No cambia


def test_vender_producto_inexistente(archivo_temp, capsys):
    """Debe mostrar mensaje si el producto no existe."""
    inventario = [{"nombre": "Ladrillo", "cantidad": 50, "precio": 500}]
    guardar_inventario(inventario)

    vender_producto(inventario, "Pintura", 1)
    capturado = capsys.readouterr().out

    assert "no existe" in capturado.lower()


# === TEST EXTRA DE VENTA EXACTA ===
def test_vender_producto_cantidad_exacta(archivo_temp):
    """Debe dejar cantidad 0 si se vende todo el stock."""
    inventario = [{"nombre": "Cable", "cantidad": 4, "precio": 2500}]
    guardar_inventario(inventario)

    vender_producto(inventario, "Cable", 4)

    with open(archivo_temp, "r", encoding="utf-8") as f:
        datos = json.load(f)

    assert datos[0]["cantidad"] == 0
