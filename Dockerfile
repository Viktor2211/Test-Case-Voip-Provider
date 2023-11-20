FROM python:3.9-alpine3.17

RUN mkdir /backend
WORKDIR /backend

COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /backend/