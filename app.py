import streamlit as st
from loan_calculator import loan_calculator
from auto_loan_calculator import auto_loan_calculator
from mortgage_calculator import mortgage_calculator
from retirement_calculator import retirement_calculator
from interest_payment_calculator import interest_payment_calculator
from compound_interest_calculator import compound_interest_calculator
from income_tax_calculator import income_tax_calculator
from investment_calculator import investment_growth_calculator
from currency_converter import currency_converter
from amortization_calculator import amortization_calculator
from budget_tracker import budget_tracker
from inflation_calculator import inflation_calculator
from salary_calculator import salary_calculator
from sales_tax_calculator import sales_tax_calculator
from mortgage_payoff_calculator import mortgage_payoff_calculator
from k401_calculator import k401_calculator


st.title("KGI Finance Simulators")

# Global currency conversion settings
currencies = {"USD": 1, "INR": 82.0}  # Example conversion rates
currency_choice = st.sidebar.selectbox("Select Currency", options=["USD", "INR"])
conversion_rate = currencies[currency_choice]

# Sidebar for navigation
calculator_choice = st.sidebar.selectbox(
    "Choose a Calculator", 
    ["Loan Calculator", "Auto Loan", "Mortgage Loan", "Retirement Calculator", "Interest Payment", 
     "Compound Interest", "Income Tax", "Investment Growth", "Amortization", "Budget Tracker",
     "Inflation Calculator", "Salary Calculator", "Sales Tax Calculator", "Mortgage Payoff",
     "401K Calculator"]
)

# Call appropriate calculator functions with currency conversion
if calculator_choice == "Loan Calculator":
    loan_calculator(conversion_rate)
elif calculator_choice == "Auto Loan":
    auto_loan_calculator(conversion_rate)
elif calculator_choice == "Mortgage Loan":
    mortgage_calculator(conversion_rate)
elif calculator_choice == "Retirement Calculator":
    retirement_calculator(conversion_rate)
elif calculator_choice == "Interest Payment":
    interest_payment_calculator(conversion_rate)
elif calculator_choice == "Compound Interest":
    compound_interest_calculator(conversion_rate)
elif calculator_choice == "Income Tax":
    income_tax_calculator(conversion_rate)
elif calculator_choice == "Investment Growth":
    investment_growth_calculator(conversion_rate)
elif calculator_choice == "Amortization":
    amortization_calculator(conversion_rate)
elif calculator_choice == "Budget Tracker":
    budget_tracker(conversion_rate)
elif calculator_choice == "Inflation Calculator":
    inflation_calculator(conversion_rate)
elif calculator_choice == "Salary Calculator":
    salary_calculator(conversion_rate)
elif calculator_choice == "Sales Tax Calculator":
    sales_tax_calculator(conversion_rate)
elif calculator_choice == "Mortgage Payoff":
    mortgage_payoff_calculator(conversion_rate)
elif calculator_choice == "401K Calculator":
    k401_calculator(conversion_rate)






import streamlit as st
from loan_calculator import loan_calculator
from auto_loan_calculator import auto_loan_calculator
from mortgage_calculator import mortgage_calculator
from retirement_calculator import retirement_calculator
from interest_payment_calculator import interest_payment_calculator
from compound_interest_calculator import compound_interest_calculator
from income_tax_calculator import income_tax_calculator
from investment_calculator import investment_growth_calculator
from currency_converter import currency_converter
from amortization_calculator import amortization_calculator
from budget_tracker import budget_tracker
from inflation_calculator import inflation_calculator
from salary_calculator import salary_calculator
from sales_tax_calculator import sales_tax_calculator
from mortgage_payoff_calculator import mortgage_payoff_calculator
from k401_calculator import k401_calculator

# Title and description
st.title("KGI Finance Simulators")
st.write("Welcome to the KGI Finance Simulators! Use the tools below to calculate various financial metrics and manage your personal or business finances effectively.")

# Global currency conversion settings
st.sidebar.header("Currency Settings")
currencies = {"USD": 1, "INR": 82.0}  # Example conversion rates
currency_choice = st.sidebar.selectbox("Select Currency", options=["USD", "INR"])
conversion_rate = currencies[currency_choice]

# Sidebar for navigation
st.sidebar.header("Calculator Selection")
calculator_choice = st.sidebar.selectbox(
    "Choose a Calculator", 
    ["Loan Calculator", "Auto Loan", "Mortgage Loan", "Retirement Calculator", "Interest Payment", 
     "Compound Interest", "Income Tax", "Investment Growth", "Amortization", "Budget Tracker",
     "Inflation Calculator", "Salary Calculator", "Sales Tax Calculator", "Mortgage Payoff",
     "401K Calculator"]
)

# Function to display calculator based on user choice
def display_calculator(choice, rate):
    st.sidebar.markdown("### About")
    st.sidebar.write("Use the selected calculator to perform detailed financial calculations.")
    
    if choice == "Loan Calculator":
        st.header("Loan Calculator")
        loan_calculator(rate)
    elif choice == "Auto Loan":
        st.header("Auto Loan Calculator")
        auto_loan_calculator(rate)
    elif choice == "Mortgage Loan":
        st.header("Mortgage Loan Calculator")
        mortgage_calculator(rate)
    elif choice == "Retirement Calculator":
        st.header("Retirement Calculator")
        retirement_calculator(rate)
    elif choice == "Interest Payment":
        st.header("Interest Payment Calculator")
        interest_payment_calculator(rate)
    elif choice == "Compound Interest":
        st.header("Compound Interest Calculator")
        compound_interest_calculator(rate)
    elif choice == "Income Tax":
        st.header("Income Tax Calculator")
        income_tax_calculator(rate)
    elif choice == "Investment Growth":
        st.header("Investment Growth Calculator")
        investment_growth_calculator(rate)
    elif choice == "Amortization":
        st.header("Amortization Calculator")
        amortization_calculator(rate)
    elif choice == "Budget Tracker":
        st.header("Budget Tracker")
        budget_tracker(rate)
    elif choice == "Inflation Calculator":
        st.header("Inflation Calculator")
        inflation_calculator(rate)
    elif choice == "Salary Calculator":
        st.header("Salary Calculator")
        salary_calculator(rate)
    elif choice == "Sales Tax Calculator":
        st.header("Sales Tax Calculator")
        sales_tax_calculator(rate)
    elif choice == "Mortgage Payoff":
        st.header("Mortgage Payoff Calculator")
        mortgage_payoff_calculator(rate)
    elif choice == "401K Calculator":
        st.header("401K Calculator")
        k401_calculator(rate)

# Display the selected calculator
display_calculator(calculator_choice, conversion_rate)
