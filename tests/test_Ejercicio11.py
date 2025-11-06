import os

import pytest

from ejercicios.Ejercicio11 import agregar_tarea, archivo_tareas, ver_tareas


@pytest.fixture(autouse=True)
def limpiar_archivo():
    """
    Fixture que limpia o elimina el archivo tareas.txt antes y después de cada prueba.
    """
    if os.path.exists(archivo_tareas):
        os.remove(archivo_tareas)
    yield
    if os.path.exists(archivo_tareas):
        os.remove(archivo_tareas)

def test_agregar_tarea_crea_archivo_y_guarda_contenido():
    """
    Prueba que al agregar una tarea se cree el archivo y se guarde correctamente.
    """
    tarea = "Hacer ejercicios"
    agregar_tarea(tarea)

    assert os.path.exists(archivo_tareas), "El archivo de tareas no se creó."

    tareas = ver_tareas()
    assert tarea in tareas, "La tarea no se guardó correctamente."


def test_ver_tareas_devuelve_lista_correcta():
    """
    Prueba que ver_tareas devuelva una lista con todas las tareas.
    """
    tareas_prueba = ["Comprar pan", "Estudiar Python"]
    for tarea in tareas_prueba:
        agregar_tarea(tarea)

    tareas = ver_tareas()
    assert tareas == tareas_prueba, "Las tareas leídas no coinciden con las esperadas."


def test_ver_tareas_con_archivo_vacio():
    """
    Prueba que si el archivo está vacío, se devuelva una lista vacía.
    """
    open(archivo_tareas, "w").close()  # Crear archivo vacío
    tareas = ver_tareas()
    assert tareas == [], "Debería devolver una lista vacía si no hay tareas."


