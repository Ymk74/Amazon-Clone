# start docker with python 3.11
FROM python:3.11.6-slim-bullseye


# setup linux python
ENV PYTHONUNBUFFERED = 1


# update linux kernal & setup tools
RUN apt-get update && apt-get -y install gcc libpq-dev


# folder project
WORKDIR /app


# copy requirements.txt
COPY requirements.txt /app/requirements.txt


# install requirements.txt
RUN pip install -r /app/requirements.txt


#copy project folders
COPY . /app/