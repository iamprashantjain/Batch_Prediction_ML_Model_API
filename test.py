import streamlit as st
import pandas as pd
import numpy as np
import pickle


df = pd.read_csv('model_data_cv_cs.csv',encoding='latin-1',low_memory=False)
model=pickle.load(open('regressor_CV_CS.pkl','rb'))

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file is not None:
    data = pd.read_csv(file)
    X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','CV_State_Clean','SELLER_SEGMENT','Meter_Reading']]
    print(X)
    predictions = model.predict(X)
    st.write("Predictions:", [predictions])