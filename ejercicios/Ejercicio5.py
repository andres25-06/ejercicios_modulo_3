from typing import NoReturn

from rich.console import Console
from rich.table import Table

tasa_IVA:float =0.19

def calcular_iva(precio_base:float)->float:
    """
    Calcula el valor del IVA usando la tasa global

    Args:
        precio_base(float): Precio del producto sin IVA

    Returns:
        float:Valor del IVA calculado
    """

    return precio_base*tasa_IVA

def actualizar_tasa_iva(nueva_tasa:float)->None:
    """
    Actualiza la varibale global tasa_IVA con un nuevo valor

    Args:
        nueva_tasa(float):Nueva tasa del IVA

    Returns:
        None
    """

    global tasa_IVA

    tasa_IVA =nueva_tasa


def mostrar_tabla_iva(precio:float)->NoReturn:
    """
    Muestra el calculo del IVa

    Args:
        precio(float): Precio base del producto sin IVA
    """

    console = Console()
    tabla=Table(
        title= " Cálculo de IVA",
        header_style="bold magenta"
    )

    tabla.add_column("Campo",justify="left",style="cyan",no_wrap=True)
    tabla.add_column("Valor",justify="right",style="white")


    iva=calcular_iva(precio)

    tabla.add_row("Precio base", f"$ {precio:.2f}")
    tabla.add_row("Tasa IVA", f"{tasa_IVA*100:.2f}%")
    tabla.add_row("IVA Calculado",f"${iva:.2f}")
    tabla.add_row("Precio Total",f"${precio +iva:.2f}")

    console.print(tabla)

if __name__ == "__main__":
    console=Console()
    console.print("[bold blue] Calculadora de Impuestos (IVA) ✨ [/bold blue]\n")
    precio=float(input("Ingrese el precio base del producto: "))

    mostrar_tabla_iva(precio)

    console.print("\n[bold green]  Actualizar tasa de IVA [/bold green]\n")

    nueva_tasa=float(input("Ingrese la tasa del IVA: "))

    actualizar_tasa_iva(nueva_tasa)

    console.print("\n[bold yellow] Cálculo con la tasa actualizada:[/bold yellow]\n]")
    mostrar_tabla_iva(precio)
