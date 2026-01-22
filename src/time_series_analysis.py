def resample_sales(df):
    df = df.set_index('Order Date')
    return {
        "daily": df['Sales'].resample('D').sum(),
        "weekly": df['Sales'].resample('W').sum(),
        "monthly": df['Sales'].resample('ME').sum(),
        "yearly": df['Sales'].resample('YE').sum()
    }
