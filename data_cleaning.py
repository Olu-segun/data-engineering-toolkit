#This file contains data simple cleaning script

import pandas as pd
from data_extraction import data_extract

def transform_data():
	print("Data transformation begins")
	df = data_extract()
	df = df.dropna()
	print("Data transformation completed successfully ✅ ")
	
if __name__==  "__main__":
	df = transform_data()
	print(df)