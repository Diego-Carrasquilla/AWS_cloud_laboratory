FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias primero (mejor uso de cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Comando de inicio del servidor Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
