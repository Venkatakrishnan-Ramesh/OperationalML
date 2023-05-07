ntroduction

The OperationalML App is a machine learning profiler application designed to help developers and data scientists optimize and improve the performance of their machine learning models. The app works by analyzing the input data and output predictions of a model, and providing insights and recommendations to improve its accuracy, speed, and efficiency.
Functional Requirements
Requirement 1: Upload Dataset

The user should be able to upload a dataset to be analyzed by the OperationalML App. Upon uploading, the dataset should be stored locally and displayed to the user for review.

python

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

Requirement 2: Exploratory Data Analysis

The user should be able to perform exploratory data analysis on the uploaded dataset. The app should use pandas_profiling to generate a report on the dataset and display it to the user.

python

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)

Requirement 3: Modelling

The user should be able to choose a target column from the uploaded dataset and run a machine learning model on it. The app should use pycaret for modelling and should allow the user to compare different models to choose the best one. The best model should be saved as a .pkl file.

python

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

Requirement 4: Download Model

The user should be able to download the best model as a .pkl file for future use.

python

if choice == "Download": 
    with open('best_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="best_model.pkl")

Non-Functional Requirements
Requirement 1: Performance

The OperationalML App should be able to analyze large datasets and run machine learning models efficiently, without causing significant delays or crashes.
Requirement 2: User Interface

The user interface of the OperationalML App should be user-friendly and intuitive, allowing users with limited technical knowledge to use the app without difficulty.
Requirement 3: Security

The OperationalML App should be secure and protect user data from unauthorized access or modification.
System Requirements

The OperationalML App requires the following system requirements:

    Python 3.7 or higher
    streamlit
    plotly
    pandas_profiling
    pycaret
    streamlit_pandas_profiling
    scikit-learn

Conclusion

The OperationalML App is a machine learning profiler application designed to help developers and data scientists optimize and improve the performance of their machine learning models. The app is user-friendly,