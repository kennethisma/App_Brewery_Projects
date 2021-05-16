############################# My soulution#####################################3
from Menu_and_resources import MENU, resources

# TODO 4. Check resources sufficient?


def check_resources(machine_resources, order_ingredients):
    """if there are enough resources in machine
        returns true."""
    for k in order_ingredients:
        if order_ingredients[k] > machine_resources[k]:
            print(f" Sorry there is not enough {k}")
            return False
    return True

# TODO 5. Process coins


def process_coins(order_price):
    """if the coins are enough for the order, it returns true and if
       the coins are more than the order,
       it returns true and prints the change."""
    number_of_quarters = int(input("How many quarters?: ")) * 0.25
    number_of_dimes = int(input("How many dimes?: ")) * 0.10
    number_of_nickles = int(input("How many nickles?: ")) * 0.05
    number_of_pennies = int(input("How many pennies?: ")) * 0.01
    customer_money = number_of_quarters + number_of_dimes + \
        number_of_nickles + number_of_pennies                # line break

    # TODO 6 Check transaction successful?
    if order_price > customer_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif customer_money > order_price:
        change = customer_money - order_price
        # "{:0.2f}" this part of the code rounds the change
        print(f"Here is {change:0.2f} dollars in change.")
        # to two decimal places.
        return True
    else:
        return True


machine_resources = resources
money_machine = 0
turn_off = False
while not turn_off:
    # TODO 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    customer_order = input(
        " What would you like? (espresso/latte/cappuccino):")

    # TODO 2.Turn off the Coffee Machine by entering “off” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off\n
    # the machine. Your code should end execution when this happens.
    if customer_order == 'off':
        turn_off = True

    # TODO 3 Print report.
        # a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif customer_order == 'report':
        print(f"Water: {machine_resources['water']}ml\n"
              f"Milk: {machine_resources['milk']}ml\n"
              f"Coffee: {machine_resources['coffee']}g\n"
              f"Money: ${money_machine}")
    else:
        order_ingredients = MENU[customer_order]["ingredients"]
        order_price = MENU[customer_order]['cost']
        enough_resources = check_resources(
            machine_resources, order_ingredients)

        # TODO 7 MAKE COFFE
        if enough_resources and process_coins(order_price):
            for k in order_ingredients:
                machine_resources[k] -= order_ingredients[k]
            money_machine += order_price
            print(f"Here is your {customer_order} ☕. Enjoy!")


###################################Angela's soulution#############################
# MENU = {
#       "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
