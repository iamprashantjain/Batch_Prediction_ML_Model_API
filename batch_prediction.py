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

user_menu = st.sidebar.selectbox('Select Options',('2W (CS)','2W (NCS)','3W (CS)', '3W (NCS)','4W (NCS)','4W (CS)','CV (CS)','CV (NCS)','CE (CS)', 'CE (NCS)' ,'FE (CS)','FE (NCS)'))

if user_menu == 'FE (NCS)':
    st.title("FE (NCS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n
        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * CV_State_Clean (State)
        * METERREADING (Meter Reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)

elif user_menu == 'FE (CS)':
    st.title("FE (CS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * STATE_MAPPED (State)
        * SELLER_SEGMENT (Seller segment)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)
    
elif user_menu == 'CV (CS)':
    st.title("CV (CS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * CV_State_Clean (State)
        * SELLER_SEGMENT (Seller segment)
        * Meter_Reading (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('regressor_CV_CS.pkl','rb'))

    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','CV_State_Clean','SELLER_SEGMENT','Meter_Reading']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)

elif user_menu == 'CV (NCS)':
    st.title("CV (NCS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * STATE_MAPPED (State)
        * Meter_Reading (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)

elif user_menu == '2W (CS)':
    st.title("2W (CS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * STATE_MAPPED (State)
        * SELLER_SEGMENT (Customer Segmentation)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('regressor_2w_cs.pkl','rb'))

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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)

elif user_menu == '2W (NCS)':
    st.title("2W (NCS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * STATE_MAPPED (State)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('regressor_2w_ncs.pkl','rb'))

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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)

elif user_menu == '4W (NCS)':
    st.title("4W (NCS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * STATE_MAPPED (State)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('regressor_2w_ncs.pkl','rb'))

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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)                        

elif user_menu == '4W (CS)':
    st.title("4W (CS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * CV_State_Clean (State)
        * SELLER_SEGMENT (Customer Segmentation)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('Final_4W_CS.pkl','rb'))

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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)            


elif user_menu == "3W (CS)":
    st.title("3W (CS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * State_Clean (State)
        * SELLER_SEGMENT (Customer Segmentation)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('FInal_regressor_3w_CS.pkl','rb'))

    with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("Upload a CSV file", type=["csv"])
        submitted = st.form_submit_button("Upload")

    if file is not None:
        data = pd.read_csv(file)
        try:
            X = data[['MAKE_YEAR','Make_Clean','Model_Clean','Variant_Clean','Fuel_Clean','State_Clean','SELLERSEGMENT','METERREADING']]
            if st.button('Get the Predictions'):
                st.spinner("Please wait...")
                with st.spinner("Please wait..."):
                    predictions = model.predict(X)
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)


elif user_menu == "3W (NCS)":
    st.title("3W (NCS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * CV_State_Clean (State)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('FInal_regressor_3w_CS.pkl','rb'))

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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)



elif user_menu == "CE (CS)":
    st.title("CE (CS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * CV_State_Clean (State)
        * SELLER_SEGMENT (Customer Segmentation)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('FInal_regressor_CE_CS.pkl','rb'))

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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)




elif user_menu == "CE (NCS)":
    st.title("CE (NCS)")
    st.markdown(""" <style> .font {
    font-size:15px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Important Note: </p>', unsafe_allow_html=True)

    st.markdown("1. Data in CSV **must not exceed 50 rows** for better performance.")

    st.markdown("""2. Columns Names **Required** in CSV : \n

        * MAKE_YEAR (make year)
        * Make_Clean (Make)
        * Model_Clean (Model)
        * Variant_Clean (Variant)
        * Fuel_Clean (Fuel)
        * CV_State_Clean (State)
        * METERREADING (Meter reading)
        * SOLDAMOUNT (Actual Sold Amount)""")

    st.markdown("""3. Upload CSV in above format, Click on **"UPLOAD"** & **"GET PREDICTIONS"** to see the Results.""")


    model=pickle.load(open('FInal_regressor_CE_NCS.pkl','rb'))

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
                    df1 = pd.DataFrame(predictions, columns = ['Predicted_Amount']).astype(int).squeeze()
                    df2 = data['SOLDAMOUNT'].rename("Actual_Amount")                    
                    df3 = (((df1.subtract(df2))/(df2.add(df1)))*100).astype(int)
                    df3 = df3.rename("%%age diff")
                    df4 = df3.to_frame()
                    df4 = df4[df4['%%age diff'] == 0].size
                    df5 = df3.to_frame().size
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.subheader("Actual VS Predicted Results")
                    avg_pct = df3.mean().astype(int)
                    col1,col2,col3 = st.columns(3)
                    col1.metric('Average % age diff of Predictions: ',avg_pct)
                    col2.metric('No. of Exact Predictions',df4)
                    col3.metric('Total Predictions',df5)                    
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    col1,col2,col3 = st.columns(3)
                    col1.table(df1)
                    col2.table(df2)
                    col3.table(df3)
        
        except Exception as e:
            st.markdown(e)

