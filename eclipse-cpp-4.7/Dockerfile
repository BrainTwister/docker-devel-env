ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y \
    curl \
    libgtk2.0-0 \
    make \
    openjdk-8-jdk \
    python3-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip \
 && pip3 install -I pyyaml==3.12 

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/oxygen/R/eclipse-cpp-oxygen-R-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN curl -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR

ADD install_plugins.py \
    plugins.yml \
    /root/

WORKDIR /root
RUN ./install_plugins.py
WORKDIR /

# Create eclipse user
RUN mkdir -p /home/eclipse \
 && groupadd -r eclipse \
 && useradd -r -g eclipse -d /home/eclipse -s /sbin/nologin -c "Docker image user" eclipse
RUN chown eclipse:eclipse /home/eclipse
USER eclipse
WORKDIR /home/eclipse

ENV CONAN_USER_HOME /home/eclipse
RUN conan remote add conan-community https://api.bintray.com/conan/conan-community/conan

CMD $INSTALLATION_DIR/eclipse/eclipse
