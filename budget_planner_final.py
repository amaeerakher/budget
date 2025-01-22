import streamlit as st

#This is the welcome message
st.title("Welcome to your Travel Budget Tracker!")
st.write("******")

#Categories defines all the things we are tracking within the planner
categories = ["Travel expenses", "Accommodation expenses", "Excursion expenses", "Food expenses", "Miscellaneous"]

#Dictionaries hold each of the amounts and the lists will hold the category names where overspending or saving is seen
budget = {}
spending = {}
saving = {}
overspending = []
savings = []

#The amounts are being stored for each category in the dictionary
st.write("Please enter your decided total budget for each category:")

for i in categories:
    budget[i] = st.number_input(i + " in rupees", key=i + " budget")   #This stores each total value of spending

st.write("Please enter your total spending for each category:")

for j in categories:
    spending[j] = st.number_input(j + " in rupees", key=j + " spending")  #This stores each total value of spending

#Each sum of budget, spending, savings and over spending according to category is saved here respectively
total_budget = sum(budget.values())
total_spending = sum(spending.values())
total_savings = 0
total_overspending = 0

#Here we compare the budgets with the spending
st.write("******")
st.write("Here is a comparison of your budget and spendings for each category:")

for category in budget:
    difference = spending[category] - budget[category]  # Calculate the difference between spending and budget
    st.write(category + ":")
    st.write("Budgeted: Rs. " + str(budget[category]))
    st.write("Spent: Rs. " + str(spending[category]))

    #This if-elif-else statement is helping us determine and print if the user has spent extra in the category or not
    if difference > 0:
        total_overspending += difference
        st.write("You have spent Rs. " + str(difference) + " extra on " + category + ".")
        overspending.append(category)
    elif difference < 0:
        savings_amt = -difference
        saving[category] = savings_amt
        total_savings += savings_amt
        st.write("You have saved Rs. " + str(saving[category]) + " on " + category + ".")
        savings.append(category)
    else:
        st.write("You have spent your full budgeted amount for " + category + ".")

# Displaying the final observations
st.write("*****")
st.write("Your spendings and savings can be seen as:")

st.write("Your total overspending across categories was: Rs. " + str(total_overspending))
st.write("Your total savings across categories was: Rs. " + str(total_savings))
st.write("Your total budget was: Rs. " + str(total_budget))
st.write("Total spending was: Rs. " + str(total_spending))

#This gives us the money saved or extra spent
total_difference = total_spending - total_budget
if total_difference > 0:
    st.write("You have gone over your total budget of Rs. " + str(total_budget) + " by Rs. " + str(total_difference) + ".")
    st.write("Please consider cutting your expenses, especially in: " + ", ".join(overspending) + ".")
elif total_difference < 0:
    st.write("You have stayed under your total budget of Rs. " + str(total_budget) + " and saved Rs. " + str(-total_difference) + ".")
    st.write("You have saved well in: " + ", ".join(savings) + ".")
else:
    st.write("You have spent your exact budget of Rs. " + str(total_budget) + ". Good job!")

# Concluding message
st.write("*****")
st.write("Thank you for using our budget planner!")
