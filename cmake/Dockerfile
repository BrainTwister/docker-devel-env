ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION
ARG ARCH="Linux-x86_64"

RUN cd opt \
 && wget -q https://cmake.org/files/v$MINOR_VERSION/cmake-$VERSION-$ARCH.tar.gz \
 && tar xf cmake-$VERSION-$ARCH.tar.gz \
 && rm cmake-$VERSION-$ARCH.tar.gz \
 && ln -sf /opt/cmake-$VERSION-$ARCH/bin/ccmake /usr/bin/ccmake \
 && ln -sf /opt/cmake-$VERSION-$ARCH/bin/cmake /usr/bin/cmake \
 && ln -sf /opt/cmake-$VERSION-$ARCH/bin/cmake-gui /usr/bin/cmake-gui \
 && ln -sf /opt/cmake-$VERSION-$ARCH/bin/cpack /usr/bin/cpack \
 && ln -sf /opt/cmake-$VERSION-$ARCH/bin/ctest /usr/bin/ctest
