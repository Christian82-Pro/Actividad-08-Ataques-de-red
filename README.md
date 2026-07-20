# Actividad 08 - Ataques de Red

## Descripción

Este proyecto implementa una estrategia básica de observabilidad para un modelo de Machine Learning desplegado mediante una API desarrollada con FastAPI. Se registran métricas, alertas e incidentes, además de utilizar MLflow para el monitoreo del modelo y dashboards para visualizar la información.

## Tecnologías utilizadas

- Python
- FastAPI
- Scikit-learn
- Pandas
- Matplotlib
- MLflow
- Docker

## Estructura del proyecto

```
Actividad 08 Ataques de red/
│
├── main.py
├── modelo_red.pkl
├── columnas.pkl
├── requirements.txt
├── dashboard.py
├── data_drift.py
├── mlflow_modelo.py
├── simular_incidentes.py
├── metricas_api.csv
├── alertas_api.csv
├── incidentes.csv
├── data_drift.csv
└── dashboards/
```

## Funcionalidades

- API para predicción de ataques de red.
- Registro automático de métricas.
- Generación de alertas por alta latencia.
- Simulación de incidentes.
- Simulación de Data Drift.
- Monitoreo del modelo mediante MLflow.
- Generación de dashboards con métricas e incidentes.

## Ejecución

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la API:

```bash
uvicorn main:app --reload
```

Iniciar MLflow:

```bash
mlflow ui
```

Generar dashboards:

```bash
python dashboard.py
```

Simular incidentes:

```bash
python simular_incidentes.py
```

Simular Data Drift:

```bash
python data_drift.py
```
## Autor
Christian Oswaldo Ortiz Rodríguez
Gestión de proyectos de inteligencia artificial
Proyecto Fase II
Luis Ariel Vázquez Piña
05 / 07 / 2026
