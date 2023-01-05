class Core:
    def __init__(self, data):
        # Recebe uma lista de objetos (db), e atribui propriedades a eles
        self.question_number = 0
        self.score = 0
        self.question_list = data

    def make_question(self):
        # Questão atual recebe uma questão da lista de questões
        question = self.question_list[self.question_number]
        # Incrementa o indice, para exibir o print correto, e preparar para a próxima chamada
        self.question_number += 1
        # Exibe a questão e solicita uma resposta
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        # Chama o método para verificar a resposta
        self.check_answer(answer, question.answer)


    def still_has_question(self):
        # Método que verifica se ainda há perguntas
        return self.question_number < len(self.question_list)

    def check_answer(self, usr_ans, r_ans):
        # Verifica se a resposta está correta e incrementa o score.
        if usr_ans.lower() == r_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {r_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")