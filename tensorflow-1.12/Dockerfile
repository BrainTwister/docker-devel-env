ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN pip3 install --upgrade pip \
 && hash -r pip3 \
 && pip3 install -I \ 
    graphviz \
    matplotlib \
    numpy \
    pydot \
    seaborn \
    sklearn \
    stn \
    tensorflow~=1.12
