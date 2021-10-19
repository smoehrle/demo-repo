#!/bin/bash
yum update -y
yum install -y git python37 screen
git clone https://github.com/smoehrle/demo-repo.git
cd demo-repo
python3 -m pip install -r requirements.txt
export FLASK_APP=app
screen -m -d flask run --host=0.0.0.0 --port=80