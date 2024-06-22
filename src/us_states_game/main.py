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
        index = states.index(answer_state)
        x_coordinate = x_coordinates.get(index)
        y_coordinate = y_coordinates.get(index)
        text_at_xy(x_coordinate, y_coordinate, answer_state)
        score += 1


game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    check_answer(answer_state, score)

# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()


screen.exitonclick()
