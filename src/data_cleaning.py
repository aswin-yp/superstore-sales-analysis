import numpy as np

def handle_missing_values(df):
    missing = df['Row ID'].isna()
    missing_sum = missing.sum()

    df.loc[missing, 'Row ID'] = np.arange(
        df['Row ID'].max() + 1,
        df['Row ID'].max() + 1 + missing_sum
    )
    return df

def remove_duplicates(df):
    return df.drop_duplicates()
