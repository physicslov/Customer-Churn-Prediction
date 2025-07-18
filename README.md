# 📉 Customer Churn Prediction

This project is focused on predicting customer churn using Deep learning. The goal is to identify customers who are likely to leave a company's services based on various demographic and behavioral features.

---

## 🔍 Project Overview

Customer churn is when existing customers stop doing business with a company. Retaining customers is critical to business growth and profitability. This project uses historical data to predict whether a customer will churn or not.

---

## 🧠 Model Summary

- **Model Type**: Binary Classification
- **Algorithm**: TensorFlow (Deep Neural Network)
- **Accuracy**: ~86% (update after training)
- **Frameworks Used**: TensorFlow/Keras, scikit-learn, Pandas, Streamlit

---

## 📁 Dataset Information

The dataset used contains the following features:

| Feature Name        | Description                                  |
|---------------------|----------------------------------------------|
| `CreditScore`       | Customer's credit score                      |
| `Geography`         | Country of the customer (e.g., France)       |
| `Gender`            | Male or Female                               |
| `Age`               | Age of the customer                          |
| `Tenure`            | Number of years as a customer                |
| `Balance`           | Bank balance                                 |
| `NumOfProducts`     | Number of bank products the customer uses    |
| `HasCrCard`         | Whether the customer has a credit card       |
| `IsActiveMember`    | Whether the customer is active               |
| `EstimatedSalary`   | Estimated annual salary                      |
| `Exited` (Target)   | 1 = Churned, 0 = Stayed                      |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/physicslov/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
streamlit run app.py
{
    "CreditScore": 600,
    "Geography": "France",
    "Gender": "Male",
    "Age": 40,
    "Tenure": 3,
    "Balance": 60000,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 50000
}
📊 Output
The model will output:

1 → The customer is likely to churn

0 → The customer is likely to stay

🛠 Technologies Used
Python

TensorFlow / Keras

scikit-learn

Pandas, NumPy

Streamlit

📌 Project Structure
bash
Copy
Edit
├── app.py                   # Streamlit web app
├── churn_model.h5           # Trained model
├── onehot_encoder_geo.pkl   # Encoders(for Geography feature)
├── label_encoder_gender.pkl  # Encoders(for Gender feature)
├── scaler.pkl                # Scaler
├── dataset.csv               # Raw dataset
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
📈 Future Improvements
Add SHAP or LIME for interpretability

Improve model performance with hyperparameter tuning

Deploy on Streamlit Cloud

🙋‍♂️ Author
Shivam Jha
ML Enthusiast 

