import streamlit as st

def break_even_analysis_calculator(conversion_rate):
    st.header("Break-even Analysis Calculator")

    # Input fields for break-even analysis
    fixed_costs = st.number_input("Fixed Costs", value=10000) * conversion_rate
    variable_costs_per_unit = st.number_input("Variable Costs per Unit", value=50) * conversion_rate
    price_per_unit = st.number_input("Price per Unit", value=100) * conversion_rate

    # Break-even calculation
    break_even_units = fixed_costs / (price_per_unit - variable_costs_per_unit)

    # Output break-even point
    st.write(f"Break-even Point: **{break_even_units:.2f} units**")
