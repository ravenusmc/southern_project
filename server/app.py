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
@app.route('/fetch_words_by_decade', methods=['GET', 'POST'])
def fetch_words_by_decade():
	if request.method == 'POST':
		analysis_object = Analysis()
		data = request.get_json()
		decade = data['decade']
		word_count_by_decase = analysis_object.get_words_by_decade(decade)
	return jsonify('pong!')


if __name__ == '__main__':
    app.run()