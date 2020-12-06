# This file will provide supporting functions to this project 

#importing supporting libraries
import numpy as np
import pandas as pd

class Support():

	def get_min_year(self, dataframe):
		return dataframe['Date'].min() # Working min year 1709
	
	def get_max_year(self, dataframe):
		return dataframe['Date'].max() # Working max year 1927
	
	def get_content_by_year(self, dataframe, min_year):
		return dataframe[(dataframe.Date == min_year)]

	def change_file_name_ending(self, file_name):
		return file_name.replace(".xml", ".txt")
	
	def get_file_name(self, content_by_year):
		content_list = []
		if len(content_by_year.Filename) = 1:
			content_by_year.Filename.iloc[0]
		print(len(content_by_year.Filename))
		input()
		return content_by_year.Filename.iloc[0]
	
	def getting_text_file(self, converted_file_name):
		return open("./data/texts/" + converted_file_name, "r")
	
	def get_text_to_textBlob_format(self, text_file):
		for x in text_file:
			print(x)
			input()

