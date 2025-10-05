🚗 CAR PRICE PREDICTION MODEL

This project predicts used car prices based on various features such as year, mileage, fuel type, transmission, and engine details.

Initially, a Linear Regression model was implemented, but the performance was poor due to non-linear patterns in the dataset. Later, a Random Forest Regressor was applied, which provided much better results.

📂 PROJECT STRUCTURE
├── data/
│   └── car_data.csv         # Dataset
├── notebooks/
│   └── car_price_prediction.ipynb  # Jupyter Notebook
├── src/
│   └── model.py             # Model training code
├── README.md
└── requirements.txt

⚙️ TECH STACK

Python 🐍

Pandas – Data manipulation

NumPy – Numerical calculations

Matplotlib & Seaborn – Data visualization

Scikit-learn – Machine Learning models (Linear Regression, Random Forest)

📊 DATASET

Features:

Name

Year

KM Driven

Fuel Type

Seller Type

Transmission

Owner

Mileage

Engine

Power

Target Variable:

Price (in INR Lakhs)

🔎 APPROACH

1. Data Preprocessing

Handled missing values

Encoded categorical variables

Converted string columns like "Mileage (kmpl)" and "Engine (CC)" into numerical values

2. Exploratory Data Analysis (EDA)

Distribution plots for price

Feature correlation analysis

Outlier detection

3. Modeling

Linear Regression – Baseline model (poor R² and high error)

Random Forest Regressor – Improved accuracy with better handling of non-linearities

📈 RESULTS
MODEL	R² SCORE	RMSE
Linear Regression	~0.45	High
Random Forest	~0.85	Low

✅ Random Forest performed significantly better compared to Linear Regression.

🚀 HOW TO RUN

1. Clone the repository:

git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction


2. Install dependencies:

pip install -r requirements.txt


3. Run the Jupyter Notebook:

jupyter notebook notebooks/car_price_prediction.ipynb

📌 FUTURE WORK

Try XGBoost / LightGBM for even better performance

Hyperparameter tuning using GridSearchCV / RandomizedSearchCV

Deploy the model using Flask / Streamlit

🙌 ACKNOWLEDGEMENTS

Dataset sourced from Kaggle / CarDekho

Inspired by practical use cases in used car marketplaces
