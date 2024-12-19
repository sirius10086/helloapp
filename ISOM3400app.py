import streamlit as st
import pandas as pd

# Task 1: Upload and Display File
st.write("### Upload and Display File")
uploaded_file = st.file_uploader("Upload a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded CSV Data")
    st.write(df)
else:
    df = pd.read_csv('superstore_dataset.csv')
    st.write("### Default CSV Data (superstore_dataset.csv)")
    st.write(df.head(10))

# Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Task 2: Filter Data by Date Range
st.write("### Filter Data by Date Range")
date_range = st.slider(
    "Select Date Range",
    min_value=df['order_date'].min().date(),
    max_value=df['order_date'].max().date(),
    value=(df['order_date'].min().date(), df['order_date'].max().date())
)
filtered_df = df[
    (df['order_date'] >= pd.to_datetime(date_range[0])) &
    (df['order_date'] <= pd.to_datetime(date_range[1]))
]
st.write(filtered_df[['order_date', 'customer', 'product_name']])

# Task 3: Analyze Sales by Region
st.write("### Analyze Sales by Region")
region = st.selectbox("Select Region", df['region'].unique())
region_df = df[df['region'] == region]
total_sales = region_df['sales'].sum()
total_profit = region_df['profit'].sum()
st.write(f"Total Sales in {region}: ${total_sales}")
st.write(f"Total Profit in {region}: ${total_profit}")

# Task 4: Customer Feedback Form
st.write("### Customer Feedback Form")
with st.form(key="feedback_form"):
    customer = st.text_input("Customer Name")
    product_name = st.text_input("Product Name")
    feedback = st.text_area("Feedback")
    agree = st.checkbox("I agree to the terms and conditions")
    submit_button = st.form_submit_button("Submit Feedback")
    if submit_button:
        if agree:
            st.write("### Submitted Feedback")
            st.write(f"**Customer:** {customer}")
            st.write(f"**Product Name:** {product_name}")
            st.write(f"**Feedback:** {feedback}")
        else:
            st.write("You must agree to the terms and conditions to submit feedback.")
