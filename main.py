import time
from turtle import Turtle , Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("PONG")
r_paddle = Paddle(position = (380, 0) ,colour="blue")
l_paddle = Paddle(position = (-390, 0),colour ="red")
ball = Ball()
scoreboard=Scoreboard()


def up_r():
   r_paddle.forward(20)
def down_r():
   r_paddle.backward(20)
def up_l():
   l_paddle.forward(20)
def down_l():
   l_paddle.backward(20)
screen.listen()
screen.onkeypress(up_r,"Up")
screen.onkeypress(down_r,"Down")
screen.onkeypress(up_l, "w")
screen.onkeypress(down_l, "s")
game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
       ball.bounce_y()
    if ball.distance(r_paddle)<=70 and ball.xcor()>340 or ball.distance(l_paddle)<=70 and ball.xcor()<-340 :

        ball.bounce_x()
    if ball.xcor()>380 :

        ball.reset_position()
        scoreboard.l_scores()
    elif ball.xcor()<-380 :
        ball.reset_position()
        scoreboard.r_scores()




screen.exitonclick()