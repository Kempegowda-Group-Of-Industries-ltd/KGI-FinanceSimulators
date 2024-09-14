import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def compound_interest_variations_calculator(conversion_rate):
    st.header("Compound Interest with Variations Calculator")

    # Input fields for compound interest
    principal = st.number_input("Principal Amount", value=5000) * conversion_rate
    annual_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    compounds_per_year = st.selectbox("Compounding Frequency", ["Daily", "Monthly", "Quarterly", "Annually"])
    years = st.slider("Years", min_value=1, max_value=50, value=20)

    # Convert compounding frequency to number of compounding periods
    if compounds_per_year == "Daily":
        n = 365
    elif compounds_per_year == "Monthly":
        n = 12
    elif compounds_per_year == "Quarterly":
        n = 4
    else:
        n = 1

    # Compound interest calculation
    future_value = principal * (1 + (annual_rate / 100 / n)) ** (n * years)

    # Output future value
    st.write(f"Future Value with {compounds_per_year} Compounding: **{future_value/conversion_rate:.2f}** {currency_choice}")

    # Plot compound interest growth
    st.subheader("Investment Growth Over Time")
    times = np.arange(0, years + 1)
    values = [principal * (1 + (annual_rate / 100 / n)) ** (n * t) for t in times]
    
    fig, ax = plt.subplots()
    ax.plot(times, np.array(values) / conversion_rate, label=f'Compound Interest ({compounds_per_year})')
    ax.set_xlabel('Years')
    ax.set_ylabel(f'Future Value ({currency_choice})')
    ax.set_title(f'Compound Interest Growth ({compounds_per_year})')
    st.pyplot(fig)
