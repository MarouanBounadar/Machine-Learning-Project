import pickle
import numpy as np

model = pickle.load(open("../models/model.pkl", "rb"))

sample = np.array([[1,0,0,10,1,0,2,1,0,0,1,0,1,1,0,2,1,3,75,1500]])

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Customer will churn")
else:
    print("Customer will stay")