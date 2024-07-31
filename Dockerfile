FROM python:3.10-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD python app.py