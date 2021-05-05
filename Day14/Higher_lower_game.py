# import random and game data
import random
from game_data import data
# get two random famous from the list game data.


def random_dict():
    '''Returns a random famous from game_data'''
    lenght_data = len(data)
    random_number = random.randint(0, lenght_data)
    random_famed = data[random_number - 1]
    return random_famed


def getting_followers(chose):
    '''returns followers'''
    if chose == 'a':
        return followers_a
    elif chose == 'b':
        return followers_b
    else:
        return


def compare_followers(famous_chose, score):
    if famous_chose == followers_a:
        if famous_chose > followers_b:
            score += 1
            print(f"You're right! Current score: {score}")
            return score
        elif famous_chose < followers_b:
            print(f"You're wrong! Final score: {score}")
            return score
        else:
            print(f"You're wrong! Final score: {score}")
            return score
    elif famous_chose == followers_b:
        if famous_chose > followers_a:
            score += 1
            print(f"You're right! Current score: {score}")
            return score
        elif famous_chose < followers_b:
            print(f"You're wrong! Final score: {score}")
            return score
        else:
            print(f"You're wrong! Final score: {score}")
            return score
    else:
        print(f"You're wrong! Final score: {score}")
        return score


famed_a = random_dict()
famed_b = random_dict()
followers_a = famed_a['follower_count']
followers_b = famed_b['follower_count']
score = 0
is_game_over = False

print(
    f"Compare A: {famed_a['name']}, a {famed_a['description']}, from {famed_a['country']}")
print(
    f"Against B: {famed_b['name']}, a {famed_b['description']}, from {famed_b['country']}")

chose = input("Who has more followers? Type 'A' or 'B': ").lower()

famous_chose = getting_followers(chose)

score = compare_followers(famous_chose, score)
print(score)
