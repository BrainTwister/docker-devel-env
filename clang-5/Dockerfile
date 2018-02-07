ARG BASE_IMAGE

FROM braintwister/$BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y clang-5.0 lldb-5.0 lld-5.0\
 && apt-get clean \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-5.0 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-5.0 100

ENV CC clang
ENV CXX clang++
