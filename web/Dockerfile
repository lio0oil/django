FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y --no-install-recommends \
    gcc \
    libc-dev \
    python3-pip --upgrade pip

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install uwsgi

EXPOSE 8001

COPY . /code/
