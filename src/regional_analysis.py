def regional_sales(df):
    return df.groupby('Region')['Sales'].sum().sort_values()

def sales_pivot(df):
    return df.pivot_table(
        values='Sales',
        index='Region',
        columns='Category',
        aggfunc='sum'
    )
