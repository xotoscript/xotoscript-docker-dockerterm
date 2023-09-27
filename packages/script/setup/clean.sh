#!/bin/bash

set -x

# LOAD .ENV FILE

if [ -f .env ]; then
   source .env
fi

# UPDATE

sudo apt-get update -y -q && sudo apt-get upgrade -y -q
