# Используем легкий образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY ./app ./app

# Указываем команду запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]