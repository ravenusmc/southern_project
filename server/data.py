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
		# Getting the min and max years
		min_year = self.support.get_min_year(self.main_csv)
		max_year = self.support.get_max_year(self.main_csv)
		# Getting the content by year 
		while min_year <= max_year:
			content_by_year = self.main_csv[(self.main_csv.Date == min_year)]
			if not content_by_year.empty:
				file_name = self.support.get_file_name(content_by_year)
				# Get sentiment of single speech during year
			min_year += 1
			
		
		#average together all sentiments for speeches in given year
		#put the year to the average sentiment for the graph data. 


test = Analysis()
test.fetch_sentiment_overtime()
