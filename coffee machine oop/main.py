from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
keep_going = True

while keep_going:
    option = menu.get_items()
    resp = input(f'What would you like ({option}): ')
    if resp == 'off':
        keep_going = False
    elif resp == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(resp)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


