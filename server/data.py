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
				file_name = self.support.get_file_name(content_by_year)
				# Have to change the end of file names. 
				converted_file_name = self.support.change_file_name_ending(file_name)
				text_file = self.support.getting_text_file(converted_file_name)

				# Get sentiment of single speech during year
			min_year += 1
			
		# I need to make sure that I loop through multiple speeches not just one 
		# average together all sentiments for speeches in given year
		# put the year to the average sentiment for the graph data. 


test = Analysis()
test.fetch_sentiment_overtime()
