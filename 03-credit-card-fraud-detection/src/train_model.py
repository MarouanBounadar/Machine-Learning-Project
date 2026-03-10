import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from preprocessing import load_data, clean_data, encode_data, split_features_target


df = load_data("Machine-Learning-Project\\02-customer-churn-prediction\\data\\telco_churn.csv")

df = clean_data(df)

df = encode_data(df)

X, y = split_features_target(df)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier()

model.fit(X_train, y_train)

pickle.dump(model, open("Machine-Learning-Project\\02-customer-churn-prediction\\models\\model.pkl", "wb"))

print("Model saved successfully!")