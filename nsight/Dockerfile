ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    firefox \
    libgtk2.0-0 \
    openjdk-8-jdk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install plugins
ADD install_plugins.py plugins.yml /config/
RUN /config/install_plugins.py -p /config/plugins.yml

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD "/usr/local/cuda/bin/nsight"
