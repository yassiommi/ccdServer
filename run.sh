#!/bin/bash
kill $(lsof -t -i:7624)
indiserver indi_sbig_ccd &> ./logs/indiserver.log &

kill $(lsof -t -i:5000)
export FLASK_APP=./__init__.py
flask run --host=0.0.0.0 &> ./logs/flask.log &

python3 ./utils/observe.py &> ./logs/observe.log &

python3 ./utils/move.py &> ./logs/move.log &
