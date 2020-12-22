# This file will provide supporting functions to this project 

#importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob
import fileinput

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
		if len(content_by_year.Filename) == 1:
			file_name = content_by_year.Filename.iloc[0]
			content_list.append(file_name)	
		elif len(content_by_year.Filename) > 1:
			count = 0	
			while count < len(content_by_year.Filename):
				file_name = content_by_year.Filename.iloc[count]
				content_list.append(file_name)
				count += 1
		return content_list
	
	def getting_text_file(self, converted_file_name):
		return open("./data/texts/" + converted_file_name, "r")
	
	def get_text_to_textBlob_format(self, text_file):
		text_file_converted = str([cell.encode('utf-8') for cell in text_file])
		return TextBlob(text_file_converted)

