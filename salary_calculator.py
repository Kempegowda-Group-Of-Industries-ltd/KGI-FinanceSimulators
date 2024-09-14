import streamlit as st

def salary_calculator(conversion_rate):
    st.header("Salary Calculator")

    # Input fields for salary
    annual_salary = st.number_input("Annual Salary", value=60000) * conversion_rate

    # Salary breakdown
    monthly_salary = annual_salary / 12
    weekly_salary = annual_salary / 52
    daily_salary = annual_salary / 260  # Assuming 5-day workweek

    # Output salary breakdown
    st.write(f"Monthly Salary: **{monthly_salary/conversion_rate:.2f}** {currency_choice}")
    st.write(f"Weekly Salary: **{weekly_salary/conversion_rate:.2f}** {currency_choice}")
    st.write(f"Daily Salary: **{daily_salary/conversion_rate:.2f}** {currency_choice}")
