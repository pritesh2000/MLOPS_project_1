FROM python:3.10-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD flask run -h 0.0.0.0 -p 8080