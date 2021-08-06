import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter: row.code for inx, row in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ")

name_list = [letter.capitalize() for letter in user_word]

nato_phonetic = [
    nato_phonetic_dict[word] for word in name_list if word in nato_phonetic_dict.keys()]

# for word in name_list:
#     if word in nato_phonetic_dict.keys:
#         nato_phonetic.append(nato_phonetic_dict.get(key))
print(nato_phonetic)
