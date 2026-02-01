import pandas as pd

def transform_data(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df['order_date'] = pd.to_datetime(df['order_date'])
    df = df.dropna()
    return df
