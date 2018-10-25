ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION="1.13"

RUN wget https://github.com/linux-test-project/lcov/archive/v$VERSION.tar.gz && \
    tar xf v$VERSION.tar.gz && \
    rm v$VERSION.tar.gz && \
    cd lcov-$VERSION && \
    make install && \
    cd .. && \
    rm -r lcov-$VERSION
