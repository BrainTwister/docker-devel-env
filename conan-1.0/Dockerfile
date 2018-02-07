ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    python-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install -I setuptools \
 && pip install -I conan==1.0

RUN conan remote add conan-community https://api.bintray.com/conan/conan-community/conan \
 && conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
