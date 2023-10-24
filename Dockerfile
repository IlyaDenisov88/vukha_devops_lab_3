FROM python:3.10

WORKDIR /calc

COPY . /calc

CMD ["python3", "printer.py"]



