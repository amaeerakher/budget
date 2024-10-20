import streamlit as st

# Display the welcome message
st.title("Welcome to your Travel Budget Tracker!")
st.write("******")

# Categories defines all the things we are tracking within the planner
categories = ["Travel expenses", "Accommodation expenses", "Excursion expenses", "Food expenses", "Miscellaneous"]

# Dictionaries to hold each of the amounts, and lists to track overspending or savings categories
budget = {}
spending = {}
saving = {}
overspending = []
savings = []

# Collect budget inputs from the user
st.write("Please enter your decided total budget for each category:")

for i in categories:
    budget[i] = st.number_input(f"{i} in rupees", min_value=0.0, step=100.0)

st.write("Please enter your total spending for each category:")

for j in categories:
    spending[j] = st.number_input(f"{j} in rupees", min_value=0.0, step=100.0)

# Calculating the total budget and total spending
total_budget = sum(budget.values())
total_spending = sum(spending.values())
total_savings = 0
total_overspending = 0

# Displaying the comparison of budgets and spendings for each category
st.write("******")
st.write("Here is a comparison of your budget and spendings for each category:")

for category in budget:
    difference = spending[category] - budget[category]  # Calculate the difference between spending and budget
    st.write(f"{category}:")
    st.write(f"Budgeted: Rs. {budget[category]}")
    st.write(f"Spent: Rs. {spending[category]}")

    # Checking if there's overspending or savings
    if difference > 0:
        total_overspending += difference
        st.write(f"You have spent Rs. {difference} extra on {category}.")
        overspending.append(category)
    elif difference < 0:
        savings_amt = -difference
        saving[category] = savings_amt
        total_savings += savings_amt
        st.write(f"You have saved Rs. {saving[category]} on {category}.")
        savings.append(category)
    else:
        st.write(f"You have spent your full budgeted amount for {category}.")

# Displaying the final observations
st.write("*****")
st.write("Your spendings and savings can be seen as:")

st.write(f"Your total overspending across categories was: Rs. {total_overspending}")
st.write(f"Your total savings across categories was: Rs. {total_savings}")
st.write(f"Your total budget was: Rs. {total_budget}")
st.write(f"Total spending was: Rs. {total_spending}")

# Providing feedback based on the overall spending vs. budget
total_difference = total_spending - total_budget
if total_difference > 0:
    st.write(f"You have gone over your total budget of Rs. {total_budget} by Rs. {total_difference}.")
    st.write(f"Please consider cutting your expenses, especially in: {', '.join(overspending)}.")
elif total_difference < 0:
    st.write(f"You have stayed under your total budget of Rs. {total_budget} and saved Rs. {-total_difference}.")
    st.write(f"You have saved well in: {', '.join(savings)}.")
else:
    st.write(f"You have spent your exact budget of Rs. {total_budget}. Good job!")

# Concluding message
st.write("*****")
st.write("Thank you for using our budget planner!")
