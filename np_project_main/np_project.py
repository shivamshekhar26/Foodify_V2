import streamlit as st
import pandas as pd
import numpy as np

st.title("AMAZON SALES DASHBOARD")

# Load the dataset
df = pd.read_csv("amazon_sales_data.csv")
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['TotalSales'] = df['Quantity'] * df['Price']

# --- Step 1: Show Data and NumPy Calculations ---
if st.button("CLICK HERE TO GET DATASET AND CALCULATIVES",type="primary"):
    st.subheader("DATASET OF AMAZON SALES")
    st.dataframe(df)

    sales_np = df['TotalSales'].to_numpy()

    # Display each metric in its own section with a header
    st.header("Total Sales")
    st.write(f"₹{np.sum(sales_np):,.2f}")

    st.header("Mean Sales")
    st.write(f"₹{np.mean(sales_np):,.2f}")

    st.header("Maximum Sales")
    st.write(f"₹{np.max(sales_np):,.2f}")

    st.header("Minimum Sales")
    st.write(f"₹{np.min(sales_np):,.2f}")

    st.header("Standard Deviation of Sales")
    st.write(f"₹{np.std(sales_np):,.2f}")

# --- Step 2: Show Graphs after clicking a button ---
if st.button("CLICK HERE TO CHECK GRAPHS",type="primary"):
    st.header("Total Sales by Product")
    sales_by_product = df.groupby("Product")["TotalSales"].sum().sort_values()
    st.bar_chart(sales_by_product)

    st.header("Total Sales by Category")
    sales_by_category = df.groupby("Category")["TotalSales"].sum()
    st.bar_chart(sales_by_category)

    st.header("Sales Over Time")
    sales_by_date = df.groupby("OrderDate")["TotalSales"].sum()
    st.line_chart(sales_by_date)
