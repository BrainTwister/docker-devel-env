ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

WORKDIR /tmp

RUN wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz \
 && tar xf release-1.8.0.tar.gz \
 && rm release-1.8.0.tar.gz \
 && cd googletest-release-1.8.0 \
 && mkdir build \
 && cd build \
 && cmake -DCMAKE_INSTALL_PREFIX=/opt/googletest-1.8.0 .. \
 && make -j \
 && make install \
 && rm -r /tmp/googletest-release-1.8.0

WORKDIR /

ENV GTEST_ROOT /opt/googletest-1.8.0
