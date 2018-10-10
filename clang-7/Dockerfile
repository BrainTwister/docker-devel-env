ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-7 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    clang-7 \
    libomp-dev \
    lldb-7 \
    lld-7 \
    gdb \
    linux-tools-generic \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-7 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-7 100

ENV CC clang
ENV CXX clang++
