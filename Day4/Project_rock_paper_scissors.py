import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

move = int(input(
    'What do you choose? type 0 for Rock, 1 for paper or two for scissors\n'))

if move == 0:
    print(rock)
elif move == 1:
    print(paper)
elif move == 2:
    print(scissors)
else:
    print('You have to choose from 0 to 2')

computer = random.randint(0, 2)

print('Computer choose: ')

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)


if computer == 0 and move == 2:
    print('You lose')
elif computer == 2 and move == 1:
    print('You lose')
elif computer == 1 and move == 0:
    print('You lose')
elif computer == move:
    print('Tie')
else:
    #     print('You win')
