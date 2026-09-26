import os
import pandas as pd
import matplotlib.pyplot as plt

INPUT = "data/processed/clean_orders.csv"
OUT = "data/processed"

def main():
    df = pd.read_csv(INPUT)
    os.makedirs(OUT, exist_ok=True)

    if "revenue" in df.columns:
        print("Total revenue:", df["revenue"].sum())
        print("Average revenue:", df["revenue"].mean())

    if "category" in df.columns and "revenue" in df.columns:
        category = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
        category.to_csv(f"{OUT}/category_revenue.csv")
        category.plot(kind="bar", title="Revenue by Category")
        plt.tight_layout()
        plt.savefig(f"{OUT}/revenue_by_category.png")
        plt.close()

    print("\nColumns:", list(df.columns))
    print("\nMissing values:\n", df.isna().sum())

if __name__ == "__main__":
    main()
