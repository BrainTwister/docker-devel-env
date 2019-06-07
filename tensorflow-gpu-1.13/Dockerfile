ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG BAZEL_VERSION=0.21.0
ARG TENSORFLOW_VERSION=1.13.1

RUN ln -snf /usr/bin/python3 /usr/bin/python

RUN apt-get update \
 && apt-get install -y \
    libcudnn7 \
    libcudnn7-dev \
    python3-tk \
    unzip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install \
    graphviz \
    matplotlib \
    mock \
    numpy \
    pydot \
    seaborn \
    setuptools \
    six \
    sklearn \
    stn \
    wheel

RUN pip install --no-deps \
    keras_applications==1.0.6 \
    keras_preprocessing==1.0.5

RUN wget https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh \
 && chmod +x bazel-$BAZEL_VERSION-installer-linux-x86_64.sh \
 && ./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh

SHELL ["/bin/bash", "-c"]
RUN source /usr/local/lib/bazel/bin/bazel-complete.bash

RUN git clone https://github.com/tensorflow/tensorflow \
 && cd tensorflow \
 && git checkout v$TENSORFLOW_VERSION \
 && ./configure \
 && bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package \
 && ./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg \
 && pip install /tmp/tensorflow_pkg/tensorflow-$TENSORFLOW_VERSION.whl

