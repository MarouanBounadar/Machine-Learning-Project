import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):

    # remove customerID
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    # convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # remove missing values
    df = df.dropna()

    return df


def encode_data(df):

    le = LabelEncoder()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = le.fit_transform(df[col])

    return df


def split_features_target(df):

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    return X, y
print("Data loaded and preprocessed successfully!")