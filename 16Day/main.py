from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

COMMAND = ["off", "report"]
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def print_report():
    coffee_maker.report()
    money_machine.report()


def main():
    menu = Menu()
    off = False
    while not off:
        command = input(f"What would you like? {menu.get_items()}: \n")
        if command in COMMAND:
            if command == "off":
                print("Have a nice day.\n")
                break
            if command == "report":
                print_report()
        elif menu.find_drink(command):
            drink = menu.find_drink(command)
            if coffee_maker.is_resource_sufficient(drink):
                print(f'Your drink cost {drink.cost}$')
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)
        else:
            continue


main()
