from ejercicios.Ejercicio7 import filtrar_aprobados


def test_filtrar_aprobados_basico():
    """
    Verifica que la función correctamente a los estudiantes con nota >=3.0
    """
    estudiantes =[("Ana",4.5),("Juan",1,.5),("Tatiana",5.0)]
    resultado =filtrar_aprobados(estudiantes)
    assert resultado==[("Ana",4.5),("Tatiana",5.0)]

def test_filtrar_aprobados_todos_aprueban():
    """
    Caso donde todos los estudiantes aprueban
    """
    estudiantes=[("Pedro", 3.0), ("Laura", 4.0), ("Andrés", 5.0)]
    resultado =filtrar_aprobados(estudiantes)
    assert len(resultado) == 3
    assert all(nota >=3.0 for _,nota in resultado)

def test_filtrar_aprobados_nadie_aprueba():
    """
    Donde ningún estudiantes aprueba
    """

    estudiantes=[("Juan",1,.5),("Camilo",2.9),("Martha",1.9)]
    resultado =filtrar_aprobados(estudiantes)
    assert resultado ==[]

def test_filtrar_aprobados_lista_vacia():
    """
    Verifica que una lista vacía retorna una lista vacpia
    """

    estudiantes=[]
    resultado =filtrar_aprobados(estudiantes)
    assert resultado==[]
