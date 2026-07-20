import requests

# URL local de la API
url = "http://127.0.0.1:8000/predict"

# Datos de prueba
params = {
    "duracion_flujo": 12000,
    "paquetes_adelante": 150,
    "paquetes_atras": 120,
    "longitud_adelante": 9000,
    "longitud_atras": 8500
}

# Enviar solicitud
response = requests.post(url, params=params)

# Mostrar resultado
print(response.json())