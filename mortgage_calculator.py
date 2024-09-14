import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def mortgage_calculator(conversion_rate):
    st.header("Mortgage Loan Calculator")

    # Input fields for mortgage
    home_price = st.number_input("Home Price", value=300000) * conversion_rate
    down_payment = st.number_input("Down Payment", value=60000) * conversion_rate
    loan_amount = home_price - down_payment
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=4.0, step=0.1)
    loan_term = st.slider("Loan Term (Years)", min_value=1, max_value=30, value=25)

    # Mortgage calculations
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

    # Output
    st.write(f"Monthly Payment: **{monthly_payment/conversion_rate:.2f}** {currency_choice}")

    # Amortization schedule
    balances = []
    balance = loan_amount
    for i in range(int(num_payments)):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        balances.append(balance)

    # Plot mortgage amortization
    st.subheader("Mortgage Amortization Schedule")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, num_payments + 1), balances, label='Remaining Balance')
    ax.set_xlabel('Month')
    ax.set_ylabel(f'Balance ({currency_choice})')
    ax.set_title('Mortgage Balance Over Time')
    st.pyplot(fig)
