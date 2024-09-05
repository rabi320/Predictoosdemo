import streamlit as st
import pandas as pd

# Set the title of the app
st.title('Predictoos AI Hub')

# File uploader for CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the first 5 rows of the DataFrame
    st.write("Here are the first 5 rows of the uploaded CSV:")
    st.dataframe(df.head())
