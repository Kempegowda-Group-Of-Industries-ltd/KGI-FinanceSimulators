import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def inflation_calculator(conversion_rate):
    st.header("Inflation Calculator")

    # Input fields for inflation
    initial_amount = st.number_input("Initial Amount", value=1000) * conversion_rate
    inflation_rate = st.slider("Inflation Rate (%)", min_value=0.0, max_value=20.0, value=3.0, step=0.1)
    years = st.slider("Years", min_value=1, max_value=50, value=20)

    # Inflation calculation
    future_value = initial_amount / ((1 + inflation_rate / 100) ** years)

    # Output the future value
    st.write(f"Future Value After Inflation: **{future_value/conversion_rate:.2f}** {currency_choice}")

    # Plot the decrease in value over time
    values = [initial_amount / ((1 + inflation_rate / 100) ** i) for i in range(years + 1)]
    fig, ax = plt.subplots()
    ax.plot(np.arange(0, years + 1), np.array(values) / conversion_rate, label='Value over Time')
    ax.set_xlabel('Years')
    ax.set_ylabel(f'Value ({currency_choice})')
    ax.set_title('Impact of Inflation Over Time')
    st.pyplot(fig)
