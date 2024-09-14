import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def loan_calculator(conversion_rate):
    st.header("Loan Calculator")

    # Input fields with currency conversion
    loan_amount = st.number_input("Loan Amount", value=10000) * conversion_rate
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    loan_term = st.slider("Loan Term (Years)", min_value=1, max_value=30, value=10)

    # Loan calculations
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

    # Output the payment in selected currency
    st.write(f"Monthly Payment: **{monthly_payment/conversion_rate:.2f}** {currency_choice}")

    # Amortization schedule (same as before)
    balances = []
    balance = loan_amount
    for i in range(int(num_payments)):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        balances.append(balance)

    # Plot amortization
    st.subheader("Amortization Schedule")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, num_payments + 1), balances, label='Remaining Balance')
    ax.set_xlabel('Month')
    ax.set_ylabel(f'Balance ({currency_choice})')
    ax.set_title('Loan Balance Over Time')
    st.pyplot(fig)
