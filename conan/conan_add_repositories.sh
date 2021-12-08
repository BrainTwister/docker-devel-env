#!/bin/bash

# Add conan repositories of conan base module for eclipse user
chroot --userspec=$USER_NAME / \
  conan remote add braintwister https://braintwister.jfrog.io/artifactory/api/conan/braintwister-conan
