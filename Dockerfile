FROM ubuntu:18.04

MAINTAINER junawaneshivani@gmail.com

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install sklearn matplotlib pandas

COPY LinearRegression.py /

CMD ["/bin/bash"]
