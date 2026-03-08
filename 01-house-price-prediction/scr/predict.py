import pickle
import pandas as pd

model = pickle.load(open("models/house_price_model.pkl", "rb"))

sample = [[120, 3, 2, 1]]

prediction = model.predict(sample)

print(prediction)