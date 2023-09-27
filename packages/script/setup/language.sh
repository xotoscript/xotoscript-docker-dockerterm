#!/bin/bash

set -x

# LOAD .ENV FILE

if [ -f .env ]; then
   source .env
fi

# GO

sudo apt-get install  --yes --no-install-recommends --allow-unauthenticated golang-go

# JAVA

echo | sudo add-apt-repository ppa:linuxuprising/java
sudo apt update

set -ex &&
  sudo apt-get install --yes --no-install-recommends --allow-unauthenticated \
    openjdk-$JAVA_VERSION-jdk-headless

# PYTHON

echo | sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"
sudo apt update

set -ex &&
  sudo apt-get install --yes --no-install-recommends --allow-unauthenticated \
    build-essential -yq \
    python3-pip

ln -s /usr/bin/python3 python
pip3 --no-cache-dir install --upgrade pip

# RUBY

git clone https://github.com/sstephenson/rbenv.git ${USER_HOME}/.rbenv
git clone https://github.com/sstephenson/ruby-build.git ${USER_HOME}/.rbenv/plugins/ruby-build

sudo sh ${USER_HOME}/.rbenv/plugins/ruby-build/install.sh
export PATH=${USER_HOME}/.rbenv/bin:$PATH
