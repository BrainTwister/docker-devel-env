ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-4.7 g++-4.7 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-4.7 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-4.7 /usr/bin/gcc

ENV CC gcc
ENV CXX g++
