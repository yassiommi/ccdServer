import sys
sys.path.append('.')

from flask import Flask, send_file, request
from utils.file import locked_write
import requests

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    locked_write(request.json, './queue/queue.json', './queue/.lock1')
    return 'done'

@app.route('/temp')
def get_temp():
    pass

if __name__ == '__main__':
    app.run()
