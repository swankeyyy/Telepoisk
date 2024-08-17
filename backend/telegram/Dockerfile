FROM python:3.10.9

WORKDIR usr/src/tg

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install netcat -y

RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

