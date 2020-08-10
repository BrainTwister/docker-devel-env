ARG BASE_IMAGE
FROM $BASE_IMAGE

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

ARG VERSION

RUN pip3 install --upgrade pip \
 && hash -r pip3 \
 && pip3 install -I \ 
    jupyter~=$VERSION

# Set up notebook config
COPY jupyter_notebook_config.py /jupyter-config/
ENV JUPYTER_CONFIG_DIR /jupyter-config

EXPOSE 8888

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --ip 0.0.0.0 --no-browser --allow-root"]
