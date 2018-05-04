FROM braintwister/ubuntu-16.04-docker-17.12

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    python3 \
    python3-setuptools \
    python3-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && hash -r pip \
 && pip install -I pyyaml==3.12 
