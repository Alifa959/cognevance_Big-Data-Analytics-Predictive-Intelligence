import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

INPUT = "data/processed/customer_features.csv"
MODEL = "models/churn_model.pkl"

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError(
            "Create data/processed/customer_features.csv using the feature-engineering step."
        )

    df = pd.read_csv(INPUT)
    target = "churn"

    if target not in df.columns:
        raise ValueError("customer_features.csv must contain a binary 'churn' column.")

    X = df.drop(columns=[target])
    X = pd.get_dummies(X, drop_first=True)
    y = df[target].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=300, random_state=42, class_weight="balanced"
    )
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]

    print(classification_report(y_test, pred))
    print("ROC-AUC:", roc_auc_score(y_test, prob))

    os.makedirs("models", exist_ok=True)
    joblib.dump({"model": model, "columns": X.columns.tolist()}, MODEL)
    print("Saved:", MODEL)

if __name__ == "__main__":
    main()
