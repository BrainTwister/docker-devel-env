ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION

RUN apt-get update \
 && git clone https://github.com/adrianzap/softwipe.git \
 && cd softwipe \
 && git checkout $VERSION \
 && yes Y | ./softwipe.py \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
