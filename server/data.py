#This file will contain the code to actually do text analysis

#importing supporting libraries
import numpy as np
import pandas as pd
import json
import datetime
from textblob import TextBlob
from pathlib import Path

class Analysis(): 

	def __init__(self):
		self.main_csv = pd.read_csv("./data/toc.csv") 

	#def test_code(self):
		# print(self.main_csv.head())

	def fetch_sentiment_overtime(self):
		#Need to get the min and max years 
		min_year = self.main_csv['Date'].min()
		max_year = self.main_csv['Date'].min()
		print(self.main_csv['Date'])
		#Need to get all speeches by year 
		#get sentiment of single speech during year
		#average together all sentiments for speeches in given year
		#put the year to the average sentiment for the graph data. 


test = Analysis()
test.fetch_sentiment_overtime()
