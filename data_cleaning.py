#This file contains data simple cleaning script

import pandas as pd
from data_extraction import data_extract

def transform_data():
	print("Data transformation begins")
	df = data_extract()
<<<<<<< HEAD
=======
	df = df.dropna()
	print("Data transformation completed successfully ✅ ")
>>>>>>> feature/transform-data
	
	
	
if__name__==  "__main__"
	transform_data()