ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    firefox \
    libgtk-3-0 \
    openjdk-11-jdk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ENV INSTALLATION_DIR /usr/local

# Needed for string substitution
SHELL ["/bin/bash", "-c"]
RUN curl -L http://download.eclipse.org/technology/epp/downloads/release/${VERSION/./-}/R/eclipse-cpp-${VERSION/./-}-R-linux-gtk-x86_64.tar.gz | tar xz -C $INSTALLATION_DIR

# Install plugins
ADD install_plugins.py plugins-$VERSION.yml /config/
RUN /config/install_plugins.py -p /config/plugins-$VERSION.yml

ADD entrypoint_eclipse.sh /entrypoint.d/

CMD "$INSTALLATION_DIR/eclipse/eclipse"
