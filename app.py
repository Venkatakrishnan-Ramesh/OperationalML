from operator import index
import streamlit as st
import plotly.express as px
#from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas_profiling
from pycaret.classification import *
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 
from sklearn.preprocessing import LabelEncoder

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0u8HzyTyC9JTlh9USdUFOCv8YrTWvoEYD9Q&usqp=CAU")
    st.title("OperationalML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("An ML profiler app is a software tool designed to help developers and data scientists optimize and improve the performance of their machine learning models. The app works by analyzing the input data and output predictions of a model, and providing insights and recommendations to improve its accuracy, speed, and efficiency.")



if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)

if choice == "Modelling": 
    chosen_target = st.selectbox('Choose the Target Column', df.columns)
    if st.button('Run Modelling'): 
        def Encoder(df):
          columnsToEncode = list(df.select_dtypes(include=['category','object']))
          le = LabelEncoder()
          for feature in columnsToEncode:
              try:
                  df = le.fit_transform(df)
              except:
                  print('Error encoding '+feature)
          return df
        df.astype(float)
        df.dropna(inplace=True)
        setup(df, target=chosen_target)
        setup_df = pull()
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.dataframe(compare_df)
        save_model(best_model, 'best_model')

if choice == "Download": 
    with open('best_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="best_model.pkl")

