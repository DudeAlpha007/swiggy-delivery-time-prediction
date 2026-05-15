

# 🛵 Swiggy Delivery Time Prediction using Machine Learning

## 📌 Project Overview

Food delivery platforms face major challenges in estimating accurate delivery times due to factors such as traffic conditions, delivery distance, weather, vehicle type, and city-related variations.

This project uses Machine Learning techniques to predict Swiggy delivery times based on delivery and location-related features. The goal is to improve customer experience, delivery planning, and operational efficiency.

The complete pipeline includes:

- Data preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Model training
- Hyperparameter tuning
- Model evaluation
- Streamlit deployment

The final model predicts estimated delivery time in minutes using real-world delivery-related inputs.

---

# 🎥 Project Demo

https://github.com/user-attachments/assets/91855b5b-c2e1-421e-9249-a645c78fa530

---

# 🎯 Business Problem

Incorrect delivery time estimation can lead to:

- Poor customer satisfaction
- Increased order cancellations
- Delivery inefficiencies
- Operational losses
- Reduced platform trust

The objective of this project is to build a Machine Learning system capable of accurately predicting food delivery times for better logistics and customer experience.

---

# 🧠 Machine Learning Objective

The model predicts:

✅ Estimated Food Delivery Time

The project focuses on:

- Reducing prediction error
- Improving model generalization
- Building a scalable prediction pipeline
- Supporting real-world delivery optimization

---

# 📂 Dataset Information

The dataset contains delivery-related information such as:

- Delivery distance
- Weather conditions
- Traffic density
- Vehicle type
- City type
- Festival impact
- Delivery partner ratings
- Order details

Problem Type:

- Regression Problem

---

# ⚙️ Technologies Used

## Programming & Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn

## Deployment

- Streamlit
- Hugging Face Spaces

---

# 🛠️ Project Workflow

## 1️⃣ Data Preprocessing

- Handled missing values
- Processed categorical variables
- Cleaned dataset features
- Encoded categorical columns
- Scaled numerical features

---

## 2️⃣ Exploratory Data Analysis

Performed analysis to understand:

- delivery patterns
- traffic impact
- city-wise delivery variations
- feature relationships
- outlier behavior

---

## 3️⃣ Feature Engineering

Created meaningful transformed features to improve model performance and capture delivery-related patterns more effectively.

---

## 4️⃣ Model Training

The following Machine Learning models were trained and evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

---

## 5️⃣ Hyperparameter Tuning

Optimized model parameters to:

- reduce overfitting
- improve prediction stability
- enhance model performance

---

# 📊 Model Evaluation Metrics

The project was evaluated using:

- R² Score
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)

These metrics helped measure prediction accuracy and model reliability.

---

# 🏆 Final Model

## ✅ Selected Model:
### XGBoost Regressor

Why?

- Better prediction accuracy
- Strong generalization performance
- Lower prediction error
- Better handling of feature relationships

---

# 📈 Key Insights

- Traffic conditions strongly affect delivery time.
- Delivery distance plays a major role in prediction.
- Feature engineering significantly improved model performance.
- Ensemble models performed better than basic regression models.

---

# 🚀 Live Deployment

The Swiggy Delivery Time Prediction system has been deployed using Streamlit on Hugging Face Spaces.

🔗 Live Application:  
https://huggingface.co/spaces/gitamacc/Swiggy_Delivery_Time_Prediction

Users can enter delivery-related details and predict estimated delivery time in real time.

---

# 💻 GitHub Repository

🔗 GitHub:  
https://github.com/DudeAlpha007/swiggy-delivery-time-prediction

---

# 📁 Project Structure

```bash
├── app.py
├── model.pkl
├── requirements.txt
├── runtime.txt
├── README.md
```
---
# 👨‍💻 Author

## Surya Teja

Machine Learning & AI Enthusiast  
Focused on building practical business-oriented AI systems.
---
