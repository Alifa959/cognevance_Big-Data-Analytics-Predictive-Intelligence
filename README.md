# Big Data Analytics & Predictive Intelligence for E-Commerce

## Level 3 B.Tech Project

This project builds an end-to-end analytics pipeline for e-commerce data using:
- Python
- SQL / MySQL
- PySpark
- Machine Learning
- SARIMA time-series forecasting
- Power BI

## Main objectives
1. Analyze sales, customers, products and KPIs.
2. Perform data cleaning and feature engineering.
3. Process scalable data with PySpark.
4. Predict customer churn.
5. Forecast sales using SARIMA.
6. Build an interactive Power BI dashboard.
7. Generate business recommendations.

## Folder structure
- `data/` - raw and processed datasets
- `src/` - Python pipeline and ML scripts
- `sql/` - database schema and analytical queries
- `pyspark/` - Spark processing
- `notebooks/` - recommended notebook workflow
- `models/` - saved trained models
- `dashboard/` - Power BI instructions/assets
- `reports/` - report templates
- `presentation/` - PPT outline
- `docs/` - architecture and workflow

## Quick start
1. Create a Python virtual environment.
2. Install `requirements.txt`.
3. Put the selected e-commerce CSV into `data/raw/orders.csv`.
4. Run `src/data_preprocessing.py`.
5. Run `src/eda.py`.
6. Run `src/churn_model.py`.
7. Run `src/sarima_forecast.py`.
8. Import processed data into MySQL and run the SQL scripts.
9. Open the generated CSVs in Power BI.
10. Follow `dashboard/POWER_BI_GUIDE.md`.

The scripts are written so that a student can replace the dataset without changing the overall architecture.
