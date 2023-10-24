FROM python:3

RUN pip install -r requirements.txt

WORKDIR /calc

COPY . /calc

CMD ["python3", "myoopcalc.py"]




