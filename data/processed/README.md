# Processed Data

This directory represents the cleaned and transformed version of the Superstore dataset used for analysis.

## 🔧 Processing Steps Applied
The raw data was processed using Python (Pandas, NumPy) with the following steps:

- Converted `Order Date` and `Ship Date` columns to datetime format
- Handled missing values in key identifier columns
- Removed duplicate records to ensure data consistency
- Prepared data for time-series resampling
- Structured data for aggregation and visualization

## 📊 Purpose of Processed Data
The processed dataset is used for:
- Time-series analysis (daily, monthly, yearly trends)
- Regional and category-wise sales comparisons
- Profitability and loss analysis
- Data visualization and business insight generation

## 📁 Storage Policy
- Processed datasets are not stored as CSV files in this repository
- All transformations are reproducible through scripts in the `src/` directory

## 🔁 Reproducibility
To regenerate the processed data:
1. Place the raw `Superstore.csv` file in your local environment
2. Run the data loading and cleaning scripts in the correct order from `src/`
