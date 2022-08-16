#!/bin/bash
echo 'Initializing...'
sudo apt -y install python3 python3.10-venv figlet > /dev/null 2>&1

figlet 'Welcome to ConvergeCast Installation'
read x

python3 -m pip install --upgrade pip
python3 -m venv venv 
#source venv/bin/activate
python -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
#pip install bson Do not install the "bson" package from pypi. PyMongo comes with its own bson package;
                # doing "easy_install bson" installs a third-party package that is incompatible with PyMongo.
pip install Flask-JSON
pip install numba
python3 -m pip install -U setuptools pip
pip install cupy-cuda117
python3 -m pip install pymongo