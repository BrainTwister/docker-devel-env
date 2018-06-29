ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    firefox \
    libgtk-3-0 \
    openjdk-11-jdk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/photon/R/eclipse-cpp-photon-R-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN curl -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD "$INSTALLATION_DIR/eclipse/eclipse"
