import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data():
    data = pd.read_csv("../data/housing.csv")
    # Fill missing values for yr_renovated
    data['yr_renovated'].fillna(0, inplace=True)
    return data

def preprocess_features(data):
    # Drop non-numeric columns for now
    X = data.drop(columns=['price', 'date', 'street', 'city', 'statezip', 'country'])
    y = data['price']
    
    # Scale numeric features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y