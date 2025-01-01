# Использовать официальную среду выполнения Python в качестве родительского образа
FROM python:3.9-slim-buster
# Установить рабочий каталог /app
WORKDIR /app
# Скопировать содержимое текущего каталога в контейнер в /app
COPY . /app
# Установить все необходимые пакеты, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Сделайте порт 5000 общедоступным за пределами этого контейнера
EXPOSE 5000
# Определить переменную окружения
CMD ["python", "app.py"]
