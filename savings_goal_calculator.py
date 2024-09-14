import streamlit as st

def savings_goal_calculator(conversion_rate):
    st.header("Savings Goal Calculator")

    # Input fields for savings goal
    goal_amount = st.number_input("Goal Amount", value=50000) * conversion_rate
    current_savings = st.number_input("Current Savings", value=10000) * conversion_rate
    years_to_save = st.slider("Years to Save", min_value=1, max_value=30, value=10)
    annual_interest_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)

    # Savings goal calculation
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_months = years_to_save * 12
    target_balance = goal_amount - current_savings
    monthly_saving = target_balance * monthly_interest_rate / ((1 + monthly_interest_rate) ** total_months - 1)

    # Output monthly saving requirement
    st.write(f"Required Monthly Saving: **{monthly_saving/conversion_rate:.2f}** {currency_choice}")
