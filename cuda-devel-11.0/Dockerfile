ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg2 curl ca-certificates && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub | apt-key add - && \
    echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda.list && \
    apt-get purge --autoremove -y curl && \
    rm -rf /var/lib/apt/lists/*

# For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-11-0=11.0.171-1 \
    cuda-compat-11-0 \
    && ln -s cuda-11.0 /usr/local/cuda && \
    rm -rf /var/lib/apt/lists/*

# Required for nvidia-docker v1
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=11.0 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441"

# CUDA devel
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-nvml-dev-11-0=11.0.167-1 \
    cuda-command-line-tools-11-0=11.0.1-1 \
    cuda-nvcc-11-0=11.0.167-1 \
    cuda-nvprof-11-0=11.0.167-1 \
    libnpp-dev-11-0=11.0.0.191-1 \
    cuda-libraries-dev-11-0=11.0.1-1 \
    cuda-minimal-build-11-0=11.0.1-1 \
    libcublas-dev-11-0=11.0.0.191-1 \
    libcusparse-11-0=11.0.0.191-1 \
    libcusparse-dev-11-0=11.0.0.191-1 \
    && rm -rf /var/lib/apt/lists/*

RUN apt update && apt install curl xz-utils -y --no-install-recommends && NCCL_DOWNLOAD_SUM=d112b722bf557cff96d571ac3386e4f539be7b3e9412561bde59b0ad6e59263d && \
    curl -fsSL https://developer.download.nvidia.com/compute/redist/nccl/v2.7/nccl_2.7.3-1+cuda11.0_x86_64.txz -O && \
    echo "$NCCL_DOWNLOAD_SUM  nccl_2.7.3-1+cuda11.0_x86_64.txz" | sha256sum -c - && \
    tar --no-same-owner --keep-old-files --lzma -xvf  nccl_2.7.3-1+cuda11.0_x86_64.txz -C /usr/local/cuda/include/ --strip-components=2 --wildcards '*/include/*' && \
    tar --no-same-owner --keep-old-files --lzma -xvf  nccl_2.7.3-1+cuda11.0_x86_64.txz -C /usr/local/cuda/lib64/ --strip-components=2 --wildcards '*/lib/libnccl.so' && \
    rm nccl_2.7.3-1+cuda11.0_x86_64.txz && \
    ldconfig && rm -rf /var/lib/apt/lists/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs:$LIBRARY_PATH

# CUDA devel cudnn
ENV CUDNN_VERSION 8.0.0.180

LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg2 curl ca-certificates

RUN CUDNN_DOWNLOAD_SUM=68558bfa5d1dd6d0300dacaea6ad66ed516ea7dfea01343bd552e6efa107b44c && \
    curl -fsSL https://developer.download.nvidia.com/compute/redist/cudnn/v8.0.0/Ubuntu18_04-x64/libcudnn8_8.0.0.180-1+cuda11.0_amd64.deb -O && \
    echo "$CUDNN_DOWNLOAD_SUM  libcudnn8_8.0.0.180-1+cuda11.0_amd64.deb" | sha256sum -c - && \
    dpkg -i libcudnn8_8.0.0.180-1+cuda11.0_amd64.deb && \
    rm -f libcudnn8_8.0.0.180-1+cuda11.0_amd64.deb

RUN CUDNN_DEV_DOWNLOAD_SUM=8d5430c00d698c2695f4025a0a07975beaecd6c37c8c494acac112977776e332 && \
    curl -fsSL https://developer.download.nvidia.com/compute/redist/cudnn/v8.0.0/Ubuntu18_04-x64/libcudnn8-dev_8.0.0.180-1+cuda11.0_amd64.deb -O && \
    echo "$CUDNN_DEV_DOWNLOAD_SUM  libcudnn8-dev_8.0.0.180-1+cuda11.0_amd64.deb" | sha256sum -c - && \
    dpkg -i libcudnn8-dev_8.0.0.180-1+cuda11.0_amd64.deb && \
    rm -f libcudnn8-dev_8.0.0.180-1+cuda11.0_amd64.deb

RUN rm -rf /var/lib/apt/lists/*

