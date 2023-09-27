#!/bin/bash

set -x

# LOAD .ENV FILE

if [ -f .env ]; then
   source .env
fi

# MONGO

sudo wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
sudo echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

sudo apt-get update

set -ex && sudo apt-get install --yes --no-install-recommends --allow-unauthenticated \
  mongodb

# POSTGRES

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

set -ex && sudo apt-get install --yes --no-install-recommends --allow-unauthenticated \
  postgresql-${POSTGRES_VERSION} \
  postgresql-contrib
