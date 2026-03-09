import pickle
import numpy as np

# Load trained model
with open('../models/house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Example house features: bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated
sample = np.array([[3, 2, 1500, 5000, 1, 0, 0, 3, 1000, 500, 1990, 0]])

prediction = model.predict(sample)
print(f"Predicted house price: ${prediction[0]:,.2f}")