import streamlit as st

def income_tax_calculator(conversion_rate):
    st.header("Income Tax Calculator")

    # Input fields for income tax
    annual_income = st.number_input("Annual Income", value=60000) * conversion_rate
    tax_brackets = {
        0: 0.1,
        9875: 0.12,
        40125: 0.22,
        85525: 0.24,
        163300: 0.32,
        207350: 0.35,
        518400: 0.37
    }

    # Tax calculation based on US federal brackets (example)
    total_tax = 0
    previous_bracket_limit = 0

    for bracket_limit, rate in tax_brackets.items():
        if annual_income > bracket_limit:
            income_in_bracket = min(annual_income - bracket_limit, bracket_limit - previous_bracket_limit)
            total_tax += income_in_bracket * rate
            previous_bracket_limit = bracket_limit
        else:
            break

    # Output tax
    st.write(f"Total Income Tax: **{total_tax/conversion_rate:.2f}** {currency_choice}")
