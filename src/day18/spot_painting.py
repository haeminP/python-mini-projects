from colors import color_list
from turtle import Turtle, Screen
import turtle
import random


turtle.colormode(255)

tim = Turtle()
tim.shape("circle")
tim.speed("fastest")
tim.hideturtle()

tim.penup()
tim.setpos(-200, -200)
tim.pendown()
for row in range(10):
    for column in range(10):
        print(tim.pos())
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.setpos(-200, -200 + (row + 1) * 50)




screen = Screen()
screen.exitonclick()