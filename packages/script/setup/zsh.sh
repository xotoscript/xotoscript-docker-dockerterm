#!/bin/bash

set -x

# LOAD .ENV FILE

if [ -f .env ]; then
   source .env
fi

# ZSH INSTALLATION

sudo wget -qO- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | zsh || true

# ZSH THEME

ZSH_PLUGINS=$ZSH_CUSTOM/plugins && ZSH_THEMES=$ZSH_CUSTOM/themes &&
  sudo git clone --single-branch --branch '0.7.1' --depth 1 https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_PLUGINS/zsh-syntax-highlighting &&
  sudo git clone --single-branch --branch 'v0.6.4' --depth 1 https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_PLUGINS/zsh-autosuggestions &&
  sudo git clone https://github.com/zsh-users/zsh-history-substring-search $ZSH_PLUGINS/zsh-history-substring-search &&
  sudo git clone https://github.com/jimeh/zsh-peco-history.git $ZSH_PLUGINS/zsh-peco-history &&
  sudo git clone --single-branch --depth 1 https://github.com/romkatv/powerlevel10k.git $ZSH_THEMES/powerlevel10k

# GITSTATUS

GITSTATUS_SHA256="e33867063f091d3c31ede9916fef079ff8cd6fdcc70d051914f962ab3b8f36fd" &&
  sudo wget -nv -O gitstatus.tgz https://github.com/romkatv/gitstatus/releases/download/v${GITSTATUS_VERSION}/gitstatusd-linux-x86_64.tar.gz &&
  sudo echo "$GITSTATUS_SHA256 gitstatus.tgz" | sha256sum -c - &&
  sudo mkdir -p ./.lscache/gitstatus &&
  sudo tar zxvf gitstatus.tgz --directory ./.cache/gitstatus &&
  sudo rm gitstatus.tgz

# STARSHIP
# sudo sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes

# MAIN CONFIG

mkdir ${USER_HOME}/.config
rm ${USER_HOME}/.zshrc && touch ${USER_HOME}/.zshrc
echo "source ${USER_HOME}/.config/zsh/.zshrc" > ${USER_HOME}/.zshrc
chown $USER_NAME:${USER_GROUP} ${USER_HOME}/.config

# ZSH CONFIG

mkdir ${USER_HOME}/.config/zsh
git clone https://github.com/xotodot/xotodot-zsh.git ${USER_HOME}/.config/zsh >/dev/null

# TMUX CONFIG

git clone https://github.com/tmux-plugins/tpm ~/.config/.tmux/plugins/tpm

# NVIM CONFIG

mkdir ${USER_HOME}/.config/nvim
git clone https://github.com/xotovim/xotovim.git ${USER_HOME}/.config/nvim >/dev/null

# ANTIGEN

sudo curl -L https://raw.githubusercontent.com/zsh-users/antigen/master/bin/antigen.zsh >${USER_HOME}/.config/antigen.zsh

