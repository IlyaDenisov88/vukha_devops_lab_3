FROM python:3.10

RUN pip install -r requirements.txt
WORKDIR /app

COPY . /app

CMD ["python3", "printer.py"]



