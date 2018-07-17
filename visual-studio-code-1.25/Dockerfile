ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ENV DOWNLOAD_URL https://vscode-update.azurewebsites.net/1.25.0/linux-deb-x64/stable

RUN wget "$DOWNLOAD_URL" -O code_1.25.0-1530796411_amd64.deb

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    libgtk2.0-0 \
    libx11-xcb-dev \
    ./code_1.25.0-1530796411_amd64.deb \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD "code"
