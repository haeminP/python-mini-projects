from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # reverse y_move's direction
        self.y_move *= -1


    def bounce_x(self):
        # reverse x_move's direction
        self.x_move *= -1
        # when the ball is touched by paddles, increase the speed
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        # reverse x-axis of the ball so, it moves to the opposite direction
        self.bounce_x()
