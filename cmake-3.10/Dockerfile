ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN cd opt \
 && wget https://cmake.org/files/v3.10/cmake-3.10.1-Linux-x86_64.tar.gz \
 && tar xf cmake-3.10.1-Linux-x86_64.tar.gz \
 && rm cmake-3.10.1-Linux-x86_64.tar.gz \
 && ln -sf /opt/cmake-3.10.1-Linux-x86_64/bin/cmake /usr/bin/cmake
