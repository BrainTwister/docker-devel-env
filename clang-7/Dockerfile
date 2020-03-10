ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN wget -q -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-7 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    clang-tidy-7 \
    clang-7 \
    clang-7-doc \
    clang-format-7 \
    clang-tools-7 \
    libc++-7-dev \
    libc++abi-7-dev \
    libclang-7-dev \
    libclang-common-7-dev \
    libclang1-7 \
    libfuzzer-7-dev \
    libllvm-7-ocaml-dev \
    libllvm7 \
    libomp-7-dev \
    lld-7 \
    lldb-7 \
    llvm-7 \
    llvm-7-dev \
    llvm-7-doc \
    llvm-7-examples \
    llvm-7-runtime \
    python-clang-7 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-7 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-7 100

ENV CC clang
ENV CXX clang++
