import json
import os

from rich.console import Console
from rich.table import Table

RUTA_ARCHIVO = "inventario.json"
console = Console()


def cargar_inventario():
    """
    Carga el inventario desde el archivo JSON especificado en RUTA_ARCHIVO.

    Returns:
        list[dict]: Una lista de diccionarios que representan los productos
        del inventario. Cada diccionario contiene las claves:
        - "nombre" (str): nombre del producto
        - "cantidad" (int): cantidad disponible
        - "precio" (float): precio por unidad

    Si el archivo no existe o está dañado, devuelve una lista vacía.
    """
    if os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                console.print(
                    "[red]Error:[/red] El archivo JSON está dañado. "
                    "Se iniciará un inventario vacío."
                )
                return []
    else:
        return []


def guardar_inventario(inventario):
    """
    Guarda el inventario actual en el archivo JSON especificado.

    Args:
        inventario (list[dict]): Lista de productos a guardar. Cada producto
        debe contener las claves "nombre", "cantidad" y "precio".

    Este proceso sobrescribe completamente el archivo JSON existente.
    """
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)


def agregar_producto(inventario, nombre, cantidad, precio):
    """
    Agrega un producto nuevo o actualiza su cantidad y precio si ya existe.

    Args:
        inventario (list[dict]): Lista actual del inventario.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad a agregar.
        precio (float): Precio por unidad.

    Efectos secundarios:
        - Modifica el inventario en memoria.
        - Guarda los cambios en el archivo JSON.
        - Muestra un mensaje en consola usando `rich`.
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["cantidad"] += cantidad
            producto["precio"] = precio  # actualiza el precio por si cambió
            console.print(f"[yellow]Producto '{nombre}' actualizado.[/yellow]")
            guardar_inventario(inventario)
            return

    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_inventario(inventario)
    console.print(f"[green]Producto '{nombre}' agregado correctamente.[/green]")


def vender_producto(inventario, nombre, cantidad):
    """
    Realiza una venta restando unidades del producto indicado.

    Args:
        inventario (list[dict]): Lista actual del inventario.
        nombre (str): Nombre del producto a vender.
        cantidad (int): Número de unidades a vender.

    Efectos secundarios:
        - Disminuye la cantidad del producto si hay suficiente stock.
        - Guarda los cambios en el archivo JSON.
        - Muestra mensajes de error o confirmación en consola.

    Casos:
        - Si no existe el producto → muestra mensaje rojo.
        - Si hay stock insuficiente → muestra advertencia.
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                guardar_inventario(inventario)
                console.print(
                    f"[cyan]Venta realizada: {cantidad} unidades de '{nombre}'.[/cyan]"
                )
                return
            else:
                console.print(f"[red]No hay suficiente stock de '{nombre}'.[/red]")
                return
    console.print(f"[red]El producto '{nombre}' no existe en el inventario.[/red]")


def mostrar_inventario(inventario):
    """
    Muestra el inventario actual en una tabla con formato usando Rich.

    Args:
        inventario (list[dict]): Lista de productos a mostrar.

    La tabla incluye:
        - Nombre del producto
        - Cantidad disponible
        - Precio en COP (pesos colombianos)

    Si el inventario está vacío, muestra un mensaje de advertencia.
    """
    table = Table(title=" Inventario Actual")
    table.add_column("Nombre", style="bold cyan")
    table.add_column("Cantidad", justify="right")
    table.add_column("Precio (COP)", justify="right")

    if not inventario:
        console.print("[yellow]El inventario está vacío.[/yellow]")
        return

    for producto in inventario:
        table.add_row(
            producto["nombre"], str(producto["cantidad"]), f"${producto['precio']:.2f}"
        )

    console.print(table)


if __name__ == "__main__":
    """
    Ejecuta la interfaz de línea de comandos del Gestor de Inventario.

    Permite al usuario:
        1. Mostrar el inventario
        2. Agregar un producto
        3. Vender un producto
        4. Salir del programa
    """
    inventario = cargar_inventario()

    while True:
        console.print("\n[bold blue]--- GESTOR DE INVENTARIO ---[/bold blue]")
        console.print("1. Mostrar inventario")
        console.print("2. Agregar producto")
        console.print("3. Vender producto")
        console.print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(inventario, nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Producto a vender: ")
            cantidad = int(input("Cantidad vendida: "))
            vender_producto(inventario, nombre, cantidad)
        elif opcion == "4":
            console.print("[bold green]Saliendo del programa...[/bold green]")
            break
        else:
            console.print("[red]Opción inválida.[/red]")
