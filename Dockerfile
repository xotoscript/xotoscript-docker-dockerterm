FROM ubuntu:20.04

#################
# VARIABLES START
#################

# PROFILE

ARG EMAIL=EMAIL
ARG NAME=NAME
ARG USER_NAME=USER_NAME

# USER GROUPS

ARG USER_GROUP=USER_GROUP

# VERSIONS

ARG NVM_VERSION=NVM_VERSION
ARG NEOVIM_VERSION=NEOVIM_VERSION
ARG YARN_VERSION=YARN_VERSION
ARG POSTGRES_VERSION=POSTGRES_VERSION
ARG JAVA_VERSION=JAVA_VERSION
ARG RUBBY_VERSION=RUBBY_VERSION
ARG NERDS_FONT_VERSION=NERDS_FONT_VERSION
ARG FZF_VERSION=FZF_VERSION
ARG GITSTATUS_VERSION=GITSTATUS_VERSION

# DIRECTORIES

ENV USER_HOME=/home/$USER_NAME
ENV ZSH_CUSTOM=${USER_HOME}/.oh-my-zsh/custom
ARG DOTFILE_REPO=DOTFILE_REPO
ARG REPO_PATH=REPO_PATH

ARG DEBIAN_FRONTEND=noninteractive

#################
# VARIABLES END
#################

# STARTER PACK

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY $REPO_PATH ./setup
RUN chmod a+x /setup/*.sh

RUN apt-get update
RUN apt-get install dos2unix

RUN find ./setup -type f -name "*.sh" -exec dos2unix {} +

# ROOT SCRIPTS

RUN /setup/user.sh
RUN /setup/root.sh

USER $USER_NAME
WORKDIR ${USER_HOME}

# USER SCRIPTS

RUN /setup/apts.sh
RUN /setup/language.sh
RUN /setup/database.sh
RUN /setup/zsh.sh
RUN /setup/package.sh

# FILES COPIED

COPY --chown=$USER_NAME:$USER_GROUP $REPO_PATH/spaceship.zsh ${USER_HOME}/.config/spaceship.zsh

# CLEANUP

RUN /setup/clean.sh

CMD ["zsh"]
