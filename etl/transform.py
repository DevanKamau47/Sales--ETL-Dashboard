import pandas as pd

def transform_data(df):
    # standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # FIX: explicitly tell pandas day comes first
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

    # remove missing values
    df = df.dropna()

    return df

