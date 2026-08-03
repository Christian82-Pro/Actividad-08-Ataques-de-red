# FASE III

# Sistema Inteligente para la Detección de Ataques de Red

## Descripción

Este proyecto consiste en el desarrollo de una solución de inteligencia artificial para detectar posibles ataques de red utilizando Machine Learning. Se entrenó un modelo Random Forest y posteriormente se publicó mediante una API desarrollada con FastAPI.

Además del modelo, se incorporaron prácticas de MLOps y GitOps, incluyendo monitoreo, automatización del pipeline, control de versiones y una propuesta de despliegue en la nube.

---

## Objetivo

Desarrollar una solución capaz de clasificar automáticamente el tráfico de red como benigno o posible ataque, integrando herramientas que permitan facilitar el despliegue, monitoreo y mantenimiento del modelo.

---

## Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Random Forest
- FastAPI
- Docker
- MLflow
- GitHub
- GitHub Actions
- AWS (propuesta de despliegue)

---

## Estructura del proyecto

---
FASE-III-Ataques-de-red/
│
├── .github/
│   └── workflows/
│       └── pipeline.yml
│
├── modelo_red.pkl
├── columnas.pkl
├── main.py
├── dashboard.py
├── mlflow_modelo.py
├── data_drift.py
├── simular_incidentes.py
├── Dockerfile
├── requirements.txt
└── README.md
---

---

## Funcionalidades

- Entrenamiento del modelo Random Forest.
- API REST desarrollada con FastAPI.
- Contenerización mediante Docker.
- Registro de métricas con MLflow.
- Monitoreo de latencia y alertas.
- Simulación de incidentes.
- Simulación de Data Drift.
- Pipeline automatizado con GitHub Actions.
- Control de versiones mediante GitHub.
- Propuesta de despliegue en AWS.

---

## Pipeline MLOps

El proyecto incluye un pipeline automatizado con GitHub Actions que realiza las siguientes tareas:

- Instalación de dependencias.
- Validación de archivos del proyecto.
- Verificación del modelo.
- Validación de la API.
- Construcción automática de la imagen Docker.
- Simulación del despliegue continuo.

---

## Monitoreo

Para supervisar el comportamiento del modelo se implementaron:

- MLflow para registrar métricas.
- Registro de alertas.
- Registro de incidentes.
- Detección de Data Drift.
- Dashboard para visualizar la información.

---

## Arquitectura

La solución está compuesta por:

Usuario → FastAPI → Modelo Random Forest → MLflow → Dashboard y registros de métricas.

---

## Resultados

Durante el desarrollo se logró:

- Entrenar un modelo funcional.
- Publicar el modelo mediante FastAPI.
- Automatizar el pipeline con GitHub Actions.
- Registrar métricas utilizando MLflow.
- Implementar monitoreo e incidentes simulados.
- Diseñar una propuesta de despliegue escalable en AWS.

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio.


git clone https://github.com/TU_USUARIO/FASE-III-Ataques-de-red.git


2. Instalar dependencias.


pip install -r requirements.txt


3. Ejecutar la API.


uvicorn main:app --reload


4. Abrir en el navegador.


http://127.0.0.1:8000/docs


---
```
## Autor
Christian Oswaldo Ortiz Rodríguez
Gestión de proyectos de inteligencia artificial
Proyecto Fase III
Luis Ariel Vázquez Piña
02 / 08 / 2026
