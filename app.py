import streamlit as st
import plotly.express as px
#from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas_profiling
from pycaret.classification import *
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os

if os.path.exists('./dataset.csv'):
    df = pd.read_csv('dataset.csv', index_col=None)
else:
    df = pd.DataFrame() # default dataframe if one has not been provided

with st.sidebar:
    st.image("https://i.pinimg.com/236x/b4/b9/42/b4b942947c8e95c1e1f0135609ae6236--cute-anime-guys-anime-boys.jpg")
    st.title("OperationalML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

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
    if chosen_target and st.button('Run Modelling'):
        setup(df, target=chosen_target, silent=True)
        setup_df=pull()
        
        best_model = compare_models()
        compare_df = pull()
        save_model(best_model, 'best_model')
        st.dataframe(compare_df)


if choice == "Download":
    if os.path.exists('best_model.pkl'):
        with open('best_model.pkl', 'rb') as f:
            st.download_button('Download Model', f, file_name="best_model.pkl")
    else:
        st.warning("No model has been saved yet. Please run modelling first.")
