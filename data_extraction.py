import pandas as pd
def data_extract():
    raw_data = []
    months = range(1, 12+1)
    print('Data extraction begins')
    for month in months:
        data_path = f'C:/Users/USER/Documents/yellow_tripdata_2024-{month:02d}.parquet'
        print(f'Reading file {data_path}')
        data = pd.read_parquet(data_path)
        raw_data.append(data)
    #Combined raw data into a single DataFrame
    combined_data = pd.concat(raw_data, ignore_index = False )
    print("Data extraction completed successfully ✅.")
    return combined_data

if __name__ == "__main__":
   df = data_extract()
   