from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.screensize(800, 600, 'black')
screen.title('Pong')
screen.tracer(0,delay=2)


rbar = Paddle((350, 0))
lbar = Paddle((-350, 0))
ball = Ball()
over_text = Score()
right_score = Score()
left_score = Score()
line = Score()
line.midline()

screen.listen()
screen.onkey(lbar.go_up, 'w')
screen.onkey(lbar.go_down, 's')
screen.onkey(rbar.go_up, 'Up')
screen.onkey(rbar.go_down, 'Down')

x=0.05
game_is_on = True
while game_is_on:
    time.sleep(x)
    screen.update()
    right_score.rscr()
    left_score.lscr()
    ball.move()
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce()
    if ball.xcor() == rbar.xcor()-10 and ball.ycor() in range(rbar.ycor()-50, rbar.ycor()+50):
        ball.hit()
        x-=0.004
    if ball.xcor() == lbar.xcor()+10 and ball.ycor() in range(lbar.ycor()-50, lbar.ycor()+50):
        ball.hit()
        x-=0.004

    if ball.xcor() > 360:
        left_score.lscore += 1
        x=0.05
        ball.reset_position()
        time.sleep(1)


    if ball.xcor() < -360:
        right_score.rscore += 1
        x=0.05
        time.sleep(1)
        ball.reset_position()








screen.exitonclick()