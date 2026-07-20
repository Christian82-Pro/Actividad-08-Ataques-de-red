FROM python:3.9

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 80

# Ejecutar API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]