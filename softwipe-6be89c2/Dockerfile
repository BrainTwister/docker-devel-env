ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && git clone https://github.com/adrianzap/softwipe.git \
 && cd softwipe \
 && git checkout 6be89c294b9d24fd336f66cfb83b41a8d66b9978 \
 && yes Y | ./softwipe.py \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
