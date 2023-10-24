FROM python:3

RUN pip install --upgrade pip && pip3 install -r my_project/setting/requirements.txt

WORKDIR /calc

COPY . /calc

CMD ["python3", "myoopcalc.py"]




