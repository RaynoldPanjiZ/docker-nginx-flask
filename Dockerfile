FROM python:3.11-slim

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r $CONTAINER_HOME/requirements.txt