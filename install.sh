#!/usr/bin/bash
sudo apt install python3-pip
sudo apt install python3-dev
pip3 install sourcedefender
sudo cp srcDef.py /usr/bin/srcDef
sudo chmod +x /usr/bin/srcDef