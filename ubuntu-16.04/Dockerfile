FROM ubuntu:16.04

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    dirmngr \
    git \
    git-svn \
    gpg-agent \
    make \
    ninja-build \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    software-properties-common \
    vim \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip \
 && hash -r pip3 \
 && pip3 install -I pyyaml~=3.12 

# Set aliases
COPY aliases /tmp/
RUN cat /tmp/aliases >> /etc/bash.bashrc && rm -f /tmp/aliases
