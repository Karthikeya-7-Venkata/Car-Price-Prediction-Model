# 🚗 Car Price Prediction Model

This repository contains a Machine Learning project that predicts used car prices based on features like **year, mileage, fuel type, transmission, and engine details**.

A **Linear Regression** model was first implemented but gave poor results due to non-linear patterns in the dataset. A **Random Forest Regressor** was later applied, which provided much better performance.

## 📁 Project Structure

├── DataSet/
│   └── Cardetails.csv # Dataset file
├── NoteBook/
│   ├── Prediction_Model.ipynb # Jupyter Notebook
│   ├── app.py # Python app file
│   └── model.pkl # Trained model file
├── README.md


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


## 🛠 Requirements

- Python 3.8+ 🐍  
- Pandas  
- NumPy  
- Matplotlib & Seaborn  
- Scikit-learn  
- Optional: Jupyter Notebook for running `.ipynb` files  

---

## 📊 Results & Observations

- ✅ Random Forest Regressor outperformed Linear Regression significantly.  
- 🔹 Linear Regression struggled due to **non-linear patterns** in features like mileage and engine.  
- 🔹 Random Forest captured complex patterns and provided **higher R² score (~0.85)** with **lower RMSE**.  
- 📈 Feature importance analysis shows that **Year, KM Driven, and Engine** had the largest impact on price prediction.  
- 🔹 Visualization of predictions vs actual prices shows **strong alignment** for Random Forest.  

---

## ✅ Conclusion

- Random Forest is a **robust model** for predicting used car prices in this dataset.  
- Proper **data preprocessing** and handling of categorical/non-linear features is crucial for performance.  
- Linear Regression can serve as a **baseline**, but for real-world datasets with complex relationships, ensemble models like Random Forest are recommended.  

---

## 🔮 Future Work

- 🎯 Experiment with **other ensemble models** (e.g., Gradient Boosting, XGBoost) for better accuracy.  
- 🧩 Include additional **features** like car brand reputation, location, and market trends.  
- 🖥 Deploy a **web app** to predict car prices in real-time using the trained model.  
- ⚡ Optimize model using **hyperparameter tuning** or **cross-validation**.  
- 📊 Implement **explainable AI techniques** (like SHAP) to better understand feature impact.


