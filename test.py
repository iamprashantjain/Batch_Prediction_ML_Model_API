import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.set_page_config(page_title='Batch Prediction Tool',layout="wide",page_icon="🧊",initial_sidebar_state="auto")
st.sidebar.title("Batch Prediction Tool")
st.sidebar.image('https://bs-uploads.toptal.io/blackfish-uploads/components/seo/content/og_image_file/og_image/1083003/python-machine-learning-flask-example-d6874d1fe01f65ba6ccf301ba4e5d122.png')



# removing streamlit 
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """


st.markdown(hide_st_style, unsafe_allow_html=True)
user_menu = st.sidebar.selectbox('Select Options',('CV (CS)','CV (NCS)','2W (CS)','2W (NCS)','FE (CS)','FE (NCS)','4W (NCS)','4W (CS)','ANPR'))            


if user_menu == 'CV (CS)':
    st.title("CV (CS)")
    model=pickle.load(open('regressor_CV_CS.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")
    

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','CV_State_Clean','SELLER_SEGMENT','Meter_Reading']]
            if st.button('Get the Predictions'):
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass


elif user_menu == 'CV (NCS)':
    st.title("CV (NCS)")
    model=pickle.load(open('cv_ncs.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','STATE_MAPPED','Meter_Reading']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass


elif user_menu == '2W (CS)':
    st.title("2W (CS)")
    model=pickle.load(open('regressor_2w_cs.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','State_Clean','MAKE_YEAR','Customer_Segmentation']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass


elif user_menu == '2W (NCS)':
    st.title("2W (NCS)")
    model=pickle.load(open('regressor_2w_ncs.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','State_Clean','MAKE_YEAR']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass


elif user_menu == 'FE (CS)':
    st.title("FE (CS)")
    model=pickle.load(open('regressor_fe_cs.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','STATE_MAPPED','SELLER_SEGMENT','METERREADING']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass



elif user_menu == 'FE (NCS)':
    st.title("FE (NCS)")
    model=pickle.load(open('regressor_FE_NCS.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','CV_State_Clean','METERREADING']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass



elif user_menu == '4W (NCS)':
    st.title("4W (NCS)")
    model=pickle.load(open('FInal_regressor_4w_NCS.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','STATE_MAPPED','METERREADING']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass




elif user_menu == '4W (CS)':
    st.title("4W (CS)")
    model=pickle.load(open('FInal_4W_CS.pkl','rb'))
    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','CV_State_Clean','SELLER_SEGMENT','METERREADING']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    st.write("Predictions:", predictions)
        except Exception as e:
            pass