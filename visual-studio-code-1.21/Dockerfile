ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ENV DOWNLOAD_URL https://go.microsoft.com/fwlink/?LinkID=760868

RUN wget "$DOWNLOAD_URL" -O visual-studio-code.deb \
 && ( dpkg -i visual-studio-code.deb || true ) \
 && apt-get install -f \
 && dpkg -i visual-studio-code.deb

# Create user
RUN mkdir -p /home/coder \
 && groupadd -r coder \
 && useradd -r -g coder -d /home/coder -s /sbin/nologin -c "Docker image user" coder
RUN chown coder:coder /home/coder

# Set user and home
USER coder
WORKDIR /home/coder

ENTRYPOINT ["code"]
