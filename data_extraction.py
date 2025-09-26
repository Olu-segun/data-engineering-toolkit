import pandas as pd
def data_extract():
    months = range(1, 12+1)
    for month in months:
        data_path = f'C:/Users/USER/Documents/yellow_tripdata_2024-{month:02d}.parquet'
        raw_data = pd.read_parquet(data_path)
        print(raw_data)

if __name__ == "__main__":
    data_extract()