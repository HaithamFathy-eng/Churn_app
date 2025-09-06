# Churn_app
This web application predicts customer churn using a machine learning model.
https://churnapp-rdachbimhevrkyx5pyxxjf.streamlit.app/

How it works:

The user enters customer details:

Age

Tenure (how long they’ve been a customer)

Sex

The app preprocesses the data (scaling & encoding).

A Naive Bayes model (trained with SMOTE to handle class imbalance) predicts whether the customer will churn.

The result is displayed as:

✅ Customer is not likely to churn

⚠️ Customer is likely to churn

Why it’s useful:

Helps businesses identify at-risk customers.

Allows companies to take proactive actions (discounts, offers, customer service follow-up).

Reduces revenue loss by improving customer retention.
