FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python manage.py migrate

COPY . .