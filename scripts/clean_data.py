import pandas as pd
def clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

def convert_dates(df, column):
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

def drop_missing(df, columns):
    return df.dropna(subset=columns)