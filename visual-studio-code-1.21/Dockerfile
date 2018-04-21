ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ENV DOWNLOAD_URL https://go.microsoft.com/fwlink/?LinkID=760868

RUN wget "$DOWNLOAD_URL" -O visual-studio-code.deb \
 && ( dpkg -i visual-studio-code.deb || true ) \
 && apt-get install -f \
 && dpkg -i visual-studio-code.deb

ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

CMD "code"
