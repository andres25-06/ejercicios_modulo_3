from rich.table import Table
from rich.console import Console


def calcular_imc(peso: float, estatura: float) -> float:
    """
    Calcula el idice de la Masa Corporal (IMC)

    Args:
        peso (float): Peso de la persona en kilogramos
        estatura (float): Estatura de la persona en metros

    Returns:
        float: El valor del IMC calculado
    """

    if estatura <= 0:
        raise ValueError("La estatura debe ser mayor a 0")

    imc = peso / (estatura**2)
    return imc


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el valor del IMC y devuelve su cllasificación.

    Args:
        imc (float): Valor del indide de la masa corporal

    Returns:
        str: Clasificación del IMC( Bajo peso, normal, sobrepeso, obesidad)
    """

    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def tabla_resultado(peso: float, estatura: float, imc: float, categoria: str) -> None:
    """
    Muestra los resultados

    Args:
        peso (float): Peso de la persona en kilogramos
        estatura (float): Estatura de la persona en metros
        imc (float): Valor del IMC calculado
        categoria (str): Categoria del resultado
    """

    console = Console()

    table = Table(title="💪 Resultado del IMC💪 ")

    table.add_column("Dato", style="bold cyan", justify="center")
    table.add_column("valor", style="bold yellow", justify="center")

    table.add_row("Peso (Kg)", f"{peso:.2f}")
    table.add_row("Estatura (M)", f"{estatura:.2f}")
    table.add_row("IMC", f"{imc:.2f}")
    table.add_row("Clasificación", categoria)

    console.print(table)


def main() -> None:
    """
    Pide los datos de la persona,calcula el IMC,
    interpreta el resultado y lo muestra en la tabla.
    """

    try:
        peso = float(input("Ingrese su peso actual en Kilogramos: "))
        estatura = float(input("Ingrese su estatura en metros: "))

        imc = calcular_imc(peso, estatura)
        categoria = interpretar_imc(imc)

        tabla_resultado(peso, estatura, imc, categoria)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
