ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    gitg=$VERSION \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

