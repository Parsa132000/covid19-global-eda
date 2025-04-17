import pandas as pd

def load_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['iso_code'].str.len() == 3]
    return df
