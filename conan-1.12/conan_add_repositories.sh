#!/bin/bash

# Add conan repositories of conan base module for eclipse user
chroot --userspec=$USER_NAME / \
  conan remote add braintwister https://api.bintray.com/conan/braintwister/conan 
  conan remote add conan-community https://api.bintray.com/conan/conan-community/conan
  conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
