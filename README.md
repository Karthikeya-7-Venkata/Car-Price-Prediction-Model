# 🚗 Car Price Prediction Model

This repository contains a Machine Learning project that predicts used car prices based on features like **year, mileage, fuel type, transmission, and engine details**.

A **Linear Regression** model was first implemented but gave poor results due to non-linear patterns in the dataset. A **Random Forest Regressor** was later applied, which provided much better performance.

## 📁 Project Structure

├── data/
│ └── car_data.csv # Dataset file
├── notebooks/
│ └── Prediction_Model.ipynb # Jupyter Notebook
├── src/
│ └── model.py # Model training code
├── README.md
└── requirements.txt


## ⚙️ Tech Stack

- **Python 🐍**  
- **Pandas** – Data manipulation  
- **NumPy** – Numerical calculations  
- **Matplotlib & Seaborn** – Data visualization  
- **Scikit-learn** – Machine Learning models (**Linear Regression, Random Forest**)  

## 📊 Dataset

**Features:** Name, Year, KM Driven, Fuel Type, Seller Type, Transmission, Owner, Mileage, Engine, Power  
**Target Variable:** Price (in INR Lakhs)  

## 🔎 Approach

- **Data Preprocessing** – handled missing values, encoded categorical data, converted string features like mileage and engine.  
- **Exploratory Data Analysis (EDA)** – visualizations, correlations, outlier detection.  
- **Modeling** – Linear Regression (baseline, poor results) and Random Forest Regressor (better accuracy).  

## 📈 Results

| Model              | R² Score | RMSE  |
|--------------------|---------:|------:|
| Linear Regression  | ~0.45    | High  |
| Random Forest      | ~0.85    | Low   |

✅ **Random Forest performed significantly better compared to Linear Regression.**


## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
## 🚀 How to Run

## 2. Install dependencies
```bash
pip install -r requirements.txt

### 📌 Future Work

- Try **XGBoost / LightGBM** for better performance  
- Hyperparameter tuning using **GridSearchCV / RandomizedSearchCV**  
- Deploy the model using **Flask / Streamlit**  

### 🙌 Acknowledgements

- Dataset sourced from **Kaggle / CarDekho**  
- Inspired by real-world **used car price prediction** use cases it is bot gt=etting correwct check



