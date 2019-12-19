ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        gnupg2 \
        curl \
        ca-certificates \
 && curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub | apt-key add - \
 && echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/cuda.list \
 && echo "deb https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list \
 && rm -rf /var/lib/apt/lists/*;

ENV CUDA_VERSION 10.2.89
ENV CUDA_PKG_VERSION 10-2=$CUDA_VERSION-1

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        cuda-cudart-$CUDA_PKG_VERSION \
        cuda-compat-10-2 \
 && ln -s cuda-10.2 /usr/local/cuda \
 && rm -rf /var/lib/apt/lists/*

ENV PATH /usr/local/cuda/bin:${PATH}

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=10.2 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 brand=tesla,driver>=418,driver<419"

ENV NCCL_VERSION 2.5.6

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        cuda-libraries-$CUDA_PKG_VERSION \
        cuda-nvtx-$CUDA_PKG_VERSION \
        libcublas10=10.2.2.89-1 \
        libnccl2=$NCCL_VERSION-1+cuda10.2 \
 && apt-mark hold libnccl2 \
 && rm -rf /var/lib/apt/lists/*

ENV CUDNN_VERSION 7.6.5.32
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        libcudnn7=$CUDNN_VERSION-1+cuda10.2 \
        libcudnn7-dev=$CUDNN_VERSION-1+cuda10.2 \
 && apt-mark hold libcudnn7 \
 && rm -rf /var/lib/apt/lists/*

