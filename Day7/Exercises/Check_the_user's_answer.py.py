import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
number_of_word = len(word_list)

random_word = random.randint(0, number_of_word - 1)

chose_word = word_list[random_word]

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter: ').lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chose_word:
    if guess == letter:
        print('Right')
    else:
        print('Wrong')

##solution##
# la unica solucion fue que yo cree un index random ella uso el modulo choice
