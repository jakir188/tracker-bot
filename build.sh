#!/usr/bin/env bash

# Install Python 3.9 with distutils support
sudo apt-get update
sudo apt-get install -y python3.9 python3.9-distutils python3.9-venv

# Create virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
