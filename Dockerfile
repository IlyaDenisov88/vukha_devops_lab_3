FROM python:3

RUN pip3 install -r requirements.txt

WORKDIR /calc

COPY . /calc

CMD ["python3", "myoopcalc.py"]




