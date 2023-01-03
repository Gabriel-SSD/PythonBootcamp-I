# Neste exercício, usei os arquivos feitos pela professora, consultando a sua documentação.

# Imports
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Declaração dos objetos
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Condição do loop
is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()})")    # Exibe os itens do menu
    if choice == "report":
        coffee_maker.report()       # Exibe o report de recursos
        money_machine.report()      # Exibe o report de dinheiro
    elif choice == "off":
        is_on = False               # Finaliza o programa
    else:
        drink = menu.find_drink(choice)     # Drink é declarado como uma classe
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Se tiver dinheiro/recursos suficientes para fazer o drink, faça
            coffee_maker.make_coffee(drink)