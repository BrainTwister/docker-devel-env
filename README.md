[![Build Status](https://jenkins.braintwister.eu/buildStatus/icon?job=BrainTwister/docker-devel-env/master)](https://jenkins.braintwister.eu/job/BrainTwister/job/docker-devel-env/job/master/)

# Docker Development Environment

Fast, reproducible, and portable software development environments

Copyright (C) 2021 Bernd Doser, bernd.doser@braintwister.eu

All rights reserved.

BrainTwister docker-devel-env is free software made available under the [MIT License](http://opensource.org/licenses/MIT).
For details see [the license file](LICENSE).


## Advantages

 * Fast build and execution compared to virtual machines
 * Portability: Same environment on different machines, platforms, and operating systems
 * Reproducible behaviors
 * Economical consumption of resources
 * Identical environment for development IDE and continuous integration
 * Easy provisioning of images 


## Docker images

Each directory correspond to an environment module. They can stick together as
a chain:

`module1` - `module2` - `module3` - `...`

The image `module1-module2-module3` is using the image `module1-module2` as
base, which will be set using the build-time variable `BASE_IMAGE`. For
example the image `ubuntu-20.04-clang-11` will be build with

```bash
cd clang-11
docker build -t braintwister/ubuntu-20.04-clang-11 --build-arg BASE_IMAGE=braintwister/ubuntu-20.04 .
```

Please find a list of available images at [images.yml](images.yml).
The images in the list will be build automatically with
[Jenkins](https://jenkins.braintwister.eu/job/BrainTwister/job/docker-devel-env/)
and pushed to [DockerHub](https://hub.docker.com/u/braintwister/dashboard/).

The docker images can be pulled with

```bash
docker pull braintwister/<image-name>
```

![Docker scheme](https://braintwister.eu/images/docker-devel-env.jpg?)

## Eclipse IDE
### Eclipse IDE for C++ development

A ready-for-action eclipse IDE with 

 * clang
 * CMake
 * conan.io

installed can be started by

```bash
docker run -d -v /tmp/.X11-unix:/tmp/.X11-unix:ro -e DISPLAY --privileged \
  braintwister/ubuntu-20.04-clang-11-eclipse-cpp-2021.03
```

or using docker-compose by

```yaml
version: "3"
services:

  eclipse:
    image: braintwister/ubuntu-20.04-clang-11-eclipse-cpp-2021.03
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro
    environment:
      - DISPLAY
    privileged: true
```

The mount of the X11 socket file (/tmp/.X11-unix) and the definition of the
environment variable `DISPLAY` induce the application within the container to
send the rendering instructions to the host X server. To allow the container to
use the host display, the command `xhost +local:` must be executed on the host
before starting the container. The privileged mode is needed for debugging with
gdb.


### Eclipse IDE for CUDA development

First of all [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) version 2
must be installed and the runtime attribute must be set to `nvidia`, that the
container get access to the host GPU card. The nvidia runtime attribute is
currently only available at docker-compose version 2.3.

For CUDA development the NVIDIA IDE
[nsight](https://developer.nvidia.com/nsight-eclipse-edition) is highly
recommended, because it provides special support for code editing, debugging,
and profiling. The version of nsight is not adjustable, as it depends to the
version of the cuda module.

```yaml
version: "2.3"
services:

  eclipse:
    image: braintwister/ubuntu-20.04-cuda-devel-11.0-clang-9-nsight
    runtime: nvidia
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro
    environment:
      - DISPLAY
    privileged: true
```


### Eclipse IDE for embedded development

For embedded programming you have to bind the host serial port (here:
/dev/ttyACM0) to get a connection to the embedded platform (Arduino, ESP32,
...).

```yaml
version: "3"
services:

  eclipse:
    image: braintwister/ubuntu-20.04-clang-11-eclipse-cpp-2021.03
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro
      - /dev/ttyACM0:/dev/ttyACM0
    environment:
      - DISPLAY
    privileged: true
```

## Visual Studio Code

The Visual Studio Code IDE can be started by using

```bash
docker run -d -v /tmp/.X11-unix:/tmp/.X11-unix:ro -e DISPLAY --privileged \
  braintwister/ubuntu-20.04-clang-11-vscode-1.57.1
```


## Persistent storage

The data in the container can be made persistent by using a [docker
volume](https://docs.docker.com/storage/volumes/) `home` for the home directory
`/home/user`.

```yaml
version: "3"
services:

  eclipse:
    image: braintwister/ubuntu-20.04-clang-11-eclipse-cpp-2021.03
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro 
      - home:/home/user
    environment:
      - DISPLAY
    privileged: true

volumes:
  home:
```


## Project-assigned development environment

The docker development environment can be directly stored within the source
code repository and is able to bind the working directory of the source code
into the development container. Therefore, the user in the container must be
the owner of the source code working directory on the host.  The user in the
container can be set with the environment variables `USER_ID`, `GROUP_ID`,
`USER_NAME`, and `GROUP_NAME`. In the following example the docker-compose file
is stored in the root directory of a git repository. Starting `docker-compose
up -d` in the root directory the current directory `.` will be bound to
`/home/${USER_NAME}/git/${PROJECT}`. It is recommended to set the variables in
an extra file `.env`, which is not controlled by the source control management,
so that the docker-compose file must not be changed.

```yaml
version: "3"
services:

  vscode:
    image: braintwister/ubuntu-20.04-clang-11-vscode-1.57.1
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro 
      - home:/home/${USER_NAME}
      - .:/home/${USER_NAME}/git/${PROJECT}
    environment:
      - DISPLAY
      - USER_ID=${USER_ID}
      - GROUP_ID=${GROUP_ID}
      - USER_NAME=${USER_NAME}
      - GROUP_NAME=${GROUP_NAME}
    privileged: true

volumes:
  home:
```

The `.env`-file can be generated by

```bash
cat << EOT > .env 
PROJECT=`basename "$PWD"`
USER_ID=`id -u $USER`
GROUP_ID=`id -g $USER`
USER_NAME=`id -un $USER`
GROUP_NAME=`id -gn $USER`
EOT
```


## Jenkins build container

A declarative Jenkinsfile can look like

```groovy
pipeline {

  agent {
    docker {
      image 'braintwister/ubuntu-20.04-clang-11'
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

## TensorFlow

For machine learning development we provide with an installation of the
open-source framework [TensorFlow](https://github.com/tensorflow/tensorflow)
using the latest cuda development drivers.

Although the usage of GPUs is highly recommended
`braintwister/ubuntu-20.04-cuda-devel-11.0-tensorflow-gpu-2.0`, a CPU version is
also available `braintwister/ubuntu-20.04-tensorflow-2.0`.

Start a plain container with

```bash
docker run -it --runtime=nvidia braintwister/ubuntu-20.04-cuda-devel-11.0-tensorflow-gpu-2.0
```

[TensorBoard](https://www.tensorflow.org/guide/summaries_and_tensorboard)
is available at `localhost:6006`, if `-p 6006:6006` was added to the `docker
run` command and tensorboard was launched within the container.


### TensorFlow with Visual Studio Code

To allow the container to use the host display, the command `xhost +local:`
must be executed on the host before starting the container.

```bash
docker run -d --runtime=nvidia -e DISPLAY \
  braintwister/ubuntu-20.04-cuda-devel-11.0-tensorflow-gpu-2.0-vscode-1.57.1
```


### TensorFlow with Jupyter

Start the container with

```bash
docker run --runtime=nvidia -p 8888:8888 \
  braintwister/ubuntu-20.04-cuda-devel-11.0-tensorflow-gpu-2.0-jupyter-1.0
```

and open localhost:8888 on your host browser.

