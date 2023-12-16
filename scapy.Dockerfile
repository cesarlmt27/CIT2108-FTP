FROM ubuntu

RUN apt update -y

RUN apt install python3 -y && \
    apt install python3-pip -y

RUN pip3 install --pre scapy[basic] && \
    pip3 install matplotlib && \
    pip3 install pyx

RUN apt install texlive-latex-base -y
