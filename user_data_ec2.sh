#!/bin/bash

APP_NAME="my_fastapi_app"
USER="ec2-user"
PROJECT_DIR="/home/$USER/$APP_NAME"
PYTHON_VERSION="3.10.0"
PYTHON_DIR="Python-$PYTHON_VERSION"
POETRY_BIN="/home/$USER/.local/bin"

log_file="/var/log/user_data.log"

log() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$log_file"
}

log "Atualizando pacotes..."
sudo yum update -y >> "$log_file" 2>&1


log "Instalando dependências..."
sudo yum -y install gcc openssl-devel bzip2-devel libffi-devel sqlite-devel zlib-devel git >> "$log_file" 2>&1

install_python() {
  if ! command -v python3.10 &> /dev/null
  then
    log "Instalando Python $PYTHON_VERSION"
    curl -O https://www.python.org/ftp/python/$PYTHON_VERSION/$PYTHON_DIR.tgz >> "$log_file" 2>&1
    tar xzf $PYTHON_DIR.tgz >> "$log_file" 2>&1
    cd $PYTHON_DIR
    sudo ./configure --enable-optimizations >> "$log_file" 2>&1
    sudo make altinstall >> "$log_file" 2>&1
    cd ..
  else
    log "Python 3.10 já instalado."
  fi
}

install_python

install_pip() {
  if ! command -v python3.10 -m pip &> /dev/null
  then
    log "Instalando pip para Python 3.10"
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py >> "$log_file" 2>&1
    sudo python3.10 get-pip.py >> "$log_file" 2>&1
  else
    log "pip já instalado para Python 3.10."
  fi
}

install_pip

install_poetry() {
  if ! command -v poetry &> /dev/null
  then
    log "Instalando Poetry"
    python3.10 -m pip install --user poetry >> "$log_file" 2>&1
    echo "export PATH=\"$POETRY_BIN:\$PATH\"" >> /home/$USER/.bashrc
  else
    log "Poetry já instalado."
  fi
}

install_poetry

log "Criando diretório do projeto..."
mkdir -p $PROJECT_DIR >> "$log_file" 2>&1
sudo chmod -R 755 $PROJECT_DIR >> "$log_file" 2>&1
sudo chown -R $USER:$USER $PROJECT_DIR >> "$log_file" 2>&1

log "Setup concluído."