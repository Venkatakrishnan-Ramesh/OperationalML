# Software Engineering Capstone

## Introduction

The OperationalML App is a machine learning profiler application designed to help developers and data scientists optimize and improve the performance of their machine learning models. The app works by analyzing the input data and output predictions of a model, and providing insights and recommendations to improve its accuracy, speed, and efficiency.

## Functional Requirements
### Requirement 1: Upload Dataset

The user should be able to upload a dataset to be analyzed by the OperationalML App. Upon uploading, the dataset should be stored locally and displayed to the user for review.

### Requirement 2: Exploratory Data Analysis

The user should be able to perform exploratory data analysis on the uploaded dataset. The app should use pandas_profiling to generate a report on the dataset and display it to the user.

### Requirement 3: Modelling

The user should be able to choose a target column from the uploaded dataset and run a machine learning model on it. The app should use pycaret for modelling and should allow the user to compare different models to choose the best one. The best model should be saved as a .pkl file.

### Requirement 4: Download Model

The user should be able to download the best model as a .pkl file for future use.

## Non-Functional Requirements
### Requirement 1: Performance

The OperationalML App should be able to analyze large datasets and run machine learning models efficiently, without causing significant delays or crashes.

### Requirement 2: User Interface

The user interface of the OperationalML App should be user-friendly and intuitive, allowing users with limited technical knowledge to use the app without difficulty.
### Requirement 3: Security

The OperationalML App should be secure and protect user data from unauthorized access or modification.
## System Requirements

The OperationalML App requires the following system requirements:

    Python 3.7 or higher
    streamlit
    plotly
    pandas_profiling
    pycaret
    streamlit_pandas_profiling
    scikit-learn

## Conclusion
 
The OperationalML App is a machine learning profiler application designed to help developers and data scientists optimize and improve the performance of their machine learning models. The app is user-friendly,
