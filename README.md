# Docker Development Environment

Docker enables a great way for fast, small, reproducible, and portable software development environments.

The advantages are:

 * Fast build and execution of containers, especially compared to virtual machines
 * Very economical consumption of resources
 * Portability: Same environment on different machines and different platforms (also different operating systems)
 * Identical environment for IDE and continuous integration
 * Easy provisioning 
 * Reproducible behaviors


## Requirements

 * docker
 * docker-compose (recommended)


## Docker images

Each directory correspond to an environment module. They can stick together as
a chain:

`module1` - `module2` - `module3` - `...`

The image `module1-module2-module3` is using the image `module1-module2` as
base, which will be set using the build-time variable `BASE_IMAGE`. For
example the image 'ubuntu-16.04-cmake-3.10' will be build with

```bash
cd cmake-3.10
docker build -t braintwister/ubuntu-16.04-cmake-3.10 --build-arg BASE_IMAGE=braintwister/ubuntu-16.04 .
```

Please find a list of available images at [images.yml](images.yml).
The docker images can be pulled with

```bash
docker pull braintwister/module1-module2-module3
```


## Eclipse IDE

A ready-for-action eclipse IDE with 

 * CMake
 * GCC
 * conan.io
 * docker-engine

installed can be started by

```bash
docker run -e /tmp/.X11-unix:/tmp/.X11-unix:ro -D DISPLAY braintwister/ubuntu-16.04-cmake-3.10-gcc-7-conan-1.0-docker-17.12-eclipse-cpp-4.7.2
```

or using docker-compose by

```yaml
version: "3"
services:

  eclipse:
    image: braintwister/ubuntu-16.04-cmake-3.10-gcc-7-conan-1.0-docker-17.12-eclipse-cpp-4.7.2
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro 
      - home:/home/eclipse
    environment:
      - DISPLAY
    privileged: true

volumes:
  home:
```

The privileged container mode is needed for debugging with gdb.

## Eclipse IDE for embedded development

To use the [Eclipse CDT Arduino
plugin](https://marketplace.eclipse.org/content/eclipse-c-ide-arduino) simply
choose the eclipse-arduino module and bind the serial port of your Arduino
connection (here: /dev/ttyACM0):

```yaml
version: "3"
services:

  eclipse:
    image: braintwister/ubuntu-16.04-cmake-3.10-gcc-7-conan-1.0-docker-17.12-eclipse-arduino-4.7.2
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro
      - /dev/ttyACM0:/dev/ttyACM0
      - home:/home/eclipse
    environment:
      - DISPLAY
    privileged: true

volumes:
  home:
```

## Jenkins build container

A declarative Jenkinsfile can look like

```groovy
pipeline {

  agent {
    docker {
      image 'braintwister/ubuntu-16.04-cmake-3.10-clang-6-conan-1.0'
    }
  }

  stages {
    stage('Conan') {
      steps {
        sh 'conan install .'
      }
    }
    stage('CMake') {
      steps {
        sh 'cmake .'
      }
    }
    stage('Build') {
      steps {
        sh 'make all'
      }
    }
    stage('Test') {
      steps {
        sh 'make test'
      }
    }
  }
}
```
