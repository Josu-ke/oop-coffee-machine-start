import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()
menu_item = MenuItem



is_on = True
while is_on:

    choice = input('what would you like?(espresso/latte/cappuccino/): ')
    if choice == 'off':
        is_on = False

    elif choice == 'report':

        coffe_machine.report()
        my_money_machine.report()
    else:
        drink = (my_menu.find_drink(choice))
        if coffe_machine.is_resource_sufficient(drink):
            my_money_machine.make_payment(drink.cost)
            coffe_machine.make_coffee(drink)

