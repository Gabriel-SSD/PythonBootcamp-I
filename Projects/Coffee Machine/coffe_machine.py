from coffe_machine_data import MENU, resources

# Request(): Solicita um pedido, encerra caso o pedido seja off, e chama report caso desejado, além disso
# A função é recursiva até que o usuário envie o comando certo. Ela retorna uma string do pedido
def request():
    a =  input("What would you like? (espresso/latte/cappuccino): ")
    if a == 'off':
        exit(0)
    elif a == 'report':
        return report()
    elif a != 'espresso':
        if a != 'latte':
            if a != 'cappuccino':
                print(f"You type {a}")
                return request()
    return a

def report():     # Faz um relatório dos recursos e do dinheiro na máquina, retorna o próximo pedido, chamando request()
    for i in resources:
        if i == 'coffee':
            print(f"{i}: {resources[i]}g".capitalize())
            break
        print(f"{i}: {resources[i]}ml".capitalize())
    print(f"Money: ${money}")
    return request()

# Process(opt): Tem como parametro o pedido, basicamente calcula o dinheiro inserido na maquina, calcula se deverá
# conceder troco, ou se deverá ressarcir o dinheiro, caso ele seja insuficiente.
# Retorna True se tiver dinheiro, dando então continuidade, ou False caso não tenha dinheiro suficiente
def process(opt):
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    cashin =  quarters + dimes + nickles + pennies
    cost = MENU[opt]["cost"]
    change = cashin - cost
    if change > 0:
        print(f"Here is ${change}")
        print(f"Here is your {opt}")
        money += cost
        return True
    elif change < 0:
        change *= -1
        print(f"Not enough money. We refund ${change}.")
    return False

def verifyresources(opt): # Verifica se há recursos suficientes para realizar a operação, caso contrário, será exibida uma mensagem de feedback e retornado falso.
    # TODO 1. Talvez exista um simplificação que reduza os Return False
    if opt == 'espresso':
        if resources["water"] - MENU["espresso"]["ingredients"]["water"] < 0:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] - MENU["espresso"]["ingredients"]["milk"] < 0:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"] < 0:
            print("Sorry there is not enough coffee.")
            return False
    elif opt == 'latte':
        if resources["water"] - MENU["latte"]["ingredients"]["water"] < 0:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] - MENU["latte"]["ingredients"]["milk"] < 0:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] - MENU["latte"]["ingredients"]["coffee"] < 0:
            print("Sorry there is not enough coffee.")
            return False
    elif opt == 'cappuccino':
        if resources["water"] - MENU["cappuccino"]["ingredients"]["water"] < 0:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"] < 0:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"] < 0:
            print("Sorry there is not enough coffee.")
            return False
    return True

def useresource(opt):     # Utiliza o recurso, decrementa os recursos com base na escolha
    if opt == 'espresso':
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif opt == 'latte':
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    elif opt == 'cappuccino':
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]


money = 0                       # Variavel de controle de dinheiro na máquina
while True:                     # Loop infinito, até alguém desligar a máquina
    chosen = request()          # Solicita um comando/pedido ao usuário
    if verifyresources(chosen): # Verifica se há recursos para a operação
        if process(chosen):     # Calcula o dinheiro inserido e troco/reembolso
            useresource(chosen) # Utiliza o recurso e concede a bebida ao usuário