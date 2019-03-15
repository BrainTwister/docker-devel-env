FROM alpine:3.7

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apk add --no-cache \
    curl \
    git \
    git-svn \
    make \
    ninja \
    vim \
    wget

COPY aliases /tmp/
RUN cat /tmp/aliases >> /etc/bash.bashrc && rm -f /tmp/aliases

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash"]
