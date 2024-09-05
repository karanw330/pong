from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.pu()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0

    def rscr(self):
        self.clear()
        self.setpos(170, 220)
        self.write(f"{self.rscore}", False, 'center', ('Arial', 30, 'normal'))

    def lscr(self):
        self.clear()
        self.setpos(-170, 220)
        self.write(f"{self.lscore}", False, 'center', ('Arial', 30, 'normal'))

    '''def over(self):
        self.write('GAME OVER', False, 'center', ('Arial', 20, 'normal') )'''

    def midline(self):
        self.sety(-300)
        self.left(90)
        for i in range(21):
            self.pd()
            self.forward(15)
            self.pu()
            self.forward(15)

