#! /bin/bash

sudo apt update; sudo apt upgrade -y
sudo apt install graphviz graphviz-dev python3 python3-dev python3-pip
pip install poetry
poetry shell
poetry install
pip install pyqt5

