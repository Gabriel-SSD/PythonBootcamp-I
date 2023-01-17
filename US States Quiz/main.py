import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
condition = 0
data = pandas.read_csv("50_states.csv")
def check_answer (ans):
    if data[data["state"]] == ans:
        pass
        # escrever nome na imagem
        # incrementar 1 estado correto
while condition < 50:
    print(data[data.state] == "Colorado")
    #answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    #check_answer(answer_state)