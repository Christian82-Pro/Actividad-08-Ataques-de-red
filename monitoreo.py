import csv
import os
from datetime import datetime


# Esta función guarda las métricas de cada predicción
def guardar_metrica(latencia, prediccion, resultado):

    nombre_archivo = "metricas_api.csv"

    # Verifica si el archivo ya existe
    existe = os.path.exists(nombre_archivo)

    with open(
        nombre_archivo,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        # Si es la primera vez crea los encabezados
        if not existe:

            escritor.writerow([
                "fecha",
                "latencia_ms",
                "prediccion",
                "resultado"
            ])

        # Guarda la información
        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            latencia,
            prediccion,
            resultado
        ])


# Esta función guarda las alertas del sistema
def guardar_alerta(tipo, descripcion):

    nombre_archivo = "alertas_api.csv"

    existe = os.path.exists(nombre_archivo)

    with open(
        nombre_archivo,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        if not existe:

            escritor.writerow([
                "fecha",
                "tipo",
                "descripcion"
            ])

        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            tipo,
            descripcion
        ])