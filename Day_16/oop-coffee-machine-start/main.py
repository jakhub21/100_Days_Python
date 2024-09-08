from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
flag = True

while flag:
    option = input(f"What cafee do you want {menu.get_items()} or report\n")
    if option == "off":
        flag = False
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


