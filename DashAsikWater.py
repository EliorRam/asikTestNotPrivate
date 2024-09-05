import streamlit as st
import pandas as pd
import io
import os

# Title of the app
st.title("Excel File Processor")

# File uploader
uploaded_file = st.file_uploader("Upload your csv file", type=["csv"])

# Function to convert dataframe to a downloadable Excel file
def to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    correct_format = "%d/%m/%Y %H:%M"
    df['timestamp'] = pd.to_datetime(df['Date'], format=correct_format)
    df['month_year'] = df['timestamp'].dt.strftime('%Y-%m')
    result = df.groupby(['Customer name'])[['Gross sales', 'Cost of goods']].sum().reset_index()
    
    file_name_change = os.path.basename(uploaded_file).split('.')[0]
    result['Profit'] = result['Gross sales'] - result['Cost of goods']
    new_file_name = f'receipts_Totals_by_month_{file_name_change}.xlsx'
    row_name = f'receipts_row_by_month_{file_name_change}.xlsx'

    st.write("Processed DataFrame")
    st.write(result)
    excel_data = to_excel(result)
    st.download_button(label="Download Processed Excel",
                        data=excel_data,
                        file_name='processed_file.xlsx',
                        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')