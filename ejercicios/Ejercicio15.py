import json
from typing import Dict, List

from rich.console import Console
from rich.table import Table

console = Console()


# === Funciones de Persistencia ===
def cargar_biblioteca(ruta_archivo: str) -> List[Dict]:
    """
    Carga los datos de la biblioteca desde un archivo JSON.

    Args:
        ruta_archivo (str): Ruta del archivo JSON.
    Returns:
        list[dict]: Lista de libros.
    """
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_biblioteca(ruta_archivo: str, biblioteca: List[Dict]) -> None:
    """
    Guarda el estado actual de la biblioteca en el archivo JSON.

    Args:
        ruta_archivo (str): Ruta del archivo JSON.
        biblioteca (list[dict]): Lista de libros actualizada.
    """
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(biblioteca, f, indent=4, ensure_ascii=False)


# === Funciones Principales ===
def prestar_libro(biblioteca: List[Dict], libro_id: str, nombre_aprendiz: str) -> bool:
    """
    Marca un libro como prestado si está disponible.

    Args:
        biblioteca (list[dict]): Lista de libros.
        libro_id (str): ID del libro.
        nombre_aprendiz (str): Nombre del aprendiz que lo toma prestado.

    Returns:
        bool: True si se prestó correctamente, False si no está disponible.
    """
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is None:
                libro["prestado_a"] = nombre_aprendiz
                return True
            else:
                return False
    return False


def devolver_libro(biblioteca: List[Dict], libro_id: str) -> bool:
    """
    Marca un libro como devuelto (prestado_a = None).

    Args:
        biblioteca (list[dict]): Lista de libros.
        libro_id (str): ID del libro.

    Returns:
        bool: True si se devolvió, False si no se encontró.
    """
    for libro in biblioteca:
        if libro["libro_id"] == libro_id:
            libro["prestado_a"] = None
            return True
    return False


def buscar_libro(biblioteca: List[Dict], query: str) -> List[Dict]:
    """
    Busca libros por coincidencia parcial en el título.

    Args:
        biblioteca (list[dict]): Lista de libros.
        query (str): Texto a buscar.

    Returns:
        list[dict]: Libros encontrados.
    """
    resultados = [
        libro for libro in biblioteca if query.lower() in libro["titulo"].lower()
    ]

    table = Table(title=f"Resultados de búsqueda para '{query}'")
    table.add_column("ID", justify="center")
    table.add_column("Título", justify="left")
    table.add_column("Prestado a", justify="center")

    for libro in resultados:
        table.add_row(
            libro["libro_id"], libro["titulo"], libro["prestado_a"] or "Disponible"
        )

    console.print(table)
    return resultados


def ver_libros_prestados(biblioteca: List[Dict]) -> List[Dict]:
    """
    Muestra los libros actualmente prestados.

    Args:
        biblioteca (list[dict]): Lista de libros.

    Returns:
        list[dict]: Libros prestados.
    """
    prestados = [libro for libro in biblioteca if libro["prestado_a"]]

    table = Table(title=" Libros Prestados")
    table.add_column("ID", justify="center")
    table.add_column("Título", justify="left")
    table.add_column("Prestado a", justify="center")

    for libro in prestados:
        table.add_row(libro["libro_id"], libro["titulo"], libro["prestado_a"])

    console.print(table)
    return prestados


# === Menú Principal ===
def menu_biblioteca(ruta_archivo: str) -> None:
    """
    Menú interactivo de la biblioteca.
    """
    biblioteca = cargar_biblioteca(ruta_archivo)

    while True:
        console.print("\n [bold cyan]Menú de Biblioteca[/bold cyan]")
        console.print("1. Prestar libro")
        console.print("2. Devolver libro")
        console.print("3. Buscar libro")
        console.print("4. Ver libros prestados")
        console.print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro_id = input("ID del libro: ")
            nombre = input("Nombre del aprendiz: ")
            if prestar_libro(biblioteca, libro_id, nombre):
                console.print("[green] Libro prestado correctamente.[/green]")
            else:
                console.print("[red] No se pudo prestar el libro.[/red]")

        elif opcion == "2":
            libro_id = input("ID del libro a devolver: ")
            if devolver_libro(biblioteca, libro_id):
                console.print("[green] Libro devuelto correctamente.[/green]")
            else:
                console.print("[red] Libro no encontrado.[/red]")

        elif opcion == "3":
            query = input("Ingrese título o parte del título: ")
            buscar_libro(biblioteca, query)

        elif opcion == "4":
            ver_libros_prestados(biblioteca)

        elif opcion == "5":
            guardar_biblioteca(ruta_archivo, biblioteca)
            console.print("[yellow] Cambios guardados. Saliendo...[/yellow]")
            break

        else:
            console.print("[red] Opción inválida.[/red]")
