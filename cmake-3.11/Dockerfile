ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN cd opt \
 && wget https://github.com/Kitware/CMake/archive/v3.11.0.tar.gz \
 && tar xf v3.11.0.tar.gz \
 && rm v3.11.0.tar.gz \
 && ln -sf /opt/v3.11.0/bin/cmake /usr/bin/cmake
