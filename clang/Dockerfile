ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION
#ARG MAJOR_VERSION="${VERSION%.*}"

RUN wget -q -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && CODENAME=$(lsb_release -cs) \
 && echo "deb http://apt.llvm.org/$CODENAME/ llvm-toolchain-$CODENAME-$VERSION main" >> /etc/apt/sources.list \
 && echo "deb-src http://apt.llvm.org/$CODENAME/ llvm-toolchain-$CODENAME-$VERSION main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    clang-tidy \
    clang-$VERSION \
    clang-$VERSION-doc \
    clang-format-$VERSION \
    libclang-$VERSION-dev \
    libclang-common-$VERSION-dev \
    libclang1-$VERSION \
    libfuzzer-$VERSION-dev \
    libllvm$VERSION \
    lld-$VERSION \
    lldb-$VERSION \
    llvm-$VERSION \
    llvm-$VERSION-dev \
    llvm-$VERSION-doc \
    llvm-$VERSION-examples \
    llvm-$VERSION-runtime

RUN if [ "${VERSION%.*}" -gt "5" ] ; then \
        apt-get install -y --no-install-recommends \
        libc++-$VERSION-dev \
        libc++abi-$VERSION-dev \
        libomp-$VERSION-dev \
        libllvm-$VERSION-ocaml-dev ; \
    else \
        apt-get install -y --no-install-recommends \
        libomp-dev ; \
    fi

RUN if [ "${VERSION%.*}" -gt "7" ] ; then \
        apt-get install -y --no-install-recommends \
        clangd-$VERSION ; \
    fi

RUN if [ "${VERSION%.*}" -gt "9" ] ; then \
        apt-get install -y --no-install-recommends \
        python3-clang-$VERSION ; \
    else \
        apt-get install -y --no-install-recommends \
        python-clang-$VERSION ; \
    fi

RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-$VERSION 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-$VERSION 100

ENV CC clang
ENV CXX clang++
