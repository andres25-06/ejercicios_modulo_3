from typing import Callable
import re
from rich.table import Table
from rich.console import Console

def aplicar_validador(datos:list,validador:Callable[[object],bool])-> list:
    """
    Aplica la función de validación a cada elemento de una lista y devuelve
    una nueva lista con los elementos que cumplen la validación

    Args:
        datos(list): Lista de elementos a validar
        validador (Callable[[object],bool]): Función que recibe un elemento y
        devuelve True si es Válido o False si no lo es.
    Returns:
        list: Nueva lista con los elementos que pasaron la validación
    """

    datos_validos:list=[]

    for elemento in datos:
        if validador(elemento):
            datos_validos.append(elemento)

    return datos_validos

def email_valido(email:str) ->bool:
    """
    Verifica si un correo electrónico un formato válido

    Args:
        email(str):Dirección de correo electrónico a validar

    Returns:
        bool: True si el correo tiene un formato válido,False si no
    """

    patron=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool (re.match(patron,email))

def es_mayor_a_10(numero:int)->bool:

    """
    Comprueba si un número es mayor a 10

    Args:
        numero (int): Número que se va a validar

    Returns:
        bool:True si el número es mayor que 10,False si no
    """

    return numero>10

if __name__ == "__main__":

    console = Console()

    emails=["Tatiana@gmail.com","invalido@","otro@correo.com","test.com"]
    numeros =[5,12,3,20,10,25]

    emails_validos=aplicar_validador(emails,email_valido)
    numeros_validos=aplicar_validador(numeros,es_mayor_a_10)

    tabla=Table(title="Resultados de validación",show_lines=True)

    tabla.add_column("Tipo de Dato",style="bold cyan")
    tabla.add_column("Entrada",style="purple")
    tabla.add_column("Entrada",style="bold blue")


    tabla.add_row("Emails",str(emails),str(emails_validos))
    tabla.add_row("Números",str(numeros),str(numeros_validos))

    console.print(tabla)




