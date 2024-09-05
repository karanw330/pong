from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(3.5, 0.6, 1)
        self.pu()
        self.speed('fastest')
        self.goto(start_position)

    def go_up(self):
        newy = self.ycor() + 40
        newx = self.xcor()
        self.goto(newx, newy)

    def go_down(self):
        nex = self.xcor()
        ney = self.ycor() - 40
        self.goto(nex, ney)

