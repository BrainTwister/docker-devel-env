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

RUN if [ $(grep DISTRIB_RELEASE=16.04 /etc/lsb-release | wc -l) -eq 1 ]; then \
        apt-get install -y --no-install-recommends \
        openjdk-8-jdk \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
    fi

RUN if [ $(grep DISTRIB_RELEASE=18.04 /etc/lsb-release | wc -l) -eq 1 ]; then \
        apt-get install -y --no-install-recommends \
        openjdk-11-jdk \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
    fi

RUN pip3 install -I jinja2 

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/2018-12/R/eclipse-cpp-2018-12-R-linux-gtk-x86_64.tar.gz
#ENV DOWNLOAD_URL http://ftp.fau.de/eclipse/technology/epp/downloads/release/2018-12/R/eclipse-cpp-2018-12-linux-gtk-x86_64.tar.gz
ENV SHA512 4d93be6701169021315439e8f8ba25c4a33e584487443c10ad23e81748838ec64e4fa6540d6ec03a60d1dc313b2b6b57f8edfdabe5895b9d82d084725cda7d8c
ENV INSTALLATION_DIR /usr/local

RUN curl -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR

# Install plugins
ADD install_plugins.py plugins.yml /config/
RUN /config/install_plugins.py -p /config/plugins.yml

ADD entrypoint_eclipse.sh /root/entrypoint.d/

CMD "$INSTALLATION_DIR/eclipse/eclipse"
