with open("./Input/Letters/starting_letter.txt") as letter:
    # Lê a mensagem padrão
    start = letter.read()
with open("./Input/Names/invited_names.txt") as names:
    # Lê os nomes a serem enviados e armazena em uma lista
    nomes = names.read()
    nomes_lista = nomes.split("\n")
for nomes in nomes_lista:
    # Substitui o placeholder com os nomes da lista
    with open(f"./Output/ReadyToSend/{nomes}.txt", "w") as file:
        replaced_text = start.replace("[name]", nomes)
        replaced_text = replaced_text.replace("Angela", "Gabriel")
        file.write(replaced_text)