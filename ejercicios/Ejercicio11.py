from rich.console import Console
from rich.table import Table

console =Console()

archivo_tareas="Tareas.txt"

def agregar_tarea(tarea:str)->None:
    """
    Agrega una tarea al archivo dee texto

    Args:
        tarea (str):Texto de la tarea a guardar
    """

    with open (archivo_tareas, "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")
    console.print(f"[green] Tarea agregada: [/green]{tarea}")

def ver_tareas()->list[str]:
    """
    Lee todas las tareas del archivo y las devulve como lista
    Returns:
        list[str]: Lista de tareas
    """

    try:
        with open (archivo_tareas,"r",encoding="utf-8") as archivo:
            tareas =[linea.strip() for linea in archivo.readlines() if linea.strip()]
        return tareas
    except FileNotFoundError:
        console.print(
            "[yellow] No se encontro el archivo de tareas."
            "Se creara uno nuevo[/yellow] ")
        with open (archivo_tareas, "w",encoding="utf-8") as archivo:
            pass
        return []

def mostrar_tareas()->None:
    """
    Muestra las tareas
    """

    tareas = ver_tareas()

    if not tareas:
        console.print("[cyan] No hay tareas registradas aún.[/cyan]")
        return

    tabla=Table(
        title="  Lista de Tareas",
        show_header=True,
        header_style="bold magenta"
    )

    tabla.add_column("N°",justify="center")
    tabla.add_column("Tarea",justify="left")

    for i, tarea in enumerate (tareas,start =1):
        tabla.add_row(str(i),tarea)

    console.print(tabla)

def main()->None:
    """
    Función principal que muestra el menú y gestiona las ciones del usuario
    """

    while True:
        console.print("\n[bold cyan]✨ Gestor de Tareas ✨ [/bold cyan]" )
        console.print("1️⃣ Agregar Tarea")
        console.print("2️⃣ Ver Tareas")
        console.print("3️⃣ Salir\n")

        opcion=input("Seleccione una opción (1-3): ")

        if opcion=="1":
            tarea =input("Escribe la nueva tarea: ").strip()
            if tarea:
                agregar_tarea(tarea)
            else:
                console.print("[red]⚠️ La tarea no puede estar vacía.[/red]")

        elif opcion=="2":
            mostrar_tareas()

        elif opcion=="3":
            console.print(
                "\n[bold green]👋 Saliendo del gestor de tareas...[/bold green]")
            break

        else:
            console.print("[red]❌ Opción no válida intenta de nuevo.[/red]")


if __name__=="__main__":
    main()




