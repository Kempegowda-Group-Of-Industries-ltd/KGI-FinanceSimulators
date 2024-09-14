import streamlit as st

def net_worth_calculator(conversion_rate):
    st.header("Net Worth Calculator")

    # Input fields for assets and liabilities
    assets = st.number_input("Total Assets", value=100000) * conversion_rate
    liabilities = st.number_input("Total Liabilities", value=50000) * conversion_rate

    # Net worth calculation
    net_worth = assets - liabilities

    # Output net worth
    st.write(f"Net Worth: **{net_worth/conversion_rate:.2f}** {currency_choice}")
