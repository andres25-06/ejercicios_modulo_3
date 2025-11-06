from ejercicios.Ejercicio3 import crear_contador

def test_contadores_independientes():
    """
    Verifica que cada contador sea independiente
    """

    contador1 = crear_contador()
    contador2 = crear_contador()

    assert contador1 () == 1
    assert contador1 () == 2
    assert contador2 () == 1
    assert contador1 () == 3
    assert contador2 () == 2

def test_incremento_correcto():
    """
    Verifica que el contador incremente correctamente
    """

    contador = crear_contador()
    resultados =[contador() for _ in range (5)]
    assert resultados == [1,2,3,4,5]

def test_tipo_retorno():
    """
    Verifica que la funciónretorne un entero
    """
    contador= crear_contador()
    valor = contador()
    assert isinstance(valor,int)