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

WORKDIR /opt

RUN wget http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.14.linux.bin.tar.gz \
 && tar xf doxygen-1.8.14.linux.bin.tar.gz \
 && rm doxygen-1.8.14.linux.bin.tar.gz \
 && ln -sf /opt/doxygen-1.8.14/bin/doxygen /usr/bin/doxygen

WORKDIR /
