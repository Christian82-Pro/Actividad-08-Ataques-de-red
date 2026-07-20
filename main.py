from fastapi import FastAPI
import pandas as pd
import joblib
import time
import csv
import os
from datetime import datetime


# Crear la aplicación
app = FastAPI()

# Cargar modelo y columnas
modelo = joblib.load("modelo_red.pkl")
columnas = joblib.load("columnas.pkl")


def guardar_metrica(
    latencia_ms,
    prediccion,
    resultado,
    probabilidad,
    estado
):
    """
    Guarda la información de cada solicitud en un archivo CSV.
    """

    nombre_archivo = "metricas_api.csv"
    archivo_existe = os.path.exists(nombre_archivo)

    with open(
        nombre_archivo,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        if not archivo_existe:
            escritor.writerow([
                "fecha",
                "latencia_ms",
                "prediccion",
                "resultado",
                "probabilidad_ataque",
                "estado"
            ])

        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            latencia_ms,
            prediccion,
            resultado,
            probabilidad,
            estado
        ])


def guardar_alerta(tipo, descripcion):
    """
    Guarda una alerta cuando ocurre un problema.
    """

    nombre_archivo = "alertas_api.csv"
    archivo_existe = os.path.exists(nombre_archivo)

    with open(
        nombre_archivo,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.writer(archivo)

        if not archivo_existe:
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


@app.get("/")
def home():
    return {
        "mensaje": "API de detección de ataques de red activa"
    }


@app.get("/estado")
def estado():
    return {
        "estado": "activo",
        "modelo": "Random Forest",
        "total_columnas": len(columnas)
    }


@app.post("/predict")
def predict(
    duracion_flujo: float = 1000,
    paquetes_adelante: float = 10,
    paquetes_atras: float = 5,
    longitud_adelante: float = 500,
    longitud_atras: float = 300,
    simular_latencia: bool = False
):
    """
    Realiza una predicción y registra las métricas.
    """

    tiempo_inicio = time.time()

    try:
        # Simulación para demostrar el incidente de latencia
        if simular_latencia:
            time.sleep(1)

        # Crear entrada básica
        datos = {
            "Flow Duration": duracion_flujo,
            "Total Fwd Packets": paquetes_adelante,
            "Total Backward Packets": paquetes_atras,
            "Total Length of Fwd Packets": longitud_adelante,
            "Total Length of Bwd Packets": longitud_atras
        }

        # Convertir a dataframe
        entrada = pd.DataFrame([datos])

        # Ajustar columnas al modelo
        entrada = entrada.reindex(
            columns=columnas,
            fill_value=0
        )

        # Realizar predicción
        prediccion = modelo.predict(entrada)[0]
        probabilidad = modelo.predict_proba(entrada)[0][1]

        # Interpretar resultado
        if prediccion == 1:
            resultado = "Ataque detectado"
        else:
            resultado = "Tráfico benigno"

        # Calcular tiempo de respuesta
        tiempo_final = time.time()
        latencia_ms = round(
            (tiempo_final - tiempo_inicio) * 1000,
            2
        )

        # Guardar métrica de la solicitud
        guardar_metrica(
            latencia_ms=latencia_ms,
            prediccion=int(prediccion),
            resultado=resultado,
            probabilidad=round(float(probabilidad), 4),
            estado="Correcta"
        )

        # Generar alerta si la latencia supera 500 ms
        if latencia_ms > 500:
            guardar_alerta(
                tipo="Latencia alta",
                descripcion=(
                    f"La solicitud tardó {latencia_ms} ms. "
                    "El límite establecido es de 500 ms."
                )
            )

        return {
            "prediccion": int(prediccion),
            "resultado": resultado,
            "probabilidad_ataque": round(
                float(probabilidad),
                4
            ),
            "latencia_ms": latencia_ms
        }

    except Exception as error:
        tiempo_final = time.time()
        latencia_ms = round(
            (tiempo_final - tiempo_inicio) * 1000,
            2
        )

        guardar_metrica(
            latencia_ms=latencia_ms,
            prediccion="",
            resultado="Error",
            probabilidad="",
            estado="Error"
        )

        guardar_alerta(
            tipo="Error en predicción",
            descripcion=str(error)
        )

        return {
            "estado": "Error",
            "mensaje": str(error),
            "latencia_ms": latencia_ms
        }