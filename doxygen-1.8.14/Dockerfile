ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y \
    graphviz \
    mscgen \
    texlive \
    texlive-lang-english \
    texlive-latex-extra \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ARG VERSION=1.8.14

RUN wget https://sourceforge.net/projects/doxygen/files/rel-$VERSION/doxygen-$VERSION.linux.bin.tar.gz \
 && tar xf doxygen-$VERSION.linux.bin.tar.gz \
 && rm doxygen-$VERSION.linux.bin.tar.gz \
 && mv doxygen-$VERSION /opt \
 && ln -sf /opt/doxygen-$VERSION/bin/doxygen /usr/bin/doxygen
