from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from data import *
from common_words import *

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
		word_count_object = Common_Words()
		data = request.get_json()
		decade = data['decade']
		all_words_list = analysis_object.get_words_by_decade(decade)
		count_of_words_and_words = word_count_object.clean_word_list(all_words_list)
		print(count_of_words_and_words)
	return jsonify('pong!')


if __name__ == '__main__':
    app.run()