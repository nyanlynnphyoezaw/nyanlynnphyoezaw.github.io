import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_star_rating import st_star_rating
import re


st.sidebar.title("MINTIFY")

page = st.sidebar.radio('Menu', ["Home","Invest","Tips", "About", "Contact", 'Rate Us'])

if page == 'Home':
    st.title("Mintify - Personal Finance Tracker")

    #income
    st.write("**Add your estimated income here**")
    income_type = st.radio("Select how often you get paid after tax", ['weekly', 'biweekly', 'monthly', 'yearly'])
    income_amount = st.number_input("Amount")
    if income_type == 'weekly':
        annual_income = income_amount * 52
    elif income_type == 'biweekly':
        annual_income = income_amount * 26
    elif income_type == 'monthly':
        annual_income = income_amount * 12
    elif income_type == 'yearly':
        annual_income = income_amount

    #expense
    st.write("**Add your estimated expenses per month here**")
    rent_amount = st.number_input("Enter your rent or mortgage payment per month")
    bill_amount = st.number_input("Enter your bill payment per month (Electricity, Phone, Wifi, Gas)")
    car_amount = st.number_input("Enter your car payment per month + insurance")
    grocery_amount = st.number_input("Enter how much you spend on grocery per month")
    dining_out_amount = st.number_input("Enter how much you spend on dining out per month")
    entertainment_amount = st.number_input("Enter how much you spend on entertainment per month")
    other_amount = st.number_input("Enter other expenses ou have per month")
    total_expense_month = rent_amount + bill_amount + car_amount + grocery_amount + dining_out_amount + entertainment_amount + other_amount
    total_expense_year = total_expense_month * 12
    balance_year = annual_income - total_expense_year
    balance_month = balance_year / 12

    expense_dict = {'Rent': rent_amount, 'Bills': bill_amount, 'Car': car_amount,
                    'Grocery': grocery_amount, 'Dining Out': dining_out_amount,
                    'Entertainment': entertainment_amount, 'Other': other_amount}
    #piechart
    expense_breakdown = st.button('Check your expense breakdown')
    if expense_breakdown:
        st.subheader('Expense Breakdown')
        labels = expense_dict.keys()
        sizes = expense_dict.values()
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    #balance
    balance_type = st.radio('Check your balance', ['Monthly', 'Yearly'])
    check_balance = st.button("Check your balance")
    if check_balance and balance_type == 'Monthly':
        st.write(f'Your estimated balance in a month: ${balance_month:,.2f}')
        st.write(f'Here is how much you can save and invest per year: ${balance_year:,.2f}')
    elif check_balance and balance_type == 'Yearly':
        st.write(f'Your estimated balance in a year: ${balance_year:,.2f}')
        st.write(f'Here is how much you can save and invest per year: ${balance_year:,.2f}')

    #setbudget
    budget_amount = st.number_input("Enter a budget to see the category that is above your budget")

    exceeded_budget = {}

    for category, expense in expense_dict.items():
        if expense > budget_amount:
            exceeded_budget[category] = expense

    if exceeded_budget:
        st.subheader("Categories Exceeding Your Budget:")
        for category, expense in exceeded_budget.items():
            st.write(f"{category}: ${expense:.2f}")
    else:
        st.success("Great news! All categories are within or equal to your budget.")

