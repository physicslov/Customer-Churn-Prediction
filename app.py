import tensorflow as tf
import streamlit as st
from tensorflow.keras.models import load_model
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler,OneHotEncoder
import numpy as np


model = load_model('my_model.h5')
with open('label_encoder_gender.pkl','rb') as file:
  label_encoder_gen = pickle.load(file)

with open('onehot_encoder_geo.pkl','rb') as file:
  onehot_encoder_geo = pickle.load(file)
  
with open('scaler.pkl','rb') as file:
  scaler= pickle.load(file)
  
st.title("Customer Churn Prediction")
geography = st.selectbox('Geography',onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender',label_encoder_gen.classes_)
age = st.slider('Age',18,92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure',0,10)
num_of_products = st.slider('Number Of Products',1,4)
has_cr_card = st.selectbox('Has Credit Card',[0,1])
is_active_member = st.selectbox('Is Active Member',[0,1])

input_data = pd.DataFrame({
  'CreditScore':[credit_score],
  'Gender':[gender],
  'Age':[age],
  'Tenure':[tenure],
  'Balance':[balance],
  'NumOfProducts':[num_of_products],
  'HasCrCard':[has_cr_card],
  'IsActiveMember':[is_active_member],
  'EstimatedSalary':[estimated_salary],
})

geo_encoder = onehot_encoder_geo.transform([[geography]])
geo_df = pd.DataFrame(geo_encoder,columns=onehot_encoder_geo.get_feature_names_out(['Geography']))
input_data['Gender'] = label_encoder_gen.transform(input_data['Gender'])
input_data = pd.concat([input_data.reset_index(drop=True),geo_df],axis=1)
input_data = scaler.transform(input_data)

if st.button('Predict Churn'):
 prediction = model.predict(input_data)
 if prediction[0][0]>0.5:
   st.write("Customer is likely to churn")
 else:
   st.write("Customer is Not likely to Churn")
