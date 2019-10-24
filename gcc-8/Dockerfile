ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    gcc-8 \
    g++-8 \
    gdb \
    linux-tools-generic \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && ln -sf /usr/bin/g++-8 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-8 /usr/bin/gcc

ENV CC gcc
ENV CXX g++

RUN pip3 install -I gcovr
