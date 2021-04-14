# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
counter = 0
elements = 0
for item in student_heights:
    counter += item
    elements += 1
average_height = counter / elements
print(average_height)
