import streamlit as st

def currency_exchange_calculator():
    st.header("Currency Exchange Calculator")

    # Input fields for currency exchange
    base_currency_amount = st.number_input("Amount in Base Currency", value=100)
    conversion_rate = st.number_input("Conversion Rate", value=0.013)  # Example: INR to USD conversion

    # Currency exchange calculation
    converted_amount = base_currency_amount * conversion_rate

    # Output the converted value
    st.write(f"Converted Amount: **{converted_amount:.2f}** in Target Currency")
