from typing import Any

from rich.console import Console
from rich.table import Table

console = Console()

def aplicar_descuento(
    productos:list[dict[str,Any]])->list[float]:
    """
    Aplica un descuento del 10 % alos precios de una lista de productos

    Args:
        productos(list[dict[str,Any]]): Lista de diccionarios,
        donde cada uno contiene:
        -'nombre'(str): el nombre del producto
        -'precio'(float o int): el precio original del producto

    Returns:
        list[float]:Nueva lista con los productos actualizados
        despues de aplicar el descuento
        del 10%
    """

    precios_descuento=list(map(
        lambda p:round(p["precio"]*0.9,2),productos))

    return precios_descuento

def mostrar_tabla(
    productos:list[
        dict[str,Any]],precios_descuento:list[float])->None:
    """
    Muestra la tabla con los productos originales y sus precios con descuanto

    Args:
        productos(list[dict[str,Any]]): Lista de productos con nombre y precio
        precios_descuento(list[float]):Lista de precios con descuento
    """

    tabla = Table(
        title=" [bold magenta] Productos con Descuanto del 10 %[/bold magenta]",
        header_style="bold white on black",
        title_style="bold magenta",
        border_style="bright_magenta",
    )

    tabla.add_column("Producto",justify="center",style="cyan")
    tabla.add_column("Precio Original",justify="center",style="yellow")
    tabla.add_column("Precio con descuento",justify="center",style="green")

    for producto, precio_desc in zip(productos,precios_descuento):
        tabla.add_row(
            producto["nombre"],
            f"${producto['precio']:,}",
            f"${precio_desc:,.2f}",
        )

    console.print(tabla)

if __name__=="__main__":

    productos=[
        {"nombre":"Camisa","precio":50000},
        {"nombre":"Pantalón","precio":80000},
        {"nombre":"Zapatos","precio":120000},
    ]

    precios_desc =aplicar_descuento(productos)
    mostrar_tabla(productos,precios_desc)
