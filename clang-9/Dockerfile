ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN wget -q -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && CODENAME=$(lsb_release -cs) \
 && echo "deb http://apt.llvm.org/${CODENAME}/ llvm-toolchain-${CODENAME}-9 main" >> /etc/apt/sources.list \
 && echo "deb-src http://apt.llvm.org/${CODENAME}/ llvm-toolchain-${CODENAME}-9 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    clang-tidy \
    clang-9 \
    clang-9-doc \
    clang-format-9 \
    clangd-9 \
    libc++-9-dev \
    libc++abi-9-dev \
    libclang-9-dev \
    libclang-common-9-dev \
    libclang1-9 \
    libfuzzer-9-dev \
    libllvm-9-ocaml-dev \
    libllvm9 \
    libomp-9-dev \
    lld-9 \
    lldb-9 \
    llvm-9 \
    llvm-9-dev \
    llvm-9-doc \
    llvm-9-examples \
    llvm-9-runtime \
    python-clang-9 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-9 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-9 100

ENV CC clang
ENV CXX clang++
