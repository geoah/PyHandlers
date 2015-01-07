FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && apt-get install -y python python-pip

# Bundle app source
ADD . /src
RUN apt-get install wget -y

# Install Python Setuptools
RUN easy_install -U setuptools && pip install -U pip
RUN sudo easy_install virtualenv pip ez_setup
RUN virtualenv /src
RUN /bin/bash -c "sourse /src/bin/activate"

# Add and install Python modules
RUN pip install -r /src/requirements.txt
RUN pip install -e /src

# Expose
EXPOSE 8008

# Run
RUN cd /src
RUN handler-serve --port 8008
