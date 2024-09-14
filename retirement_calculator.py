import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def retirement_calculator(conversion_rate):
    st.header("Retirement Calculator")

    # Input fields for retirement
    current_savings = st.number_input("Current Savings", value=50000) * conversion_rate
    annual_contribution = st.number_input("Annual Contribution", value=12000) * conversion_rate
    retirement_goal = st.number_input("Retirement Goal", value=1000000) * conversion_rate
    annual_return_rate = st.slider("Annual Return Rate (%)", 0.0, 15.0, value=7.0, step=0.1)
    years_to_retirement = st.slider("Years to Retirement", 1, 50, value=30)

    # Retirement savings calculations
    monthly_rate = annual_return_rate / 100 / 12
    months = years_to_retirement * 12
    balance = current_savings
    balances = []

    for i in range(months):
        balance += (annual_contribution / 12)
        balance *= (1 + monthly_rate)
        balances.append(balance)

    # Output projected balance
    st.write(f"Projected Savings at Retirement: **{balance/conversion_rate:.2f}** {currency_choice}")

    # Plot savings growth
    st.subheader("Savings Growth Over Time")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, months + 1), balances, label='Retirement Savings')
    ax.set_xlabel('Month')
    ax.set_ylabel(f'Savings ({currency_choice})')
    ax.set_title('Retirement Savings Growth')
    st.pyplot(fig)
