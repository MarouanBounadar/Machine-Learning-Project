# Customer Churn Prediction

## 📌 Project Overview

Customer churn is a major challenge for telecom companies.
This project uses Machine Learning to predict whether a customer will leave the service (churn) or stay with the company.

By analyzing customer data such as contract type, tenure, monthly charges, and services used, the model learns patterns that help identify customers at risk of leaving.

---

## 📊 Dataset

The dataset used in this project is the **Telco Customer Churn Dataset**.

Main features include:

* Customer demographics (gender, partner, dependents)
* Account information (tenure, contract type)
* Services subscribed (internet, streaming, tech support)
* Billing information (monthly charges, payment method)

Target variable:

* **Churn** (Yes / No)

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 🧠 Machine Learning Model

The model used in this project:

**Random Forest Classifier**

Why Random Forest?

* Handles categorical and numerical data well
* Reduces overfitting
* Provides good accuracy for classification problems

Expected accuracy:
**~80% – 85%**

---

## 📂 Project Structure

```
02-customer-churn-prediction
│
├── data
│   └── telco_churn.csv
│
├── notebooks
│   └── churn_analysis.ipynb
│
├── src
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── models
│   └── model.pkl
│
├── requirements.txt
│
└── README.md
```

---

## 🧹 Data Preprocessing

The preprocessing step includes:

* Removing unnecessary columns (customerID)
* Handling missing values
* Converting categorical features into numerical values
* Preparing data for training

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/MarouanBounadar/02-customer-churn-prediction.git
cd 02-customer-churn-prediction
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the model

```
python src/train_model.py
```

This will create the trained model:

```
models/model.pkl
```

### 4️⃣ Run prediction

```
python src/predict.py
```

---

## 📈 Possible Improvements

Future improvements for this project:

* Hyperparameter tuning
* Feature engineering
* Using advanced models like XGBoost
* Building a web app with Flask or Streamlit
* Deploying the model

---

## 👨‍💻 Author

Machine Learning Project built for learning and portfolio purposes.

---

⭐ If you like this project, feel free to give it a star!
