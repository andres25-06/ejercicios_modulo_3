from ejercicios.Ejercicio2 import crear_perfil

def test_crear_perfil_condatos():
    """
    Verifia que la función funcione correctamente con todos los datos
    """
    resultado=crear_perfil(
        "Tatiana",
        25,
        "Cocinar","Dormir",
        facebook="@tattys",
        instagram="@tattys"
    )

    assert "Tatiana" in resultado
    assert "Cocinar" in resultado
    assert "Dormir" in resultado

def test_crear_perfil_sindatos():
    """
    Verifica el comportamiento cuando no se ingresan hobbies ni redes
    """
    resultado=crear_perfil("Laura",30 )
    assert "No especificados" in resultado
    assert "No registradas" in resultado




