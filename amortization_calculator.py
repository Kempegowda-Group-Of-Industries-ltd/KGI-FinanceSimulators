import streamlit as st
import numpy as np
import pandas as pd

def amortization_calculator(conversion_rate):
    st.header("Amortization Calculator")

    # Input fields for amortization
    loan_amount = st.number_input("Loan Amount", value=100000) * conversion_rate
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=4.0, step=0.1)
    loan_term = st.slider("Loan Term (Years)", min_value=1, max_value=30, value=15)

    # Amortization calculations
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

    # Amortization schedule
    amortization_schedule = []
    balance = loan_amount
    for i in range(1, int(num_payments) + 1):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        amortization_schedule.append([i, principal, interest, balance])

    # Display amortization schedule
    df = pd.DataFrame(amortization_schedule, columns=["Month", "Principal", "Interest", "Balance"])
    df['Principal'] /= conversion_rate
    df['Interest'] /= conversion_rate
    df['Balance'] /= conversion_rate
    st.write(df)

    # Display monthly payment
    st.write(f"Monthly Payment: **{monthly_payment/conversion_rate:.2f}** {currency_choice}")
