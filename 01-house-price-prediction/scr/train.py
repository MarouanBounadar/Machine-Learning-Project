import pickle
from sklearn.linear_model import LinearRegression
from preprocessing import load_data, preprocess_features

data = load_data()
X, y = preprocess_features(data)

model = LinearRegression()
model.fit(X, y)

# Save the model
with open('../models/house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")