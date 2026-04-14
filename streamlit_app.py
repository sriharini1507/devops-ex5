import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart harini Analyzer", layout="centered")

st.title("💰 Smart Expense Analyzer")
st.write("Analyze your expenses and savings easily!")

# Input section
income = st.number_input("Enter your monthly income (₹)", min_value=0)

st.subheader("Enter your expenses:")

food = st.number_input("Food (₹)", min_value=0)
rent = st.number_input("Rent (₹)", min_value=0)
travel = st.number_input("Travel (₹)", min_value=0)
shopping = st.number_input("Shopping (₹)", min_value=0)
others = st.number_input("Others (₹)", min_value=0)

# Calculate button
if st.button("Analyze Expenses"):

    total_expense = food + rent + travel + shopping + others
    savings = income - total_expense

    st.subheader("📊 Summary")
    st.write(f"Total Expense: ₹{total_expense}")
    st.write(f"Savings: ₹{savings}")

    if savings > 0:
        st.success("Great! You are saving money 👍")
    elif savings == 0:
        st.warning("You are breaking even 😐")
    else:
        st.error("You are overspending ⚠️")

    # Create DataFrame
    data = {
        "Category": ["Food", "Rent", "Travel", "Shopping", "Others"],
        "Amount": [food, rent, travel, shopping, others]
    }

    df = pd.DataFrame(data)

    # Plot pie chart
    st.subheader("📈 Expense Distribution")

    fig, ax = plt.subplots()
    ax.pie(df["Amount"], labels=df["Category"], autopct="%1.1f%%")
    ax.axis("equal")

    st.pyplot(fig)
