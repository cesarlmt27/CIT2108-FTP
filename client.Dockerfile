FROM ubuntu

RUN apt-get -y update -y && \
    apt-get install curl -y