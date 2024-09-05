import streamlit as st
import pandas as pd
from io import BytesIO

# Title of the app
st.title("Excel File Processor")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

# Function to convert dataframe to a downloadable Excel file
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

# Process the uploaded file
if uploaded_file is not None:
    # Load the Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Display the DataFrame
    st.write("Original DataFrame")
    st.write(df)

    # Process the DataFrame (example: adding a new column)
    df['New Column'] = df['Some Existing Column'] * 2  # Example processing

    # Display the processed DataFrame
    st.write("Processed DataFrame")
    st.write(df)

    # Provide a download link for the processed Excel file
    excel_data = to_excel(df)
    st.download_button(label="Download Processed Excel",
                       data=excel_data,
                       file_name='processed_file.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
