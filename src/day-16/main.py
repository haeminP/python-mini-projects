# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cornflowerblue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#


# from prettytable import PrettyTable
# table = PrettyTable()
# # table.field_names = ["Pokemon Name", "Type"]
# # table.add_row(["Pikachu", "Electric"])
# # table.add_row(["Squirtle", "Water"])
# # table.add_row(["Charmander", "Fire"])
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)


# oop coffee machine
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_maker.report()

choice = input(f"What would you like to drink ({menu.get_items()})? ")
if menu.find_drink(choice) != None:
    order = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(order):
        order_cost = order.cost
        if money_machine.make_payment(order_cost):
            coffee_maker.make_coffee(order)


