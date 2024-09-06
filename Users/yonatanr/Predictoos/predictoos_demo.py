import streamlit as st
import pandas as pd

st.markdown("![](https://www.diplomat-global.com/wp-content/uploads/2018/06/logo.png)")
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


    # Allow users to select which columns to display
    columns = st.multiselect("Select columns to display", options=df.columns.tolist(), default=df.columns.tolist())

    # Show the selected columns
    if columns:
        st.write("Here are the selected columns:")
        st.dataframe(df[columns])
