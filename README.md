# Proyecto de Fase II

## Sistema para la detección de ataques de red

### Descripción
En este proyecto se desarrolla una API que utiliza un modelo de Machine Learning para identificar si un registro de tráfico de red corresponde a tráfico normal o a un posible ataque.

El modelo fue entrenado previamente utilizando una muestra del conjunto de datos CICIDS2017 y posteriormente se integró con FastAPI para realizar predicciones. Además, se preparó la aplicación para ejecutarse dentro de un contenedor Docker y facilitar su despliegue.

## Archivos del proyecto
-	`modelo_red.pkl`: modelo entrenado.
-	`columnas.pkl`: columnas utilizadas durante el entrenamiento.
-	`main.py`: contiene la API.
-	`simula_consumo.py`: realiza una prueba de consumo de la API.
-	`Dockerfile`: archivo para crear la imagen Docker.
-	`requirements.txt`: dependencias del proyecto.

## Requisitos
Antes de ejecutar el proyecto es necesario tener instalado:
-	Python 3.9 o superior
-	Docker (para la parte de contenerización)
También se deben instalar las librerías del proyecto.
pip install -r requirements.txt

## Ejecutar la aplicación
Desde la carpeta del proyecto ejecutar: Proyecto Fase2 Ataques de red
uvicorn main:app --reload
Si todo funciona correctamente, la API quedará disponible en:
http://127.0.0.1:8000
La documentación automática se puede consultar en:
http://127.0.0.1:8000/docs

## Prueba de la API
Para realizar una prueba sencilla se puede ejecutar:
python simula_consumo.py
Este archivo envía una solicitud a la API y muestra la respuesta obtenida.

## Docker
Para construir la imagen ejecutar:
docker build -t modelo-ataques-red .
Para iniciar el contenedor:
docker run -p 8000:80 modelo-ataques-red
Después se puede acceder nuevamente a:
http://localhost:8000
o a la documentación:
http://localhost:8000/docs

## Dataset
El modelo utilizado en este proyecto fue entrenado con una muestra del conjunto de datos **CICIDS2017**, utilizado para investigaciones relacionadas con la detección de intrusiones en redes de la actividad anterior.

## Autor
Christian Oswaldo Ortiz Rodríguez
Gestión de proyectos de inteligencia artificial
Proyecto Fase II
Luis Ariel Vázquez Piña
05 / 07 / 2026