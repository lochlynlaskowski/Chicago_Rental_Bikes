import pandas as pd

def wrangle_bikes(): 
    # This function acquires the initial combined datframe, drops unneccesary columns
    # and converts started_at and ended_at to datetime.
    df = pd.read_csv('Total_Rental_Info.csv', dtype={'start_station_id': str, 'end_station_id': str})
    df.drop(columns=['Unnamed: 0'],inplace=True)
    df['started_at']= pd.to_datetime(df['started_at'])
    df['ended_at']= pd.to_datetime(df['ended_at'])
    df.dropna(inplace=True)
    df.drop(columns=['start_station_id', 'end_station_id'], inplace=True)
    return df