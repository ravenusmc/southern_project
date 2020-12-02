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

	def practice(self):
		# data = pd.read_csv("./data/toc.csv") 
		# print(data.head())
		# print(self.main_csv.head())


test = Analysis()
test.practice()
