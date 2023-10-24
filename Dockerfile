FROM python:3.10

WORKDIR /app

COPY . /app

CMD ["python", "printer.py"]

RUN cat numbers.txt



