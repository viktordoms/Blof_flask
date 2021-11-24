FROM python:3.9.5-slim-buster

WORKDIR /application

RUN pip install flask

COPY ./requirements.txt /application/requirements.txt

RUN  pip install -r requirements.txt

CMD flask run --host=0.0.0.0 --port=8080