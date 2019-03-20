ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    firefox \
    libgtk-3-0

RUN if [ $(grep DISTRIB_RELEASE=16.04 /etc/lsb-release | wc -l) -eq 1 ]; then \
        apt-get install -y --no-install-recommends \
        openjdk-8-jdk; \
    fi

RUN if [ $(grep DISTRIB_RELEASE=18.04 /etc/lsb-release | wc -l) -eq 1 ]; then \
        apt-get install -y --no-install-recommends \
        openjdk-11-jdk; \
    fi

RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install -I jinja2 

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/2019-03/R/eclipse-cpp-2019-03-R-linux-gtk-x86_64.tar.gz
ENV SHA512 32a74771dd9588ee2fd1b2a92ea0d6b875599eaad8c4a9b2cd85f3a45a545902332a1cb2fc29f984535339039534b20e346c0f547a16432759b74b4c2e056247
ENV INSTALLATION_DIR /usr/local

RUN curl -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR

# Install plugins
ADD install_plugins.py plugins.yml /config/
RUN /config/install_plugins.py -p /config/plugins.yml

ADD entrypoint_eclipse.sh /entrypoint.d/

CMD "$INSTALLATION_DIR/eclipse/eclipse"
