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
		min_year = self.support.get_min_year(self.main_csv)
		max_year = self.support.get_max_year(self.main_csv)
		# Getting the content by year 
		while min_year <= max_year:
			content_by_year = self.support.get_content_by_year(self.main_csv, min_year)
			if not content_by_year.empty:
				# Possibly need to added another loop here 
				content_list = self.support.get_file_name(content_by_year)
				for text_file in content_list:
					# Have to change the end of file names.
					converted_file_name = self.support.change_file_name_ending(text_file)
					text_file = self.support.getting_text_file(converted_file_name)
					
					#text_converted = self.support.get_text_to_textBlob_format(text_file)

				# Get sentiment of single speech during year
			min_year += 1
			
		# average together all sentiments for speeches in given year
		# put the year to the average sentiment for the graph data. 


test = Analysis()
test.fetch_sentiment_overtime()
