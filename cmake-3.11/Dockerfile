ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN cd opt \
 && wget https://cmake.org/files/v3.11/cmake-3.11.0-Linux-x86_64.tar.gz \
 && tar xf cmake-3.11.0-Linux-x86_64.tar.gz \
 && rm cmake-3.11.0-Linux-x86_64.tar.gz \
 && ln -sf /opt/cmake-3.11.0-Linux-x86_64/bin/cmake /usr/bin/cmake
