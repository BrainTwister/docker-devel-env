ARG VERSION

FROM alpine:$VERSION

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apk add --no-cache \
    curl \
    git \
    git-svn \
    make \
    ninja \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-tk \
    vim \
    wget

RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 1

RUN pip install --upgrade pip \
 && hash -r pip3 \
 && pip install \
    cmake==3.18.0 \
    conan==1.28.0 \
    pyyaml==5.3.1

# Set aliases
COPY aliases /tmp/
RUN cat /tmp/aliases >> /etc/bash.bashrc && rm -f /tmp/aliases

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
