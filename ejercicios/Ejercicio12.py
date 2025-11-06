import csv

from rich.console import Console
from rich.table import Table


def analizar_csv(nombre_archivo: str, columna: str) -> dict:
    console = Console()
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            valores = []

            for fila in lector:
                if columna not in fila:
                    raise KeyError(f"La columna '{columna}' no existe en el archivo.")
                valor = fila[columna].strip()
                if valor:  # Evita valores vacíos
                    valores.append(float(valor))

            if not valores:
                raise ValueError(
                    f"La columna '{columna}' no contiene datos numéricos válidos."
                )

            promedio = sum(valores) / len(valores)
            maximo = max(valores)
            minimo = min(valores)

            resultados = {"Promedio": promedio, "Máximo": maximo, "Mínimo": minimo}

            # Mostrar tabla con rich
            tabla = Table(title=f"📊 Análisis de la columna '{columna}'")
            tabla.add_column("Métrica", justify="center")
            tabla.add_column("Valor", justify="center")

            for k, v in resultados.items():
                tabla.add_row(k, f"{v:.2f}")

            console.print(tabla)
            return resultados

    except FileNotFoundError:
        console.print(f"❌ Error: El archivo '{nombre_archivo}' no se encontró.")
        raise
    except KeyError as e:
        console.print(f"❌ Error: {e}")
        raise
    except ValueError as e:
        console.print(f"❌ Error: {e}")
        raise


def mostrar_tabla(resultados: dict, columna: str):
    """Muestra los resultados en formato tabla usando rich."""
    console = Console()
    tabla = Table(title=f"Análisis de la columna '{columna}'", show_lines=True)

    tabla.add_column("Estadística", justify="center", style="cyan", no_wrap=True)
    tabla.add_column("Valor", justify="center", style="magenta")

    for clave, valor in resultados.items():
        tabla.add_row(clave, f"{valor:.2f}")

    console.print(tabla)


# === EJEMPLO DE USO ===
if __name__ == "__main__":
    # Suponiendo un archivo estudiantes.csv con columnas: nombre,edad,calificacion
    analizar_csv("estudiantes.csv", "calificacion")
