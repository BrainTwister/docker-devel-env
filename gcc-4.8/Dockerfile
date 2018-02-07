ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-4.8 g++-4.8 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-4.8 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-4.8 /usr/bin/gcc

ENV CC gcc
ENV CXX g++
