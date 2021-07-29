# List comprehension
numbers = [1, 2, 3]
# new_numbers = [new_item for item in numbers]
# ||
# ||
# ||
new_numbers = [n + 1 for n in numbers]

# -------------------------#
name = "Kenneth"

letters_list = [letter for letter in name]

#--------- Challenge----------#

numbers_double = [n*2 for n in range(1, 5)]

# print(numbers_double)

#---------2nd Challenge--------#

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
