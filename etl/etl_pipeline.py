from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    df = extract_data("data/raw/sales.csv")
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    run_pipeline()
