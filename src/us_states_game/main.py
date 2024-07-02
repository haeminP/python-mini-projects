import turtle
from turtle import Turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# read the data
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()

states = list(data_dict["state"].values())
x_coordinates = data_dict["x"]
y_coordinates = data_dict["y"]


score = 0


def text_at_xy(x, y, text):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(text, font=('Arial', 8, 'normal'))

def get_mouse_click_coor(x, y):
    print(x, y)

def check_answer(answer_state, score):
    if answer_state in states:
        guessed_states.append(answer_state)
        index = states.index(answer_state)
        x_coordinate = x_coordinates.get(index)
        y_coordinate = y_coordinates.get(index)
        text_at_xy(x_coordinate, y_coordinate, answer_state)
        score += 1


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    check_answer(answer_state, score)

# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()

# states to learn.csv


screen.exitonclick()
