import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def k401_calculator(conversion_rate):
    st.header("401K Calculator")

    # Input fields for 401K
    current_savings = st.number_input("Current 401K Savings", value=50000) * conversion_rate
    annual_contribution = st.number_input("Annual Contribution", value=18000) * conversion_rate
    employer_match = st.slider("Employer Match (%)", min_value=0.0, max_value=100.0, value=50.0) / 100
    employer_match_limit = st.number_input("Employer Match Limit (%)", value=6.0) / 100
    annual_return_rate = st.slider("Annual Return Rate (%)", 0.0, 15.0, value=7.0, step=0.1)
    years_to_retirement = st.slider("Years to Retirement", 1, 50, value=30)

    # 401K savings calculation
    employer_contribution = min(annual_contribution, employer_match_limit * current_savings) * employer_match
    total_contribution = annual_contribution + employer_contribution
    balance = current_savings
    balances = []

    for i in range(years_to_retirement):
        balance += total_contribution
        balance *= (1 + annual_return_rate / 100)
        balances.append(balance)

    # Output final savings
    st.write(f"Projected 401K Savings at Retirement: **{balance/conversion_rate:.2f}** {currency_choice}")

    # Plot 401K growth
    st.subheader("401K Savings Growth Over Time")
    fig, ax = plt.subplots()
    ax.plot(np.arange(1, years_to_retirement + 1), np.array(balances) / conversion_rate, label='401K Savings')
    ax.set_xlabel('Years')
    ax.set_ylabel(f'Savings ({currency_choice})')
    ax.set_title('401K Growth')
    st.pyplot(fig)
