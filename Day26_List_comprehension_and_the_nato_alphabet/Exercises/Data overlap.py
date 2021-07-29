

# Write your code above 👆
with open("file1.txt") as file1:
    file1_numbers = file1.readlines()

with open("file2.txt") as file2:
    file2_numbers = file2.readlines()

result = [int(number)
          for number in file1_numbers if number in file2_numbers]

print(result)
