ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION

WORKDIR /tmp

RUN wget -q https://github.com/google/googletest/archive/release-$VERSION.tar.gz \
 && tar xf release-$VERSION.tar.gz \
 && rm release-$VERSION.tar.gz \
 && cd googletest-release-$VERSION \
 && mkdir build \
 && cd build \
 && cmake -DCMAKE_INSTALL_PREFIX=/opt/googletest-$VERSION .. \
 && make -j \
 && make install \
 && rm -r /tmp/googletest-release-$VERSION

WORKDIR /

ENV GTEST_ROOT /opt/googletest-$VERSION
