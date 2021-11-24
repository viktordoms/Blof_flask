FROM python:3.9.5-slim-buster

WORKDIR /application

RUN pip install flask

COPY ./requirements.txt /application/requirements.txt

RUN  pip install -r requirements.txt

#COPY ./wait-for-it.sh /usr/bin/wait-for-it.sh

CMD flask run --host=0.0.0.0 --port=8080

#CMD ["./wait-for-it.sh", "db:3306", "--", "flask","app:app"]