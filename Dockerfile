FROM ubuntu:18.04

# Basic setup
RUN apt-get update && apt-get install -y -q --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        wget \
        software-properties-common


### INSTALL NPM ###
# We need version 12 or above
# We will install it usinv NVM.

# NVM environment variables
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 14.16.0
# Install NVM
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash

# Install Node and NPM
RUN . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# Add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH


### Install Lux AI ###
RUN npm i -g @lux-ai/2021-challenge@latest

### Install Python ###
# Python 3.8
RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        ipython3
# Set Python3.8 as default
RUN ln -s python3.8 /usr/bin/python
RUN ln -s pip3 /usr/bin/pip

### LucIA setup ###
WORKDIR /root
COPY ./requirements.txt .
RUN pip install -r requirements.txt

### Execute jupyter notebook
ENTRYPOINT jupyter notebook visualizer.ipynb --port=8888 --no-browser --ip=0.0.0.0 --allow-root
