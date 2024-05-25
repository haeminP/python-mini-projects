import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = Turtle()
tim.shape("turtle")
tim.color("SkyBlue")
tim.speed("fastest")

# drawing a square
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# drawing a dashed line
#     for _ in range(15):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()

# colours = ["cornflower blue", "gold", "misty rose", "light sea green", "orange red", "navy", "medium purple", "dark olive green", "cadet blue", "rosy brown", "deep pink", "thistle", "light salmon", "orange"]

# draw shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)
#     tim.color(random.choice(colours))

# random walk
# tim.pensize(7)
# directions = [0, 90, 180, 270]
#
# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(20)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)




draw_spirograph(5)

screen = Screen()
screen.exitonclick()