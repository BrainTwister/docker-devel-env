ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION=1.18

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    python-setuptools \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip \
 && hash -r pip3 \
 && pip3 install -I conan~=$VERSION

# Add entrypoint
ADD conan_add_repositories.sh /entrypoint.d/
