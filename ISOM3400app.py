import streamlit as st

# Title and introductory text
st.title("Business Dashboard")
st.header("Product Sales and Customer Engagement Overview")
st.subheader("Key Metrics")
st.write("This dashboard provides insights into product sales performance and customer interactions.")

# Different text elements
st.markdown("**Sales Summary**")
st.text("Below is a summary of the latest sales data.")
st.code("sales_data = pd.read_csv('sales_data.csv')", language="python")
st.caption("Data source: Company database")
st.divider()
