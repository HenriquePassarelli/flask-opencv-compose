FROM ubuntu:18.04
LABEL maintainer="henrique.passarellicc@gmail.com"

RUN apt-get update -y && apt-get install -y build-essential cmake \
    libsm6 libxext6 libxrender-dev \
    python3 python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install -r requirements.txt

COPY . /app
CMD ["python3","main.py"]