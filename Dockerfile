FROM python:3

WORKDIR /calc

COPY . /calc

CMD ["python3", "main.py"]




