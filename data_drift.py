import csv
import os
from datetime import datetime


# Función para guardar los eventos de Data Drift
def guardar_drift(
    variable,
    valor_anterior,
    valor_actual,
    estado
):

    nombre_archivo = "data_drift.csv"

    archivo_existe = os.path.exists(nombre_archivo)

    with open(
        nombre_archivo,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        # Crear encabezados
        if not archivo_existe:

            escritor.writerow([
                "fecha",
                "variable",
                "valor_anterior",
                "valor_actual",
                "estado"
            ])

        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            variable,
            valor_anterior,
            valor_actual,
            estado
        ])


print("===== Simulación de Data Drift =====\n")


# Ejemplo 1
guardar_drift(
    variable="Flow Duration",
    valor_anterior=850,
    valor_actual=2600,
    estado="Drift Detectado"
)

print("✔ Drift detectado en Flow Duration")


# Ejemplo 2
guardar_drift(
    variable="Total Fwd Packets",
    valor_anterior=12,
    valor_actual=55,
    estado="Drift Detectado"
)

print("✔ Drift detectado en Total Fwd Packets")


# Ejemplo 3
guardar_drift(
    variable="Modelo",
    valor_anterior="Random Forest",
    valor_actual="Reentrenado",
    estado="Drift Corregido"
)

print("✔ Modelo actualizado")


print("\nProceso terminado.")