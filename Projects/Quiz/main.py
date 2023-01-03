# Imports
# TODO 1. Randomizar a pergunta
from question_model import Question
from data import data
from core import Core

def userinterface ():
    while True:
        entrada = input("Choose a difficulty (easy/medium/hard): ").lower()
        if entrada != 'easy':
            if entrada != 'medium':
                if entrada != 'hard':
                    print(f"You typed {entrada}\n")
        else:
            return entrada

# Main function
questions = []      # Inicializa uma lista vazia
diff = userinterface()

for i in range(0, len(data)):
    # Atribui a var local_question uma classe que contem uma questão e resposta
    local_question =  Question(data[i]["question"], data[i]["correct_answer"], data[i]["difficulty"])
    if local_question.diff == diff:
        questions.append(local_question)  # Adiciona à lista, as questões que tem a dificuldade certa

# quiz é uma var que recebe uma classe (ver core para mais detalhes)
quiz = Core(questions)

# Enquanto ainda tiver questões
while quiz.still_has_question():
    quiz.make_question()

# Print de finalização
print(f"You've completed the {diff} quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")