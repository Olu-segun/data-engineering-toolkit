#This file contains data cleaning process

import pandas as pd

from data_extraction import data_extract

def transform_data():
	df = data_extract()
	df = df.dropna()
	return df
	
	
if __name__=="__main__":
    df = transform_data()
    print(df)