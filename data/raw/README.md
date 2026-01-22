# Raw Data

This directory contains the raw dataset used for the Superstore Sales Analysis project.

## 📌 Dataset Source
- Dataset Name: Superstore Sales Dataset
- Format: CSV
- File: `Superstore.csv`
- Source: Public retail sales dataset commonly used for data analysis practice

> ⚠️ The raw CSV file is not included in this repository to avoid large file uploads and to follow data-sharing best practices.

## 🧾 Description
The dataset contains historical retail transaction data, including:
- Order and shipping dates
- Product, category, and sub-category details
- Sales, profit, and quantity information
- Customer segment and regional data

## 📄 Key Columns
- `Order Date` – Date when the order was placed
- `Ship Date` – Date when the order was shipped
- `Region` – Sales region
- `Category` – Product category
- `Product Name` – Product identifier
- `Sales` – Revenue generated
- `Profit` – Profit or loss from the sale

## ⚠️ Notes
- The raw data may contain missing values and duplicate records
- No preprocessing or transformations are applied at this stage
- Data cleaning is handled in the `src/data_cleaning.py` module
