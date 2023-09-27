#!/bin/bash

# run this file through following command :

set -x

# LOAD .ENV FILE

if [ -f .env ]; then
   source .env
fi

echo "USER_NAME=$USER_NAME"

# SET HOME ENV

if [ "$USER_NAME" = "root" ]; then
  echo "USER_HOME=/$USER_NAME"
  echo "ZSH_CUSTOM=/$USER_NAME/.oh-my-zsh/custom"
else
  echo "USER_HOME=/home/$USER_NAME"
  echo "ZSH_CUSTOM=/home/$USER_NAME/.oh-my-zsh/custom"
fi

# PROFILE

echo "EMAIL=$EMAIL"
echo "NAME=$NAME"
echo "USER_GROUP=$USER_GROUP"

# VERSIONS

echo "NVM_VERSION=$NVM_VERSION"
echo "NEOVIM_VERSION=$NEOVIM_VERSION"
echo "YARN_VERSION=$YARN_VERSION"
echo "POSTGRES_VERSION=$POSTGRES_VERSION"
echo "JAVA_VERSION=$JAVA_VERSION"
echo "RUBBY_VERSION=$RUBBY_VERSION"
echo "NERDS_FONT_VERSION=$NERDS_FONT_VERSION"
echo "FZF_VERSION=$FZF_VERSION"
echo "GITSTATUS_VERSION=$GITSTATUS_VERSION"

apt-get update
apt-get install dos2unix
find ./packages/script/setup -type f -name "*.sh" -exec dos2unix {} +
dos2unix .env

# SCRIPT

sudo chmod a+x ./packages/script/setup/*.sh

# ROOT

sudo ./packages/script/setup/root.sh

# USER

sudo  ./packages/script/setup/apts.sh
sudo  ./packages/script/setup/language.sh
sudo  ./packages/script/setup/database.sh
sudo  ./packages/script/setup/zsh.sh
sudo  ./packages/script/setup/package.sh

cp -o $USER_NAME ./packages/script/setup/ccat /usr/local/bin/

sudo  ./packages/script/setup/clean.sh

# zsh

# FINISH
echo " ___________________   ";
echo "	< FINISHED >         ";
echo " -------------------   ";
echo "   \                   ";
echo "    \                  ";
echo "        .--.           ";
echo "       |o_o |          ";
echo "       |:_/ |          ";
echo "      //   \ \         ";
echo "     (|     | )        ";
