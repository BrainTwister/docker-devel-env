ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y \
    gcc-6 \
    g++-6 \
    gdb \
 && apt-get clean \
 && ln -sf /usr/bin/g++-6 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-6 /usr/bin/gcc

ENV CC gcc
ENV CXX g++
