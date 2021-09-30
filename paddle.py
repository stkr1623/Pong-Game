
from turtle import Turtle , Screen
screen=Screen()


class Paddle(Turtle):
    def __init__(self,position , colour):
        super().__init__()
        self.shape("square")
        self.color(colour)
        self.penup()
        self.position = position
        self.goto(position)
        self.turtlesize(stretch_wid=1, stretch_len=8)
        self.setheading(90)




