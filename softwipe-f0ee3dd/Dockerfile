ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && git clone https://github.com/adrianzap/softwipe.git \
 && cd softwipe \
 && git checkout f0ee3dd9b05bd2de4b9e89d07cae1149e566cbfa \
 && yes Y | ./softwipe.py \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
