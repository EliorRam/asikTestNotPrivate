import streamlit as st
import pandas as pd
import mysql.connector

# Print secrets for debugging (be cautious with this)
st.write("Database Password:", st.secrets["db_password"])

# Establish database connection
db_conn = mysql.connector.connect(
    host=st.secrets["db_host"],
    user=st.secrets["db_username"],
    password=st.secrets["db_password"],
    database=st.secrets["db_name"]
)

# Title
st.title("Interactive Dashboard")

# Sample DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Values': [100, 200, 500]
})

# Dropdown for user selection
category = st.selectbox("Choose a Category", df['Category'])

# Display selected category details
st.write(f"Selected Category: {category}")
st.write(df[df['Category'] == category])