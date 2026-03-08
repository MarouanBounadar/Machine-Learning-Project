import pandas as pd

def load_data():
    data = pd.read_csv("data/housing.csv")
    return data