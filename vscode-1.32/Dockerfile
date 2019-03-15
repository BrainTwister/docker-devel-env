ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ENV SHELL /bin/bash
ENV DOWNLOAD_URL https://vscode-update.azurewebsites.net/1.32.1/linux-deb-x64/stable

RUN wget -q "$DOWNLOAD_URL" -O code.deb

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    libasound2 \
    libgtk-3-0 \
    libxtst6 \
    libx11-xcb-dev \
    ./code.deb \
 && apt-get clean \
 && rm ./code.deb \
 && rm -rf /var/lib/apt/lists/*

ADD keep_running.sh /postprocess.d/

CMD ["code"]
