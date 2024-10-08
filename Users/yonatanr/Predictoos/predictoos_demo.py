import streamlit as st
import pandas as pd
import time 

# Display the logo
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

    # Suggest "date" and "sales" columns
    date_candidate = next((col for col in df.columns if "date" in col.lower()), None)
    sales_candidate = next((col for col in df.columns if "sales" in col.lower()), None)

    # Allow the user to select the date column
    date_column = st.selectbox("Select the date column", options=df.columns.tolist(), index=df.columns.tolist().index(date_candidate) if date_candidate else 0)

    # Allow the user to select the sales column with a default suggestion
    sales_column = st.selectbox("Select the sales column", options=df.columns.tolist(), index=df.columns.tolist().index(sales_candidate) if sales_candidate else 0)

    # Display the selected columns for confirmation
    st.write(f"Selected date column: {date_column}")
    st.write(f"Selected sales column: {sales_column}")

    # Save the confirmed selections
    if st.button("Confirm selections"):
        # Add a loading spinner with a delay
        with st.spinner('Calculating predictions...'):
            time.sleep(5)  # Wait for 5 seconds
            
        st.session_state.selected_date_column = date_column
        st.session_state.selected_sales_column = sales_column
        st.success("Selections saved!")

    # Display the selected columns alongside the original
    if 'selected_date_column' in st.session_state and 'selected_sales_column' in st.session_state:
        selected_df = df[[st.session_state.selected_date_column, st.session_state.selected_sales_column]]
        st.write("Here is a sample of your demand forecast:")
        st.dataframe(selected_df.head(10))

        # Function to convert DataFrame to CSV in memory
        def convert_df_to_csv(df):
            return df.to_csv(index=False).encode('utf-8')

        # Create a download button for the selected DataFrame
        csv = convert_df_to_csv(selected_df)
        st.download_button(
            label="Download full forecast",
            data=csv,
            file_name='forecast.csv',
            mime='text/csv'
        )
