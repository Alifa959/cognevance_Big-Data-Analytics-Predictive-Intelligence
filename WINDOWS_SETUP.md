# Windows Setup

## 1. Install
- Python 3.11 or newer
- MySQL Community Server
- MySQL Workbench
- Power BI Desktop
- Git
- Java (required by many PySpark setups)

## 2. Open Command Prompt in this project folder

```text
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

## 3. Run preprocessing

```text
python src\\data_preprocessing.py
```

## 4. Run EDA

```text
python src\\eda.py
```

## 5. Run PySpark

```text
python pyspark\\big_data_processing.py
```

Then proceed to SQL, customer feature engineering, churn modeling, SARIMA and Power BI.
