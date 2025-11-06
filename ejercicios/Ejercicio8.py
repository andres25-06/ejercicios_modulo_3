from typing import List,Dict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

def filtrar_palabras_largas(texto:str)->List[str]:
    """
    Genera una lista de palabras del texto que tengan mas de 5 letras
    y las conviette a mayúsculas

    Args:
        texto (str): Texto que se recibe para analizar

    Returns:
        List[str]:Lista de palabras en mayúsculas con una longitud >5
    """

    return [palabra.upper () for palabra in texto.split() if len(palabra)>5]

def contar_longitud_palabras(palabras:List[str])->Dict[str,int]:
    """
    Crea un diccionario donde cada palabra es la clave y su longitud el valor

    Args:
        palabras(List[str]):Lista de palabras en Mayúsculas

    Returns:
        Dict[str,int]:Diccionario con las palabras y su longitud
    """
    return {palabra: len(palabra)for palabra in palabras}

def mostrar_tabla(diccionario:Dict[str,int])->None:

    """
    Muestra los resultados

    Args:
        diccionario(Dict[str,int]):Diccionario con las palabras y su longitud

    Returns:
        None
    """

    console=Console()

    tabla=Table(
        title="  Longitud de palabras mayúsculas y largas",
        style="bright_cyan",
        border_style="magenta"
    )

    tabla.add_column("Palabra",justify="center",style="bold yellow")
    tabla.add_column("Longitud",justify="center",style="bold green")


    for palabra,longitud in diccionario.items():
        tabla.add_row(palabra,str(longitud))

    console.print(tabla)
console=Console()

def main ()->None:

    """
    Funcion principal que ejecuta el flujo completo dele programa
    """

    console.print(
        Panel.fit(
            Text("  Transformación de Datos ",style="bold white on pink"),
            border_style="bright_magenta",
            title="✨ Procesamiento de Texto ✨"
        )
    )

    texto=console.input("[bold purple]✍️  Ingrese un Texto: [/bold purple]")


    palabras_filtradas=filtrar_palabras_largas(texto)
    longitudes=contar_longitud_palabras(palabras_filtradas)


    console.print("\n [bold cyan] Resultados [/bold cyan]\n")
    mostrar_tabla(longitudes)

if __name__=="__main__":
    main()
