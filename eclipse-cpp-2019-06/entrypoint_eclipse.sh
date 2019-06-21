#!/bin/bash

# Give permission to access /dev/tty*
usermod -a -G dialout $USER_NAME

# Set user as owner of eclipse installation directory to allow updates of plugins
chown -R $USER_NAME:$GROUP_NAME $INSTALLATION_DIR/eclipse
