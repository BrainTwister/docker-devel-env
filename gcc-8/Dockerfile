ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    binutils \
    gdb \
    linux-tools-generic

RUN apt-add-repository -y ppa:jonathonf/gcc-8.1 \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    gcc-8 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && ln -sf /usr/bin/g++-8 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-8 /usr/bin/gcc

ENV CC gcc
ENV CXX g++
