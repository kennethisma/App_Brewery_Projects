import random
import os
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def score(cards):
    '''return the sum of the numbers in the list'''
    ace = 11
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    elif score > 21 and ace in cards:
        cards.remove(ace)
        ace = 1
        cards.append(ace)
        score = sum(cards)
        return score
    else:
        return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "You lose, your opponent has a blackjack"
    elif user_score == 0:
        return "You win, you have a blackjack :O"
    elif computer_score > 21:
        return "You win, opponent went over 21"
    elif user_score > 21:
        return "You went over 21, you lose"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def clear():
    return os.system('cls')


def play():

    user_cards = random.choices(deck, k=2)  # List with 2 random numbers
    computer_cards = random.choices(deck, k=2)
    is_game_over = False

    while not is_game_over:
        user_score = score(user_cards)
        computer_score = score(computer_cards)

        print(f' Your hand: {user_cards}, current score: {user_score}\n'
              f" Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if should_deal == 'y':
                user_cards.append(random.choice(deck))
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(deck))
        computer_score = score(computer_cards)

    print(f" Your final hand: {user_cards}, final score: {user_score}\n"
          f" Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play()
