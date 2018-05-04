ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    python-pip \
    python-setuptools \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && hash -r pip \
 && pip install -I conan==1.3

# Add conan repositories for root
ADD conan_add_repositories.sh /config/
RUN /config/conan_add_repositories.sh
