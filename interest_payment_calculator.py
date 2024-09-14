import streamlit as st

def interest_payment_calculator(conversion_rate):
    st.header("Interest Payment Calculator")

    # Input fields for interest payment
    loan_amount = st.number_input("Loan Amount", value=20000) * conversion_rate
    interest_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    loan_term = st.slider("Loan Term (Years)", min_value=1, max_value=30, value=10)

    # Interest calculation
    total_interest = loan_amount * (interest_rate / 100) * loan_term

    # Output total interest
    st.write(f"Total Interest Paid: **{total_interest/conversion_rate:.2f}** {currency_choice}")
