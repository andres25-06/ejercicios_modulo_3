from typing import Any, Union

from rich.console import Console
from rich.tree import Tree

console=Console()

def explorar_estructura(elemento:Any,profundidad:int=1,arbol:Union[Tree,None]=None)->None:
    """
    Explora recursivamente estructuras de datos aninadas (listas,diccionarios,tuplas...

    Args:
        elemento (Any): Estructura o valor a explorar
        profundidad(int,opcional): Nivel actual de profundidad. Por defecto 1
        arbol (Tree | none,opcional): Estructura visual de árbol para mostrar en consola
    """

    if arbol is None:
        arbol =Tree("[bold magenta] Exploración recursiva [/bold magenta]")

    if isinstance(elemento,dict):
        rama = arbol.add(f"[cyan] Diccianario nivel  {profundidad}) [/cyan] ")
        for clave,valor in elemento.items():
            rama_hija=rama.add(f"[yellow] {clave}[/yellow]->[white]{type(valor).__name__}[/white]")
            explorar_estructura(valor,profundidad +1, rama_hija)

    elif isinstance(elemento,(list,tuple,set)):
        rama=arbol.add(f"[green] Secuencia nivel {profundidad}[/green] ")
        for i,item in enumerate(elemento,start=1):
            rama_hija=rama.add(f"[purple] Elemento {i}[/purple]")
            explorar_estructura(item,profundidad +1,rama_hija)

    else:
        arbol.add(
            f"[white] Valor: [bold] {elemento}[/bold], Profundidad: [bold cyan] {profundidad}[/bold cyan]"
        )

    if profundidad == 1:
        console.print(arbol)

if __name__ == "__main__":
    console.print("[bold green] Explorador de Estructuras ✨ [/bold green]\n")

    estructura =[1,[2,3],{"a":4,"b":[5,{"c":6}]}]

    console.print(f"[bold yellow]  Estructura a explorar: [/bold yellow]{estructura}")
    console.print("\n[bold cyan] Resultado: [/bold cyan]\n")

    explorar_estructura(estructura)
