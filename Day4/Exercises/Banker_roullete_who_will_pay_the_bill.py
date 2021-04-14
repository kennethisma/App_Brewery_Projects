# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_of_names = len(names)

random_name_number = random.randrange(0, number_of_names)

print(f'{names[random_name_number]} is going to buy the meal today!')
