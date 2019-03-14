ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION="0.2.3"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    libncurses5-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN cd opt && \
    wget -q https://github.com/Syllo/nvtop/archive/$VERSION.tar.gz && \
    tar xf $VERSION.tar.gz && \
    rm $VERSION.tar.gz && \
    mkdir -p nvtop-$VERSION/build && \
    cd nvtop-$VERSION/build && \
    cmake .. -DNVML_RETRIEVE_HEADER_ONLINE=True && \
    make && \
    make install
