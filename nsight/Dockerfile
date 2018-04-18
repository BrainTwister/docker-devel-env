ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
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

# Install plugins
ADD install_plugins.py plugins.yml /config/
RUN /config/install_plugins.py -p /config/plugins.yml

# Create eclipse user
RUN mkdir -p /home/eclipse \
 && groupadd -r eclipse \
 && useradd -r -g eclipse -d /home/eclipse -s /sbin/nologin -c "Docker image user" eclipse
RUN chown eclipse:eclipse /home/eclipse

# Add eclipse user to docker group
RUN grep -qF 'docker' /etc/group && usermod -aG docker eclipse || true

# Set eclipse user
USER eclipse
WORKDIR /home/eclipse

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/local/cuda/bin/nsight"]
