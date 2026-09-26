import os
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

INPUT = "data/processed/monthly_sales.csv"
OUTPUT = "data/processed/sales_forecast.csv"

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError(
            "Create monthly_sales.csv with columns: date,revenue"
        )

    df = pd.read_csv(INPUT, parse_dates=["date"])
    df = df.sort_values("date").set_index("date")
    series = df["revenue"].asfreq("MS").interpolate()

    # Starter seasonal model. Tune orders after ACF/PACF and validation.
    model = SARIMAX(
        series,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    fitted = model.fit(disp=False)

    forecast = fitted.get_forecast(steps=12)
    result = forecast.summary_frame()[["mean", "mean_ci_lower", "mean_ci_upper"]]
    result = result.rename(columns={"mean": "forecast"})
    result.to_csv(OUTPUT)

    print(result)
    print("Saved:", OUTPUT)

if __name__ == "__main__":
    main()
