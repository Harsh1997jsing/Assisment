# -*- coding: utf-8 -*-



import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle

# loading the saved model

pickle_in = open('k_mean_final.pkl', 'rb')
loaded_model = pickle.load(pickle_in)


# Defining a function for prediction

def Cluster_prediction(input_data):

    # Predicting Cluster
    prediction = loaded_model.predict(input_data)

    if (prediction[0] == 0):
        return 'Range is 0-25%'
    elif (prediction[0] == 1):
        return 'Range is 25% to 50%'
    elif (prediction[0] == 2):
        return 'Range under 50% to 70%'
    elif (prediction[0] == 3):
        return 'Range under 70% to 100%'
    else:
        return 'Try with different value'


def main():

    # giving a title
    st.markdown("<h1 style='color:green;'>Predicting PFA Data set</h1>",
                unsafe_allow_html=True)
    st.markdown("<h5 style='color:blue;'>Check the Values</h5>",
                unsafe_allow_html=True)
    st.sidebar.markdown(
        "<h5 style='color: blue ;'>Enter the necessary details to find Range</h5>",
        unsafe_allow_html=True)
    st.sidebar.markdown(
        "<h5 style='color: red ;'>Note: Please Enter all Values to avoid Errors</h5>", unsafe_allow_html=True)

    # getting the input data from the user
    T1 = st.sidebar.number_input('T1 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T2 = st.sidebar.number_input('T2 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T3 = st.sidebar.number_input('T3 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T4 = st.sidebar.number_input('T4 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T5 = st.sidebar.number_input('T5 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T6 = st.sidebar.number_input('T6 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T7 = st.sidebar.number_input('T7 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T8 = st.sidebar.number_input('T8 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T9 = st.sidebar.number_input('T9 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T10 = st.sidebar.number_input('T10 (-41 to -91)', min_value=-95, max_value=-39, value=-39)
    T11 = st.sidebar.number_input('T11 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T12 = st.sidebar.number_input('T12 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T13 = st.sidebar.number_input('T13 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T14 = st.sidebar.number_input('T14 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T15 = st.sidebar.number_input('T15 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T16 = st.sidebar.number_input('T16 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T17 = st.sidebar.number_input('T17 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
    T18 = st.sidebar.number_input('T18 (-41 to -91)',min_value=-95, max_value=-39, value=-39)
   

    data = {'T1': T1, 'T2': T2, 'T3': T3,
            'T4': T4, 'T5': T5,
            'T6': T6, 'T7': T7, 'T8': T8,
            'T9': T9, 'T10': T10, 'T11': T11,
            'T12': T12, 'T13': T13, 'T14': T14,
            'T15': T15, 'T16': T16, 'T17': T17,
            'T17': T18 }

    df = pd.DataFrame(data, index=['Values'])
    df = df.T
    st.dataframe(df, width=500, height=650)

    # code for Prediction
    Prediction = ''

    # creating a button for Prediction

    if st.button('Prediction'):
        Prediction = Cluster_prediction([[ T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18]])

        

        st.write(Prediction, unsafe_allow_html=True)


if __name__ == '__main__':
    main()