ARG VERSION

FROM ubuntu:$VERSION

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG TIMEZONE='Europe/Berlin'
ARG DEBIAN_FRONTEND=noninteractive

RUN echo $TIMEZONE > /etc/timezone && \
  apt-get update && apt-get install -y tzdata && \
  rm /etc/localtime && \
  ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && \
  dpkg-reconfigure -f noninteractive tzdata && \
  apt-get clean

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    dirmngr \
    git \
    git-svn \
    gpg-agent \
    make \
    ninja-build \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-tk \
    software-properties-common \
    sudo \
    vim \
    wget

RUN if [ $(grep DISTRIB_RELEASE=18.04 /etc/lsb-release | wc -l) -eq 1 ]; then \
        apt-get install -y --no-install-recommends \
        libgbm-dev; \
    fi

RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 1

RUN pip install --upgrade pip \
 && hash -r pip3 \
 && pip install \
    cmake==3.20.3 \
    conan==1.37.2 \
    pyyaml==5.4.1

# Set aliases
COPY aliases /tmp/
RUN cat /tmp/aliases >> /etc/bash.bashrc && rm -f /tmp/aliases

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
