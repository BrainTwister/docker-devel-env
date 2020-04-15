ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN wget -q -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && CODENAME=$(lsb_release -cs) \
 && echo "deb http://apt.llvm.org/${CODENAME}/ llvm-toolchain-${CODENAME}-10 main" >> /etc/apt/sources.list \
 && echo "deb-src http://apt.llvm.org/${CODENAME}/ llvm-toolchain-${CODENAME}-10 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    clang-tidy \
    clang-10 \
    clang-10-doc \
    clang-format-10 \
    clangd-10 \
    libc++-10-dev \
    libc++abi-10-dev \
    libclang-10-dev \
    libclang-common-10-dev \
    libclang1-10 \
    libfuzzer-10-dev \
    libllvm-10-ocaml-dev \
    libllvm10 \
    libomp-10-dev \
    lld-10 \
    lldb-10 \
    llvm-10 \
    llvm-10-dev \
    llvm-10-doc \
    llvm-10-examples \
    llvm-10-runtime \
    python3-clang-10 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-10 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-10 100

ENV CC clang
ENV CXX clang++
