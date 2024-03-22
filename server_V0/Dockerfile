# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los scripts del servidor a la imagen
COPY name_server.py .
COPY chat_server.py .
COPY redis_server.py .

# Instala las dependencias necesarias
RUN pip install grpcio grpcio-tools redis

# Define el comando por defecto para ejecutar el servidor
CMD ["python", "chat_server.py"]