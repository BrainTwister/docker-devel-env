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

RUN pip3 install --upgrade pip \
 && hash -r pip3 \
 && pip3 install -I pyyaml~=3.12 

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/oxygen/3/eclipse-cpp-oxygen-3-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN curl -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR

# Install plugins
ADD install_plugins.py plugins.yml /config/
RUN /config/install_plugins.py -p /config/plugins.yml

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD "$INSTALLATION_DIR/eclipse/eclipse"
