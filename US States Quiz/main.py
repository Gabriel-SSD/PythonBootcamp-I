import turtle
import pandas

def screen_configs():
    scr = turtle.Screen()
    scr.title("U.S States Game")
    image = "blank_states_img.gif"
    scr.addshape(image)
    turtle.shape(image)
    return scr
def check_answer (ans):
    global condition
    if ans in states:
        condition += 1
        sdata = data[data.state == ans]
        write(ans, sdata)
        states.remove(ans)
    elif ans == 'Exit':
        condition = 51
def write (ans, sdata):
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(int(sdata.x), int(sdata.y))
    text.write(ans)
screen = screen_configs()
condition = 0
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

while condition < 50:
    answer_state = screen.textinput(title=f"{condition}/50", prompt="What's another state's name?").title()
    check_answer(answer_state)
if condition == 51:
    missing = pandas.DataFrame(states)
    missing.to_csv("missing_states.csv")
else:
    print("You win!")