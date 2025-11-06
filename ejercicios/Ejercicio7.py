from typing import List,Tuple
from rich.console import Console
from rich.table import Table

def filtrar_aprobados(estudiantes:List[Tuple[str,float]])->List[Tuple[str,float]]:
    """
    Filtra los estudiantes cuya nota sea mayor o igual a 3.0 usanto filter o lambda

    Args:
        estudiantes (List[Tuple[str,float]]): Lista de tuplas con nombre,nota

    Returns:
        List[Tuple[str,float]]: Lista de tuplas solo con os estudiantes aprobados
    """
    aprobados = list (filter(lambda estudiante: estudiante[1] >=3.0,estudiantes))
    return aprobados

def mostrar_tabla(estudiantes:List[Tuple[str,float]])->None:
    """
    Muestra los estudiantes en un tabla

    Args:
        estudiantes(List[tuple[str,float]]): Lista de tuplas con nombre,nota

    Returns:
        None
    """
    console=Console()
    tabla=Table(
        title="🎓  Estudiantes aprobados",
        title_style="bold bright_yellow",
        border_style="bright_cyan"
    )

    tabla.add_column("Nombre",justify="center",style="bold white")
    tabla.add_column("Nota",justify="center",style="green")

    for nombre,nota in estudiantes:
        tabla.add_row(nombre,f"{nota:.2f}")

    console.print(tabla)


if __name__=="__main__":
    estudiantes=[("Ana",4.5),("Juan",1,.5),("Tatiana",5.0),("Andres",3.0),("Camilo",2.9)]

    aprobados=filtrar_aprobados(estudiantes)

    mostrar_tabla(aprobados)




