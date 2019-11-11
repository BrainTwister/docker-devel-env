ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && git clone https://github.com/BerndDoser/softwipe.git \
 && cd softwipe \
 && git checkout 18a7313e9269e94d95fcfc97b1808212268e894b \
 && yes Y | ./softwipe.py \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
