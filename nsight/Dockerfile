ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    firefox \
    libgtk2.0-0 \
    openjdk-11-jdk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN if [ $(grep DISTRIB_RELEASE=16.04 /etc/lsb-release | wc -l) -eq 1 ]; then \
        apt-get install -y --no-install-recommends \
        openjdk-8-jdk \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*
    fi

RUN if [ $(grep DISTRIB_RELEASE=18.04 /etc/lsb-release | wc -l) -eq 1 ]; then \
        apt-get install -y --no-install-recommends \
        openjdk-11-jdk \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*
    fi

# Install plugins
ADD install_plugins.py plugins.yml /config/
RUN /config/install_plugins.py -p /config/plugins.yml

CMD "/usr/local/cuda/bin/nsight"
