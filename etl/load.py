from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine("postgresql://user:password@localhost:5432/salesdb")
    df.to_sql("sales", engine, if_exists="replace", index=False)