elif page == 'Invest':

        st.title("Compound Interest Calculator")
        initial_deposit = st.number_input("Initial Deposit", format="%.2f")
        interest_rate = st.number_input("Interest Rate (%)", format="%.2f")
        time = st.number_input("Time (Years)", format="%.2f")
        contribution_type = st.radio("Contribution Type", ['Yearly', 'Monthly'])
        contribution_amount = st.number_input("Contribution Amount", min_value=0.01, format="%.2f")
        calculate_button = st.button("Calculate")

        def calculate_compound_interest(initial_deposit, interest_rate, time, contribution_type, contribution_amount):
            if contribution_type == 'Monthly':
                contribution_amount=contribution_amount*12
            balances = [initial_deposit]
            time=int(time)
            for i in range(1,time+1):
                balance = initial_deposit + initial_deposit * (interest_rate/100) + contribution_amount
                balances.append(balance)
                initial_deposit=balance
            return balances

        if calculate_button:
            balances = calculate_compound_interest(initial_deposit, interest_rate, time, contribution_type,
                                                   contribution_amount)
            st.subheader(f"Final Balance: ${balances[-1]:,.2f}")
            st.subheader("Compound Interest Growth Over Time")
            periods = list(range(len(balances)))
            df = pd.DataFrame({'Period(Years)': periods, 'Balance': balances})
            st.dataframe(df, hide_index=True)
            st.line_chart(df.set_index('Period(Years)'))

elif page == 'Tips':
    st.title("Money Tips")

    money_topics = [
        "How to Improve Credit Score",
        "Money Saving Tips",
        "Investing for Beginners",
        "Creating a Budget",
        "Debt Management Strategies"
    ]

    selected_option = st.selectbox('Select a Money Tip:', money_topics)

    st.subheader(f"Tips for '{selected_option}':")

    if selected_option == "How to Improve Credit Score":
        tips = [
            "Pay your bills on time.",
            "Reduce outstanding debt.",
            "Check your credit report regularly.",
            "Avoid opening too many new credit accounts."
        ]
    elif selected_option == "Money Saving Tips":
        tips = [
            "Create a budget and stick to it.",
            "Cut unnecessary expenses.",
            "Build an emergency fund.",
            "Take advantage of discounts and coupons."
        ]
    elif selected_option == "Investing for Beginners":
        tips = [
            "Start with a diversified portfolio.",
            "Understand your risk tolerance.",
            "Research before making investment decisions.",
            "Consider long-term goals."
        ]
    elif selected_option == "Creating a Budget":
        tips = [
            "Track your income and expenses.",
            "Categorize and prioritize your spending.",
            "Set realistic financial goals.",
            "Adjust your budget as needed."
        ]
    elif selected_option == "Debt Management Strategies":
        tips = [
            "Prioritize high-interest debt.",
            "Consider debt consolidation.",
            "Negotiate with creditors for better terms.",
            "Seek professional advice if needed."
        ]
    else:
        tips = []

    for tip in tips:
        st.success(f"• {tip}")

elif page == 'About':
    st.title("About Mintify")

    st.write(
        "Mintify is a personal finance tracking application designed to help users manage their expenses, set budgets, and make informed financial decisions.")

    st.header("Features")
    st.markdown("- **Expense Tracking:** Easily input and categorize your expenses.")
    st.markdown("- **Budget Setting:** Set monthly budgets for different expense categories.")
    st.markdown("- **Visualization:** View visualizations of your spending patterns.")
    st.markdown("- **Financial Tips:** Access tips and advice for effective money management.")
    st.markdown(
        "- **Educational Resources:** Explore links to educational resources about personal finance for continuous learning.")
    st.write("Thank you for choosing Mintify for your personal finance needs.")

elif page == 'Contact':
    def check(email):
        if (re.fullmatch(regex, email)):
            st.success("Thank you for reaching out! We'll get back to you soon.")
            st.write("**Name:**", name)

            st.write("**Email:**", email)
            st.write("**Message:**", message)
        else:
            st.write("Invalid Email. Please enter a valid one")
    st.title("Contact Us")

    st.write("Have questions or suggestions? Reach out to us by filling out the form below.")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if st.button("Submit"):
        check(email)


elif page == 'Rate Us':
    st.title("Rate Us")

    st.write("**We value your feedback! Please provide a rating on a scale of 1 to 5.**")
    stars = st_star_rating("", maxValue=5, defaultValue=3, key="rating",dark_theme=True)

    if st.button("Submit Rating"):
        st.success(f"Thank you for your rating! You rated us {stars}/5.")

