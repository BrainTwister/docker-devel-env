ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    firefox \
    libgtk2.0-0 \
    make \
    python3-setuptools \
    openjdk-8-jdk \
    python3-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install -I pyyaml==3.12 

# Install gosu
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

# Install plugins
ADD install_plugins.py plugins.yml /config/
RUN /config/install_plugins.py -p /config/plugins.yml

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/local/cuda/bin/nsight"]
