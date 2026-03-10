# House Price Prediction

## Overview
Predict house prices based on property features like bedrooms, bathrooms, sqft, and more.

## Dataset
Columns include:
- date, price, bedrooms, bathrooms, sqft_living, sqft_lot
- floors, waterfront, view, condition
- sqft_above, sqft_basement, yr_built, yr_renovated
- street, city, statezip, country

## Model
Linear Regression (can upgrade to Random Forest / XGBoost)

## Folder Structure
- `data/` → dataset
- `notebooks/` → EDA and experiments
- `src/` → preprocessing, training, prediction scripts
- `models/` → saved model
- `images/` → visualizations

## How to Run
```bash
pip install -r requirements.txt
python src/train.py
python src/predict.py
