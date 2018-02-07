ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y \
    curl \
    freeglut3-dev \
    git \
    libfreetype6-dev \
    libgl1-mesa-dev \
    libglew-dev \
    libglm-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    make \
    ninja-build \
    software-properties-common \
    vim \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
