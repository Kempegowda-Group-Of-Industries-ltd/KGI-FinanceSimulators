import streamlit as st

def sales_tax_calculator(conversion_rate):
    st.header("Sales Tax Calculator")

    # Input fields for sales tax
    price = st.number_input("Price of Item", value=100) * conversion_rate
    sales_tax_rate = st.slider("Sales Tax Rate (%)", min_value=0.0, max_value=15.0, value=7.0)

    # Sales tax calculation
    total_cost = price * (1 + sales_tax_rate / 100)

    # Output total cost
    st.write(f"Total Cost Including Tax: **{total_cost/conversion_rate:.2f}** {currency_choice}")
