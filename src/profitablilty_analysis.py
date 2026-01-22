def category_profit(df):
    return df.groupby('Category')['Profit'].sum().sort_values()

def profit_vs_sales(df):
    return df['Sales'], df['Profit']
