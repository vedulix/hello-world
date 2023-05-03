# Установка базового образа
FROM python:3.9-slim-buster

# Копирование файлов проекта в контейнер
COPY . /app

# Установка зависимостей
RUN pip install --no-cache-dir -r /app/requirements.txt

# Установка переменных среды
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Установка рабочей директории
WORKDIR /app

# Запуск приложения
CMD ["python", "/app/server.py"]
