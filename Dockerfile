FROM python:3.9-slim-bullseye

WORKDIR /

RUN apt-get -y update
RUN apt-get -y upgrade

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

CMD ["python3", "app.py"]