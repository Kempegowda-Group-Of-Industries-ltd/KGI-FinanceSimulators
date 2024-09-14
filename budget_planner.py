import streamlit as st
import matplotlib.pyplot as plt

def budget_planner(conversion_rate):
    st.header("Budget Planner")

    # Input fields for income and expenses
    income = st.number_input("Monthly Income", value=4000) * conversion_rate
    expenses = {
        "Rent": st.number_input("Rent", value=1000) * conversion_rate,
        "Groceries": st.number_input("Groceries", value=500) * conversion_rate,
        "Utilities": st.number_input("Utilities", value=200) * conversion_rate,
        "Transportation": st.number_input("Transportation", value=300) * conversion_rate,
        "Entertainment": st.number_input("Entertainment", value=150) * conversion_rate,
        "Others": st.number_input("Other Expenses", value=350) * conversion_rate
    }

    # Budget breakdown calculation
    total_expenses = sum(expenses.values())
    savings = income - total_expenses

    # Output budget breakdown
    st.write(f"Total Monthly Expenses: **{total_expenses/conversion_rate:.2f}** {currency_choice}")
    st.write(f"Remaining Savings: **{savings/conversion_rate:.2f}** {currency_choice}")

    # Pie chart for budget breakdown
    fig, ax = plt.subplots()
    ax.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
