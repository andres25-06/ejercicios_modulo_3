from typing import Callable

from rich.console import Console
from rich.table import Table


def crear_contador () -> Callable [[],int]:
    """
    Crea un contador  independiente que recuarda cuantas veces ha sido llamado

    Returns:
        Callable [[],int]: una función interna que incrementa y devuelve el conteo actual
    """

    conteo=0

    def incrementar()->int:
        """
        Incrementa el valor del contador de 1 y lo devuelve.

        Returns:
            int:El número actual del contador despues de incrementar.
        """
        nonlocal conteo #modifica la variable "conteo" que esta en el ambito externo
        conteo+=1
        return conteo

    return incrementar

def mostrar_contadores(resultados:dict[str,list[int]]) ->None:
    """
    Muestra los resultados de varios contadores en la tabla

    Args:
        resultados(dict[str,list[int]]):
        diccionario donde las claves son los nombres de los contadores y los valores
        son listas con los resultados de las llamadas de cada contador
    """
    console=Console()


    tabla=Table(
        title="  Resultados de Contadores",
        header_style="bold magenta",
        show_header=True,
    )

    tabla.add_column("Contador",style="cyan",justify="center")
    tabla.add_column("Llamadas Realizadas",style="white")

    for nombre,valores in resultados.items():
        valores_texto=", ".join(map(str,valores))
        tabla.add_row(nombre,valores_texto)

    console.print(tabla)

if __name__ == "__main__":

    console=Console()

    console.print("[bold green]✨ Demostración de contadores  ✨ [/bold green]\n")

    contador_a=crear_contador()
    contador_b=crear_contador()

    resultados={
        "Contador A":[contador_a(),contador_a(),contador_a()],
        "Contador B":[contador_b(),contador_b()],
        "Contador A (otra vez)":[contador_a()],
    }

    mostrar_contadores(resultados)





