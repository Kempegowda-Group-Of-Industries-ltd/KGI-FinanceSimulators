import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def debt_reduction_calculator(conversion_rate):
    st.header("Debt Reduction Calculator")

    # Input fields for debt reduction
    loan_amount = st.number_input("Loan Amount", value=20000) * conversion_rate
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    monthly_payment = st.number_input("Monthly Payment", value=300) * conversion_rate
    additional_payment = st.number_input("Additional Monthly Payment", value=100) * conversion_rate

    # Debt reduction calculation
    total_payment = monthly_payment + additional_payment
    monthly_rate = interest_rate / 100 / 12
    months = 0
    total_interest = 0
    balance = loan_amount

    while balance > 0:
        interest = balance * monthly_rate
        principal = total_payment - interest
        balance -= principal
        total_interest += interest
        months += 1

    payoff_years = months // 12
    payoff_months = months % 12

    # Output debt reduction results
    st.write(f"Debt Payoff Time: **{payoff_years} years, {payoff_months} months**")
    st.write(f"Total Interest Paid: **{total_interest/conversion_rate:.2f}** {currency_choice}")
