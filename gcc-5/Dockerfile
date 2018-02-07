ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y \
    gcc-5 \
    g++-5 \
    gdb \
 && apt-get clean \
 && ln -sf /usr/bin/g++-5 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-5 /usr/bin/gcc

ENV CC gcc
ENV CXX g++
