import requests
import pandas as pd
import numpy
from matplotlib import pyplot as plt
from io import StringIO

url = "http://hgis.uw.edu/virus/assets/virus.csv"

def getData():
    response = requests.get(url, allow_redirects=True)
    f = StringIO(response.text)
    return pd.read_csv(f, dtype=str, parse_dates=True)

def formatData(df):
    df = df.set_index('datetime')
    df.fillna(value='0-0-0-0', inplace=True)
    return df

if __name__ == "__main__":
    df = getData()
    df = formatData(df)
    print(df)
