from typing import Dict, Tuple

from rich.console import Console
from rich.table import Table


def crear_perfil (nombre:str,edad:int,*hobbies:str,**redes_sociales:str)->str:
    """
    Genera un perfil de usuario con información básica,hobbies y redes sociales.

    Args:
        nombre (str):Nombre del Usuario
        edad (int):Edad del Usuario
        *hobbies (str):Lista de los hobbies
        **redes_sociales (str):Redes sociales con sus nombres de usuario

    Returns:
        str: Perfil de usuario
    """

    table =Table(
        title=f"👤Perfil de {nombre}",
        show_header=True, #encabezado
        header_style="bold magenta" #Color
    )

    #columnas principales
    table.add_column("Campo",justify="left",style="cyan",no_wrap=True)
    table.add_column("Información",style="white")

    #Información básica
    table.add_row("Nombre",nombre)
    table.add_row("Edad",str(edad))

    table.add_row("Hobbies", ", ".join(hobbies) if hobbies else 'No especificados')

    if redes_sociales:
        redes="\n".join(f"{red}:{usuario}"for red,usuario in redes_sociales.items())
        table.add_row("Redes Sociales",redes)

    else:
        table.add_row("Redes Sociales",'No registradas')


    console=Console()
    console.print(table)

    perfil_texto=(
        f"Perfil de {nombre}\n"
        f"Edad: {edad}\n"
        f"Hobbies:{
            ', '.join(hobbies)
            if
                hobbies
            else
                'No especificados'}\n"
        f"Redes:{
            ', '.join(redes_sociales.keys())
            if
                redes_sociales
            else
                'No registradas'}"
    )

    return perfil_texto

def solicitar_datos_usuario()->Tuple[str,int,Tuple[str, ...],Dict[str,str]]:
    """
    solicita al usuario sus datos personales,hobbies y redes sociales

    Returns:Tuple[str,int,Tuple[str, ...]Dict[str,str]]:
    Retorna nombre, edad, tupla de hobbies y diccionario de redes.
    """

    nombre=input("  Ingrese su nombre: ").strip()
    edad=int(input("  Ingrese su edad: "))
    hobbies_input=input(
        "Ingrese sus hobbies separados por comas(o deja vacío si no tienes): ").strip()

    hobbies=tuple(
        h.strip() for h in hobbies_input.split(
            ",") if h.strip()) if hobbies_input else()

    redes_sociales:Dict[str, str]={}
    print("\n  Ingresa tus redes sociales (deja el nombre vacío para terminar): ")

    while True:
        red =input("Nombre de la red social: ").strip().lower()
        if not red:#si esta vacío el bucle  termina
            break
        usuario = input(f"Usuario en {red}: ").strip()
        redes_sociales[red]=usuario

    return nombre,edad,hobbies,redes_sociales

if __name__=="__main__":
    console=Console()

    console.print("[bold green] Bienvenido al generador de Perfiles ✨[/bold green]\n")

    nombre,edad,hobbies,redes_sociales=solicitar_datos_usuario()

    console.print("\n[bold yellow] Perfil Generado: [/bold yellow]\n")
    crear_perfil(nombre,edad,*hobbies,**redes_sociales)


