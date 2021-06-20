ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION

ENV SHELL /bin/bash
ENV DOWNLOAD_URL https://update.code.visualstudio.com/$VERSION/linux-deb-x64/stable

RUN wget -q "$DOWNLOAD_URL" -O code.deb

RUN apt-get update \
 && apt-get install -y \
    firefox \
    libdrm2 \
    libgbm1 \
    libxcb-dri3-0 \
    libx11-xcb1 \
    ./code.deb \
 && apt-get clean \
 && rm ./code.deb \
 && rm -rf /var/lib/apt/lists/*

ADD keep_running.sh /postprocess.d/

CMD ["code", "--no-xshm"]
