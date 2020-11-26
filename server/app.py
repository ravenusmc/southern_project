from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# This route .
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')



if __name__ == '__main__':
    app.run()