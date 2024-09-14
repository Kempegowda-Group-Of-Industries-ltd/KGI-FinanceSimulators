import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def compound_interest_calculator(conversion_rate):
    st.header("Compound Interest Calculator")

    # Input fields for compound interest
    principal = st.number_input("Initial Investment", value=10000) * conversion_rate
    annual_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    compounds_per_year = st.slider("Compounds Per Year", min_value=1, max_value=12, value=12)
    years = st.slider("Number of Years", min_value=1, max_value=50, value=20)

    # Compound interest calculation
    future_value = principal * (1 + (annual_rate / 100 / compounds_per_year)) ** (compounds_per_year * years)

    # Output future value
    st.write(f"Future Value: **{future_value/conversion_rate:.2f}** {currency_choice}")

    # Plot the compound growth
    times = np.arange(0, years + 1, 1)
    values = [principal * (1 + (annual_rate / 100 / compounds_per_year)) ** (compounds_per_year * t) for t in times]

    fig, ax = plt.subplots()
    ax.plot(times, np.array(values) / conversion_rate, label='Investment Growth')
    ax.set_xlabel('Years')
    ax.set_ylabel(f'Future Value ({currency_choice})')
    ax.set_title('Compound Interest Growth Over Time')
    st.pyplot(fig)
