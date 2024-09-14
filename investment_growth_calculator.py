import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def investment_growth_calculator(conversion_rate):
    st.header("Investment Growth Calculator")

    # Input fields for investment growth
    initial_investment = st.number_input("Initial Investment", value=10000) * conversion_rate
    annual_contribution = st.number_input("Annual Contribution", value=5000) * conversion_rate
    annual_return_rate = st.slider("Annual Return Rate (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.1)
    years = st.slider("Investment Period (Years)", min_value=1, max_value=50, value=30)

    # Investment growth calculation
    balance = initial_investment
    balances = []
    for i in range(years):
        balance += annual_contribution
        balance *= (1 + annual_return_rate / 100)
        balances.append(balance)

    # Output the final value
    st.write(f"Projected Investment Value: **{balance/conversion_rate:.2f}** {currency_choice}")

    # Plot investment growth
    st.subheader("Investment Growth Over Time")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, years + 1), np.array(balances) / conversion_rate, label='Investment Growth')
    ax.set_xlabel('Years')
    ax.set_ylabel(f'Investment Value ({currency_choice})')
    ax.set_title('Investment Growth Over Time')
    st.pyplot(fig)
