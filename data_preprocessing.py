import os
import pandas as pd

RAW = "data/raw/orders.csv"
OUT = "data/processed/clean_orders.csv"

def main():
    if not os.path.exists(RAW):
        raise FileNotFoundError(
            "Place your e-commerce dataset at data/raw/orders.csv"
        )

    df = pd.read_csv(RAW)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Standardize common date columns
    date_candidates = ["order_date", "date", "purchase_date", "transaction_date"]
    date_col = next((c for c in date_candidates if c in df.columns), None)
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df = df.dropna(subset=[date_col])

    df = df.drop_duplicates()

    # Numeric cleanup
    for c in df.select_dtypes(include="number").columns:
        df[c] = df[c].fillna(df[c].median())

    # Text cleanup
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].fillna("Unknown").astype(str).str.strip()

    # Create revenue where possible
    if "revenue" not in df.columns:
        if {"quantity", "unit_price"}.issubset(df.columns):
            discount = df["discount"] if "discount" in df.columns else 0
            df["revenue"] = df["quantity"] * df["unit_price"] * (1 - discount / 100)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f"Saved {len(df):,} rows to {OUT}")

if __name__ == "__main__":
    main()
