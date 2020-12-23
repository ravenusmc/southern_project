# This file will contain the code to actually do text analysis

# importing supporting libraries
import numpy as np
import pandas as pd
import json
import datetime
from textblob import TextBlob
from pathlib import Path

# Importing libraries I wrote 
from support import *
from sentiment import * 


class Analysis(): 

	def __init__(self):
		self.main_csv = pd.read_csv("./data/toc.csv") 
		self.support = Support()
		self.sentiment = Sentiment()

	#def test_code(self):
		# print(self.main_csv.head())

	def fetch_sentiment_overtime(self):
		sentiment_overtime_data = []
		columns = ['Year', 'Sentiment']
		sentiment_overtime_data.append(columns)
		min_year = self.support.get_min_year(self.main_csv)
		max_year = self.support.get_max_year(self.main_csv)
		while min_year <= max_year:
			rows = []
			content_by_year = self.support.get_content_by_year(self.main_csv, min_year)
			if not content_by_year.empty:
				content_list = self.support.get_file_name(content_by_year)
				list_for_multiple_speeches_in_year = []
				for text_file in content_list:
					converted_file_name = self.support.change_file_name_ending(text_file)
					text_file = self.support.getting_text_file(converted_file_name)
					text_converted = self.support.get_text_to_textBlob_format(text_file)
					sentiment_sentence_list = self.sentiment.get_sentiment_values_of_single_speech(text_converted)
					sentiment_speech_average = self.sentiment.get_sentiment_average_per_speech(sentiment_sentence_list)
					if len(content_list) > 1:
						list_for_multiple_speeches_in_year.append(sentiment_speech_average)
				if len(list_for_multiple_speeches_in_year) > 1:
					sentiment_speech_average_longer_content_list = self.sentiment.get_sentiment_average_per_speech(list_for_multiple_speeches_in_year)
					rows.append(min_year)
					sentiment_speech_average_longer_content_list
					rows.append(sentiment_speech_average_longer_content_list)
					sentiment_overtime_data.append(rows)
				else:
					rows.append(min_year)
					rows.append(format(sentiment_speech_average, '.2f'))
					sentiment_overtime_data.append(rows)
			min_year += 1
		print(sentiment_overtime_data)



test = Analysis()
test.fetch_sentiment_overtime()
