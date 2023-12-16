FROM ubuntu

RUN apt-get update -y && \
    apt-get install pure-ftpd -y

RUN  groupadd ftpgroup && \
    useradd -g ftpgroup -d /dev/null -s /etc ftpuser && \
    mkdir /root/ftphome