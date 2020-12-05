# This file will provide supporting functions to this project 

#importing supporting libraries
import numpy as np
import pandas as pd

class Support():

	def get_min_year(self, dataframe):
		return dataframe['Date'].min() # Working min year 1709
	
	def get_max_year(self, dataframe):
		return dataframe['Date'].max() # Working max year 1927
	
	def get_file_name(self, content_by_year):
		return content_by_year.Filename.iloc[0]

