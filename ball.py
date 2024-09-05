import random
from turtle import Turtle
from random import Random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('cyan')
        self.shapesize(0.3, 0.3, 10)
        self.pu()
        self.y_move = 10
        self.x_move = 10

    def move(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx, newy)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)

