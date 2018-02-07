ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y \
    gcc-7 \
    g++-7 \
    gdb \
 && apt-get clean \
 && ln -sf /usr/bin/g++-7 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-7 /usr/bin/gcc

ENV CC gcc
ENV CXX g++
