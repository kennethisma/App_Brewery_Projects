import pandas
students_dict = {"students": ["Fabis", "Paola", "Kenneth"],
                 "score": [56, 57, 58]}

students_dataframe = pandas.DataFrame(students_dict)

for index,row in students_dataframe.iterrows():
    print(index)
