# script para atualizar pip e apt
# rodar antes de qualquer outro

sudo apt -y update
sudo apt -y upgrade

sudo apt install -y python3-pip
pip3 install --upgrade pip
