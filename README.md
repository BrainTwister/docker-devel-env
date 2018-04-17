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
example the image `ubuntu-16.04-cmake-3.10` will be build with

```bash
cd cmake-3.10
docker build -t braintwister/ubuntu-16.04-cmake-3.11 --build-arg BASE_IMAGE=braintwister/ubuntu-16.04 .
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
docker run -e /tmp/.X11-unix:/tmp/.X11-unix:ro -D DISPLAY braintwister/ubuntu-16.04-cmake-3.11-gcc-7-conan-1.2-docker-18.03-eclipse-cpp-4.7.3
```

or using docker-compose by

```yaml
version: "3"
services:

  eclipse:
    image: braintwister/ubuntu-16.04-cmake-3.11-gcc-7-conan-1.2-docker-18.03-eclipse-cpp-4.7.3
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro 
      - home:/home/eclipse
    environment:
      - DISPLAY
    privileged: true

volumes:
  home:
```

The mount of the X11 socket file (/tmp/.X11-unix) and the definition of the
environment variable `DISPLAY` induce the application within the conainer to
send the rendering instructions to the host X server. To allow the container to
use the host display, the command `xhost +local:` must be executed on the host
before starting the container. The privileged mode is needed for debugging with
gdb.


## Eclipse IDE with CUDA

First of all [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) must be
installed to connect the host GPU card to the container.

```yaml
version: "2.3"
services:

  eclipse:
    image: braintwister/ubuntu-16.04-cuda-9.1-cmake-3.11-gcc-7-conan-1.2-nsight
    runtime: nvidia
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro
      - home:/home/eclipse
    environment:
      - DISPLAY
    privileged: true

volumes:
  home:
```

The runtime must be set to `nvidia`, which is currently only supported by
docker-compose version 2.3. As IDE NVIDIA nsight is recommended, which has
special support for CUDA code editing, debugging, and profiling. The nsight
version depends to the cuda version.


## Eclipse IDE for embedded development

To use the [Eclipse CDT Arduino
plugin](https://marketplace.eclipse.org/content/eclipse-c-ide-arduino) simply
choose the eclipse-arduino module and bind the serial port of your Arduino
connection (here: /dev/ttyACM0):

```yaml
version: "3"
services:

  eclipse:
    image: braintwister/ubuntu-16.04-cmake-3.11-gcc-7-conan-1.2-docker-18.03-eclipse-arduino-4.7.3
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
      image 'braintwister/ubuntu-16.04-cmake-3.11-clang-6-conan-1.2'
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
