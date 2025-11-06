from functools import reduce
from turtledemo.chaos import jumpto
from typing import List
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

console = Console()

def sumar_lista(numeros:list[int])->int:
    """
    Calcula la suma de una lista de números usando reduce

    Args:
        numeros (List[in]): Lista de números a sumar

    Returns:
        int: Resultadode la suma total
    """
    return reduce(lambda a, b: a + b, numeros)

def concatenar_texto(partes:List[str])->str:

    """
    Concatena los elementos de una lista de strings en una sola frase

    Args:
        partes (List[str]): Lista de fragmentos de texto

    Returns:
        str: Frase completa resultante
    """

    return reduce(lambda a, b: a + b, partes)

def mostrar_resultados(numeros:List[int],partes:List[str])->None:

    """
    Muestra los resultados 
    
    Args:
        numeros(List[int]): Lista de numeros a sumar
        partes (List[str]): Lista de fragmentos de texto a concatenar
    """

    suma_total=sumar_lista(numeros)
    frase_final=concatenar_texto(partes)

    tabla=Table(
        title="  Resultados de operaciones con reduce()",
        title_style="bold white on magenta",
        header_style="bold magenta",
        border_style="bright_blue"
    )

    tabla.add_column("Operación",style="cyan",justify="center")
    tabla.add_column("Resultado",style="yellow",justify="center")

    tabla.add_row(" Sumatoria",str(suma_total))
    tabla.add_row(" Concatenación",frase_final)

    console.print(tabla)

def main()->None:
    """
    Función principal que ejecuta el flujo completp del programa
    """

    console.print(
        Panel.fit(
            Text(" Reduce en acción ✨",style="bold white on purple"),
            border_style="bright_magenta",
            title=" Programa funcional",
        )
    )

    numeros=[1,2,3,4,5]

    partes=["Hola", " ","SENA","!"]

    mostrar_resultados(numeros,partes)

if __name__ == "__main__":
    main()
