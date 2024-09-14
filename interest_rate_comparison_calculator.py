import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def interest_rate_comparison_calculator(conversion_rate):
    st.header("Interest Rate Comparison Calculator")

    # Input fields for interest rate comparison
    loan_amount = st.number_input("Loan Amount", value=50000) * conversion_rate
    loan_term = st.slider("Loan Term (Years)", min_value=1, max_value=30, value=15)
    interest_rate1 = st.slider("Interest Rate 1 (%)", min_value=0.0, max_value=20.0, value=4.0, step=0.1)
    interest_rate2 = st.slider("Interest Rate 2 (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)

    # Interest comparison calculation
    monthly_rate1 = interest_rate1 / 100 / 12
    monthly_rate2 = interest_rate2 / 100 / 12
    months = loan_term * 12
    monthly_payment1 = loan_amount * monthly_rate1 / (1 - (1 + monthly_rate1) ** -months)
    monthly_payment2 = loan_amount * monthly_rate2 / (1 - (1 + monthly_rate2) ** -months)
    total_payment1 = monthly_payment1 * months
    total_payment2 = monthly_payment2 * months

    # Output comparison
    st.write(f"Total Payment at {interest_rate1}%: **{total_payment1/conversion_rate:.2f}** {currency_choice}")
    st.write(f"Total Payment at {interest_rate2}%: **{total_payment2/conversion_rate:.2f}** {currency_choice}")

    # Plot interest rate comparison
    fig, ax = plt.subplots()
    ax.bar(['Rate 1', 'Rate 2'], [total_payment1 / conversion_rate, total_payment2 / conversion_rate], color=['blue', 'orange'])
    ax.set_ylabel(f'Total Payment ({currency_choice})')
    ax.set_title('Interest Rate Comparison')
    st.pyplot(fig)
