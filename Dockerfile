FROM python:3.8-alpine

MAINTAINER Jan Füsting

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]