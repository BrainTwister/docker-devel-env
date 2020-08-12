#!/usr/bin

# Add user to docker group and start service
usermod -aG docker $USER_NAME
start-stop-daemon -SbCv -x /usr/bin/dockerd -- -H unix://
