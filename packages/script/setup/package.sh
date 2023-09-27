#!/bin/bash

set -x

# LOAD .ENV FILE

if [ -f .env ]; then
   source .env
fi

# MAVEN

set -ex && sudo apt-get install --yes --no-install-recommends --allow-unauthenticated \
  maven
