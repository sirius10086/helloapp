import streamlit as st

# Dashboard Title
st.title("Company Performance Dashboard")

# Main Header
st.header("Executive Summary")

# Subheader
st.subheader("Company Overview")

# Text Descriptions
st.write("Our company focuses on delivering high-quality products to our customers globally, leveraging technology to drive innovation.")
st.text("All figures are updated quarterly.")

# Formatted Text with Markdown
st.markdown("**Mission Statement:** Deliver excellence through innovation and customer-centric solutions.")

# Code Example
st.code("""
def calculate_growth(revenue_q1, revenue_q2):
    return (revenue_q2 - revenue_q1) / revenue_q1 * 100
""", language="python")

# Caption for Code Example
st.caption("This function calculates quarterly growth based on revenue.")

# Divider
st.divider()
