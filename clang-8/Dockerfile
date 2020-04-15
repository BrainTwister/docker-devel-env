ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN wget -q -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && CODENAME=$(lsb_release -cs) \
 && echo "deb http://apt.llvm.org/${CODENAME}/ llvm-toolchain-${CODENAME}-8 main" >> /etc/apt/sources.list \
 && echo "deb-src http://apt.llvm.org/${CODENAME}/ llvm-toolchain-${CODENAME}-8 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    clang-tidy \
    clang-8 \
    clang-8-doc \
    clang-format-8 \
    #clang-tools-8 \
    clangd-8 \
    libc++-8-dev \
    libc++abi-8-dev \
    libclang-8-dev \
    libclang-common-8-dev \
    libclang1-8 \
    libfuzzer-8-dev \
    libllvm-8-ocaml-dev \
    libllvm8 \
    libomp-8-dev \
    lld-8 \
    lldb-8 \
    llvm-8 \
    llvm-8-dev \
    llvm-8-doc \
    llvm-8-examples \
    llvm-8-runtime \
    python-clang-8 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-8 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-8 100

ENV CC clang
ENV CXX clang++
