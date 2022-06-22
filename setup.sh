#!/bin/bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip install tk
pip install pyautogui
echo "Install scrot: https://github.com/resurrecting-open-source-projects/scrot"
