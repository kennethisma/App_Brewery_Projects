# My solution #######################################33
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for k in student_scores:
    student_grades[k] = student_scores[k]
    if student_grades[k] >= 91 and student_grades[k] <= 100:
        student_grades[k] = 'Outstanding'
    elif student_grades[k] >= 81 and student_grades[k] <= 90:
        student_grades[k] = "Exceeds Expectations"
    elif student_grades[k] >= 71 and student_grades[k] <= 80:
        student_grades[k] = 'Acceptable'
    else:
        student_grades[k] = 'fail'


# 🚨 Don't change the code below 👇
print(student_grades)


################################### Angela's solution ##########################################

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to covert scores into grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# Don't change the code below 👇
print(student_grades)
