import turtle
from turtle import Turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
print(answer_state)

# read the data
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()

states = list(data_dict["state"].values())
x_coordinates = data_dict["x"]
y_coordinates = data_dict["y"]


def text_at_xy(x, y, text):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(text, font=('Arial', 8, 'normal'))

def get_mouse_click_coor(x, y):
    print(x, y)

if answer_state in states:
    text_at_xy(30, 50, answer_state)

# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()


screen.exitonclick()
