import random


names = ["Kenneth", "Alex", "Fabis", "Paola", "Camila", "Sheyla"]
# Creating a new dictionary
students_score = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for student,
                   score in students_score.items() if score >= 60}

print(passed_students)
