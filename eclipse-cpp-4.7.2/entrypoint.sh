#!/bin/bash

# Add conan repositories of conan base module for eclipse user
if [ -f /config/conan_add_repositories.sh ]
then
  /config/conan_add_repositories.sh
fi

$INSTALLATION_DIR/eclipse/eclipse
