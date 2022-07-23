FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN python -m pip install pip --upgrade
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./src /app
WORKDIR /app

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
