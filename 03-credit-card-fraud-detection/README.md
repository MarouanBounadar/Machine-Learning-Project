# Credit Card / Financial Fraud Detection

Machine Learning project to detect fraudulent financial transactions.

## Dataset
[PaySim Synthetic Financial Transactions](https://www.kaggle.com/datasets/ealaxi/paysim1)

## Features
- step
- type (CASH-IN, CASH-OUT, PAYMENT, TRANSFER)
- amount
- oldbalanceOrg, newbalanceOrig
- oldbalanceDest, newbalanceDest
- isFlaggedFraud

Target:
- isFraud (0 = normal, 1 = fraud)

## Model
Random Forest Classifier

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure
data/ -> dataset  
notebooks/ -> EDA + graphs  
src/ -> preprocessing, train, predict  
models/ -> saved model  
images/ -> saved plots