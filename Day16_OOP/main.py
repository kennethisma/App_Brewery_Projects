from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# latte = MenuItem("latte", 100, 80, 15, 1.5)
# espresso = MenuItem("espresso", 60, 0, 20, 2.5)
# cappuccino = MenuItem("cappuccino", 200, 150, 40, 4.5)


machine_resources = CoffeeMaker()
products = Menu()
money = MoneyMachine()
turn_off = False
while not turn_off:
    order = input(f"What would you like? {products.get_items()}: ")

    if order == 'report':
        machine_resources.report()
        money.report()
    elif order == 'off':
        turn_off = True
    else:
        user_order = products.find_drink(order)
        print(user_order)
        if machine_resources.is_resource_sufficient(user_order) and money.make_payment(user_order.cost):
            machine_resources.make_coffee(user_order)
