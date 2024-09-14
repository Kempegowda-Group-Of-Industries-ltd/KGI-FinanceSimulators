import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def auto_loan_calculator(conversion_rate):
    st.header("Auto Loan Calculator")
    
    # Input fields for auto loan
    car_price = st.number_input("Car Price", value=20000) * conversion_rate
    down_payment = st.number_input("Down Payment", value=5000) * conversion_rate
    loan_amount = car_price - down_payment
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=3.5, step=0.1)
    loan_term = st.slider("Loan Term (Years)", min_value=1, max_value=7, value=5)

    # Loan calculations
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

    # Output
    st.write(f"Monthly Payment: **{monthly_payment/conversion_rate:.2f}** {currency_choice}")

    # Generate amortization graph (same approach as loan calculator)
