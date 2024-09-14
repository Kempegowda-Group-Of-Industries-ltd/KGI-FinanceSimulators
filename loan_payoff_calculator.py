import streamlit as st

def loan_payoff_calculator(conversion_rate):
    st.header("Loan Payoff Calculator")

    # Input fields for loan payoff
    loan_amount = st.number_input("Loan Amount", value=10000) * conversion_rate
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    monthly_payment = st.number_input("Monthly Payment", value=200) * conversion_rate

    # Loan payoff calculation
    monthly_rate = interest_rate / 100 / 12
    months = 0
    balance = loan_amount
    while balance > 0:
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance -= principal
        months += 1

    payoff_years = months // 12
    payoff_months = months % 12

    # Output payoff time
    st.write(f"Loan Payoff Time: **{payoff_years} years, {payoff_months} months**")
