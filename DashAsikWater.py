import streamlit as st
import pandas as pd

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