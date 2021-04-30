######################################## My solution ########################################
import random
from art import logo
# Have a random number between 1 and 100
random_number = random.randint(1, 100)


def chose_level():
    ''' Returns the lives according to the chosen level '''
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        lives = 10
        return lives
    else:
        lives = 5
        return lives


def checking_number(guessed, random_number):
    if guessed > random_number:
        return "Too high.\nGuess again."
    elif guessed < random_number:
        return "To low.\nGuess again."


end_game = False
print(logo)
lives = chose_level()
while not end_game:
    print(f"You have {lives} attemps remaining to guess the number.")
    guessed = int(input("Make a guess: "))

    if guessed == random_number:
        end_game = True
        print(f"You got it! The answer was {random_number}")

    elif guessed != random_number:
        print(checking_number(guessed, random_number))
        lives -= 1

    if lives == 0:
        end_game = True
        print("You've run out of guesses, you lose.")


###################################### Angela's solution ###############################
# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}")

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()
