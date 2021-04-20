# My solution ###############################3
from art import logo
import os

print(logo)

auction_dict = {}
other_bidders = True


def clear():  # Clean the terminal
    return os.system('cls')


while other_bidders:
    user_name = input("What is your name?\n")
    user_bid = int(input("What's your bid?\n$"))

    auction_dict[user_name] = user_bid

    gamblers = input("Are there any other bidders? Type 'yes' or 'no'\n")

    values = auction_dict.values()
    max_bet = max(values)

    for k in auction_dict:
        if max_bet == auction_dict[k]:
            winner = k

    if gamblers == 'yes':
        clear()
        continue

    elif gamblers == 'no':
        print(f"The winner is {winner} with a bid of {max_bet} ")
        other_bidders = False

    else:
        other_bidders = False


#######################################Angela's solution #########################################

# from replit import clear
# from art import logo
# print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
