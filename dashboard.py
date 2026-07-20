import pandas as pd
import matplotlib.pyplot as plt
import os


# Verificar si existe el archivo de métricas
if os.path.exists("metricas_api.csv"):

    # Leer las métricas registradas por la API
    metricas = pd.read_csv("metricas_api.csv")

    # Crear una gráfica de latencia
    plt.figure(figsize=(10, 5))

    plt.plot(
        metricas.index + 1,
        metricas["latencia_ms"],
        marker="o"
    )

    # Agregar una línea que representa el límite permitido
    plt.axhline(
        y=500,
        linestyle="--",
        label="Límite de 500 ms"
    )

    plt.title("Latencia de las solicitudes")
    plt.xlabel("Número de solicitud")
    plt.ylabel("Latencia en milisegundos")
    plt.legend()
    plt.grid()

    # Ajustar el contenido de la gráfica
    plt.tight_layout()

    # Guardar la gráfica como imagen
    plt.savefig("dashboard_latencia.png")

    # Cerrar la gráfica
    plt.close()

    print("Gráfica de latencia creada correctamente.")

else:

    print(
        "No se encontró metricas_api.csv. "
        "Primero realiza predicciones en la API."
    )


# Verificar si existe el archivo de incidentes
if os.path.exists("incidentes.csv"):

    # Leer los incidentes simulados
    incidentes = pd.read_csv("incidentes.csv")

    # Contar cuántos registros existen por estado
    cantidad_estados = incidentes["estado"].value_counts()

    # Crear gráfica de incidentes
    plt.figure(figsize=(8, 5))

    cantidad_estados.plot(
        kind="bar"
    )

    plt.title("Estados registrados durante los incidentes")
    plt.xlabel("Estado")
    plt.ylabel("Cantidad de registros")
    plt.xticks(rotation=0)
    plt.grid(axis="y")

    # Ajustar el contenido
    plt.tight_layout()

    # Guardar la gráfica
    plt.savefig("dashboard_incidentes.png")

    # Cerrar la gráfica
    plt.close()

    print("Gráfica de incidentes creada correctamente.")

else:

    print(
        "No se encontró incidentes.csv. "
        "Primero ejecuta simular_incidentes.py."
    )


# Verificar si existe el archivo de alertas
if os.path.exists("alertas_api.csv"):

    # Leer las alertas generadas
    alertas = pd.read_csv("alertas_api.csv")

    # Contar las alertas por tipo
    cantidad_alertas = alertas["tipo"].value_counts()

    # Crear gráfica de alertas
    plt.figure(figsize=(8, 5))

    cantidad_alertas.plot(
        kind="bar"
    )

    plt.title("Alertas generadas por la API")
    plt.xlabel("Tipo de alerta")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=0)
    plt.grid(axis="y")

    # Ajustar la gráfica
    plt.tight_layout()

    # Guardar imagen
    plt.savefig("dashboard_alertas.png")

    # Cerrar la gráfica
    plt.close()

    print("Gráfica de alertas creada correctamente.")

else:

    print(
        "No se encontró alertas_api.csv. "
        "Primero realiza una prueba con latencia alta."
    )


print("\nProceso de generación de dashboard terminado.")