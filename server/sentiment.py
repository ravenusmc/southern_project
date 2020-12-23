# This class will do all the main sentiment analysis for this project 

# importing supporting libraries
import numpy as np
import pandas as pd
import json
from textblob import TextBlob

class Sentiment():

	def get_sentiment_values_of_single_speech(self, text_converted):
		sentiment_sentence_list = []
		for sentence in text_converted.sentences:
				sentence_sentiment = sentence.sentiment[0]
				sentiment_sentence_list.append(sentence_sentiment)
		return sentiment_sentence_list
	
	def get_sentiment_average_per_speech(self, sentiment_sentence_list):
		return sum(sentiment_sentence_list) / len(sentiment_sentence_list)