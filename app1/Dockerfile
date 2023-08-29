# FROM ubuntu:20.04

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# WORKDIR /usr/src/app/

# RUN apt-get update
# RUN apt install python3.9 -y
# RUN apt install python3-pip -y
# RUN apt update 
# RUN apt install python3.8 -y
# RUN pip install --upgrade pip

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# # RUN python3 manage.py runserver 0.0.0.0:8000

FROM python:3-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
