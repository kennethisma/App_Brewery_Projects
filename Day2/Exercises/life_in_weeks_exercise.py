# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age_expectative = 90 - int(age)

days_left = age_expectative * 365

weeks_left = age_expectative * 52

months_left = age_expectative * 12

print(
    f"You have {days_left} days, {weeks_left} weeks and {months_left} months")
