ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    gcc-$VERSION \
    g++-$VERSION \
    gdb \
    linux-tools-generic \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && ln -sf /usr/bin/g++-$VERSION /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-$VERSION /usr/bin/gcc

ENV CC gcc
ENV CXX g++
