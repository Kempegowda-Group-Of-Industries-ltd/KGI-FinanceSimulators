import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def mortgage_payoff_calculator(conversion_rate):
    st.header("Mortgage Payoff Calculator")

    # Input fields for mortgage payoff
    loan_amount = st.number_input("Remaining Loan Balance", value=200000) * conversion_rate
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=4.0, step=0.1)
    loan_term = st.slider("Loan Term Remaining (Years)", min_value=1, max_value=30, value=25)
    extra_payment = st.number_input("Extra Monthly Payment", value=500) * conversion_rate

    # Mortgage payoff calculation
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)
    total_monthly_payment = monthly_payment + extra_payment
    balances = []
    balance = loan_amount
    payoff_time = 0

    for i in range(int(num_payments)):
        interest = balance * monthly_rate
        principal = total_monthly_payment - interest
        balance -= principal
        balances.append(balance)
        if balance <= 0:
            payoff_time = i + 1
            break

    # Output payoff time
    payoff_years = payoff_time // 12
    payoff_months = payoff_time % 12
    st.write(f"Mortgage Payoff Time: **{payoff_years} years, {payoff_months} months**")

    # Plot payoff schedule
    st.subheader("Mortgage Payoff Schedule")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, payoff_time + 1), balances[:payoff_time] / conversion_rate, label='Remaining Balance')
    ax.set_xlabel('Month')
    ax.set_ylabel(f'Balance ({currency_choice})')
    ax.set_title('Mortgage Payoff Over Time')
    st.pyplot(fig)
