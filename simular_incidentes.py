import csv
import os
from datetime import datetime


# Función para guardar los incidentes
def guardar_incidente(
    tipo,
    descripcion,
    estado
):

    nombre_archivo = "incidentes.csv"

    archivo_existe = os.path.exists(nombre_archivo)

    with open(
        nombre_archivo,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        # Crear encabezados si el archivo no existe
        if not archivo_existe:

            escritor.writerow([
                "fecha",
                "tipo",
                "descripcion",
                "estado"
            ])

        # Guardar el incidente
        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            tipo,
            descripcion,
            estado
        ])


print("===== Simulación de incidentes =====\n")


# Funcionamiento normal
guardar_incidente(
    "Servicio",
    "La API funciona correctamente.",
    "Normal"
)

print("✔ Funcionamiento normal registrado")


# Incidente de latencia
guardar_incidente(
    "Latencia",
    "El tiempo de respuesta fue mayor a 500 ms.",
    "Incidente"
)

print("✔ Incidente de latencia registrado")


# Recuperación
guardar_incidente(
    "Latencia",
    "La latencia volvió a valores normales.",
    "Recuperado"
)

print("✔ Recuperación registrada")


# Degradación del modelo
guardar_incidente(
    "Modelo",
    "Disminuyó el desempeño del modelo (accuracy, precision, recall y F1).",
    "Incidente"
)

print("✔ Degradación del modelo registrada")


# Recuperación del modelo
guardar_incidente(
    "Modelo",
    "El modelo fue reentrenado y recuperó su desempeño.",
    "Recuperado"
)

print("✔ Recuperación del modelo registrada")


print("\nSimulación terminada.")